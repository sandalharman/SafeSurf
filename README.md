# SafeSurf 🛡️🌐

**SafeSurf** is a Python-based application designed to provide safer and more controlled internet usage. Whether you're a parent, educator, or a privacy-conscious user, SafeSurf helps you monitor and filter online activity with ease.

## 🚀 Features

- 🔒 Website blocking based on keywords or domains
- 🧠 Intelligent content filtering using text analysis
- 📊 Activity logging for audits and reports
- ⏱️ Scheduled internet usage restrictions
- 📍 Customizable allow/block lists
- 🖥️ Cross-platform support (Windows, macOS, Linux)

## 🛠️ Built With

- Python 3.x
- `tkinter` (for GUI - optional)
- `requests`, `beautifulsoup4` (for content analysis and scraping)
- `re` (regular expressions for content filtering)
- Custom blacklist/whitelist management

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/sandalharman/SafeSurf.git
cd safesurf
Install dependencies (if applicable):

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python safesurf.py
⚠️ Some features may require administrator/root privileges (e.g., modifying system DNS or hosts files).

📁 Project Structure
kotlin
Copy code
safe-surf/
├─ docker-compose.yml          # 3‑container stack
├─ Dockerfile                  # FastAPI + proxies
├─ Makefile
├─ README.md
├─ config/
│  ├─ policy.json              # User/group/time rules
│  ├─ categories.csv           # Domain → category
│  └─ threat_list.txt          # Simple IP/domain blacklist
├─ app/
│  ├─ main.py                  # FastAPI entry point
│  ├─ policy.py
│  ├─ url_categorizer.py
│  ├─ content_analyzer.py
│  ├─ threat_intel.py
│  └─ decision.py
├─ models/                     # Trained ML model (XGBoost)
│  └─ url_classifier.pkl
└─ tests/                      # Unit tests (optional)

📚 Usage
Launch the application and navigate the GUI or CLI.

Use settings to configure filters or schedules.

Check logs in /logs/activity_log.txt to review history.

🧪 Example Use Cases
Parental Control: Block adult or harmful content for children.

School Environment: Prevent access to distracting or unsafe websites.

Focus Mode: Block social media or time-wasting websites during work hours.

🙌 Contributing
Contributions are welcome! To contribute:

Fork the project

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push origin feature-name)

Open a pull request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
Developer: Harman,Jai,Aastha,Ashita,Vishesh
Email: sandalharmann@gmail.com
GitHub: @sandalharman

Made with ❤️ in Python

yaml
Copy code

---

Let me know if:
- You want to tailor this to a different set of features
- Your project uses Flask, Django, or any other framework
- You’d like to generate a `requirements.txt` or add badges

I'm happy to adjust it to match your actual SafeSurf project.

