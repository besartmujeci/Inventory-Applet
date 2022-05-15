import sqlite3
import pandas as pd
from os.path import exists


class Item:
    LATEST_ID = 0

    def __init__(self, label, count, image):
        self._id = str(Item.LATEST_ID)
        self._label = label
        self._count = count
        self._image = image

    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def count(self):
        return self._count

    @property
    def image(self):
        return self._image

    @label.setter
    def label(self, label):
        self._label = label

    @count.setter
    def count(self, count):
        if count < 0:
            self._count = count

    def create_item(self):
        self.count = self.count(self.count)
        quick_connect = sqlite3.connect("inventory.db")
        with quick_connect:
            quick_connect.cursor().execute(
                "INSERT INTO inventory VALUES (:id, :label, :count, :image)",
                {'id': self.id, 'label': self.label, 'count': self.count,
                 'image': self.image}
            )

    def update_item(self, db_id):
        self.count = self.count(self.count)
        quick_connect = sqlite3.connect("inventory.db")
        with quick_connect:
            quick_connect.cursor().execute(
                "UPDATE inventory SET label = (:label), count = (:count),"
                " image = (:image) WHERE id = (:id)",
                {'label': self.label, 'count': self.count, 'image': self.image,
                 'id': db_id}
            )

    @staticmethod
    def create_DB():
        if not exists("inventory.db"):
            quick_connect = sqlite3.connect("inventory.db")
            quick_connect.cursor().execute(
                """CREATE TABLE inventory (
                                id text,
                                label text,
                                count integer,
                                image text
                                )"""
            )
            quick_connect.close()

    @staticmethod
    def delete_item(db_id):
        quick_connect = sqlite3.connect("inventory.db")
        with quick_connect:
            quick_connect.cursor().execute(
                "DELETE FROM inventory WHERE id = (:id)", {'id': db_id}
            )


    @staticmethod
    def get_all():
        quick_connect = sqlite3.connect("inventory.db")
        with quick_connect:
            return quick_connect.cursor(). \
                execute("SELECT * FROM inventory").fetchall()

    @staticmethod
    def get_csv():
        quick_connect = sqlite3.connect("inventory.db")
        with quick_connect:
            df = pd.read_sql_query("SELECT * FROM inventory", quick_connect)
            df.to_csv("inventory.csv", index=False)

    @staticmethod
    def card_html():
        return """
        <div id={id} style='width:400px; height:500px; border: solid white;'>
            <div>
                <img src='{image}' alt='NO IMG' width=395px height=400px>
            </div>
            <div style='text-align:center'>{label}</div>
            <div style='text-align:center'>Inventory Count: {count}</div>
            <div style='text-align:center'>Item ID: {visible_id}</div>
        </div>"""
