# 🛡️ SafeSurf - Website Blocker

SafeSurf is a simple Python script that helps you block or unblock access to specific websites by modifying your system's `hosts` file. It's designed to promote safer browsing by restricting access to adult content, gambling sites, and social media platforms.

---

## 🚀 Features

- Block access to a predefined list of websites
- Unblock previously blocked websites
- Works on both Windows and Unix-based systems
- Simple command-line interface
- Requires administrator/root privileges

---

## ⚙️ How It Works

The script redirects specified domains to `127.0.0.1` (localhost) by appending entries to your system's `hosts` file. This effectively prevents your browser from reaching those sites.

---

## 📋 Blocked Sites

The default list includes:

- Adult content (e.g., pornhub.com, xvideos.com)
- Gambling sites (e.g., bet365.com, gambling.com)
- Social media (e.g., facebook.com, instagram.com)
- Other harmful or distracting domains

You can customize the list by editing the `BLOCKED_SITES` variable in the script.

---

## 🖥️ Installation

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the script with administrator/root privileges.

---

## 🔐 Usage

```bash
python safesurf.py

You'll be prompted to choose:

SafeSurf - Website Blocker
1. Block sites
2. Unblock sites
Choose an option (1 or 2):

⚠️ You must run the script as an administrator (Windows) or with sudo (Linux/macOS) for it to work.

🧠 Notes
Changes to the hosts file take effect immediately, but some browsers may cache DNS results. Restarting the browser or flushing DNS may help.

Always back up your hosts file before making changes.

🛠️ Troubleshooting
Permission Denied: Make sure you're running the script with elevated privileges.

Sites Not Blocking: Check for typos in the domain names or browser caching issues.

📜 License
This project is open-source and free to use under the MIT License.

🙌 Contributing
Feel free to fork the project and submit pull requests to improve functionality, add features, or expand the blocked site list.


---

Let me know if you'd like to add setup instructions for a GUI version or include logging features.


