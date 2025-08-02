# 🪙 Minimum Withdrawal Fee API

This project provides a simple API that scrapes and displays the **minimum withdrawal fees** for available cryptocurrencies across various Iranian brokers.

---

## 🚀 Getting Started

### 1. Install Dependencies

Ensure you have **Python 3.7+** installed. Then, install required packages:

```bash
pip install -r requirements.txt
```

### 2. Set Up Selenium WebDriver

Download the WebDriver for your browser:

- **Chrome**: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Edge**: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **Safari**: [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

📝 Place the downloaded **WebDriver executable** in the same directory as `main.py`.

---

### 3. Run the Script

Open a terminal in the project folder and run:

```bash
python main.py
```

You’ll see a list of coins sorted from **lowest to highest withdrawal fee**.

- note: for default main.py set the chrome webdriver. if you want to use another browser, just change that line in main.py
---

## 📂 Project Structure

```
minimum_withdrawal_fee/
│
├── main.py                 # Main script
├── nobitex.py
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📌 Notes

- Make sure your browser version is compatible with the WebDriver version.
- Selenium is used for web scraping, so a stable internet connection is necessary.
- You can uncomment the headless option if you want to watch it work visually.

---

## 📜 License

GNU GENERAL PUBLIC LICENSE V3

---
