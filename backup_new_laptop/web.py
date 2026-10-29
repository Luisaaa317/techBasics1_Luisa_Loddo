import streamlit as st


def update_count():
    st.session_state.click_count += 1

def update_todo(todo_item):
    st.session_state.todo_list.append(todo_item)

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = ["Breakfast", "Grocery Shopping", "TechBasics 1"]

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🌙")


st.title("To-Do List")
st.write("---")

container = st.container(border=False, horizontal=True, horizontal_alignment="center", vertical_alignment="bottom", gap="medium")
with container:
    user_input = st.text_input(label="Add something", key="user_input")
    st.button("+ Add to list", on_click=update_todo)


for item in enumerate(st.session_state.todo_list):
    print(index, item)
    st.checkbox(item, key=index)
