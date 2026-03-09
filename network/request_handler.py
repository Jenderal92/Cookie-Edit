import requests
from utils.logger import logger

class RequestHandler:
    @staticmethod
    def send_request(method, url, cookies_dict):
        try:

            session = requests.Session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CookieEditor/1.0 (Jenderal92)',
                'Accept': 'application/json, text/html'
            }
            
            response = session.request(
                method, 
                url, 
                cookies=cookies_dict, 
                headers=headers, 
                timeout=12
            )
            
            return {
                "status": response.status_code,
                "new_cookies": session.cookies.get_dict(),
                "headers": dict(response.headers)
            }
        except Exception as e:
            logger.error(f"Failed to make request: {e}")
            return None