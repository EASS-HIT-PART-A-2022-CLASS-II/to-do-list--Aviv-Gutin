import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
import plotly.express as px

backend = "http://backend:8080"


def main():
    st.title("ToDO List")
    menu = ["Create", "Read", "Update","Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Create Task")
        col1, col2 = st.columns(2)
        with col1:
            task = st.text_area("Task To Do")
        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Due Date")
        if st.button("Add Task"):
            data = {"task_name": task, "task_status": task_status, "task_due_date": str(task_due_date)}
            res = requests.post(f"{backend}/tasks/", json=data)
            st.success("Successfully added task {}".format(task))
    elif choice == "Read":
        st.subheader("View Task")
        res = requests.get(f"{backend}/tasks").json()
        df = pd.DataFrame(res, columns=['task_name', 'task_status', 'task_due_date'])
        df.rename(columns={"task_name": "Task Name", "task_status": "Task Status", "task_due_date": "Due Date"},
                  inplace=True)
        with st.expander("View all Tasks"):
            st.dataframe(df)
        with st.expander("Task Status"):
            task_df = df['Task Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='Task Status')
            st.plotly_chart(p1)
    elif choice == "Update":
        st.subheader("Update Task")
        res = requests.get(f"{backend}/tasks").json()
        df = pd.DataFrame(res, columns=['task_name', 'task_status', 'task_due_date'])
        df.rename(columns={"task_name": "Task Name", "task_status": "Task Status", "task_due_date": "Due Date"},
                  inplace=True)
        with st.expander("Current Data"):
            st.dataframe(df)
        list_tasks = {i["id"]: i['task_name'] for i in res}
        selected_task = st.selectbox("Task To Edit", list_tasks.keys(), format_func=lambda x: list_tasks[x])
        if selected_task:
            task = requests.get(f"{backend}/task/{selected_task}").json()
            task_id = selected_task
            task_name = task["task"]["task_name"]
            task_status = task["task"]["task_status"]
            task_due_date = task["task"]["task_due_date"]
            st.subheader("Update Task")
            col1, col2 = st.columns(2)
            with col1:
                new_task = st.text_area("Task To Do", task_name)
            with col2:
                new_task_status = st.selectbox(key=task_status, options=["ToDo", "Doing", "Done"], label='Status')
                new_task_due_date = st.date_input(label='Due Date', value=datetime.strptime(task_due_date, '%Y-%m-%d'))
            if st.button("Update Task"):
                data = {"task_name": new_task, "task_status": new_task_status, "task_due_date": str(new_task_due_date)}
                res = requests.put(f"{backend}/task/{task_id}", json=data)
                st.success("Successfully added task {}".format(new_task))
            st.write(selected_task)
    elif choice == "Delete":
        st.subheader("Delete Task")
        res = requests.get(f"{backend}/tasks").json()
        df = pd.DataFrame(res, columns=['task_name', 'task_status', 'task_due_date'])
        df.rename(columns={"task_name": "Task Name", "task_status": "Task Status", "task_due_date": "Due Date"},
                  inplace=True)
        with st.expander("Current Data"):
            st.dataframe(df)
        list_tasks = {i["id"]: i['task_name'] for i in res}
        selected_task = st.selectbox("Task To Delete", list_tasks.keys(), format_func=lambda x: list_tasks[x])
        if st.button("Delete Task"):
            res = requests.delete(f"{backend}/task/{selected_task}")
            st.success("Successfully deleted task")

if __name__ == '__main__':
    main()
