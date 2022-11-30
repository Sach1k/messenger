import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("sweetkind")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
window.geometry("400x580")
window.title("Telegramm2")

vvod = customtkinter.CTkEntry(master=window, placeholder_text="Ведите текст", placeholder_text_color='grey',width=200)
vvod.place(y = 530, x = 100)

window.mainloop()
