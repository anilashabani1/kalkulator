import tkinter as tk

root = tk.Tk()

#Vendosja e hapsires se window, titulli i aplikacionit
root.geometry('500x500')
root.title('my first GUI app')

#Me label e kena vendos titullin.
label = tk.Label (root, text='Mirsevini te kalkulatori jone!', font=('Arial', 20))
#Me .pack() e kena vendos qat sen ne window
label.pack(padx= 20, pady= 20)

#E ka kriju ni input prej metodes .text()
textbox= tk.Text(root,height=3)
#Me .pack() e kena vendos qat sen ne window
textbox.pack()

buttonframe= tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="1", font=('Arial', 16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="2", font=('Arial', 16))
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="3", font=('Arial', 16))
btn1.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="+", font=('Arial', 16))
btn1.grid(row=0, column=3, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="4", font=('Arial', 16))
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="5", font=('Arial', 16))
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="6", font=('Arial', 16))
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="-", font=('Arial', 16))
btn1.grid(row=1, column=3, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="7", font=('Arial', 16))
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="8", font=('Arial', 16))
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="9", font=('Arial', 16))
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="*", font=('Arial', 16))
btn1.grid(row=2, column=3, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="/", font=('Arial', 16))
btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="=", font=('Arial', 16))
btn1.grid(row=3, column=1, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text="%", font=('Arial', 16))
btn1.grid(row=3, column=2, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")

#Krijimi i butonave
btn1= tk.Button(buttonframe, text=",", font=('Arial', 16))
btn1.grid(row=3, column=3, sticky=tk.W+tk.E)

buttonframe.pack (fill="x")


root.configure(bg='lightblue')

root.mainloop()