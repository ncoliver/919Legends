# 919Legends

# 🏀 Local Basketball Team Web App

This is a Django-based web application developed for a local basketball team. The project provides a clean and responsive frontend using Bootstrap and includes a modern landing page designed with custom fonts and icons.

## 🔧 Features

- 🌐 **Landing Page**: Visually appealing homepage with team branding.
- 🧱 **Class-Based Views**: Clean, modular code using Django's class-based views.
- 🎨 **Bootstrap Styling**: Fully responsive layout using Bootstrap 5.
- 📄 **Base Template**: A central `base.html` file ensures DRY templating and consistent layout.
- 🔠 **Google Fonts**: Custom fonts integrated via Google Fonts for a polished look.
- ⭐ **Font Awesome Icons**: Interactive and modern icons throughout the site.

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Templating**: Django Templates with inheritance via `base.html`
- **Fonts**: Google Fonts

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

```bash
git clone https://github.com/yourusername/basketball-team.git
cd basketball-team
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
