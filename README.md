# Inventory Applet

<center><img src='https://user-images.githubusercontent.com/27745342/168490746-6bd1247a-e0b1-4047-9422-50d6ec75f9de.png'></center>

# Description
A rudimentary create/update/delete application with a Streamlit front-end SQLite back-end that enables a user to create/update/delete custom objects that appear as HTML cards.

## Run
1. In your IDE of choice open a terminal. 


2. Type the following command "streamlit run App.py"

    2a. This should open the app up on a local environment. Do not run the actual code in an IDE.

## Applet Navigation

*Create*

  In the associated text area above the create button, following the format LABEL; COUNT; IMAGE_URL to create a new ITEM and update the database.

*Delete*

  In the associated text area above the delete button, enter the ID of one of the inventory cards that are visible to remove an item from the database.

*Edit*

  In the associated text area above the edit button, following the format ID; LABEL; COUNT; IMAGE_URL, update the item of your choice.

*Download*

  Downloads a CSV file (local to the folder) of the current database instance.
