import os
import subprocess
import sys
from tkinter import Tk, Button, messagebox

# desocupar puerto
# os.system('lsof -i :5000')
# os.system('kill -9 1234')

class Vista:
    
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.master.title('Aplicación')
        self.master.geometry('400x100')
        self.master.resizable(0, 0)
        self.boton = Button(master, text='Abrir servidor', command=self.lanzar_servidor)
        self.boton.pack(side='left')
        self.apagar = Button(master, text='Apagar servidor', command=self.apagar_servidor)
        self.apagar.pack(side='left')
        self.salir = Button(master, text='Salir', command=self.salir)
        self.salir.pack(side='left')
        # agregar ruta al servidor
        self.ruta = os.path.abspath(os.path.dirname(__file__))
        self.ruta_ser = os.path.join(self.ruta, 'servidores/servidor.py')
        self.proceso = None

    def salir(self):
        if self.proceso is not None:
            self.proceso.kill()
        self.master.quit()
        self.master.destroy()
    
    def lanzar_servidor(self):
        self.proceso = subprocess.Popen([sys.executable, self.ruta_ser])
        messagebox.showinfo('Servidor', 'Servidor lanzado')
    
    def apagar_servidor(self):
        if self.proceso is not None:
            self.proceso.kill()
            print('...')
            messagebox.showinfo('Servidor', 'Servidor apagado')
        else:
            messagebox.showinfo('Servidor', 'Servidor no lanzado')

def main():
    root = Tk()
    app = Vista(root)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()