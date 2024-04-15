from tkinter import *
from tkinter import Tk, ttk

# cores --------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# Janelas --------------------------
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela -------------------------------
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo= Frame(janela, width=310, height=250, bg=co2, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# Configurando frame de cima ----------------------------------
l_nome = Label(frame_cima, text='LOGIN', anchor=NE,font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

janela.mainloop()