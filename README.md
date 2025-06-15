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


git clone https://github.com/kushAnkit/ride-pricing-module/

cd ride-pricing-module


### 2. Set up virtual environment
 
python -m venv venv

source venv/bin/activate <br> 
For Windows: venv\Scripts\activate

pip install -r requirements.txt

### 3. Run migrations and start the server
   
  cd ride_pricing  # For main app

python manage.py makemigrations <br>
python manage.py migrate <br>
python manage.py createsuperuser  # For admin access <br>
python manage.py runserver


🧪 API Usage <br>
 ## for price configuration admin panel/form and Change Log <br>
 Endpoint: /admin

 ## for calculation of fare <br>
Endpoint: /api/pricing/calculate-fare/


Method: GET

Params:

Param	      Type	     Description <br>
distance	  float   	 Distance traveled (km) <br>
time	      int	       Duration of ride (minutes) <br>
wait	      int	       Waiting time (minutes) <br>

Example:

GET /api/pricing/calculate-fare/?distance=12.5&time=80&wait=7

Response:

{
  "total_fare": 178.75
}

