import streamlit as st

st.set_page_config(page_title="Student Task Planner", page_icon="📚")

st.title("Student Task Planner")
st.write("Plan your study tasks and track your progress!")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.subheader("+ Add a New Task")

task_name = st.text_input("What do you want to study?")
subject = st.selectbox("Choose a subject", ["Python", "Linear Algebra", "DBMS", "Data Ethics", "Git & GitHub", "Other"])
priority = st.selectbox("Choose priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if task_name.strip(): 
        st.session_state.tasks.append({
            "task" : task_name.strip(),
            "subject" : subject,
            "priority" : priority,
            "done" : False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task name.")

st.divider()
st.subheader("My Tasks")

tasks = st.session_state.tasks

if not tasks:
    st.info("No tasks added yet. Add your first study task above!")
else:
    for index, task in enumerate(tasks):
        task["done"] = st.checkbox(
            f'{task["task"]} - {task["subject"]} '
            f'({task["priority"]} priority) ',
            value=task["done"],
            key=f"task_{index}"
        )

    total_tasks = len(tasks)
    completed_tasks = sum(task["done"] for task in tasks)
    remaining_tasks = total_tasks - completed_tasks

    st.divider()
    st.subheader("My Progress")

    st.metric("Total Tasks", total_tasks)
    st.metric("Completed", completed_tasks)
    st.metric("Remaining", remaining_tasks)

    progress = completed_tasks / total_tasks
    st.progress(progress)
    st.write(f"You have completed {progress:.0%} of your tasks!")

    if completed_tasks == total_tasks:
        st.success("Amazing! You completed all your tasks!")