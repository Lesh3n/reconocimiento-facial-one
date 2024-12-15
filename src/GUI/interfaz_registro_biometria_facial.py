from tkinter import *
from tkinter import ttk
from tkinter import font

import DAO.face_recognition_validations as face_recognition_validations

class InterfazRegistroBiometriaFacial:
    def __init__(self, root):
        self.root = root
        root.title('Registro de biometria facial')
        root.geometry("800x600")

        fuente_titulo_registro = font.Font(family="Helvetica",name='tituloInterfazRegistro', size=20, weight="bold")

        label_titulo_registro = Label(root, text="Registro de biometria facial", font=fuente_titulo_registro)
        label_titulo_registro.place(relx=0.5,rely=0.1, anchor=CENTER)

        #Treeview para ver los datos desde un recuadro en donde el usuario podra hacer doble click para comenzar el enrolamiento.
        self.tree = ttk.Treeview(root, columns=('clienteID', 'nombre'), show='headings', selectmode='browse' ) #selectmode='browse' permite seleccionar una fila a la vez.
        self.tree.heading('clienteID', text='ID')
        self.tree.heading('nombre', text='Nombre')
        self.tree.place(relx=0.5, rely=0.45, anchor=CENTER, width=600, height=300)

        self.cargar_datos_tree()

    #TODO: Retorna los datos con exito y se visualizan. Tengo que ver una forma de que al clickear cierta fila
    # se guarde en una variable el ID del cliente para luego incrustar el encoding del rostro en la base de datos segun
    # su ID
    def cargar_datos_tree(self):
        #Aqui ira la carga de datos desde la base de datos.
        registros_recuperados = face_recognition_validations.recuperar_clientes()
        print(registros_recuperados)
        if face_recognition_validations.recuperar_clientes():
            try:
                for registro in registros_recuperados:
                    self.tree.insert('', 'end', values=registro)
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')



if __name__ == '__main__':
    root = Tk()
    InterfazRegistroBiometriaFacial(root)
    root.mainloop()