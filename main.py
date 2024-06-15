import tkinter as tk
from tkinter import ttk
from Grafik import Grafik 
from veriseti import Veriseti

class SecimEkrani:
    def __init__(self, master):
        self.master = master
        self.master.title("Derin Öğrenme Projesi Seçim Ekranı")
        self.master.geometry("450x300")
        self.master.configure(background="white")
        tk.Label(self.master, text="Mehmet Akif Altınsoy", bg="white", fg="black", font=("Arial", 14)).pack()
        tk.Label(self.master, text="Alper SARGIN", bg="white", fg="black", font=("Arial", 14)).pack()
        tk.Label(self.master, text="Lütfen Seçim yapınız.", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Button(self.master, text="Fotoğraf Tespiti", bg="blue", fg="white", height=2, width=50, font=("Arial", 12), command=self.handle_veriseti).pack(pady=5)
        tk.Button(self.master, text="Eğitim Grafiği", bg="blue", fg="white", height=2, width=50, font=("Arial", 12), command=self.handle_grafik).pack(pady=5)

    def handle_veriseti(self):
        self.master.destroy()
        Veriseti(self.restart)

    def handle_grafik(self):
        self.master.destroy() 
        Grafik(self.restart)

    def restart(self):
        self.master = tk.Tk()
        self.__init__(self.master)
        self.master.mainloop()

def main():
    root = tk.Tk()
    secim_ekrani = SecimEkrani(root)
    root.mainloop()

if __name__ == "__main__":
    main()
