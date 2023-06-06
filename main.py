import tkinter as tk
import sqlite3


def mouse_entrou(event):
    button_note.config(image=image_button_2)


def mouse_saiu(event):
    button_note.config(image=image_button)


# Criando banco de dados
conn = sqlite3.connect("notas.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS notas (conteudo TEXT)")
conn.commit()
conn.close()

# Criando Janela
window = tk.Tk()

# Titulo e icone da janela
window.title("EasyNote")
window.iconbitmap("resources/bloco1.ico")

# Carregando foto do botao
image_button = tk.PhotoImage(file="resources/photo_button.png")
image_button_2 = tk.PhotoImage(file="resources/photo_button_2.png")

# Dimensoes da janela
window.geometry("720x480")

# Criando o frame vertical
frame_vertical = tk.Frame(window, width=150, bg="#2F7889")
frame_vertical.pack(side="left", fill="y")

# Desabilitando o redimensionamento automático do frame
frame_vertical.pack_propagate(False)

# Criando botao
button_note = tk.Button(frame_vertical, image=image_button, bd=0, highlightthickness=0, relief=tk.RAISED)
button_note.pack(pady=7)
button_note.bind("<Enter>", mouse_entrou)
button_note.bind("<Leave>", mouse_saiu)

# Criando a área de texto
text_area = tk.Text(window, bg="white", font=("Arial", 12), padx=10, pady=10)
text_area.pack(side="right", fill="both", expand=True)


# Apresentando a janela
window.mainloop()