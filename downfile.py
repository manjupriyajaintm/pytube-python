# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:40:33 2019

@author: MANJU
@Desc : download the pdf,txt,and img file form the internet
"""

import tkinter.filedialog as dialog
import urllib.request
import tkinter



def save(root,text):
    data=text.get('0.0', tkinter.END)    
    form=urllib.request.urlopen(data).read()
    filename = dialog.asksaveasfilename(parent=root, filetypes=[('Text', '*.txt'),('PDF',"*.pdf"),('img',"*.jpg")],title='Saveas. Image..')
    writer=open(filename,'wb')
    writer.write(form)
    writer.close()

def quit(root):
    root.destroy()
    
    
window = tkinter.Tk()
w = tkinter.Label(window, text="URL Path")
w.grid(column=0, row=0)
text = tkinter.Text(window,height=1)
text.grid(column=1, row=0)
menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label='Save', command=lambda : save(window, text))
filemenu.add_command(label='Quit', command=lambda : quit(window))
menubar.add_cascade(label= 'File', menu=filemenu)
window.config(menu=menubar)
filemenu = tkinter.Menu(menubar)
window.config(menu=menubar)
window.winfo_toplevel().title("Download File")


window.mainloop()
