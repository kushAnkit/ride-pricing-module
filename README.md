# 🚖 Django Ride Pricing Module

A configurable and extensible ride-pricing engine inspired by Uber/Ola-style fare systems. Built with Django, this backend module allows dynamic fare computation based on distance, duration, waiting time, and configurable time multipliers.

![Django](https://img.shields.io/badge/Framework-Django-green)
![Status](https://img.shields.io/badge/Status-Completed-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 📌 Features

- 💼 Dynamic **Pricing Configuration Management** via Django Admin
- 🧮 Fare calculation API using:
  - Base price
  - Distance slabs
  - Time multipliers
  - Waiting charges
- 🔧 Admin form for creating/editing configurations
- 📜 Configuration change logs with timestamp and user tracking
- 🔒 Only one active pricing config at a time
- ✅ Supports edge-case handling with robust validations

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
<<<<<<< HEAD
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Run migrations and start the server
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # For admin access
python manage.py runserver
🧪 API Usage
Endpoint: /api/pricing/calculate-fare/
Method: GET
Params:

Param	Type	Description
distance	float	Distance traveled (km)
time	int	Duration of ride (minutes)
wait	int	Waiting time (minutes)

Example:

bash
Copy
Edit
GET /api/pricing/calculate-fare/?distance=12.5&time=80&wait=7
Response:

json
Copy
Edit
{
  "total_fare": 178.75
}
=======
>>>>>>> 035d02169f898b6d0475c928d9f2e53bcc3716ce
