import tkinter as tk


class calc:

    # colors = {"bg": "#007BA4", "main_frame": "#0DA7BF", "txt": "#ffffff"}
    # colors = {"bg": "#0F172A", "main_frame": "#1E293B", "txt": "#F8FAFC"}
    # colors = {"bg": "#1C1917", "main_frame": "#292524", "txt": "#FFF7ED"}
    # colors = {"bg": "#0F172A", "main_frame": "#1E293B", "txt": "#F8FAFC"}
    colors = {"bg": "#0B2E26", "main_frame": "#145A4A", "txt": "#E8FFF5"}
    res_text = ""
    display_font = ("Consolas", 30)
    button_font = ("Segoe UI", 11)
    operator_font = ("Segoe UI", 16, "bold")

    def __init__(self, root):
        self.root = root
        self.root.title("Kamyar Calculator")
        self.root.geometry("450x600")
        self.root.configure(bg=self.colors["bg"])
        self.root.resizable(False, False)

        self.build_output_frame()

    def build_output_frame(self):
        self.output_frame = tk.Frame(
            self.root, bg=self.colors["main_frame"], width=50, height=7
        )
        self.output_lbl = tk.Label(
            self.output_frame,
            text="output Lable",
            font=self.display_font,
            fg=self.colors["txt"],
            bg=self.colors["main_frame"],
        )

        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.output_lbl.pack(padx=5, pady=10, side="right")
        self.build_button_frame()

    def build_button_frame(self):
        self.button_frame = tk.Frame(
            self.root, width=50, height=18, bg=self.colors["main_frame"]
        )
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        row1 = ["AC", "%", "<-", "/"]
        row2 = [7, 8, 9, "*"]
        row3 = [4, 5, 6, "-"]
        row4 = [1, 2, 3, "+"]
        row5 = ["00", 0, ".", "="]

        rows = [row1, row2, row3, row4, row5]

        for i in range(5):
            for j in range(4):
                tk.Button(
                    self.button_frame,
                    font=self.button_font,
                    width=10,
                    height=3,
                    text=rows[i][j],
                    command=lambda txt=rows[i][j]: self.processing(txt),
                    bg=self.colors["bg"],
                    fg=self.colors["txt"],
                ).grid(row=i, column=j, padx=6, pady=6)

    def processing(self, txt):
        if txt == "AC":
            self.output_lbl.config(text="0")
            self.res_text = ""
        elif txt == "<-":
            self.res_text = self.res_text[0:-1]
            self.output_lbl.config(text=self.res_text if self.res_text else "0")
        elif txt == "=":
            try:
                self.result = eval(self.res_text)
                self.output_lbl.config(text=self.result)
                self.res_text = ""
            except:
                self.res_text = ""
                self.output_lbl.config(text="0")
        else:
            self.output_lbl.config(text=f"{self.res_text}{txt}")
            self.res_text = self.res_text + str(txt)


def main():
    root = tk.Tk()
    calc(root)
    root.mainloop()


if __name__ == "__main__":
    main()
