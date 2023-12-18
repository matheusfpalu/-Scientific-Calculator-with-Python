import codigo
import codigo_cientifica
import codigo_menu
import math
from PyQt5.QtCore import QObject, pyqtSlot

from PyQt5 import QtCore, QtGui, QtWidgets

funções = {"sqrt":math.sqrt,"sin":math.sin,"cos":math.cos,"tan":math.tan, "π" : math.pi, "e": math.e, "ln": math.log
           , "log_10": math.log10, "log_2": math.log2, "fatorial":math.factorial}


class controller():
        
    def __init__(self):
        
        self.ANS = 0
        
        self.Dialog_codigo = QtWidgets.QDialog()
        self.ui_codigo = codigo.Ui_Dialog()
        self.ui_codigo.setupUi(self.Dialog_codigo)

        self.Dialog_cientifica = QtWidgets.QDialog()
        self.ui_cientifica = codigo_cientifica.Ui_Dialog()
        self.ui_cientifica.setupUi(self.Dialog_cientifica)

        self.Dialog_menu = QtWidgets.QDialog()
        self.ui_menu = codigo_menu.Ui_Dialog()
        self.ui_menu.setupUi(self.Dialog_menu)
        
        self.ui_menu.T.clicked.connect(self.abre_tradicional)
        self.ui_menu.C.clicked.connect(self.abre_cientifica)
        self.ui_codigo.volta_trad.clicked.connect(self.abre_menu)
        self.ui_cientifica.volta_cient.clicked.connect(self.abre_menu)

        self.ui_codigo.label.setText("0")
        self.ui_cientifica.label.setText("0")
        
        trad = self.ui_codigo
        cient = self.ui_cientifica
        
        botões= [trad.pushButton_7,trad.pushButton_9,cient.pushButton_7,cient.pushButton_9]
                          
        numeros = [trad.pushButton,trad.pushButton_2,trad.pushButton_3,trad.pushButton_4,
                   trad.pushButton_5,trad.pushButton_6,trad.pushButton_8,trad.pushButton_10,
                   trad.pushButton_11,trad.pushButton_14,
                   
                   cient.pushButton,cient.pushButton_2,cient.pushButton_3,cient.pushButton_4,
                   cient.pushButton_5,cient.pushButton_6,cient.pushButton_8,cient.pushButton_10,
                   cient.pushButton_11,cient.pushButton_14]
        
        for botão in botões:
            botão.clicked.connect(self.escrever)
            
        for botão in numeros:
            botão.clicked.connect(self.escrever_numeros)

        trad.pushButton_16.clicked.connect(self.enter_trad)
        cient.pushButton_16.clicked.connect(self.enter_cientifica)
        
        trad.pushButton_20.clicked.connect(self.troca_sinal_trad)
        cient.pushButton_20.clicked.connect(self.troca_sinal_cientifica)
        
        trad.pushButton_18.clicked.connect(self.limpa)
        cient.pushButton_18.clicked.connect(self.limpa)
        
        trad.pushButton_13.clicked.connect(self.raiz_quadrada)
        cient.pushButton_13.clicked.connect(self.raiz_quadrada)
        
        trad.pushButton_17.clicked.connect(self.deletar)
        cient.pushButton_17.clicked.connect(self.deletar)
        
        trad.pushButton_19.clicked.connect(self.ponto)
        cient.pushButton_19.clicked.connect(self.ponto)
        
        trad.pushButton_28.clicked.connect(self.porcentagem_trad)
        cient.pushButton_28.clicked.connect(self.porcentagem_cientifica)
        
        trad.pushButton_27.clicked.connect(self.parenteses_fecha)
        cient.pushButton_27.clicked.connect(self.parenteses_fecha)

        cient.pushButton_21.clicked.connect(self.seno)
        cient.pushButton_22.clicked.connect(self.cosseno)
        cient.pushButton_23.clicked.connect(self.tangente)
        cient.pushButton_25.clicked.connect(self.elevado)
        cient.pushButton_24.clicked.connect(self.radianos) 
        cient.pushButton_35.clicked.connect(self.graus)
        cient.pushButton_36.clicked.connect(self.fatorial)
        cient.pushButton_34.clicked.connect(self.ln)
        cient.pushButton_33.clicked.connect(self.log_10)
        cient.pushButton_32.clicked.connect(self.log_2)
        
        trad.pushButton_29.clicked.connect(self.escrever_diferenciado)
        cient.pushButton_29.clicked.connect(self.escrever_diferenciado)
        cient.pushButton_30.clicked.connect(self.escrever_diferenciado)
        trad.pushButton_26.clicked.connect(self.escrever_diferenciado)
        cient.pushButton_26.clicked.connect(self.escrever_diferenciado)
        
        trad.pushButton_12.clicked.connect(self.div_mult)
        trad.pushButton_15.clicked.connect(self.div_mult)
        cient.pushButton_12.clicked.connect(self.div_mult)
        cient.pushButton_15.clicked.connect(self.div_mult)
        
        trad.pushButton_30.clicked.connect(self.ans)
        cient.pushButton_31.clicked.connect(self.ans)
        
    def abre_tradicional(self):
        self.Dialog_menu.close()
        self.Dialog_codigo.show()
        
    def abre_cientifica(self):
        self.Dialog_menu.close()
        self.Dialog_cientifica.show()
        
    def abre_menu(self):
        self.Dialog_codigo.close()
        self.Dialog_cientifica.close()
        self.Dialog_menu.show()
        self.ui_codigo.label.setText("0")
        self.ui_cientifica.label.setText("0")
        self.ui_codigo.lcdNumber.display(0)
        self.ui_cientifica.lcdNumber.display(0)
        
    def escrever(self):
        #Para os botões "+" e "-"        
        
        #Calculadora Tradicional
        if self.ui_codigo.label.text() == "0":
            self.ui_codigo.label.clear()  
        self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
        
        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.clear()  
        self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())
        
    def escrever_numeros(self):
        #Código para escrever os números, serve para verificar se o último digito é "π", ")" ou "e", isto é, caso o útimo
        #dígito seja esse, verificar dígito é 0, caso seja 0 e o tamanho da string for 1, ou seja, se só
        #tiver o "0", apaga esse "0" e escreve o número, caso contrário, adiciona um "*" entre o 0 e o caractere, além 
        #disso, caso o último caractere seja "π", ")" ou "e" e o ultimo digito não for "0", também adiciona um "*" entre eles

        #Serve para adicionar um "*" entre dois caracteres (a depender desses dois caracteres)
        
        #Calculadora Tradicional
           
        if self.ui_codigo.label.text()[-1] == "π" or self.ui_codigo.label.text()[-1] == ")" or self.ui_codigo.label.text()[-1] == "e":
            if self.ui_codigo.label.text() == "0":
                if len(self.ui_codigo.label.text()) != 1:
                    self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + self.Dialog_codigo.sender().text())
                else:
                    self.ui_codigo.label.clear()
                    
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
            else:
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + self.Dialog_codigo.sender().text())
        else:
            if self.ui_codigo.label.text() == "0":
                if len(self.ui_codigo.label.text()) != 1:
                    self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
                else:
                    self.ui_codigo.label.clear()
                    
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
            else:
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())

        #Calculadora Científica
        
        if self.ui_cientifica.label.text()[-1] == "π" or self.ui_cientifica.label.text()[-1] == ")" or self.ui_cientifica.label.text()[-1] == "e":
            if self.ui_cientifica.label.text()[-1] == "0":
                if len(self.ui_cientifica.label.text()) != 1:
                    self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + self.Dialog_cientifica.sender().text())
                else:
                    self.ui_cientifica.label.clear()
                    
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())
            else:
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + self.Dialog_cientifica.sender().text())
        else:
            if self.ui_cientifica.label.text()[-1] == "0":
                if len(self.ui_cientifica.label.text()) != 1:
                    self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())
                else:
                    self.ui_cientifica.label.clear()
                    
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())
            else:
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())
      
    def escrever_diferenciado(self):
        #Serve para adicionar um "*" entre dois caracteres (a depender desses dois caracteres)
        #e não permite colocar o valor depois de um decimal 

        caracteres = ["1","2","3","4","5","6","7","8","9","0",")","π","e"]        

        #Calculadora Tradicional
        if self.ui_codigo.label.text()[-1] == ".":
            self.ui_codigo.label.setText(self.ui_codigo.label.text())
            
        elif self.ui_codigo.label.text()[-1] in caracteres:
            if self.ui_codigo.label.text() == "0":
                if len(self.ui_codigo.label.text()) != 1:
                    self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + self.Dialog_codigo.sender().text())
                else:
                    self.ui_codigo.label.clear()
                    
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
            else:
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + self.Dialog_codigo.sender().text())
        else:
            self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())

        #Calculadora Científica
        if self.ui_cientifica.label.text()[-1] == ".":
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text())
            
        elif self.ui_cientifica.label.text()[-1] in caracteres:
            if self.ui_cientifica.label.text() == "0":
                if len(self.ui_cientifica.label.text()) != 1:
                    self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + self.Dialog_cientifica.sender().text())
                else:
                    self.ui_cientifica.label.clear()
                    
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_codigo.sender().text())
            else:
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + self.Dialog_cientifica.sender().text())
        else:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())

    def enter_trad(self):
                
        #Calculadora Tradicional
        if self.ui_codigo.label.text() == "0":
            self.ui_codigo.label.setText("0")
        else:
            self.ui_codigo.lcdNumber.display(eval(self.ui_codigo.label.text(),funções))
            
            #Exibe apenas com quatro casas decimais
            #self.ui_codigo.label.setText("{:.4f}".format(eval(self.ui_codigo.label.text(),funções)))

            self.ANS = eval(self.ui_codigo.label.text(),funções)
            
            self.ui_codigo.label.setText("0")
            
            #Exibe com todas as casas decimais
            #self.ui_codigo.label.setText(str(eval(self.ui_codigo.label.text(),funções)))
   
    def enter_cientifica(self):
        
        #Calculadora Científica
        
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("0")
        else:
            self.ui_cientifica.lcdNumber.display(eval(self.ui_cientifica.label.text(),funções))
            
            #Exibe apenas com quatro casas decimais
            #self.ui_cientifica.label.setText("{:.4f}".format(eval(self.ui_cientifica.label.text(),funções)))

            self.ANS = eval(self.ui_cientifica.label.text(),funções)
            
            self.ui_cientifica.label.setText("0")
            
            #Exibe com todas as casas decimais
            #self.ui_cientifica.label.setText(str(eval(self.ui_cientifica.label.text(),funções)))

    def limpa(self):
        
        #Calculadora Tradicional
        self.ui_codigo.label.setText("0")
        self.ui_codigo.lcdNumber.display(0)
        
        #Calculadora Científica
        self.ui_cientifica.label.setText("0")
        self.ui_cientifica.lcdNumber.display(0)
        
    def raiz_quadrada(self):
        
        #Calculadora Tradicional    
        if self.ui_codigo.label.text() == "0":
            self.ui_codigo.label.setText("sqrt(")
        else:
            self.ui_codigo.label.setText("sqrt(" + self.ui_codigo.label.text())
        
        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("sqrt(")
        else:
            self.ui_cientifica.label.setText("sqrt(" + self.ui_cientifica.label.text())

    def seno(self):
                      
        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("sin(")
        else:
            self.ui_cientifica.label.setText("sin(" + self.ui_cientifica.label.text())
            
    def cosseno(self):
                
        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("cos(")
        else:
            self.ui_cientifica.label.setText("cos(" + self.ui_cientifica.label.text())

    def tangente(self):

        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("tan(")
        else:
            self.ui_cientifica.label.setText("tan(" + self.ui_cientifica.label.text())
            
    def ln(self):

        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("ln(")
        else:
            self.ui_cientifica.label.setText("ln(" + self.ui_cientifica.label.text())

    def log_10(self):

        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("log_10(")
        else:
            self.ui_cientifica.label.setText("log_10(" + self.ui_cientifica.label.text())

    def log_2(self):

        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("log_2(")
        else:
            self.ui_cientifica.label.setText("log_2(" + self.ui_cientifica.label.text())

    def fatorial(self):

        #Calculadora Científica
        if self.ui_cientifica.label.text() == "0":
            self.ui_cientifica.label.setText("fatorial(")
        else:
            self.ui_cientifica.label.setText("fatorial(" + self.ui_cientifica.label.text())

    def troca_sinal_trad(self):
           
       #Calculadora Tradicional
       if self.ui_codigo.label.text() == "0":
           self.ui_codigo.label.setText("0")
       else:
           indice_mais = self.ui_codigo.label.text().rfind('+')
           indice_menos = self.ui_codigo.label.text().rfind('-')
           indice_div = self.ui_codigo.label.text().rfind('/')
           indice_mult = self.ui_codigo.label.text().rfind('*')
                      
           ultimo_operador = max(indice_mais,indice_menos,indice_div,indice_mult)
            
           if ultimo_operador != -1:
            
               if indice_mais == ultimo_operador:
                   #Verifica se o ultimo operador é "+", se for troca pega o que tem antes dele, adiciona "-" e põe o que tinha depois do "+"
                   novo_text = self.ui_codigo.label.text()[:indice_mais] + '-' + self.ui_codigo.label.text()[indice_mais+1:]
                   
               elif indice_menos == ultimo_operador:
                   #Verifica se o ultimo operador é "-", se for troca pega o que tem antes dele, adiciona "+" e põe o que tinha depois do "-"
                   novo_text = self.ui_codigo.label.text()[:indice_menos] + '+' + self.ui_codigo.label.text()[indice_menos+1:]
                   
               elif indice_div == ultimo_operador:
                   #Verifica se o ultimo operador é "/", se for troca pega o que tem antes dele, adiciona "/-" e põe o que tinha depois do "/"
                   novo_text = self.ui_codigo.label.text()[:indice_div] + '/-' + self.ui_codigo.label.text()[indice_div+1:]
                   
               elif indice_mult == ultimo_operador:
                   #Verifica se o ultimo operador é "*", se for troca pega o que tem antes dele, adiciona "*-" e põe o que tinha depois do "*"
                   novo_text = self.ui_codigo.label.text()[:indice_mult] + '*-' + self.ui_codigo.label.text()[indice_mult+1:]
                   
               self.ui_codigo.label.setText(novo_text)

           else:
               self.ui_codigo.label.setText(str((float(self.ui_codigo.label.text())*(-1))))

    def troca_sinal_cientifica(self):

       #Calculadora Científica
       if self.ui_cientifica.label.text() == "0":
           self.ui_cientifica.label.setText("0")
       else:
           indice_mais = self.ui_cientifica.label.text().rfind('+')
           indice_menos = self.ui_cientifica.label.text().rfind('-')
           indice_div = self.ui_cientifica.label.text().rfind('/')
           indice_mult = self.ui_cientifica.label.text().rfind('*')
                      
           ultimo_operador = max(indice_mais,indice_menos,indice_div,indice_mult)
            
           if ultimo_operador != -1:
            
               if indice_mais == ultimo_operador:
                   #Verifica se o ultimo operador é "+", se for troca pega o que tem antes dele, adiciona "-" e põe o que tinha depois do "+"
                   novo_text = self.ui_cientifica.label.text()[:indice_mais] + '-' + self.ui_cientifica.label.text()[indice_mais+1:]
                   
               elif indice_menos == ultimo_operador:
                   #Verifica se o ultimo operador é "-", se for troca pega o que tem antes dele, adiciona "+" e põe o que tinha depois do "-"
                   novo_text = self.ui_cientifica.label.text()[:indice_menos] + '+' + self.ui_cientifica.label.text()[indice_menos+1:]
                   
               elif indice_div == ultimo_operador:
                   #Verifica se o ultimo operador é "/", se for troca pega o que tem antes dele, adiciona "/-" e põe o que tinha depois do "/"
                   novo_text = self.ui_cientifica.label.text()[:indice_div] + '/-' + self.ui_cientifica.label.text()[indice_div+1:]
                   
               elif indice_mult == ultimo_operador:
                   #Verifica se o ultimo operador é "*", se for troca pega o que tem antes dele, adiciona "*-" e põe o que tinha depois do "*"
                   novo_text = self.ui_cientifica.label.text()[:indice_mult] + '*-' + self.ui_cientifica.label.text()[indice_mult+1:]
                
               self.ui_cientifica.label.setText(novo_text)

           else:
               self.ui_cientifica.label.setText(str((float(self.ui_cientifica.label.text())*(-1))))


    def deletar(self):
        
        #Calculadora Tradicional
        if self.ui_codigo.label.text() == "0" or len(self.ui_codigo.label.text()) == 1:
            self.ui_codigo.label.setText("0")
        else:
            self.ui_codigo.label.setText(self.ui_codigo.label.text()[:-1])
        
       #Calculadora Científica
        if self.ui_cientifica.label.text() == "0" or len(self.ui_cientifica.label.text()) == 1:
            self.ui_cientifica.label.setText("0")
        else:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text()[:-1])

    def porcentagem_trad(self):
        
        #Calculadora Tradicional
        if self.ui_codigo.label.text()[-1] == ("/" or "/-" or "*" or "*-"):
            self.ui_codigo.label.setText(self.ui_codigo.label.text())
        else:
            self.ui_codigo.label.setText("{:.4f}".format(eval((self.ui_codigo.label.text()+("/100")),funções)))
        
    def porcentagem_cientifica(self):

       #Calculadora Científica
        if self.ui_cientifica.label.text()[-1] == ("/" or "/-" or "*" or "*-"):
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text())
        else:
            self.ui_cientifica.label.setText("{:.4f}".format(eval((self.ui_cientifica.label.text()+("/100")),funções)))
    def elevado(self):
        
        #Calculadora Científica
        self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "**")

    def radianos(self):
        
        #Calculadora Científica
        self.ui_cientifica.label.setText("{:.4f}".format(eval((self.ui_cientifica.label.text()+("*π/180")),funções)))
    
    def graus(self):
        
        #Calculadora Científica
        self.ui_cientifica.label.setText("{:.4f}".format(eval((self.ui_cientifica.label.text()+("*180/π")),funções)))
        
    def ponto(self):
        operadores = ['+', '-', '*', '/']
        
        if self.ui_codigo.label.text()[-1] == "π" or self.ui_codigo.label.text()[-1] == "e":
            self.ui_codigo.label.setText(self.ui_codigo.label.text())
            
        else:          
        
            #Calculadora Tradicional
            
            expressao = self.ui_codigo.label.text()
            ultimo_operador = ""
            
            for op in operadores:
                if op in expressao:
                    ultimo_operador = op
            
            #O rfind acha o indice com maior valor se tiver mais de um
            ultimo_ponto = expressao.rfind('.')
        
            #Lógica
            #Se não houver nenhum ponto na expressão
            #OU o ultimo operador não for vazio E o indice do ultimo ponto for menor 
            #que o indice do ultimo operador, pode adicionar um ponto
            if ((ultimo_ponto == -1) or (ultimo_operador != "" and ultimo_ponto < expressao.rfind(ultimo_operador))):
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + ".")
        
            #Calculadora Científica
            
            expressao_cientifica = self.ui_cientifica.label.text()
            ultimo_operador_cientifico = ""
            
            for op in operadores:
                if op in expressao_cientifica:
                    ultimo_operador_cientifico = op
        
            ultimo_ponto_cientifico = expressao_cientifica.rfind('.')
        
            if ((ultimo_ponto_cientifico) == -1 or (ultimo_operador_cientifico != "" and ultimo_ponto_cientifico < expressao_cientifica.rfind(ultimo_operador_cientifico))):
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + ".")
      
    def parenteses_fecha(self):
        # Calculadora Tradicional
        count_abertos = self.ui_codigo.label.text().count("(")
        count_fechados = self.ui_codigo.label.text().count(")")
        
        if count_abertos > count_fechados:
            self.ui_codigo.label.setText(self.ui_codigo.label.text() + ")")

        # Calculadora Científica
        count_abertos = self.ui_cientifica.label.text().count("(")
        count_fechados = self.ui_cientifica.label.text().count(")")
        
        if count_abertos > count_fechados:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + ")")
    
    def div_mult(self):
        #Não permite colocar um "*" seguido de um "/" e vice versa, além de não permitir colocar um "/" depois 
        #de um "+" ou "-" e não permite colcoar um "*" depois de um "+" ou "-"

        #Calculadora Tradicional
        
        if self.ui_codigo.label.text()[-1] == "/" or self.ui_codigo.label.text()[-1] == "*" or self.ui_codigo.label.text()[-1] == "+" or self.ui_codigo.label.text()[-1] == "-":
            self.ui_codigo.label.setText(self.ui_codigo.label.text())
        else:
            self.ui_codigo.label.setText(self.ui_codigo.label.text() + self.Dialog_codigo.sender().text())
            
        #Calculadora Científica
        
        if self.ui_cientifica.label.text()[-1] == "/" or self.ui_cientifica.label.text()[-1] == "*" or self.ui_cientifica.label.text()[-1] == "+" or self.ui_cientifica.label.text()[-1] == "-":
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text())
        else:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + self.Dialog_cientifica.sender().text())        

    def ans(self):
        #Salva o valor da pultima conta em uma variável, a lógica no geral é parecida com o escreve_numero
        
        caracteres = ["1","2","3","4","5","6","7","8","9","0",")","π","e"]        

        #Calculadora Tradicional
        if self.ui_codigo.label.text()[-1] == ".":
            self.ui_codigo.label.setText(self.ui_codigo.label.text())
            
        elif self.ui_codigo.label.text()[-1] in caracteres:
            if self.ui_codigo.label.text() == "0":
                if len(self.ui_codigo.label.text()) != 1:
                    self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + "{:.4f}".format(self.ANS))
                else:
                    self.ui_codigo.label.clear()
                    
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + "{:.4f}".format(self.ANS))
            else:
                self.ui_codigo.label.setText(self.ui_codigo.label.text() + "*" + "{:.4f}".format(self.ANS))
        else:
            self.ui_codigo.label.setText(self.ui_codigo.label.text() + "{:.4f}".format(self.ANS))
        
        #Calculadora Científica
        if self.ui_cientifica.label.text()[-1] == ".":
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text())
            
        elif self.ui_cientifica.label.text()[-1] in caracteres:
            if self.ui_cientifica.label.text() == "0":
                if len(self.ui_cientifica.label.text()) != 1:
                    self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + "{:.4f}".format(self.ANS))
                else:
                    self.ui_cientifica.label.clear()
                    
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "{:.4f}".format(self.ANS))
            else:
                self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "*" + "{:.4f}".format(self.ANS))
        else:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "{:.4f}".format(self.ANS))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = controller()
    #c.Dialog_codigo.show()
    #c.Dialog_cientifica.show()
    c.Dialog_menu.show()
    sys.exit(app.exec_())