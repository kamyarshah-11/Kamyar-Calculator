import tkinter as tk


class calc:

    colors = {"bg": "#007BA4", "main_frame": "#0DA7BF", "txt": "#ffffff"}

    def __init__(self, root):
        self.root = root
        self.root.title("Kamyar Calculator")
        self.root.geometry("450x600")
        self.root.configure(bg=self.colors["bg"])

        self.build_output_frame()

    def build_output_frame(self):
        self.output_frame = tk.Frame(
            self.root, bg=self.colors["main_frame"], width=50, height=7
        )
        self.output_lbl = tk.Label(
            self.output_frame,
            text="output Lable",
            font=("Arial", 15),
            fg=self.colors["txt"],
            bg=self.colors["main_frame"],
        )

        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.output_lbl.pack(side="left", padx=5, pady=10)
        self.build_button_frame()

    def build_button_frame(self):
        self.button_frame = tk.Frame(self.root, width=50, height=20)
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


def main():
    root = tk.Tk()
    calc(root)
    root.mainloop()


if __name__ == "__main__":
    main()
