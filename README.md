# ⚡ Electricity Bill Calculator

A full-stack Electricity Bill Calculator web application built using **Django REST Framework**, **JavaScript**, **Bootstrap 5**, and **SQLite**.

The application allows users to enter their customer name and electricity units consumed. It calculates the electricity bill based on different unit slabs, adds fixed charges and tax, displays the complete bill breakdown, and stores the bill details in the Django backend.

---

## 🚀 Features

- Enter customer name
- Enter electricity units consumed
- Calculate electricity charges based on unit slabs
- Apply fixed charges
- Calculate 5% tax
- Display subtotal and total bill
- Display usage messages:
  - Low Usage
  - Normal Usage
  - High Usage
- Responsive Bootstrap 5 interface
- Django REST API backend
- Store bill records in SQLite database
- View saved bills through Django Admin
- Print bill functionality
- Input validation for customer name and units

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Backend
- Python
- Django
- Django REST Framework

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Live Server

---

## 📁 Project Structure

```text
electricity/
│
├── bills/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── electricity/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── manage.py
├── db.sqlite3
└── README.md
```
## 💰 Electricity Bill Calculation

The electricity bill is calculated using progressive unit slabs.
| Units Consumed | Energy Rate | Fixed Charge |
|---|---:|---:|
| 0–100 | ₹1.50/unit | ₹50 |
| 101–200 | ₹2.50/unit for units above 100 | ₹75 |
| 201–500 | ₹4.00/unit for units above 200 | ₹100 |
| Above 500 | ₹6.00/unit for units above 500 | ₹150 |

### Tax

A 5% tax is applied to the subtotal.
```text
Subtotal = Energy Charge + Fixed Charge
Tax = Subtotal × 5%
Total Bill = Subtotal + Tax
```

### 📊 Usage Messages

The application displays a message based on electricity consumption:
| Units |	Usage Message |
|---|---|
| 0 - 100 |	Low Usage |
| 101 - 300 |	Normal Usage |
| Above 300	| High Usage |

## 🔌 API Endpoints
Calculate and Save Bill
```text
POST /api/calculate-bill/
```
Get Saved Bills
```text
GET /api/bills/
```
Django Admin
```text
/admin/
```
## 🔄 Application Flow

```text
User enters customer name and units
                ↓
        JavaScript validates input
                ↓
        Frontend sends POST request
                ↓
       Django REST Framework API
                ↓
       Django calculates the bill
                ↓
       Bill is saved in SQLite
                ↓
       API returns bill details
                ↓
       Frontend displays the bill
```
