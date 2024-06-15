import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageViewer(tk.Tk):
    def __init__(self, folder_path, callback):
        super().__init__()
        self.callback = callback
        self.title("Fotoğraf Tespiti")
        self.geometry("900x700")

        self.folder_path = folder_path
        self.image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        self.image_files.sort()  # Sort files alphabetically
        self.current_index = 0

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.image_label = ttk.Label(self)
        self.image_label.pack(expand=True)

        self.prev_button = ttk.Button(self, text="<< Geri", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, expand=True)

        self.next_button = ttk.Button(self, text="İleri >>", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, expand=True)

        self.show_image()

    def show_image(self):
        if self.image_files:
            image_path = os.path.join(self.folder_path, self.image_files[self.current_index])
            image = Image.open(image_path)
            image = image.resize((800, 600), Image.Resampling.LANCZOS)  # Resize image to fit window
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.config(text="Resim Bulunamadı.")

    def show_previous_image(self):
        if self.image_files:
            self.current_index = (self.current_index - 1) % len(self.image_files)
            self.show_image()

    def show_next_image(self):
        if self.image_files:
            self.current_index = (self.current_index + 1) % len(self.image_files)
            self.show_image()

    def on_closing(self):
        self.destroy()
        self.callback()

def Veriseti(callback):
    folder_path = "C:/Users/SARGIN/Desktop/derinogr_kod/yolov5/runs/detect/exp"
    app = ImageViewer(folder_path, callback)
    app.mainloop()
