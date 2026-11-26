import tkinter as tk
from tkinter import ttk, messagebox

MATKUL = ["Kalkulus", "Fisika", "Kimia", "Pemrograman", "Basis Data"]

class Sistem:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistem Informasi Akademik")
        self.root.geometry("900x440")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.vars()
        self.create_widgets()
        
    # ==== DataBase ===
    def vars(self):
        self.nim = tk.StringVar()
        self.nama = tk.StringVar()
        self.email = tk.StringVar()
        self.gender = tk.StringVar()
        self.kontak = tk.StringVar()
        self.kota = tk.StringVar()
        self.fakultas = tk.StringVar()
        self.prodi = tk.StringVar()
        
    # ===== UI =====
    def create_widgets(self):
        # Judul
        tk.Label(self.root, text="Sistem Informasi Akademik", font=("Arial", 16, "bold"), bg="#030acc", fg="white"
                 ).place(x=0, y=8, width=900, height=26)
        
        # Label
        def label(text, x, y):
            tk.Label(self.root, text=text, font=("Arial", 11, "bold"), bg="#f0f0f0").place(x=x, y=y)
       
       # Entry
        def entry(var, x, y, w):
            e = tk.Entry(self.root, textvariable=var, 
                         font=("Arial", 10),relief="solid", bd=1)
            e.place(x=x, y=y, width=w, height=22)
            return e
      
        # Kolom Kiri
        label("Nama", 10, 68)
        entry(self.nama, 113, 70, 150)
        label("NIM", 10, 98)
        entry(self.nim, 113, 100, 150)
        label("Email", 10, 128)
        entry(self.email, 113, 130, 150)
        label("Kontak", 10, 158)
        entry(self.kontak, 113, 160, 112)
        label("Gender", 10, 188)
        ttk.Combobox(self.root, textvariable=self.gender, values=("Laki-laki", "Perempuan"), state="readonly",
                    font=("Arial", 10, "bold"), justify="center").place(x=113, y=190, width=150, height=22)
        
        # Kolom Tengah
        label("Kota", 273, 68)
        entry(self.kota, 360, 70, 150)
        label("Fakultas", 273, 98)
        entry(self.fakultas, 360, 100, 150)
        label("Prodi", 273, 128)
        entry(self.prodi, 360, 130, 150)

if __name__ == "__main__":
    root = tk.Tk()
    Sistem(root)
    root.mainloop()