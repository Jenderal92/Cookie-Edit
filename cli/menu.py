import os
import time
from core.cookie_manager import CookieManager
from network.request_handler import RequestHandler
from utils.table_view import TableView

class CookieEditorCLI:
    def __init__(self):
        self.manager = CookieManager()
        self.http = RequestHandler()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def header(self, title):
        self.clear()
        print("="*60)
        print(f" 🍪 COOKIE EDITOR  | {title.upper()}")
        print("="*60)

    def run(self):
        while True:
            self.header("Main Menu")
            print("1. View All Cookies (Flat List)")
            print("2. View Grouped by Domain")
            print("3. Add New Cookie")
            print("4. Send HTTP Request & Capture")
            print("5. Search Cookies")
            print("6. Cookie Statistics & Analytics")
            print("7. Export as Curl String")
            print("8. Cleanup Expired Cookies")
            print("0. Exit")
            
            choice = input("\nSelect Option > ")
            
            if choice == '1': self._view_flat()
            elif choice == '2': self._view_grouped()
            elif choice == '3': self._add_logic()
            elif choice == '4': self._http_logic()
            elif choice == '5': self._search_logic()
            elif choice == '6': self._show_stats()
            elif choice == '7': self._export_curl()
            elif choice == '8': self._cleanup_logic()
            elif choice == '0': break
            else: input("Invalid input! Press Enter...")

    def _view_flat(self):
        self.header("Flat Cookie List")
        data = self.manager.get_all()
        display = []
        for i, c in enumerate(data):
            display.append({
                "ID": i,
                "Name": c['name'],
                "Domain": c.get('domain', 'N/A'),
                "Health": self.manager.get_cookie_health(c)
            })
        TableView.render(display)
        print("\nOption: [d] Delete ID, [b] Return")
        cmd = input("Command > ")
        if cmd.lower().startswith('d'):
            try:
                idx = int(input("Enter the ID to be deleted: "))
                self.manager.delete_cookie(idx)
            except: print("Failed to delete!")

    def _view_grouped(self):
        self.header("Grouped by Domain")
        groups = self.manager.get_grouped_by_domain()
        if not groups:
            print("No cookies yet.")
        for domain, cookies in groups.items():
            print(f"\n🌍 DOMAIN: {domain}")
            data = [{"Name": c['name'], "Value": c['value'][:15]+"...", "Status": self.manager.get_cookie_health(c)} for c in cookies]
            TableView.render(data)
        input("\nPress Enter to return...")

    def _add_logic(self):
        self.header("Add Cookie")
        n = input("Name: ")
        v = input("Value: ")
        d = input("Domain (ex: example.com): ")
        self.manager.add_cookie({"name": n, "value": v, "domain": d})
        print("Added successfully!")
        time.sleep(1)

    def _http_logic(self):
        self.header("Send HTTP Request")
        url = input("Target URL (https://...): ")
        method = input("Method (GET/POST): ").upper() or "GET"
        
        flat_cookies = {c['name']: c['value'] for c in self.manager.get_all()}
        res = self.http.send_request(method, url, flat_cookies)
        
        if res:
            print(f"\n[Status {res['status']}] Success!")
            if res['new_cookies']:
                print(f"Catch {len(res['new_cookies'])} new cookies!")
                for k, v in res['new_cookies'].items():
                    self.manager.add_cookie({"name": k, "value": v, "domain": url})
            else: print("No new cookies from the server.")
        input("\nPress Enter...")

    def _show_stats(self):
        self.header("Statistics")
        s = self.manager.get_stats()
        TableView.render([
            ["Total Cookies", s['total']],
            ["Unique Domains", s['unique_domains']],
            ["Secure", s['secure_count']],
            ["HttpOnly", s['httponly_count']]
        ])
        input("\nPress Enter...")

    def _export_curl(self):
        self.header("Curl Export")
        c_str = self.manager.get_curl_string()
        print(f'--cookie "{c_str}"')
        input("\nCopy the code above. Press Enter....")

    def _cleanup_logic(self):
        count = self.manager.clear_expired()
        print(f"Successfully cleared {count} expired cookies.")
        time.sleep(1.5)

    def _search_logic(self):
        self.header("Search Cookies")
        q = input("Keyword: ")
        res = self.manager.search(q)
        TableView.render(res)
        input("\nPress Enter...")