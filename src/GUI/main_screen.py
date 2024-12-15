from tkinter import *
from tkinter import ttk
from interfaz_reconocimiento_facial import InterfazReconocimientoFacial
from interfaz_registro_biometria_facial import InterfazRegistroBiometriaFacial

'''
Aqui irá la interfaz de usuario en donde podrá elegir entre dos botones. Estos dos botones son:
- Registrar información biométrica de un cliente
- Reconocer clientes.

Aun estoy viendo una forma de hacer que la ejecución de reconocimiento de clientes sea permanente hasta presionar un determinado botón.
'''

class MainScreen:
    def __init__(self, root):
        self.root = root #Si no se define el atributo root dentro del codigo no se podra abrir otra ventana.
        root.title('Reconocimiento ONE')
        root.geometry("800x600")

        #self.image = PhotoImage(file="static/logos/onegymlogo.png") #Esperando al crisaceo...
        label_gym = Label(root, text="ONE GYM", font="bold")
        label_gym.place(relx=0.5,rely=0.1, anchor=CENTER)

        boton_registro_facial = Button(root, text="Registrar informacion biometrica clienta", width=40, command=self.abrir_ventana_registro_biometria_facial)
        boton_registro_facial.place(relx=0.5,rely=0.3, anchor=CENTER)

        boton_reconocimiento_facial = Button(root, text="Tomar asistencia", width=40, command=self.abrir_ventana_reconocimiento_facial)
        boton_reconocimiento_facial.place(relx=0.5,rely=0.4, anchor=CENTER)

    def abrir_ventana_reconocimiento_facial(self):
        self.root.destroy() #Cierra la ventana
        nueva_ventana = Tk()
        InterfazReconocimientoFacial(nueva_ventana)
        # nueva_ventana.mainloop() Al parecer no es necesario porque ya se ejecuta en la clase InterfazReconocimientoFacial

    def abrir_ventana_registro_biometria_facial(self):
        self.root.destroy()
        nueva_ventana = Tk()
        InterfazRegistroBiometriaFacial(nueva_ventana)

if __name__ == '__main__':
    root = Tk()
    MainScreen(root)
    root.mainloop()
