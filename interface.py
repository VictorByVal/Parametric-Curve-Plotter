
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("800x350")
window.configure(bg="#FFFFFF")


Entry_id7 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Step ",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id7.place(x=590, y=90)
Entry_id6 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Inferior Limit",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id6.place(x=590, y=50)
Entry_id5 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Upper Limit",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id5.place(x=590, y=10)
Entry_id4 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Insert f(g) function",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id4.place(x=240, y=20)
Entry_id2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Insert f(t) function",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id2.place(x=30, y=20)
Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Plot",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id1.place(x=650, y=250)



#run the main loop
window.mainloop()