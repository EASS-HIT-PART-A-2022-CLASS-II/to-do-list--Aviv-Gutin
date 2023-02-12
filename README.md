# to-do-list app

This project is a to-do-list application built with:

- Docker Compose
- FastAPI
- Streamlit 

The application allows users to:

- Create a task
- Read a task
- Update a task
- Delete a task

as well as view all tasks in a list. The backend is built with FastAPI and connected to Redis for data storage. The frontend is built with Streamlit and communicates with the backend to retrieve and manipulate data.

# Prerequisites
You will need to have Docker and Docker Compose installed on your machine in order to run the application.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

## Running the Application
Clone the repository to your local machine. Then, navigate to the root of the project in the terminal and run:

```docker-compose up```

This will build the Docker images and start the containers. Once the containers are running, you can access the frontend in your web browser at
http://localhost:8501.

# How to use
Use the App
The To-do-List App is divided into five main sections, which can be accessed via the menu in the sidebar:

### Create
This section allows you to create a new task. You can enter the task name in the text area, select the task status from a dropdown menu, and select the due date from the date picker. Once you have filled in the details, click on the Add Task button to add the task.

### Read
This section displays a list of all the tasks you have created, grouped by task status. You can view all the tasks by clicking on the View all Tasks expander. You can also view the number of tasks for each task status by clicking on the Task Status expander.

### Update
This section allows you to update an existing task. Select the task you want to update from the dropdown menu. The task details will be displayed in the text area, dropdown menu, and date picker. You can update the task by changing the details in the text area, dropdown menu, and date picker. Then click on the Update Task button to save the changes.

### Delete 
This section allows you to delete an existing task. Select the task you want to delete from the dropdown menu, then click on the Delete Task button.

# Built With
- Docker Compose - A tool for defining and running multi-container Docker applications.
- FastAPI - A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Streamlit - An open-source app framework for Machine Learning and Data Science teams.
- Redis - An open source, in-memory data structure store, used as a database, cache, and message broker.

# Video
- https://youtu.be/NfPbEM4QPNk
