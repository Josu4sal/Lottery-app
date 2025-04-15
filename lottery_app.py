
from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox as mb
import time

def close_win():
    root.destroy()

def mostrar_Disponibles():
    list_box.delete(0, END)
    for j,v  in dictionary_nums.items():
        if v[1]=="Disponible":
            list_box.insert(END, f'Numero: {j},     Estado: {v[1]}')
    list_box.pack(padx=30, pady=90,  fill="both")

def mostrar_NoDisponibles():
    list_box.delete(0, END)
    for j,v  in dictionary_nums.items():
        if v[1]=="No Disponible":
            list_box.insert(END, f'Numero: {j},     Nombre: {v[0]}      Estado: {v[1]}')    
    list_box.pack(padx=0, pady=90,  fill="both")
  
def comprarNumero(event):
    list_box.forget()
    try:
        num = int(numero.get())
        name = nombre.get().strip()
        if not name:
            mb.showwarning("Falta el nombre", "Por favor ingrese el nombre del comprador.")
            return

        if dictionary_nums[num][1] == "Disponible":
            dictionary_nums[num] = [name, "No Disponible"]
            mb.showinfo("Confirmación", f"¡El número {num} ha sido comprado exitosamente por {name}!")

        else:
            mb.showerror("Error", "Este número ya ha sido comprado.")
    except ValueError:
        mb.showerror("Error", "Por favor ingrese un número válido.")

def buscarPorNombre():
    list_box.delete(0, END)
    for i,v in dictionary_nums.items():
        if v[0]==nombre.get():
            list_box.insert(END,  f'Numero: {i},     Nombre: {v[0]}      Estado: {v[1]}')
    list_box.pack()

def buscarPorNumero():
    list_box.delete(0, END)
    for i,v in dictionary_nums.items():
        if i==int(numero.get()):
            list_box.insert(END,  f'Numero: {i},     Nombre: {v[0]}      Estado: {v[1]}')
    list_box.pack()


root=Tk()
root.configure(bg='light blue')

dictionary_nums={i:["",  "Disponible"] for i in range(0, 100)}

frame_entries= Frame(root)
frame_entries.pack(pady=8, expand=False)

frame_buttons= Frame(root, bg="light blue")
frame_buttons.pack(pady=20, padx=300, expand=False)
frame_list= Frame(root)
frame_list.pack(pady=20, expand=False,)

label_main=Label(frame_entries, text="Ingrese: ", height=1, font=('arial', 16), width=15)
label_main.grid(column=0, row=0, columnspan=2, pady=3)

label1=Label(frame_entries, text="Numero: ", height=2, font=('arial', 11), width=10)
label1.grid(column=0, row=1, pady=2)

label2=Label(frame_entries, text="Nombre: ", height=2, font=('arial', 11), width=10)
label2.grid(column=0, row=2)

numero=Entry(frame_entries )
numero.grid(column=1, row=1)
nombre=Entry(frame_entries)
nombre.grid(column=1, row=2, pady=10)

comprar_button = Button(frame_buttons, height=1, width=19, text="Comprar Numero", font=('arial', 14), command=comprarNumero)
comprar_button.grid(column=0, row=0, padx=6, pady=6)

mostrar_Disponibles_button=Button(frame_buttons, height=1, width=19, text="Mostrar Disponibles", font=('arial', 14),
    command=mostrar_Disponibles)
mostrar_Disponibles_button.grid(column=1, row=0, padx=6, pady=6)

mostrar_NoDisponibles_button=Button(frame_buttons, height=1, width=19, text="Mostrar No Disponibles", font=('arial', 14), 
    command=mostrar_NoDisponibles)
mostrar_NoDisponibles_button.grid(column=2, row=0, padx=6, pady=6)

Buscar_numero_button = Button(frame_buttons, height=1, width=19, text="Buscar por Numero",
        font=('arial', 14), command=buscarPorNumero)
Buscar_numero_button.grid(column=0, row=1, columnspan=2, padx=6, pady=6)

Buscar_nombre_button = Button(frame_buttons, height=1, width=19, text="Buscar por Nombre",
        font=('arial', 14), command=buscarPorNombre)
Buscar_nombre_button.grid(column=1, row=1, columnspan=2, padx=6, pady=6)

list_box=Listbox(frame_list, width=90, height=10)


#Key Bindings 
root.bind("<Return>", comprarNumero)


root.mainloop()






