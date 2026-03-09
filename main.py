import sys
from cli.menu import CookieEditorCLI
from utils.logger import logger

def main():
    try:
        app = CookieEditorCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n[!] Closing CookieEdit... See you!")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Application stopped suddenly: {e}")

if __name__ == "__main__":
    main()