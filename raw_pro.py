#Apicacion para registrar los numeros disponibles y ya comprados 

from tkinter import *
import tkinter as tkk

dictonary_nums={i: "Disponible" for i in range(0, 100)}

def mostrarDisponible():
    for clave, valor in dictonary_nums.items():
        if valor=="Disponible":
            print(f"Numero: {clave} Estado: {valor}")

def mostrarComprados():
    for clave, valor in dictonary_nums.items():
        if valor[1]=="No disponible":
            print(f"Numero: {clave} Estado: {valor[1]} Comprador: {valor[0]}")

def comprarNumero():
    numero=int(input("Cual numero desea comprar?  >> "))
    if dictonary_nums[numero]=="Disponible":
        comprador=input("Quien compra este numero? >> ")
        dictonary_nums[numero]=[comprador, "No disponible"]

        print("Numero comprado exitosamente!!")   

    else:
        print("Algo salio mal!!")

def buscarPorComprador(d):
    nombre=input("Ingrese el nombre del comprador: >> ")
    for i,v in d.items():
        if v[0]==nombre:
            print(f"El numero que compro {nombre} es {i}")

def buscarPorNumero(d):
    numero=int(input("Ingrese el Numero comprado: >> "))
    for i,v in d.items():
        if i==numero:
            print(f"El numero {numero } fue comprado por {v[0]}")
        

mostrarDisponible()
comprarNumero()
mostrarComprados()
buscarPorComprador(dictonary_nums)
buscarPorNumero(dictonary_nums)
