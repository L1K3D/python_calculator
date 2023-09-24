#Importando a biblioteca "tkinter"#
from tkinter import *
from tkinter import ttk
from tkinter import font

#Cores usadas no programa#
cor1 = "#3b3b3b" #Cor preta#
cor2 = "#feffff" #Branco#
cor3 = "#38576b" #Azul Pastel#
cor4 = "#ECEFF1" #Cinza#
cor5 = "#FFAB40" #Laranja#

#Exibição da janela principal e a divisão das janelas#
janela = Tk()
janela.title("Caculadora") #Titulo da aplicação#
janela.geometry("235x320") #Medidas da janela da aplicação: largura X comprimento
janela.config(bg=cor1) #Definição da cor de interpretação dos números (parte de baixo/digitação da calculadora)#

#Configuração do Frame1/Superior/Display#
frame_tela = Frame(janela, width=235, height=50, bg=cor3) #Divisão do display onde aparece os números e os números disponiveis para uso, 'width' = largura do display, 'height' = altura do display#
frame_tela.grid(row=0, column=0)

#Configuração do Frame2/Inferior/Teclado#
frame_corpo = Frame(janela, width=235, height=268) 
frame_corpo.grid(row=1, column=0)

#Variavel de definição de valores inseridos#
todos_valores = ''

#Função de definição de valores#
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #Passando valor para o display#
    valor_texto.set(todos_valores)

#Função para calcular#
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#Função limpar tela#
def limpar_tela():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
    todos_valores = ""
    valor_texto.set("")


#Label/display#
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('EVOGRIA 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#BOTÕES#
#BOTÕES - Linha 1#
b1 = Button(frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE)#Botão de limpar operação
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command = lambda:entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Botão de modulo "Resto de divisão"
b2.place(x=115, y=0)
b3 = Button(frame_corpo, command = lambda:entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Botão de divisão#
b3.place(x=177, y=0)

#BOTÕES - Linha 2#
b4 = Button(frame_corpo, command = lambda:entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 7
b4.place(x=0, y=55)
b5 = Button(frame_corpo, command = lambda:entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 8
b5.place(x=55, y=55)
b6 = Button(frame_corpo, command = lambda:entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 9
b6.place(x=115, y=55)
b7 = Button(frame_corpo, command = lambda:entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Multiplicação#
b7.place(x=177, y=55)

#BOTÕES - Linha 3#
b8 = Button(frame_corpo, command = lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 4
b8.place(x=0, y=110)
b9 = Button(frame_corpo, command = lambda:entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 5
b9.place(x=55, y=110)
b10 = Button(frame_corpo, command = lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 6
b10.place(x=115, y=110)
b11 = Button(frame_corpo, command = lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Subtração#
b11.place(x=177, y=110)

#BOTÕES - Linha 4#
b12 = Button(frame_corpo, command = lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 1
b12.place(x=0, y=165)
b13 = Button(frame_corpo, command = lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 2
b13.place(x=55, y=165)
b14 = Button(frame_corpo, command = lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 3
b14.place(x=115, y=165)
b15 = Button(frame_corpo, command = lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Soma#
b15.place(x=177, y=165)

#BOTÕES - Linha 5#
b16 = Button(frame_corpo, command = lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Número 0
b16.place(x=0, y=220)
b17 = Button(frame_corpo, command = lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Ponto/Virgula
b17.place(x=115, y=220)
b18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('EVOGRIA 12'), relief=RAISED, overrelief=RIDGE) #Igual
b18.place(x=177, y=220)

#OPERAÇÕES#

#Sistema de excução ineterrupta#
janela.mainloop()