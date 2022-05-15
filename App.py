import streamlit as st
from Item import Item


def run():
    if 'id' not in st.session_state:
        st.session_state.id = 0
    else:
        Item.LATEST_ID = st.session_state.id
    if 'db' not in st.session_state:
        st.session_state.db = True
        Item.create_DB()
    interface()


def interface():
    header()
    button_sequence()


def header():
    cols = st.columns(3)
    cols[1].write(
        "<h1 style='font-weight: bold; font-size: 55px'>INVENTORY</h1>",
        unsafe_allow_html=True)


def button_sequence():
    cols = st.columns(3)
    download_button = cols[1].button("Download CSV")
    cols = st.columns(2)
    user_input_create = cols[0].text_input("Enter a new item in the form: "
                                           " LABEL; COUNT; IMAGE_URL")
    create_button = cols[0].button("CREATE")
    user_input_delete = cols[1].text_input("Enter the ID of the item"
                                           " you wish to delete:")
    delete_button = cols[1].button("DELETE")
    user_input_edit = st.text_input("Enter the ID of the item you wish to edit"
                                    " and the information in the form:"
                                    " ID; LABEL; COUNT; IMAGE_URL")
    edit_button = st.button("EDIT")
    if create_button and user_input_create:
        split_input = [item.strip() for item in user_input_create.split(";")]
        st.session_state.id += 1
        Item(split_input[0], split_input[1], split_input[2]).create_item()
        st.write("Item created.")
    if download_button:
        Item.get_csv()
        st.write("CSV downloaded successfully.")
    if delete_button and user_input_delete:
        Item.delete_item(user_input_delete)
        st.write("Item deleted.")
    if edit_button and user_input_edit:
        split_input = [item.strip() for item in user_input_edit.split(";")]
        Item(split_input[1], split_input[2],
             split_input[3]).update_item(split_input[0])
        st.write("Item updated.")
    display_items()


def display_items():
    rows = Item.get_all()
    i = 0

    while i < len(rows):
        cols = st.columns(3)
        cols[0].write(Item.card_html().format(id=rows[i][0], label=rows[i][1],
                                              count=rows[i][2],
                                              visible_id=rows[i][0],
                                              image=rows[i][3]),
                      unsafe_allow_html=True)
        if i + 1 < len(rows):
            i += 1
            cols[2].write(
                Item.card_html().format(id=rows[i][0], label=rows[i][1],
                                        count=rows[i][2],
                                        visible_id=rows[i][0],
                                        image=rows[i][3]),
                unsafe_allow_html=True)
        i += 1
        st.columns(1)


if __name__ == '__main__':
    run()
