# 🧠 Competitive Programming Tracker

A Django web application that helps users **track their contest performance** on **Codeforces** and **Leetcode**. Users can register using their platform handles, and the app fetches and displays their contest history using dynamic tables and charts.

---

## ✨ Features

- 🔐 **User Authentication** – Register/Login system using Django’s built-in auth.
- 🧑‍💻 **Handle Submission** – Save Codeforces and Leetcode handles during registration.
- 📈 **Visual Analytics** – Chart.js powered rating graph (Codeforces) and stats bar chart (Leetcode).
- 📅 **Contest History Table** – Sortable contest records with ranks, ratings, and dates.
- 🌐 **Responsive UI** – Built with Bootstrap for clean styling and layout.

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Backend | Django 5+ |
| Frontend | HTML, Bootstrap 5 |
| Charts | Chart.js |
| Database | SQLite (default) |
| APIs Used | Codeforces API, Leetcode API (unofficial) |


---

## ⚙️ Setup Instructions

# Clone the repository
```bash
git clone https://github.com/your-username/contest-tracker.git
cd contest-tracker
```
# (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
# Install dependencies
```bash
pip install -r requirements.txt
```
# Apply migrations
```bash
python manage.py migrate
```
# Run the development server
```bash
python manage.py runserver
```
## 📂 Directory Structure

 ```bash
   contest-tracker/
   ├── tracker/                 # Main Django app
   │   ├── models.py            # Contest & Profile models
   │   ├── views.py             # Main logic
   │   ├── forms.py             # User registration form
   │   ├── urls.py              # App URLs
   │   └── signals.py           # Auto-create user profiles
   ├── templates/
   │   ├── base.html
   │   ├── home.html
   │   ├── register.html
   │   ├── contest_history.html
   │   └── registration/
   │       └── login.html       # Django expects login.html here
   ├── static/                  # Optional custom CSS/JS
   ├── db.sqlite3               # SQLite database
   ├── manage.py                # Django management script
   ├── requirements.txt         # Python dependencies
   └── README.md
```

## 📌 Future Enhancements
   Support for CodeChef / AtCoder handles

   Leaderboard among users

   OAuth-based login (Google/GitHub)

   Email notifications for upcoming contests

## 🙏 Acknowledgements
Django
Bootstrap
Chart.js
Codeforces API
Leetcode Stats

## 📄 License
This project is licensed under the MIT License.

Built with 💻 and ❤️ by Chandra Vardhan Reddy




