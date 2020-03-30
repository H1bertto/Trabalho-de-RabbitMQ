import tkinter as tk
from PIL import ImageTk, Image
import sys
try:
    from .Receive import BolsaDeValores
except ImportError:
    from Receive import BolsaDeValores

try:
    from .Broker import Broker
except ImportError:
    from Broker import Broker

import threading
from datetime import datetime


class Worker(tk.Frame):
    def __init__(self, master=None, name=None, **kwargs):
        tk.Frame.__init__(self, master)
        self.cor = "#ffd500"
        self.cor2 = "#000000"
        self.comprou = False
        self.vendeu = False
        self.first_time = False
        if "bolsa_de_valores" in kwargs:
            self.func1 = kwargs["bolsa_de_valores"]
        self.func2 = Broker
        self.name = name
        self.fonte_padrao = ("Century Gothic", "9", "bold")
        self.fonte_padrao2 = ("Century Gothic", "11", "bold")
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.create_table()
        self.create_widgets()

    def create_table(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=5)
        self.rowconfigure(3, weight=5)
        self.rowconfigure(4, weight=5)
        self.rowconfigure(5, weight=5)
        self.rowconfigure(6, weight=5)
        self.rowconfigure(7, weight=5)
        self.rowconfigure(8, weight=5)
        self.rowconfigure(9, weight=5)
        self.rowconfigure(10, weight=5)
        self.rowconfigure(11, weight=5)
        self.rowconfigure(12, weight=5)
        self.rowconfigure(13, weight=5)
        self.rowconfigure(14, weight=5)
        self.rowconfigure(15, weight=5)
        self.rowconfigure(16, weight=5)
        self.rowconfigure(17, weight=5)
        self.rowconfigure(18, weight=5)
        self.rowconfigure(19, weight=5)

        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=5)
        self.columnconfigure(4, weight=5)
        self.columnconfigure(5, weight=5)
        self.columnconfigure(6, weight=5)

        background_image = ImageTk.PhotoImage(Image.open('bolsa.jpg'))
        background_label = tk.Label(self, image=background_image, bg=self.cor2)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_widgets(self):
        choices2 = {}
        choices3 = {}
        choices4 = {}
        ativos = open("ativos.txt", 'r', encoding="utf-8")
        i = 0
        colu2 = 0
        colu3 = 1
        colu4 = 2
        box2 = {}
        box3 = {}
        box4 = {}
        for ativo in ativos:
            atv = ativo.strip().split('|')
            choices2[i] = atv[0]
            choices3[i] = atv[1]
            choices4[i] = atv[2]
            box2[i] = tk.Label(self, text=choices2[i], bg=self.cor2, fg=self.cor)
            box2[i]["font"] = self.fonte_padrao
            box2[i]["padx"] = 7
            box2[i]["pady"] = 2
            box2[i].grid(row=i, column=colu2, sticky=tk.N + tk.S + tk.E + tk.W)

            box3[i] = tk.Label(self, text=choices3[i], bg=self.cor2, fg=self.cor)
            box3[i]["font"] = self.fonte_padrao
            box3[i]["padx"] = 10
            box3[i].grid(row=i, column=colu3, sticky=tk.N + tk.S + tk.E + tk.W)

            box4[i] = tk.Label(self, text=choices4[i], bg=self.cor2, fg=self.cor, wraplength=490, justify=tk.LEFT)
            box4[i]["font"] = self.fonte_padrao
            box4[i]["padx"] = 7
            box4[i].grid(row=i, column=colu4, columnspan=3, sticky=tk.N + tk.S + tk.W)
            if i == 0:
                box2[i]["font"] = self.fonte_padrao2
                box3[i]["font"] = self.fonte_padrao2
                box4[i]["font"] = self.fonte_padrao2
                box4[i].grid(row=i, column=colu4, columnspan=3, sticky=tk.N + tk.S + tk.E + tk.W)
            i += 1

        self.corretora_label = tk.Label(self, text="", font=self.fonte_padrao, background=self.cor, foreground=self.cor2)
        self.corretora_label.grid(row=16, column=0, columnspan=5, sticky=tk.N + tk.S + tk.E + tk.W)

        if self.name == "Broker":
            #
            self.corretora_label = tk.Label(self, text="Corretora", font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
            self.corretora_label.grid(row=17, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

            self.quant_label = tk.Label(self, text="Quantidade", font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
            self.quant_label.grid(row=17, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

            self.valor_label = tk.Label(self, text="Valor", font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
            self.valor_label.grid(row=17, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

            #
            self.buy = tk.Button(self, text="Compra", font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
            # self.buy['relief'] = 'flat'
            self.buy['command'] = self.compra
            self.buy.grid(row=17, column=3, rowspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

            #
            cods = list(choices3.values())
            cods.pop(0)
            self.tkvar = tk.StringVar(self)
            self.corretora = tk.OptionMenu(self, self.tkvar, *cods)
            self.corretora["font"] = self.fonte_padrao
            self.corretora["bg"] = self.cor2
            self.corretora["fg"] = self.cor
            # self.corretora["borderwidth"] = 0
            self.corretora["highlightthickness"] = .5
            self.corretora["highlightbackground"] = "#000000"
            self.corretora.grid(row=18, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

            self.quant = tk.Entry(self, font=self.fonte_padrao, background=self.cor2, foreground=self.cor, insertbackground=self.cor)
            self.quant.grid(row=18, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

            self.valor = tk.Entry(self, font=self.fonte_padrao, background=self.cor2, foreground=self.cor, insertbackground=self.cor)
            self.valor.grid(row=18, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

            #
            self.sell = tk.Button(self, text="Venda", font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
            # self.sell['relief'] = 'flat'
            self.sell['command'] = self.venda
            self.sell.grid(row=17, column=4, rowspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.output = tk.Text(self, width=80, height=10, font=self.fonte_padrao, background=self.cor2, foreground=self.cor)
        self.output.grid(row=19, column=0, columnspan=5, sticky=tk.N + tk.S + tk.E + tk.W)
        sys.stdout = self

    def write(self, txt):
        self.output.insert(tk.END, str(txt) + "\n")
        self.update_idletasks()

    def receive(self):
        t1 = threading.Thread(target=self.func1, args=[self])
        t1.start()

    def compra(self):
        execute = True
        try:
            float(self.quant.get().replace(",", "."))
        except ValueError:
            self.write("Operação invalida! - Quantidade no Formato Incorreto")
            execute = False
        try:
            float(self.valor.get().replace(",", "."))
        except ValueError:
            execute = False
            self.write("Operação invalida! - Valor no Formato Incorreto")
        if execute:
            key = "compra.ativo"
            msg = f'COD: {self.tkvar.get()} QUANT: {self.quant.get()} VALOR: {self.valor.get()}'
            t1 = threading.Thread(target=self.func2, args=[key, msg, self])
            t1.start()
            # self.transacao("COMPRA")
            self.comprou = True

    def venda(self):
        execute = True
        try:
            float(self.quant.get().replace(",", "."))
        except ValueError:
            self.write("Operação invalida! - Quantidade no Formato Incorreto")
            execute = False
        try:
            float(self.valor.get().replace(",", "."))
        except ValueError:
            execute = False
            self.write("Operação invalida! - Valor no Formato Incorreto")
        if execute:
            key = "vende.ativo"
            msg = f'COD: {self.tkvar.get()} QUANT: {self.quant.get()} VALOR: {self.valor.get()}'
            t1 = threading.Thread(target=self.func2, args=[key, msg, self])
            t1.start()
            # self.transacao("VENDA")
            self.vendeu = True

    def transacao(self, tipo, msg):
        key = "transacao.ativo"
        msg = f' <{datetime.now().strftime("%d/%m/%Y %H:%M")}> {tipo} - {msg}'
        t1 = threading.Thread(target=self.func2, args=[key, msg, self])
        t1.start()
        self.comprou = False
        self.vendeu = False

    def pressiona_esc(self, event=None):
        self.master.destroy()
        sys.exit()

    def verifica_codigo(self):
        # usuario_digitadoSAP = self.usuarioSAP.get()
        # senha_digitadaSAP = self.senhaSAP.get()
        # if usuario_digitadoSAP == "":
        #     self.mensagem["text"] = "Favor informar o Usuário do SAP!"
        # elif senha_digitadaSAP == "":
        #     self.mensagem["text"] = "Favor informar a Senha do SAP!"
        # else:
        #     self.user_SAP = usuario_digitadoSAP
        #     self.pswd_SAP = senha_digitadaSAP
        self.sucesso = True

    def run(self):
        self.master.title(self.name)
        self.master.bind("<Escape>", self.pressiona_esc)
        self.master.focus_force()
        self.configure(background='#1f1f1f')
        self.receive()
        self.mainloop()


if __name__ == '__main__':
    Worker(name=sys.argv[1].replace("_", " ").title(), bolsa_de_valores=BolsaDeValores).run()
