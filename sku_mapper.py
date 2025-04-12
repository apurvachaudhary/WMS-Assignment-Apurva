import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class SKUMapper:
    def __init__(self, master):
        self.master = master
        self.master.title("SKU to MSKU Mapper")
        self.mapping = {}

        self.label = tk.Label(master, text="Upload SKU Mapping File (CSV)")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(master, text="Upload", command=self.load_mapping)
        self.upload_button.pack()

        self.map_button = tk.Button(master, text="Map SKUs", command=self.map_skus)
        self.map_button.pack(pady=10)

    def load_mapping(self):
        path = filedialog.askopenfilename()
        try:
            df = pd.read_csv(path)
            self.mapping = dict(zip(df['SKU'], df['MSKU']))
            messagebox.showinfo("Success", "Mapping loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load mapping: {e}")

    def map_skus(self):
        path = filedialog.askopenfilename()
        try:
            sales = pd.read_csv(path)
            sales['MSKU'] = sales['SKU'].map(self.mapping)
            save_path = filedialog.asksaveasfilename(defaultextension=".csv")
            sales.to_csv(save_path, index=False)
            messagebox.showinfo("Done", "SKUs mapped and saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Mapping failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SKUMapper(root)
    root.mainloop()