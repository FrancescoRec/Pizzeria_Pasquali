# **Pizzeria Pasquali 🍕👨‍🍳 **

A note from the creator:

This repository was created to help small developers like myself organize their work and build an app that accomplishes tasks like order management and role-based access. It might not represent the perfect setup for every project, but it’s what works best for me and my workflow. Remember, what you see on YouTube or read in tutorials isn’t always the "best" way—it’s simply the method that works best for someone else. Find what suits you and don't be afraid to tailor it to your own needs. ❤️

Pizzeria Pasquali is a Django-based web application that allows customers to place pizza orders, while employees can manage those orders. The project features user authentication, role-based access control, order management, and administrative capabilities. The project is Dockerized for easy deployment and includes separate configurations for local and production environments. ✨🚀

---

## **Table of Contents**
1. [Features](#features)
2. [Technologies](#technologies)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Running the Project](#running-the-project)
6. [Docker Setup](#docker-setup)
7. [Usage](#usage)
8. [API Endpoints](#api-endpoints)
9. [Running Tests](#running-tests)
10. [Environment Variables](#environment-variables)
11. [File Structure](#file-structure)
12. [Contributing](#contributing)
13. [License](#license)

---

## **Features 🧑‍💻**

### **Customer Dashboard:**
- Customers can register and log in.
- Customers can browse available pizzas.
- Customers can place pizza orders.
- Customers can view their order history and request changes to pending orders.

### **Employee Dashboard:**
- Employees can log in to view and manage orders.
- Employees can update the status of orders (Pending, Picked Up, Rejected).

### **Order Management:**
- Customers can place orders, select pizzas, and choose the quantity.
- Employees can track and manage orders, ensuring a smooth process from order placement to fulfillment.

### **API Features:**
- Fully RESTful API built using Django Rest Framework (DRF).
- Separate API endpoints for managing customers, employees, and orders.
- Swagger-based API documentation using `drf-spectacular`.

---

## **Technologies 💻 **
- **Python** 3.11
- **Django** 5.1.1
- **Django Rest Framework** (DRF)
- **PostgreSQL** for production database
- **SQLite** for local development
- **Docker** for containerization
- **Swagger** for API documentation
- **Pytest** for testing

---

## **Prerequisites 💾**
- **Python 3.11** or later
- **Docker** and **Docker Compose**
- PostgreSQL (for production)
- Basic understanding of Django and Docker

---

## **Installation 🔧**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/Pizzeria_Pasquali.git
cd Pizzeria_Pasquali
```

### **2. Install Dependencies**
If you're running the project locally without Docker, use **Pipenv** to install the dependencies:
```bash
pipenv install
pipenv shell  t
```

### **3. Set Up Environment Variables**
Create an `.env` file in the project root and define the following variables:
```bash
DEBUG=True
SECRET_KEY='your-secret-key'
DATABASE_URL=postgres://user:password@localhost:5432/pizzeria_db  
```

---

## **Running the Project 🏃**

### **Local Development**
1. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

---

## **Docker Setup 🐳**

### **1. Build and Run the Docker Containers**
The project comes with a **Dockerfile** for both local and production environments.

For **local development**:
```bash
docker-compose -f docker-compose.local.yml up --build
```

For **production**:
```bash
docker-compose -f docker-compose.production.yml up --build -d
```

### **2. Access the Application**
Once the server is running, access the app at:
- **Local:** `http://127.0.0.1:8000`
- **Production:** Based on your deployment setup.

---

## **Usage 🧑‍💻**

### **Customer Usage**
1. **Register/Login**: Visit the `/register` or `/login` pages to create an account or log in.
2. **Place Orders**: Browse pizzas and place orders from the customer dashboard.
3. **Order History**: View previous orders and request changes to pending ones (when they arrive)

### **Employee Usage**
1. **Login**: Employees must log in using the employee credentials.
2. **Manage Orders**: Employees can view all orders and update their status from the employee dashboard.

---

## **API Endpoints 🚕**

- **Swagger API Documentation**: `/docs`
- **Order Management**:
    - `GET /orders/`: List all orders.
    - `POST /orders/place_order/`: Place an order.
    - `GET /orders/customer_orders/`: View customer orders.
---

## **Running Tests 📋✅**

To run tests using **pytest**:
```bash
pytest
```
Ensure that test cases cover both customer and employee functionalities, as well as the API endpoints.

---

## **Environment Variables 🌳**

Create environment variables in the `.env` file or pass them directly in your Docker Compose YAML files. Key variables include:
- `SECRET_KEY`
- `DATABASE_URL`
- `DEBUG`
- `ALLOWED_HOSTS`

---

## **File Structure 🚧**

```
Pizzeria_Pasquali/
│
├── api/
│   ├── customers/
│   ├── employees/
│   ├── orders/
│   └── pizzas/
├── manage.py
├── Dockerfile
├── docker-compose.local.yml
├── docker-compose.production.yml
├── Pipfile
├── Pipfile.lock
├── README.md
└── Pizzeria_Pasquali/
    ├── settings/
    │   ├── base.py
    │   ├── local.py
    │   └── production.py
    └── urls.py
```

---

## **Contributing 👍**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/feature-name`).
5. Create a new Pull Request.

---

## **License **

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to adjust the URLs, images, and sections based on the final state of your project. This README covers everything from installation and usage to contributing and running tests, ensuring a smooth experience for developers and users alike!