import mysql.connector
import streamlit as st
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
#connection to databse
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital_management_system"
)
cursor = connection.cursor()
#login page
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
if st.session_state.page == "login":
    st.title("Login Page")
    st.header("Hospital Management System")
    name = st.text_input("Enter name")
    password = st.text_input("Enter password", type="password")
    role = st.selectbox("Select role", ["doctor", "patient"])
    login = st.button("Login")
    #register page
    register = st.button("register if new user")
    if register:
        st.session_state.page = "register"
        st.rerun()
#patient dashboard
    if login:
        if role == "patient":
            cursor.execute(
                "select * from patients where patient_name=%s and password=%s",(name, password))
            result = cursor.fetchone()
            if result:
                # st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.name = name
                st.session_state.patient_id = result[0]
                st.success("Login Successful")
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Check name or password")
        elif role == "doctor":
            cursor.execute(
                "select * from doctors where doctor_name=%s and password=%s",
                (name, password)
            )
            result = cursor.fetchone()
            if result:
                # st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.name = name
                st.success("Login Successful")
                st.session_state.page = "dashboard"
                st.rerun()
elif st.session_state.page == "register":
    st.subheader("Register New User")
    reg_role=st.selectbox("role", ["Patient", "Doctor"])
    if reg_role == "Patient":
        reg_name=st.text_input("name")
        reg_password=st.text_input("password", type="password")
        reg_age=st.number_input("age", min_value=1, max_value=120)
        reg_gender=st.selectbox("gender", ["male", "female"])
        reg_bp=st.number_input("bp", min_value=0)
        reg_sugar=st.number_input("sugar", min_value=0)
        reg_risk=st.selectbox("risk", ["low", "high"])  
        reg_disease=st.text_input("disease")
        new_acc=st.button("create patient account")
    else:
        reg_name=st.text_input("name")
        reg_password=st.text_input("password", type="password")
        reg_spec=st.text_input("specialization")
        new_acc=st.button("create doctor account")
    if new_acc:
        if reg_role == "Patient":
            cursor.execute("insert into patients(patient_name,password,age,gender,bp,sugar,risk,disease) values(%s,%s,%s,%s,%s,%s,%s,%s)", (reg_name, reg_password, reg_age, reg_gender, reg_bp, reg_sugar, reg_risk, reg_disease))
            connection.commit()
        elif reg_role == "Doctor":
            cursor.execute("insert into doctors(doctor_name,password,specialization) values(%s,%s,%s)", (reg_name, reg_password, reg_spec))
            connection.commit()
        st.success("account created")
        st.session_state.page = "login"
        st.rerun()
# Logged in dashboards
else:
    st.success("Logged in successfully")
# prediction
    if st.session_state.role=="patient":
        data=load_diabetes()
        X=data.data[:, [0, 1, 2, 3, 4, 9]]
        y=data.target
        y=(y > y.mean()).astype(int)
        model=LogisticRegression()
        model.fit(X, y)
        st.subheader("Patient Dashboard")
        st.write("Welcome", st.session_state.name)
        age=st.number_input("age")
        sex=st.selectbox("gender (0:female,1:male)",[0, 1])
        bmi=st.number_input("bmi")
        bp=st.number_input("bp")
        s1=st.number_input("cholesterol ")
        s6=st.number_input("sugar ")
        predict=st.button("predict")
        if predict:
            inputdata=np.array([[age, sex, bmi, bp, s1, s6]])
            result=model.predict(inputdata)
            if result[0]==1:
                st.error("high risk")
            else:
                st.success("low risk")
        cursor.execute("select doctor_id, doctor_name from doctors")
        doctors=cursor.fetchall()
        doctor_choice=st.selectbox("select doctor for appointment", doctors)
        selected_doctor_id=doctor_choice[0]
        request = st.button("Request Appointment")
        if request:
            cursor.execute(
                "insert into appointments (doctor_id, patient_id, status) values (%s, %s, %s)",(selected_doctor_id, st.session_state.patient_id, "pending"))
            connection.commit()
            st.success("Appointment Requested")
            #doctor dash board
    elif st.session_state.role=="doctor":
        st.subheader("Doctor Dashboard")
        st.write("Welcome",st.session_state.name)
        cursor.execute("SELECT patient_id, patient_name, age, bp, sugar, risk, disease, gender FROM patients")
        patients_data=cursor.fetchall()
        df=pd.DataFrame(patients_data, columns=["patient_id","patient_name","age","bp","sugar","risk","disease","gender"])
        high_bp=st.checkbox("High BP (>140)")
        high_sugar=st.checkbox("High Sugar (>150)")
        male=st.checkbox("male")
        female=st.checkbox("Female")
        risk=st.checkbox("High Risk")
        filtered_df=df.copy()
        if high_bp:
            filtered_df=filtered_df[filtered_df["bp"] > 140]
        if high_sugar:
            filtered_df=filtered_df[filtered_df["sugar"] > 150]
        if male:
            filtered_df=filtered_df[filtered_df["gender"] == "male"]
        if female:
            filtered_df=filtered_df[filtered_df["gender"] == "female"]
        if risk:
            filtered_df=filtered_df[filtered_df["risk"] == "high"]
        gb = GridOptionsBuilder.from_dataframe(filtered_df)
        gridOptions = gb.build()
        AgGrid(filtered_df, gridOptions=gridOptions)
        st.subheader("Appointment Requests")
        cursor.execute(
            "select a.appointment_id, p.patient_name, a.status from appointments as a join patients as p on a.patient_id=p.patient_id where a.doctor_id=(select doctor_id from doctors where doctor_name=%s) and a.status='pending'",
            (st.session_state.name,)
        )
        appointments = cursor.fetchall()
        for appointment in appointments:
            app_id = appointment[0]
            patient_name = appointment[1]
            st.write(f"**Patient:** {patient_name}|**Appointment ID:** {app_id}")
            col1,col2=st.columns(2)
            with col1:
                if st.button(f"approve",key=f"approve_{app_id}"):
                    cursor.execute("update appointments set status='accepted' where appointment_id=%s",(app_id,))
                    connection.commit()
                    st.success("appointment accepted")
                    st.rerun()
            with col2:
                if st.button(f"reject", key=f"reject_{app_id}"):
                    cursor.execute("update appointments set status='rejected'where appointment_id=%s",(app_id,))
                    connection.commit()
                    st.error("appointment rejected")
                    st.rerun()