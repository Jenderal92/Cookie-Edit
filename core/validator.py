class Validator:
    @staticmethod
    def validate_cookie(cookie_dict):
        required = ['name', 'value', 'domain']
        return all(key in cookie_dict for key in required)