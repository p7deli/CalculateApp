import customtkinter as tk

class Calculate(tk.CTk):
    def __init__(self):
        super().__init__()
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("blue")
        self.geometry("815x585")
        self.resizable(width=False, height=False)
        
        self.title('Application CALCULATOR')

        self.frame_window = tk.CTkFrame(self)
        self.frame_window.grid(row=0, pady=10, padx=50)

        self.Label_name = tk.CTkLabel(self.frame_window, text="Calculator",
                                   font=("Arial", 50, "bold"))
        self.Label_name.grid(row=0, column=0, pady=50, padx=100)
        self.Text_box = tk.CTkEntry(self.frame_window, width=600,
                                    height=50, font=("Arial", 30)
                                    , placeholder_text="Enetr number ...")
        self.Text_box.grid(row=1, ipadx=40, ipady=20, padx=10, pady=10)

        self.button_frame = tk.CTkFrame(self)
        self.button_frame.grid(row=1, pady=10, padx=50)

        self.create_button("1", self.button_frame, 0, 0, lambda: self.add_number(1))
        self.create_button("2", self.button_frame, 0, 1, lambda: self.add_number(2))
        self.create_button("3", self.button_frame, 0, 2, lambda: self.add_number(3))
        self.create_button("4", self.button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button("5", self.button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button("6", self.button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button("7", self.button_frame, 2, 0, lambda: self.add_number(7))
        self.create_button("8", self.button_frame, 2, 1, lambda: self.add_number(8))
        self.create_button("9", self.button_frame, 2, 2, lambda: self.add_number(9))
        self.create_button("0", self.button_frame, 3, 1, lambda: self.add_number(0))
        self.create_button("+", self.button_frame, 0, 3,
                           lambda: self.add_operation("+"), "black")
        self.create_button("-", self.button_frame, 1, 3,
                           lambda: self.add_operation("-"), "black")
        self.create_button("*", self.button_frame, 2, 3,
                           lambda: self.add_operation("*"), "black")
        self.create_button("/", self.button_frame, 3, 3,
                           lambda: self.add_operation("/"), "black")
        self.create_button("=", self.button_frame, 3, 2, self.calculate, "green")
        self.create_button("C", self.button_frame, 3, 0, self.clear, "red")

    def create_button(self, text, frame, row, column, command, bg='grey', text_color='white'):
        self.Button = tk.CTkButton(frame, text=text, command=command, font=("Arial", 18),
                              width=155, height=50, fg_color=bg, text_color=text_color)
        self.Button.grid(row=row, column=column, padx=10, pady=10)

    def add_number(self, number):
        current = self.Text_box.get()
        current += str(number)
        self.Text_box.delete(0, tk.END)
        self.Text_box.insert(0, current)

    def add_operation(self, operator):
        current = self.Text_box.get()
        current += operator
        self.Text_box.delete(0, tk.END)
        self.Text_box.insert(0, current)

    def calculate(self):
        current = self.Text_box.get()
        self.Text_box.delete(0, tk.END)
        self.Text_box.insert(0, eval(current))

    def clear(self):
        self.Text_box.delete(0, tk.END)

def main():
    App = Calculate()
    App.mainloop()

if __name__ == "__main__":
    main()