import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Grafik:
    def __init__(self, restart_callback):
        self.restart_callback = restart_callback
        self.root = tk.Tk()
        self.root.title("Eğitim Grafiği")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

        grafik_konumu = os.path.join(os.getcwd(), "Grafik")
        if not os.path.exists(grafik_konumu):
            os.makedirs(grafik_konumu)

        self.resim_listesi = [
            os.path.join(grafik_konumu, f"{i}.jpeg")
            for i in range(1, 11)
        ]

        self.app = self.ResimGosterici(self.root, self.resim_listesi)
        
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        self.restart_callback()

    class ResimGosterici:
        def __init__(self, root, resim_listesi):
            self.root = root
            self.resim_listesi = resim_listesi
            self.gecerli_indeks = 0

            self.resim_etiketi = ttk.Label(self.root)
            self.resim_etiketi.pack()

            self.geri_buton = ttk.Button(self.root, text="<< Geri", command=self.onceki_resim)
            self.geri_buton.pack(side=tk.LEFT)

            self.ileri_buton = ttk.Button(self.root, text="İleri >>", command=self.sonraki_resim)
            self.ileri_buton.pack(side=tk.RIGHT)

            self.resim_referanslari = []
            self.resmi_goster(self.gecerli_indeks)

        def resmi_goster(self, indeks):
            resim_yolu = self.resim_listesi[indeks]
            if os.path.exists(resim_yolu):
                image = Image.open(resim_yolu)
                image = image.resize((600, 600), Image.LANCZOS)
                self.photo = ImageTk.PhotoImage(image)
                self.resim_etiketi.config(image=self.photo)
                self.resim_referanslari.append(self.photo)  # Referansı sakla
            else:
                self.resim_etiketi.config(text=f"Resim bulunamadı: {resim_yolu}")

        def sonraki_resim(self):
            if self.gecerli_indeks < len(self.resim_listesi) - 1:
                self.gecerli_indeks += 1
                self.resmi_goster(self.gecerli_indeks)

        def onceki_resim(self):
            if self.gecerli_indeks > 0:
                self.gecerli_indeks -= 1
                self.resmi_goster(self.gecerli_indeks)

if __name__ == "__main__":
    Grafik(lambda: print("Yeniden Başlat!"))
