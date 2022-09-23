from multiprocessing.sharedctypes import Value
from turtle import update
import flet 

from flet import IconButton, Page, Row, Text, TextField, View, icons

def main (page: Page):
    page.title= "Flet Page Counter Example"

    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="center")

    def minus_number (e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def add_number  (e):
        txt_number.value = int(txt_number.value) + 1
        page.update()


    page.add(Row([
        IconButton(icons.REMOVE,  on_click=minus_number),
        txt_number,
        IconButton(icons.ADD, on_click=add_number)   
    ]))

flet.app(target=main)