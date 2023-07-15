import customtkinter as ctk
from PIL import Image
import random

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tentativa = ''
        self.palavra = ''
        self.count = 0
        self.letras_erradas = []
        self.letras_escolhidas = []

        self.title('Hangman')
        self.resizable(False,False)
        self.iconbitmap('icone.ico')

        f = ('Calibri', 24)
        
        img1 = ctk.CTkImage(Image.open('./imagens/img1.png'), size=(250,250))
        img2 = ctk.CTkImage(Image.open('./imagens/img2.png'), size=(250,250))
        img3 = ctk.CTkImage(Image.open('./imagens/img3.png'), size=(250,250))
        img4 = ctk.CTkImage(Image.open('./imagens/img4.png'), size=(250,250))
        img5 = ctk.CTkImage(Image.open('./imagens/img5.png'), size=(250,250))
        img6 = ctk.CTkImage(Image.open('./imagens/img6.png'), size=(250,250))
        img7 = ctk.CTkImage(Image.open('./imagens/img7.png'), size=(250,250))
        lista_imagem_status = [img2, img3, img4, img5, img6, img7]
        
        # Labels
        self.lb_imagem = ctk.CTkLabel(master=self, image=img1, text='', anchor='center')
        self.lb_palavra = ctk.CTkLabel(master=self, text='Palavra: ', font=f)
        self.lb_hidenPalavra = ctk.CTkLabel(master=self, text='', font=f)
        self.lb_corretas = ctk.CTkLabel(master=self, text='Palavras Corretas: ', font=f)
        self.lb_corretasAtt = ctk.CTkLabel(master=self, text='', font=f)
        self.lb_erradas = ctk.CTkLabel(master=self, text='Palavras Erradas: ', font=f)
        self.lb_erradasAtt = ctk.CTkLabel(master=self, text='', font=f)
        self.lb_status = ctk.CTkLabel(master=self, text='', font=f)

        # Botões alfabéto
        self.bt_a = ctk.CTkButton(master=self, text='A', command=lambda: press('a'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_b = ctk.CTkButton(master=self, text='B', command=lambda: press('b'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_c = ctk.CTkButton(master=self, text='C', command=lambda: press('c'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_d = ctk.CTkButton(master=self, text='D', command=lambda: press('d'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_e = ctk.CTkButton(master=self, text='E', command=lambda: press('e'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_f = ctk.CTkButton(master=self, text='F', command=lambda: press('f'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_g = ctk.CTkButton(master=self, text='G', command=lambda: press('g'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_h = ctk.CTkButton(master=self, text='H', command=lambda: press('h'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_i = ctk.CTkButton(master=self, text='I', command=lambda: press('i'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_j = ctk.CTkButton(master=self, text='J', command=lambda: press('j'), width=30, height=30, fg_color='coral', hover_color='tomato')
        self.bt_k = ctk.CTkButton(master=self, text='K', command=lambda: press('k'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_l = ctk.CTkButton(master=self, text='L', command=lambda: press('l'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_m = ctk.CTkButton(master=self, text='M', command=lambda: press('m'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_n = ctk.CTkButton(master=self, text='N', command=lambda: press('n'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_o = ctk.CTkButton(master=self, text='O', command=lambda: press('o'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_p = ctk.CTkButton(master=self, text='P', command=lambda: press('p'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_q = ctk.CTkButton(master=self, text='Q', command=lambda: press('q'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_r = ctk.CTkButton(master=self, text='R', command=lambda: press('r'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_s = ctk.CTkButton(master=self, text='S', command=lambda: press('s'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_t = ctk.CTkButton(master=self, text='T', command=lambda: press('t'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_u = ctk.CTkButton(master=self, text='U', command=lambda: press('u'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_v = ctk.CTkButton(master=self, text='V', command=lambda: press('v'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_w = ctk.CTkButton(master=self, text='W', command=lambda: press('w'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_x = ctk.CTkButton(master=self, text='X', command=lambda: press('x'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_y = ctk.CTkButton(master=self, text='Y', command=lambda: press('y'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_z = ctk.CTkButton(master=self, text='Z', command=lambda: press('z'), width=30, height=30,fg_color='coral', hover_color='tomato')
        self.bt_resetar = ctk.CTkButton(master=self, text='Jogar Novamente', command=lambda: reset(),fg_color='coral', hover_color='tomato')


        # Grids
        self.lb_imagem.grid(row=0,columnspan=14)
        self.lb_palavra.grid(row=1,columnspan=7,padx=2.5,pady=2.5)
        self.lb_hidenPalavra.grid(row=1,columnspan=13,padx=(5,2.5),pady=2.5)
        self.lb_corretas.grid(row=2,columnspan=7,padx=2.5,pady=2.5)
        self.lb_corretasAtt.grid(row=2,columnspan=13,padx=(0,100),pady=2.5,sticky='e')
        self.lb_erradas.grid(row=3,columnspan=7,padx=2.5,pady=2.5)
        self.lb_erradasAtt.grid(row=3,columnspan=13,padx=(0,100),pady=2.5,sticky='e')
        self.bt_a.grid(row=4,column=0,padx=2.5,pady=(2.5,0))
        self.bt_b.grid(row=4,column=1,padx=(0,2.5),pady=(2.5,0))
        self.bt_c.grid(row=4,column=2,padx=(0,2.5),pady=(2.5,0))
        self.bt_d.grid(row=4,column=3,padx=(0,2.5),pady=(2.5,0))
        self.bt_e.grid(row=4,column=4,padx=(0,2.5),pady=(2.5,0))
        self.bt_f.grid(row=4,column=5,padx=(0,2.5),pady=(2.5,0))
        self.bt_g.grid(row=4,column=6,padx=(0,2.5),pady=(2.5,0))
        self.bt_h.grid(row=4,column=7,padx=(0,2.5),pady=(2.5,0))
        self.bt_i.grid(row=4,column=8,padx=(0,2.5),pady=(2.5,0))
        self.bt_j.grid(row=4,column=9,padx=(0,2.5),pady=(2.5,0))
        self.bt_k.grid(row=4,column=10,padx=(0,2.5),pady=(2.5,0))
        self.bt_l.grid(row=4,column=11,padx=(0,2.5),pady=(2.5,0))
        self.bt_m.grid(row=4,column=12,padx=(0,2.5),pady=(2.5,0))
        self.bt_n.grid(row=5,column=0,padx=2.5,pady=2.5)
        self.bt_o.grid(row=5,column=1,padx=(0,2.5),pady=2.5)
        self.bt_p.grid(row=5,column=2,padx=(0,2.5),pady=2.5)
        self.bt_q.grid(row=5,column=3,padx=(0,2.5),pady=2.5)
        self.bt_r.grid(row=5,column=4,padx=(0,2.5),pady=2.5)
        self.bt_s.grid(row=5,column=5,padx=(0,2.5),pady=2.5)
        self.bt_t.grid(row=5,column=6,padx=(0,2.5),pady=2.5)
        self.bt_u.grid(row=5,column=7,padx=(0,2.5),pady=2.5)
        self.bt_v.grid(row=5,column=8,padx=(0,2.5),pady=2.5)
        self.bt_w.grid(row=5,column=9,padx=(0,2.5),pady=2.5)
        self.bt_x.grid(row=5,column=10,padx=(0,2.5),pady=2.5)
        self.bt_y.grid(row=5,column=11,padx=(0,2.5),pady=2.5)
        self.bt_z.grid(row=5,column=12,padx=(0,2.5),pady=2.5)
        self.lb_status.grid(row=6, columnspan=8)
        self.bt_resetar.grid(row=6, columnspan=13,padx=(150,2.5))
          

        def rand_palavra():
            palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
            palavra = random.choice(palavras)
            return palavra
        
        self.palavra = rand_palavra()

        self.letras_descobertas = ['_' for letra in self.palavra]

        self.lb_hidenPalavra.configure(text=self.letras_descobertas)

        def press(v):
            self.tentativa = v
            if self.tentativa in self.palavra and self.tentativa not in self.letras_escolhidas:
                index = 0
                self.letras_escolhidas.append(self.tentativa)
                for letra in self.palavra:
                    if self.tentativa == letra:
                        self.letras_descobertas[index] = letra
                        self.lb_hidenPalavra.configure(text=self.letras_descobertas)
                    index += 1

            elif self.tentativa not in self.palavra and self.tentativa not in self.letras_erradas:
                self.letras_erradas.append(self.tentativa)
                self.count += 1
                self.lb_imagem.configure(image=lista_imagem_status[self.count-1])

            self.lb_corretasAtt.configure(text=self.letras_escolhidas)
            self.lb_erradasAtt.configure(text=self.letras_erradas)

            status()

        def status():

            if '_' not in self.letras_descobertas:
                self.lb_status.configure(text='Você ganhou!')
                self.bt_a.configure(state='disabled')
                self.bt_b.configure(state='disabled')
                self.bt_c.configure(state='disabled')
                self.bt_d.configure(state='disabled')
                self.bt_e.configure(state='disabled')
                self.bt_f.configure(state='disabled')
                self.bt_g.configure(state='disabled')
                self.bt_h.configure(state='disabled')
                self.bt_i.configure(state='disabled')
                self.bt_j.configure(state='disabled')
                self.bt_k.configure(state='disabled')
                self.bt_l.configure(state='disabled')
                self.bt_m.configure(state='disabled')
                self.bt_n.configure(state='disabled')
                self.bt_o.configure(state='disabled')
                self.bt_p.configure(state='disabled')
                self.bt_q.configure(state='disabled')
                self.bt_r.configure(state='disabled')
                self.bt_s.configure(state='disabled')
                self.bt_t.configure(state='disabled')
                self.bt_u.configure(state='disabled')
                self.bt_v.configure(state='disabled')
                self.bt_w.configure(state='disabled')
                self.bt_x.configure(state='disabled')
                self.bt_y.configure(state='disabled')
                self.bt_z.configure(state='disabled')

            if self.count == 6:
                self.lb_status.configure(text='Você perdeu!')
                self.bt_a.configure(state='disabled')
                self.bt_b.configure(state='disabled')
                self.bt_c.configure(state='disabled')
                self.bt_d.configure(state='disabled')
                self.bt_e.configure(state='disabled')
                self.bt_f.configure(state='disabled')
                self.bt_g.configure(state='disabled')
                self.bt_h.configure(state='disabled')
                self.bt_i.configure(state='disabled')
                self.bt_j.configure(state='disabled')
                self.bt_k.configure(state='disabled')
                self.bt_l.configure(state='disabled')
                self.bt_m.configure(state='disabled')
                self.bt_n.configure(state='disabled')
                self.bt_o.configure(state='disabled')
                self.bt_p.configure(state='disabled')
                self.bt_q.configure(state='disabled')
                self.bt_r.configure(state='disabled')
                self.bt_s.configure(state='disabled')
                self.bt_t.configure(state='disabled')
                self.bt_u.configure(state='disabled')
                self.bt_v.configure(state='disabled')
                self.bt_w.configure(state='disabled')
                self.bt_x.configure(state='disabled')
                self.bt_y.configure(state='disabled')
                self.bt_z.configure(state='disabled')
        
        def reset():
            self.count = 0
            self.palavra = ''
            self.tentativa = ''
            self.letras_erradas.clear()
            self.letras_escolhidas.clear()
            self.lb_corretasAtt.configure(text=self.letras_escolhidas)
            self.lb_erradasAtt.configure(text=self.letras_erradas)
            self.lb_status.configure(text='')
            self.letras_descobertas.clear()
            self.palavra = rand_palavra()
            self.letras_descobertas = ['_' for letra in self.palavra]
            self.lb_hidenPalavra.configure(text=self.letras_descobertas)
            self.lb_imagem.configure(image=img1)
            self.bt_a.configure(state='normal')
            self.bt_b.configure(state='normal')
            self.bt_c.configure(state='normal')
            self.bt_d.configure(state='normal')
            self.bt_e.configure(state='normal')
            self.bt_f.configure(state='normal')
            self.bt_g.configure(state='normal')
            self.bt_h.configure(state='normal')
            self.bt_i.configure(state='normal')
            self.bt_j.configure(state='normal')
            self.bt_k.configure(state='normal')
            self.bt_l.configure(state='normal')
            self.bt_m.configure(state='normal')
            self.bt_n.configure(state='normal')
            self.bt_o.configure(state='normal')
            self.bt_p.configure(state='normal')
            self.bt_q.configure(state='normal')
            self.bt_r.configure(state='normal')
            self.bt_s.configure(state='normal')
            self.bt_t.configure(state='normal')
            self.bt_u.configure(state='normal')
            self.bt_v.configure(state='normal')
            self.bt_w.configure(state='normal')
            self.bt_x.configure(state='normal')
            self.bt_y.configure(state='normal')
            self.bt_z.configure(state='normal')



if __name__ == '__main__':
    App().mainloop()


# pyinstaller --noconfirm --onefile --windowed --add-data "C:/Users/danie/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/" App.py --icon=icone.ico --name="Hangman"