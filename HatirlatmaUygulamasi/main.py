from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

master = Tk()
canvas = Canvas(master, height=450, width=750)
canvas.pack()
frame_ust = Frame(master, bg="#add8e6")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)
frame_alt_sol = Frame(master, bg="#add8e6")
frame_alt_sol.place(relx=0.1, rely=0.23, relwidth=0.23, relheight=0.6)
frame_alt_sag = Frame(master, bg="#add8e6")
frame_alt_sag.place(relx=0.34, rely=0.23, relwidth=0.51, relheight=0.6)
hatirlatma_tipi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tipi", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)
hatirlatma_tipi_secilen = StringVar(frame_ust)
hatirlatma_tipi_secilen.set("\t")
hatirlatma_tipi_menu = OptionMenu(frame_ust, hatirlatma_tipi_secilen, "Doğum Günü", "Alışveriş", "Bayram")
hatirlatma_tipi_menu.pack(padx=10, pady=10, side=LEFT)
hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, background='orange', foreground='black', borderwidth=1,
                                    locale='de_DE')
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)
hatirlatma_tarihi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tarihi", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)
Label(frame_alt_sol, text="Hatırlatma Yöntemi", bg="#add8e6", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)
varRadio = IntVar()
R1 = Radiobutton(frame_alt_sol, text="E-posta Gönder", variable=varRadio, value=1, font="Verdana 8", bg="#add8e6")
R1.pack(padx=15, pady=5, anchor=NW)
R2 = Radiobutton(frame_alt_sol, text="Sisteme Gönder", variable=varRadio, value=2, font="Verdana 8", bg="#add8e6")
R2.pack(padx=15, pady=5, anchor=NW)
varCheck1 = IntVar()
C1 = Checkbutton(frame_alt_sol, text="Aynı Gün", variable=varCheck1, onvalue=1, offvalue=0, font="Verdana 7",
                 bg="#add8e6")
C1.pack(padx=25, pady=2, anchor=NW)
varCheck2 = IntVar()
C2 = Checkbutton(frame_alt_sol, text="Bir Gün Önce", variable=varCheck2, onvalue=1, offvalue=0, font="Verdana 7",
                 bg="#add8e6")
C2.pack(padx=25, pady=2, anchor=NW)
varCheck3 = IntVar()
C3 = Checkbutton(frame_alt_sol, text="Bir Hafta Önce", variable=varCheck3, onvalue=1, offvalue=0, font="Verdana 7",
                 bg="#add8e6")
C3.pack(padx=25, pady=2, anchor=NW)
Label(frame_alt_sag, text="Hatırlatma Mesajı", bg="#add8e6", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)
metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure('stil', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
metin_alani.pack()
karsilama_metni = "Mesajınızı giriniz."
metin_alani.insert(END, karsilama_metni, 'stil')


def gonder():
    son_mesaj = ""
    try:
        if varRadio.get():
            if varRadio.get() == 1:
                son_mesaj += "E-posta yolu ile hatırlatma yapılacaktır."
                tip = hatirlatma_tipi_secilen.get() if hatirlatma_tipi_secilen.get() != "\t" else "Genel"
                tarih = hatirlatma_tarih_secici.get()
                mesaj = metin_alani.get("1.0", "END")
                with open('hatirlatmalar.txt', 'w') as dosya:
                    dosya.write("{} kategorisinde {} tarihli ve {} notuyla hatırlatma!".format(tip, tarih, mesaj))
                    dosya.close()
            elif varRadio.get() == 2:
                son_mesaj += "Sisteme hatırlatma yapılacaktır."
            messagebox.showinfo("İşlem Başarılı", son_mesaj)
        else:
            son_mesaj += "Gerekli alanların doldurulduğundan emin olun."
            messagebox.showwarning("Yetersiz bilgi", son_mesaj)
    except:
        son_mesaj += "İşlem Başarısız"
        messagebox.showerror("Başarısız İşlem", son_mesaj)
    finally:
        master.destroy()


gonder_butonu = Button(frame_alt_sag, text='Gönder', command=gonder)
gonder_butonu.pack(anchor=S)
master.mainloop()