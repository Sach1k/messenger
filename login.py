from datebase import conn,cur
import tkinter
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("sweetkind")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
window.geometry("400x580")
window.title("login")
frame_1 = customtkinter.CTkFrame(master=window)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


password1 =customtkinter.CTkEntry(master=frame_1, placeholder_text="password", placeholder_text_color='grey',width=100)
password1.pack(pady = 50,padx = 100)
loginent1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="login", placeholder_text_color='grey',width=100)
loginent1.pack(pady = 80,padx = 100)

#register = customtkinter.CTkButton(master=frame_1,command=button_callback)
#button_1.pack(pady=12, padx=10)


window.mainloop()