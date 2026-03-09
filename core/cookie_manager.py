import time
from config.settings import COOKIE_FILE
from utils.json_handler import JSONHandler
from core.validator import Validator
from utils.logger import logger

class CookieManager:
    def __init__(self):
        self.cookies = JSONHandler.load_json(COOKIE_FILE)

    def get_all(self):
        return self.cookies

    def add_cookie(self, cookie_data):

        if 'added_at' not in cookie_data:
            cookie_data['added_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
        

        for idx, c in enumerate(self.cookies):
            if c['name'] == cookie_data['name'] and c.get('domain') == cookie_data.get('domain'):
                self.cookies[idx].update(cookie_data)
                self.save()
                return True
        
        self.cookies.append(cookie_data)
        self.save()
        return True

    def update_cookie(self, index, updated_data):
        if 0 <= index < len(self.cookies):
            self.cookies[index].update(updated_data)
            self.save()
            return True
        return False

    def delete_cookie(self, index):
        if 0 <= index < len(self.cookies):
            self.cookies.pop(index)
            self.save()
            return True
        return False

    def get_stats(self):
        domains = set(c.get('domain') for c in self.cookies if c.get('domain'))
        return {
            "total": len(self.cookies),
            "unique_domains": len(domains),
            "secure_count": len([c for c in self.cookies if c.get('secure')]),
            "httponly_count": len([c for c in self.cookies if c.get('httponly')])
        }

    def get_curl_string(self):
        return "; ".join([f"{c['name']}={c['value']}" for c in self.cookies])
        
    def clear_expired(self):
        now = time.time()
        initial = len(self.cookies)

        self.cookies = [c for c in self.cookies if not (c.get('expiry') and float(c['expiry']) < now)]
        self.save()
        return initial - len(self.cookies)

    def search(self, query):
        query = query.lower()
        return [c for c in self.cookies if query in c['name'].lower() or query in c.get('domain', '').lower()]

    def get_grouped_by_domain(self):
        grouped = {}
        for c in self.cookies:
            domain = c.get('domain', 'Unknown')
            if domain not in grouped:
                grouped[domain] = []
            grouped[domain].append(c)
        return grouped

    def get_cookie_health(self, cookie):
        if 'expiry' not in cookie or not cookie['expiry']:
            return "Session (No Expiry)"
        
        remaining = float(cookie['expiry']) - time.time()
        if remaining <= 0:
            return "EXPIRED"
        
        mins = int(remaining // 60)
        if mins < 60:
            return f"Live: {mins}m"
        hours = mins // 60
        return f"Live: {hours}h {mins % 60}m"
        
    def save(self):
        JSONHandler.save_json(COOKIE_FILE, self.cookies)