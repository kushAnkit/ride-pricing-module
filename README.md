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
