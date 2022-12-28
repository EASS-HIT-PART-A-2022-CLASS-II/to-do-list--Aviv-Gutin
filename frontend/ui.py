import requests
import pandas as pd
import requests as requests
import streamlit as st

url = "http://backend:8080/tasks"


def load_data():
    result = requests.get(url).json()
    tasks = []
    for task in result:
        tasks.append(task["task"])
    return pd.DataFrame(
        {
            "Task name": tasks,
        }
    )


st.title("To-Do List")
df = load_data()
task_list = st.dataframe(df)


# Add new task
task_input = st.text_input("Enter a new task:")

if st.button("Add Task") and task_input != "":
    res = requests.post(url, params={"task": task_input}).json()
    data = {"Task name": [res["task"]]}
    temp_df = pd.DataFrame(data)
    task_list.add_rows(temp_df)


# Update task
task_id_input = st.number_input("Enter the task ID to update:")
update_input = st.text_input("Enter the updated task:")
if st.button("Update Task") and update_input != "" and task_id_input != "":
    update_url = "http://backend:8080/tasks/{task_id}"
    res = requests.put(update_url.format(task_id=int(task_id_input)), params={"task": update_input}).json()
    st.write(f"Task {task_id_input} updated:", update_input)


# Delete task
delete_input = st.number_input("Enter the task ID to delete:")
if st.button("Delete Task") and delete_input != "":
    delete_url = "http://backend:8080/tasks/{task_id}"
    res = requests.delete(delete_url.format(task_id=int(delete_input)))
