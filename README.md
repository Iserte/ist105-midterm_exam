# IST105 Midterm – Django Math Application

**Student Name:** Gustavo Iserte Bonfim  
**Student ID:** CT1010953

This project was developed for the IST105 – Introduction to Programming midterm exam at the Canadian College of Technology and Business. It showcases a Django-based web application deployed on AWS EC2 with Auto Scaling and Load Balancer integration.

---

## 🔧 Project Overview

**Project Name:** `mathapp`  
**Django App:** `calculator`  
**Functionality:** Users input two numbers and select a math operation. The app performs the calculation and displays the result dynamically using Django templates.

---

## 🚀 Features

- Basic operations: Add, Subtract, Multiply, Divide
- Loop-based operations:
  - For loop sum
  - While loop product
- Input validation and exception handling
- Result logic:
  - If result > 100 → multiply by 2
  - If result < 0 → add 50
- Friendly error messages for invalid input and division by zero

---

## 🖥️ Deployment Architecture

- **AWS EC2** with Launch Template
- **Auto Scaling Group** (Min: 1, Max: 7)
  - Target tracking policy: CPU > 15%
  - Warm-up time: 30 seconds
- **Application Load Balancer**
  - Health check path: `/calculate/`
  - Success code: `200`
- **Startup script** via `user-data` to auto-deploy Django

## 📂 GitHub Repository Structure

**Repository Name:** `ist105-midterm_exam`  
**Branches:**
- `main` – Final version
- `development` – Testing and fixes
- `feature1` – Initial implementation
