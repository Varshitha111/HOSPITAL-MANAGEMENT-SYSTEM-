
# 🏥 Hospital Management System (Streamlit + MySQL)

## 📌 Overview

This project is a **Hospital Management System** built using:

* Python
* Streamlit (for UI)
* MySQL (for database)
* Machine Learning (Logistic Regression)

It allows:

* Patients and Doctors to **register & login**
* Patients to **predict health risk**
* Patients to **request appointments**
* Doctors to **view patients & manage appointments**

---

## 🚀 Features

### 👤 Patient

* Register and login
* Predict health risk (Low / High)
* View doctors list
* Request appointment

### 👨‍⚕️ Doctor

* Register and login
* View patient details
* Filter patients (BP, Sugar, Gender, Risk)
* Approve / Reject appointments

---

## 🧠 Machine Learning

* Dataset: Diabetes dataset from `sklearn`
* Model: Logistic Regression
* Output:

  * **High Risk**
  * **Low Risk**

---

## 🛠️ Technologies Used

* Python
* Streamlit
* MySQL
* NumPy & Pandas
* scikit-learn
* st-aggrid

---

## ⚙️ Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
```

---

### 2. Install Dependencies

```bash
pip install streamlit mysql-connector-python pandas numpy scikit-learn streamlit-aggrid
```

---

### 3. Setup MySQL Database

Create database:

```sql
CREATE DATABASE hospital_management_system;
USE hospital_management_system;
```

---

### 4. Create Tables

#### Patients Table

```sql
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(50),
    password VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    bp INT,
    sugar INT,
    risk VARCHAR(10),
    disease VARCHAR(100)
);
```

#### Doctors Table

```sql
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(50),
    password VARCHAR(50),
    specialization VARCHAR(50)
);
```

#### Appointments Table

```sql
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    status VARCHAR(20)
);
```

---

### 5. Update Database Credentials

In your Python file:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital_management_system"
)
```

---

### 6. Run the Application

```bash
streamlit run app.py
```

---

## 📊 Project Flow

1. User logs in (Doctor / Patient)
2. Patient:

   * Predicts health risk
   * Requests appointment
3. Doctor:

   * Views patient data
   * Filters data
   * Accepts/Rejects appointments

---

## 📸 Screens (Optional)

* Login Page
* Register Page
* Patient Dashboard
* Doctor Dashboard

---

## ⚠️ Limitations

* No encryption for passwords
* Uses basic ML model
* No real-time notifications

---

## 🔮 Future Enhancements

* Add password encryption
* Use advanced ML models
* Email/SMS notifications
* Add patient history tracking
* Improve UI design

---

## 👩‍💻 Author

* Varshitha (Final Year Data Science Student)

---

## ⭐ Conclusion

This project demonstrates integration of:

* Web App (Streamlit)
* Database (MySQL)
* Machine Learning

It helps in **early health risk prediction and efficient hospital management**.
