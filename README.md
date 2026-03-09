# 🍪 Cookie-Edit


---

**Cookie-Edit** is a lightweight, professional CLI tool built for developers to manage, test, and analyze HTTP cookies. Designed with a clean modular architecture, it's perfect for debugging APIs and testing web sessions directly from your terminal or Termux.


## ✨ Features
- **Centralized Management**: Create, Read, Update, and Delete (CRUD) cookies in a local JSON store.
- **Smart Grouping**: Organize and view cookies automatically grouped by their domain.
- **Health Tracking**: Monitor cookie expiration with real-time "Live" vs "Expired" status indicators.
- **Request Engine**: Send GET/POST requests and automatically capture new cookies from server responses.
- **Curl Integration**: Instantly generate `--cookie` strings for use in external terminal commands.
- **Deep Analytics**: View statistics on your cookie jar, including Secure and HttpOnly flags.
- **One-Click Cleanup**: Quickly wipe all expired cookies to keep your workspace clean.

## 📂 Project Structure
```text
Cookie-Edit/
├── main.py              # Application entry point
├── network/             # HTTP request and capture logic
├── core/                # Data management and cookie health logic
├── utils/               # Table rendering, JSON I/O, and logging
├── config/              # Path and environment settings
└── data/                # Local storage (cookies.json)

```

## 🚀 Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/Jenderal92/Cookie-Edit.git
cd Cookie-Edit

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the tool:**
```bash
python main.py

```



## 🛠 Usage

* **Testing APIs**: Use the HTTP Request menu to see how a server interacts with your current cookies.
* **Debugging**: Check the "Health" status to ensure your session hasn't timed out during testing.
* **Migration**: Export your session as a Curl string to continue testing in other professional tools.

## 🛡 Security

Cookie-Edit stores data locally in `data/cookies.json`. To protect your session data, the `data/` directory is included in `.gitignore` to prevent it from being uploaded to public repositories.

---



