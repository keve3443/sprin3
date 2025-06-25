import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("AGRO.MAX")
root.geometry("400x600")
root.configure(bg="white")

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)


bottom_nav = tk.Frame(root, bg="white", height=60, bd=1, relief="raised")
bottom_nav.pack(side="bottom", fill="x")

def load_icon(path, size=(30, 30)):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

icon_inicio = load_icon("inicio.png")
icon_categorias = load_icon("lupa.png")
icon_tu = load_icon("usuario.png")
icon_carrito = load_icon("carrito.png")

def go_inicio():
    print("Inicio")

def go_categorias():
    print("Categorías")

def go_tu():
    print("Tú")

def go_carrito():
    print("Carrito")

btn_inicio = tk.Button(bottom_nav, image=icon_inicio, text="Inicio", compound="top",
                       command=go_inicio, bd=0, bg="white", activebackground="white")
btn_inicio.pack(side="left", expand=True)


btn_categorias = tk.Button(bottom_nav, image=icon_categorias, text="Buscar", compound="top",
                           command=go_categorias, bd=0, bg="white", activebackground="white")
btn_categorias.pack(side="left", expand=True)


frame_tu = tk.Frame(bottom_nav, bg="white")
frame_tu.pack(side="left", expand=True)

btn_tu = tk.Button(frame_tu, image=icon_tu, text="Usuario", compound="top",
                   command=go_tu, bd=0, bg="white", activebackground="white")
btn_tu.pack()


frame_carrito = tk.Frame(bottom_nav, bg="white")
frame_carrito.pack(side="left", expand=True)

btn_carrito = tk.Button(frame_carrito, image=icon_carrito, text="Carrito", compound="top",
                        command=go_carrito, bd=0, bg="white", activebackground="white")
btn_carrito.pack()



root.mainloop()