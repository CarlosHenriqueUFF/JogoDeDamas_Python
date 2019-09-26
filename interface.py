# -*- coding: cp1252 -*-
import jogoDeDamas
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import * 



root = Tk()
frame = Frame(root)
frame.pack()

photoMinComum =PhotoImage(file="minComum.gif")
photoMinDama  =PhotoImage(file="minDama.gif")
photoMaxComum =PhotoImage(file="maxComum.gif")
photoMaxDama  =PhotoImage(file="maxDama.gif")
photoMinSelect =PhotoImage(file="minSelect.gif")
photoVazio =PhotoImage()

selecionado = -1
TABULEIRO = []
jdd = jogoDeDamas
photoSelect = photoMinComum

b00 = Button(frame, bg="brown", height=5, width=10, activebackground="blue")
b00.pack( side = LEFT)
b01 = Button(frame, bg="orange", height=5, width=10, activebackground="blue")
b01.pack( side = LEFT)
b02 = Button(frame, bg="brown", height=5, width=10, activebackground="blue")
b02.pack( side = LEFT)
b03 = Button(frame, bg="orange", height=5, width=10, activebackground="blue")
b03.pack( side = LEFT)
b04 = Button(frame, bg="brown", height=5, width=10, activebackground="blue")
b04.pack( side = LEFT)
b05 = Button(frame, bg="orange", height=5, width=10, activebackground="blue")
b05.pack( side = LEFT)
b06 = Button(frame, bg="brown", height=5, width=10, activebackground="blue")
b06.pack( side = LEFT)
b07 = Button(frame, bg="orange", height=5, width=10, activebackground="blue")
b07.pack( side = LEFT)

frame1 = Frame(root)
frame1.pack( side = TOP)
b08 = Button(frame1, bg="orange", height=5, width=10, activebackground="blue")
b08.pack( side = LEFT)
b09 = Button(frame1, bg="brown", height=5, width=10, activebackground="blue")
b09.pack( side = LEFT)
b10 = Button(frame1, bg="orange", height=5, width=10, activebackground="blue")
b10.pack( side = LEFT)
b11 = Button(frame1, bg="brown", height=5, width=10, activebackground="blue")
b11.pack( side = LEFT)
b12 = Button(frame1, bg="orange", height=5, width=10, activebackground="blue")
b12.pack( side = LEFT)
b13 = Button(frame1, bg="brown", height=5, width=10, activebackground="blue")
b13.pack( side = LEFT)
b14 = Button(frame1, bg="orange", height=5, width=10, activebackground="blue")
b14.pack( side = LEFT)
b15 = Button(frame1, bg="brown", height=5, width=10, activebackground="blue")
b15.pack( side = LEFT)

frame2 = Frame(root)
frame2.pack( side = TOP)
b16 = Button(frame2, bg="brown", height=5, width=10, activebackground="blue")
b16.pack( side = LEFT)
b17 = Button(frame2, bg="orange", height=5, width=10, activebackground="blue")
b17.pack( side = LEFT)
b18 = Button(frame2, bg="brown", height=5, width=10, activebackground="blue")
b18.pack( side = LEFT)
b19 = Button(frame2, bg="orange", height=5, width=10, activebackground="blue")
b19.pack( side = LEFT)
b20 = Button(frame2, bg="brown", height=5, width=10, activebackground="blue")
b20.pack( side = LEFT)
b21 = Button(frame2, bg="orange", height=5, width=10, activebackground="blue")
b21.pack( side = LEFT)
b22 = Button(frame2, bg="brown", height=5, width=10, activebackground="blue")
b22.pack( side = LEFT)
b23 = Button(frame2, bg="orange", height=5, width=10, activebackground="blue")
b23.pack( side = LEFT)

frame3 = Frame(root)
frame3.pack( side = TOP)
b24 = Button(frame3, bg="orange", height=5, width=10, activebackground="blue")
b24.pack( side = LEFT)
b25 = Button(frame3, bg="brown", height=5, width=10, activebackground="blue")
b25.pack( side = LEFT)
b26 = Button(frame3, bg="orange", height=5, width=10, activebackground="blue")
b26.pack( side = LEFT)
b27 = Button(frame3, bg="brown", height=5, width=10, activebackground="blue")
b27.pack( side = LEFT)
b28 = Button(frame3, bg="orange", height=5, width=10, activebackground="blue")
b28.pack( side = LEFT)
b29 = Button(frame3, bg="brown", height=5, width=10, activebackground="blue")
b29.pack( side = LEFT)
b30 = Button(frame3, bg="orange", height=5, width=10, activebackground="blue")
b30.pack( side = LEFT)
b31 = Button(frame3, bg="brown", height=5, width=10, activebackground="blue")
b31.pack( side = LEFT)

frame4 = Frame(root)
frame4.pack( side = TOP)
b32 = Button(frame4, bg="brown", height=5, width=10, activebackground="blue")
b32.pack( side = LEFT)
b33 = Button(frame4, bg="orange", height=5, width=10, activebackground="blue")
b33.pack( side = LEFT)
b34 = Button(frame4, bg="brown", height=5, width=10, activebackground="blue")
b34.pack( side = LEFT)
b35 = Button(frame4, bg="orange", height=5, width=10, activebackground="blue")
b35.pack( side = LEFT)
b36 = Button(frame4, bg="brown", height=5, width=10, activebackground="blue")
b36.pack( side = LEFT)
b37 = Button(frame4, bg="orange", height=5, width=10, activebackground="blue")
b37.pack( side = LEFT)
b38 = Button(frame4, bg="brown", height=5, width=10, activebackground="blue")
b38.pack( side = LEFT)
b39 = Button(frame4, bg="orange", height=5, width=10, activebackground="blue")
b39.pack( side = LEFT)

frame5 = Frame(root)
frame5.pack( side = TOP)
b40 = Button(frame5, bg="orange", height=5, width=10, activebackground="blue")
b40.pack( side = LEFT)
b41 = Button(frame5, bg="brown", height=5, width=10, activebackground="blue")
b41.pack( side = LEFT)
b42 = Button(frame5, bg="orange", height=5, width=10, activebackground="blue")
b42.pack( side = LEFT)
b43 = Button(frame5, bg="brown", height=5, width=10, activebackground="blue")
b43.pack( side = LEFT)
b44 = Button(frame5, bg="orange", height=5, width=10, activebackground="blue")
b44.pack( side = LEFT)
b45 = Button(frame5, bg="brown", height=5, width=10, activebackground="blue")
b45.pack( side = LEFT)
b46 = Button(frame5, bg="orange", height=5, width=10, activebackground="blue")
b46.pack( side = LEFT)
b47 = Button(frame5, bg="brown", height=5, width=10, activebackground="blue")
b47.pack( side = LEFT)

frame6 = Frame(root)
frame6.pack( side = TOP)
b48 = Button(frame6, bg="brown", height=5, width=10, activebackground="blue")
b48.pack( side = LEFT)
b49 = Button(frame6, bg="orange", height=5, width=10, activebackground="blue")
b49.pack( side = LEFT)
b50 = Button(frame6, bg="brown", height=5, width=10, activebackground="blue")
b50.pack( side = LEFT)
b51 = Button(frame6, bg="orange", height=5, width=10, activebackground="blue")
b51.pack( side = LEFT)
b52 = Button(frame6, bg="brown", height=5, width=10, activebackground="blue")
b52.pack( side = LEFT)
b53 = Button(frame6, bg="orange", height=5, width=10, activebackground="blue")
b53.pack( side = LEFT)
b54 = Button(frame6, bg="brown", height=5, width=10, activebackground="blue")
b54.pack( side = LEFT)
b55 = Button(frame6, bg="orange", height=5, width=10, activebackground="blue")
b55.pack( side = LEFT)

frame7 = Frame(root)
frame7.pack( side = TOP)
b56 = Button(frame7, bg="orange", height=5, width=10, activebackground="blue")
b56.pack( side = LEFT)
b57 = Button(frame7, bg="brown", height=5, width=10, activebackground="blue")
b57.pack( side = LEFT)
b58 = Button(frame7, bg="orange", height=5, width=10, activebackground="blue")
b58.pack( side = LEFT)
b59 = Button(frame7, bg="brown", height=5, width=10, activebackground="blue")
b59.pack( side = LEFT)
b60 = Button(frame7, bg="orange", height=5, width=10, activebackground="blue")
b60.pack( side = LEFT)
b61 = Button(frame7, bg="brown", height=5, width=10, activebackground="blue")
b61.pack( side = LEFT)
b62 = Button(frame7, bg="orange", height=5, width=10, activebackground="blue")
b62.pack( side = LEFT)
b63 = Button(frame7, bg="brown", height=5, width=10, activebackground="blue")
b63.pack( side = LEFT)
#label = Label( root, text = "Selecione sua peça", relief=RAISED , height=5, width=80)
#label.pack(side = TOP)
botoes = [b00, b01, b02, b03, b04, b05, b06, b07,
          b08, b09, b10, b11, b12, b13, b14, b15,
          b16, b17, b18, b19, b20, b21, b22, b23,
          b24, b25, b26, b27, b28, b29, b30, b31,
          b32, b33, b34, b35, b36, b37, b38, b39,
          b40, b41, b42, b43, b44, b45, b46, b47,
          b48, b49, b50, b51, b52, b53, b54, b55,
          b56, b57, b58, b59, b60, b61, b62, b63]


def callback(b):
    global TABULEIRO
    global selecionado
    global photoSelect
    if len(TABULEIRO) ==64:
        if TABULEIRO[b] == jdd.minComum:
            if selecionado == -1:
                botoes[b].config(image=photoMinSelect, width=75 ,height=80)
                botoes[b].pack()
                selecionado = b
                photoSelect = photoMinComum
            elif selecionado == b:
                botoes[b].config(image=photoMinComum, width=75 ,height=80)
                botoes[b].pack()
                selecionado = -1
        elif TABULEIRO[b] == jdd.minDama:
            if selecionado == -1:
                botoes[b].config(image=photoMinSelect, width=75 ,height=80)
                botoes[b].pack()
                selecionado = b
                photoSelect = photoMinDama
            elif selecionado == b:
                botoes[b].config(image=photoMinDama, width=75 ,height=80)
                botoes[b].pack()
                selecionado = -1
        elif selecionado != -1 and selecionado != b and TABULEIRO[b] == jdd.vazio:
            botoes[selecionado].config(image=photoSelect, width=75 ,height=80)
            botoes[selecionado].pack()
            PROXIMA_JOGADA(selecionado, b)
            selecionado = -1

b01.config(command = lambda: callback(1))
b01.pack(side=LEFT)
b03.config(command = lambda: callback(3))
b03.pack(side=LEFT)
b05.config(command = lambda: callback(5))
b05.pack(side=LEFT)
b07.config(command = lambda: callback(7))
b07.pack(side=LEFT)
b08.config(command = lambda: callback(8))
b08.pack(side=LEFT)
b10.config(command = lambda: callback(10))
b10.pack(side=LEFT)
b12.config(command = lambda: callback(12))
b12.pack(side=LEFT)
b14.config(command = lambda: callback(14))
b14.pack(side=LEFT)
b17.config(command = lambda: callback(17))
b17.pack(side=LEFT)
b19.config(command = lambda: callback(19))
b19.pack(side=LEFT)
b21.config(command = lambda: callback(21))
b21.pack(side=LEFT)
b23.config(command = lambda: callback(23))
b23.pack(side=LEFT)
b24.config(command = lambda: callback(24))
b24.pack(side=LEFT)
b26.config(command = lambda: callback(26))
b26.pack(side=LEFT)
b28.config(command = lambda: callback(28))
b28.pack(side=LEFT)
b30.config(command = lambda: callback(30))
b30.pack(side=LEFT)
b33.config(command = lambda: callback(33))
b33.pack(side=LEFT)
b35.config(command = lambda: callback(35))
b35.pack(side=LEFT)
b37.config(command = lambda: callback(37))
b37.pack(side=LEFT)
b39.config(command = lambda: callback(39))
b39.pack(side=LEFT)
b40.config(command = lambda: callback(40))
b40.pack(side=LEFT)
b42.config(command = lambda: callback(42))
b42.pack(side=LEFT)
b44.config(command = lambda: callback(44))
b44.pack(side=LEFT)
b46.config(command = lambda: callback(46))
b46.pack(side=LEFT)
b49.config(command = lambda: callback(49))
b49.pack(side=LEFT)
b51.config(command = lambda: callback(51))
b51.pack(side=LEFT)
b53.config(command = lambda: callback(53))
b53.pack(side=LEFT)
b55.config(command = lambda: callback(55))
b55.pack(side=LEFT)
b56.config(command = lambda: callback(56))
b56.pack(side=LEFT)
b58.config(command = lambda: callback(58))
b58.pack(side=LEFT)
b60.config(command = lambda: callback(60))
b60.pack(side=LEFT)
b62.config(command = lambda: callback(62))
b62.pack(side=LEFT)

def PRINT_TABULEIRO():
    global TABULEIRO
    pos = 1
    for i in range (1, 9):
        fim = pos+6
        while pos <= fim:
            if TABULEIRO[pos] == jdd.minComum:
                botoes[pos].config(image=photoMinComum, width=75 ,height=80)
                botoes[pos].pack(side=LEFT)
            elif TABULEIRO[pos] == jdd.minDama:
                botoes[pos].config(image=photoMinDama, width=75 ,height=80)
                botoes[pos].pack(side=LEFT)
            elif TABULEIRO[pos] == jdd.maxComum:
                botoes[pos].config(image=photoMaxComum, width=75 ,height=80)
                botoes[pos].pack(side=LEFT)
            elif TABULEIRO[pos] == jdd.maxDama:
                botoes[pos].config(image=photoMaxDama, width=75 ,height=80)
                botoes[pos].pack(side=LEFT)
            elif TABULEIRO[pos] == jdd.vazio:
                botoes[pos].config(image= photoVazio, width=75 ,height=80)
                botoes[pos].pack(side=LEFT)
            pos = pos+2
        if (i % 2) == 0: pos = pos + 1
        elif True: pos = pos - 1

def PROXIMA_JOGADA(posIni, posFim):
    global TABULEIRO
    jdd.PROXIMA_JOGADA(2, posIni, posFim)
    TAB = []
    TAB[:] = jdd.GET_TABULEIRO()
    TABULEIRO[:] = TAB
    PRINT_TABULEIRO()

def INICIAR():
    global TABULEIRO
    global selecionado
    global photoSelect
    selecionado = -1
    TABULEIRO = []
    photoSelect = photoMinComum
    jdd.DEFINIR_VALORES_MIN_MAX()
    TABULEIRO[:] = jdd.GET_TABULEIRO()
    PRINT_TABULEIRO()
    


    
    
buttonNewGame = Button(root, bg="yellow", height=5, width=50, activebackground="purple" , text="Novo Jogo", command= lambda:INICIAR())
buttonNewGame.pack( side = TOP)



root.mainloop()
