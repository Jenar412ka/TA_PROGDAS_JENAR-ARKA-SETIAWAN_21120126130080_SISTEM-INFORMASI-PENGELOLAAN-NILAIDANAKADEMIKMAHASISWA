import sqlite3
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
        self.init_db()
        self.create_widgets()
        
    # ==== DataBase ====
    def vars(self):
        self.nim = tk.StringVar()
        self.nama = tk.StringVar()
        self.email = tk.StringVar()
        self.gender = tk.StringVar(value="Pilih")
        self.kontak = tk.StringVar()
        self.kota = tk.StringVar()
        self.fakultas = tk.StringVar()
        self.prodi = tk.StringVar()
        self.cari = tk.StringVar()
        self.matkul_var = tk.StringVar()
        
    def init_db(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim TEXT PRIMARY KEY,
                    nama TEXT,
                    email TEXT,
                    gender TEXT,
                    kontak TEXT,
                    kota TEXT,
                    fakultas TEXT,
                    prodi TEXT
                )
            """)
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS nilai (
                    nim TEXT PRIMARY KEY,
                    matkul TEXT,
                    nilai REAL,
                    PRIMARY KEY (nim, matkul),
                )
            """)
        self.conn.commit()
        
    # ===== UI =====
    def create_widgets(self):
        # Judul
        tk.Label(self.root, text="Sistem Informasi Akademik", font=("Arial", 16, "bold"), bg="#030acc", fg="white"
                ).place(x=0, y=8, width=900, height=26)
        
        # Label
        def label(text, x, y):
            tk.Label(self.root, text=text, font=("Arial", 11, "bold"), bg="#f0f0f0"
                     ).place(x=x, y=y)
       
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
        entry(self.kontak, 113, 160, 150)
        
        # Kolom Tengah
        label("Kota", 273, 68)
        entry(self.kota, 360, 70, 150)
        label("Fakultas", 273, 98)
        entry(self.fakultas, 360, 100, 150)
        label("Prodi", 273, 128)
        entry(self.prodi, 360, 130, 150)
        label("Gender", 273, 158)
        ttk.Combobox(self.root, textvariable=self.gender, values=("Pilih", "Laki-laki", "Perempuan"), state="readonly",
            font=("Arial", 10, "bold"), justify="center").place(x=360, y=160, width=150, height=22)
        
        # Tombol
        def button(text, color, x, cmd):
            tk.Button(self.root, text=text, bg=color, fg="white", font=("Arial", 11, "bold"), cursor="hand2", bd=0,
                      command=cmd, activebackground=color, activeforeground="white"
                      ).place(x=x, y=320, width=82, height=29)
            
        button("Simpan", "#4eef76", 113, self.simpan)
        button("Reset", "#2da5dc", 203, self.reset)
        button("Hapus", "#f54242", 293, self.hapus)
        button("Clear", "#474746", 383, self.clear)
        
        # Panel Kanan: Cari
        label("NIM", 542, 68) 
        entry(self.cari, 640, 70, 150)
        tk.Button(self.root, text="Cari", command=self.cari_data, bg="#2da5dc"
                  , fg="white", font=("Arial", 11, "bold"), cursor="hand2", bd=0).place(x=803, y=68, width=90, height=22)
        
        # Panel Kanan: Input Nilai
        label("Mata Kuliah", 542, 98)
        ttk.Combobox(self.root, textvariable=self.matkul_var, values=MATKUL
                    ).place(x=542, y=118, width=170, height=22)
        label("Nilai", 725, 98)
        entry(self.nilai, 725, 118, 60)
        tk.Button(self.root, text="Tambah Nilai", command=self.simpan_nilai, bg="#4eef76"
                  , fg="white", font=("Arial", 9, "bold"), cursor="hand2", bd=0).place(x=797, y=117, width=96, height=24)
        tk.Button(self.root, text="Hapus Nilai", command=self.hapus_nilai, bg="#f54242"
                  , fg="white", font=("Arial", 9, "bold"), cursor="hand2", bd=0).place(x=797, y=148, width=96, height=24)
        
        label("Daftar Nilai", 542, 158)
        
        # Tabel Nilai
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(x=542, y=178, width=352, height=245)
        self.tree = ttk.Treeview(frame, columns=("Nama", "NIM"), show="tree headings")
        self.tree.heading("#0", text="Nama")
        self.tree.heading("#1", text="NIM")
        self.tree.heading("#2", text="Nilai")
        self.tree.column("#0", width=170, anchor="center")
        self.tree.column("#1", width=80, anchor="center")
        self.tree.column("#2", width=70, anchor="center")
        self.tree.tag_configure("avg", background="#f0f0f0",
                                font=("Arial", 9, "bold"))
        sb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.bind("<ButtonRelease-1>", self.on_click)
        
    # ==== Main Program ====
    def data(self):
        return {
            "nim": self.nim.get().strip(),
            "nama": self.nama.get().strip(),
            "email": self.email.get().strip(),
            "gender": self.gender.get(),
            "kontak": self.kontak.get().strip(),
            "kota": self.kota.get().strip(),
            "fakultas": self.fakultas.get().strip(),
            "prodi": self.prodi.get().strip()
        }

    def cek_data(self, nim):
        return self.cursor.execute("SELECT 1 FROM mahasiswa WHERE nim=?", 
                                   (nim,)).fetchone() is not None
        
    # ==== CRUD Mahasiswa ==== 
    def save(self):
        

if __name__ == "__main__":
    root = tk.Tk()
    Sistem(root)
    root.mainloop()