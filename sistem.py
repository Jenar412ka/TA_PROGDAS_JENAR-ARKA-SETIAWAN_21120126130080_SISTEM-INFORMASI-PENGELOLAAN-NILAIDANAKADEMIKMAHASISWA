import tkinter as tk
from tkinter import ttk, messagebox

MATKUL = ["Kalkulus", "Fisika", "Kimia", "Pemrograman", "Basis Data"]

class Sistem:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistem Informasi Akademik")
        self.root.geometry("900x413")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.init