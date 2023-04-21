import BDDLogic
import sqlite3
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox
import tkinter.constants as tkc

class Frames(tk.Tk):

    ## Ventana principal de la interfaz gráfica
    def __init__(self, master):
        self.master = master        
        self.master.title ("Games Collection App")
        self.master.geometry ("940x300")
        self.master.resizable (False, False)
        self.master.configure (background="#0A0C45")
        
        self.create_frames()
    
    ## Se establecen los frames para cada tipo de Widget
    def create_frames(self):
        self.frame_botones = tk.Frame(self.master, width=200, height=300, background="#0A0C45")
        self.frame_botones.grid (row=0, column=0, rowspan=3)

        self.frame_texto = tk.Frame(self.master, width=500, height=300)
        self.frame_texto.grid(row=0, column=1, padx=20, pady=10, sticky="n")

        self.frame_bottom = tk.Frame(self.master, width=940, height=100)
        self.frame_bottom.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.frame_busqueda = tk.Frame(self.frame_bottom, width=300, height=100)
        self.frame_busqueda.grid(row=1, column=0, rowspan=4)
        self.frame_busqueda.configure(background="#0A0C45")

        self.style2 = ThemedStyle(self.frame_botones)
        self.style2.theme_use("clam")
        self.style2.configure("TLabel", borderwidth=2, relief="raised", foreground="black", background="white", padding=2)
        self.style2.configure("TEntry", borderwidth=2, relief="raised", foreground="black", background="white", padding=2)

class Widgets(Frames):
    def __init__(self, master):      
        super().__init__(master)

        self.create_widgets()

    ## Se crean los labels y los entrys principales
    def create_widgets(self):
        self.label_nombre = ttk.Label(self.frame_botones, text="Nombre: ", style="TLabel")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = ttk.Entry(self.frame_botones, style="TEntry")
        self.entry_nombre.grid(row=0, column=1)
        self.entry_nombre.bind('<Return>', lambda event: Functions.on_enter_pressed_guardar(self, event))

        self.label_genero = ttk.Label(self.frame_botones, text="Genero: ", style='TLabel')
        self.label_genero.grid(row=1, column=0, padx=10, pady=10)

        self.entry_genero = ttk.Entry(self.frame_botones, style="TEntry")
        self.entry_genero.grid(row=1, column=1)
        self.entry_genero.bind('<Return>', lambda event: Functions.on_enter_pressed_guardar(self, event))

        self.label_fecha = ttk.Label(self.frame_botones, text="Fecha: ", style='TLabel')
        self.label_fecha.grid(row=2, column=0, padx=10, pady=10)

        self.entry_fecha = ttk.Entry(self.frame_botones, style="TEntry")
        self.entry_fecha.grid(row=2, column=1)
        self.entry_fecha.bind('<Return>', lambda event: Functions.on_enter_pressed_guardar(self, event))

        self.label_empresa = ttk.Label(self.frame_botones, text="Empresa: ", style='TLabel')
        self.label_empresa.grid(row=3, column=0, padx=10, pady=10)

        self.entry_empresa = ttk.Entry(self.frame_botones, style="TEntry")
        self.entry_empresa.grid(row=3, column=1)
        self.entry_empresa.bind('<Return>', lambda event: Functions.on_enter_pressed_guardar(self, event))

        self.label_plataforma = ttk.Label(self.frame_botones, text="Plataforma: ", style='TLabel')
        self.label_plataforma.grid(row=4, column=0, padx=10, pady=10)

        self.entry_plataforma = ttk.Entry(self.frame_botones, style="TEntry")
        self.entry_plataforma.grid(row=4, column=1)
        self.entry_plataforma.bind('<Return>', lambda event: Functions.on_enter_pressed_guardar(self, event))

        self.busqueda_entry = tk.Entry(self.frame_busqueda)
        self.busqueda_entry.grid(row=0, column=1)
        self.busqueda_entry.bind("<Return>", lambda event: Functions.on_enter_pressed_buscar(self, event))

        self.boton_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=lambda: Functions.buscar_juego(self))
        self.boton_buscar.grid(row=0, column=2, padx=10)

        self.boton_guardar = tk.Button(self.frame_botones, text="Guardar", command=lambda: Functions.save(self))
        self.boton_guardar.grid(row=7, column=0, padx=5, pady=10, sticky="s")

        self.boton_borrar = tk.Button(self.frame_botones, text="Borrar", command=lambda: Functions.delete(self))
        self.boton_borrar.grid(row=7, column=1, padx=5, pady=10, sticky="s")

        self.empty_label = tk.Label(self.frame_busqueda, width=20)
        self.empty_label.grid(row=0, column=0)
        self.empty_label.configure(background="#0A0C45")

        self.total_label = tk.Label(self.frame_busqueda, text="Juegos Totales: 0 ", width=15)
        self.total_label.config(text=f"Juegos Totales: {BDDLogic.totales()}")
        self.total_label.grid(row=0, column=5, padx=10, pady=10, sticky="w")

class Treeview(Widgets):
    def __init__(self, master):
        super().__init__(master)

        ## Se establecen los estilos vistuales del tipo Label y Entry
        self.style = ThemedStyle(root)
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading", foreground="black", background="lightblue", borderwidth=2, relief="raised")

        self.tree = ttk.Treeview(self.frame_texto, columns=("nombre", "genero", "fecha", "empresa", "plataforma"), show="headings", style="Treeview")
        self.tree.grid(row=0, column=0, rowspan=6)

        self.scrollbar = ttk.Scrollbar(self.frame_texto, orient='vertical', command=self.tree.yview)
        self.scrollbar.grid(row=0, column=10, rowspan=7, sticky='ns')

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.column("nombre", width=300)
        self.tree.column("plataforma", width=70)
        self.tree.column("fecha", width=70)
        self.tree.column("genero", width=90)
        self.tree.column("empresa", width=150) 

        self.tree.heading("nombre", text="Nombre", command=lambda: Functions.refresh_treeview(self))
        self.tree.heading("genero", text="Género")
        self.tree.heading("fecha", text="Fecha", command=lambda: Functions.order_fecha(self))
        self.tree.heading("empresa", text="Empresa")
        self.tree.heading("plataforma", text="Plataforma")

        self.conexion = BDDLogic.crear_conexion()
        self.juegos = BDDLogic.get_juegos(self.conexion)

        for juego in self.juegos:
            self.tree.insert("", "end", text="", values=(juego[1], juego[2], juego[3], juego[4], juego[5]))

        root.protocol("WM_DELETE_WINDOW", Functions.cerrar_programa)

class Functions(Treeview):
    def __init__(self, master):
        super().__init__(master)

    ## Actualiza el TreeView
    def refresh_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        conexion = BDDLogic.crear_conexion()
        self.juegos = BDDLogic.get_juegos(conexion) 

        for juego in self.juegos:
            self.tree.insert("", "end", text="", values=(juego[1], juego[2], juego[3], juego[4], juego[5]))
            self.tree.selection_set(self.tree.get_children()[0])
            self.tree.focus(self.tree.get_children()[0])
            self.tree.see(self.tree.get_children()[0])

    ## Limpia los campos de entrada y hace focus sobre la entrada "Nombre"        
    def clean_fields(self):
        self.entry_nombre.delete(0, tkc.END)
        self.entry_genero.delete(0, tkc.END)
        self.entry_fecha.delete(0, tkc.END)
        self.entry_empresa.delete(0, tkc.END)
        self.entry_plataforma.delete(0, tkc.END)
        self.entry_nombre.focus()
    
    ## Muestra el total de los juegos guardados
    def totales(self):
        self.total_label.config(text=f"Juegos Totales: {BDDLogic.totales()}")
    
    ## Guarda los datos de entrada en la Base de Datos
    def save(self):
        conexion = sqlite3.connect("games.db")
        nombre = self.entry_nombre.get()
        genero = self.entry_genero.get()
        fecha = self.entry_fecha.get()
        empresa = self.entry_empresa.get()
        plataforma = self.entry_plataforma.get()

        if nombre and genero and fecha and empresa and plataforma:
            game_exist = BDDLogic.validation(conexion, nombre)
            if game_exist > 0:
                messagebox.showerror("Error", "Este juego ya existe en la Base de Datos.")
            else:
                BDDLogic.save_game(conexion, nombre, genero, fecha, empresa, plataforma)
                Functions.clean_fields(self)
                Functions.refresh_treeview(self)
                Functions.totales(self)
                self.tree.selection_set(self.tree.get_children()[-1])
                self.tree.focus(self.tree.get_children()[-1])
                self.tree.see(self.tree.get_children()[-1])
                
        else:
            messagebox.showwarning("Campos Vacios","Todos los campos deben estar completos.")

    ## Elimina un registro de la Base de Datos
    def delete(self):
        selected = self.tree.focus()
        if selected:
            nombre = self.tree.item(selected)['values'][0]
            BDDLogic.delete_game(self.conexion, nombre)
            Functions.refresh_treeview(self)
            Functions.totales(self)

    ## Ordena los registros por "Fecha"
    def order_fecha(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        order = BDDLogic.order_by_date(self.conexion)
        for juego in order:
            self.tree.insert("", "end", text="", values=(juego[1], juego[2], juego[3], juego[4], juego[5]))
            self.tree.selection_set(self.tree.get_children()[0])
            self.tree.focus(self.tree.get_children()[0])
            self.tree.see(self.tree.get_children()[0])

    ## Busca un dato en la base de datos desde la entrada "Buscar"
    def buscar_juego(self):
        nombre_juego = self.busqueda_entry.get()

        # Limpiar resultados anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

        if nombre_juego == "":
            Functions.refresh_treeview(self)

        # Muestra los resultados de busqueda en el TreeView
        else:
            resultados = BDDLogic.search_game(self.conexion, nombre_juego)
            if resultados:
                for juego in resultados:
                    self.tree.insert("", "end", text="", values=(juego[1], juego[2], juego[3], juego[4], juego[5]))
                
                # Seleccionar el primer resultado y hacer focus
                self.tree.selection_set(self.tree.get_children()[0])
                self.tree.focus(self.tree.get_children()[0])
                self.tree.see(self.tree.get_children()[0])
                self.busqueda_entry.delete(0, tkc.END)
            else:
                self.busqueda_entry.delete(0, tkc.END)
                messagebox.showerror("Error", "Juego no encontrado en la base de datos")

    ## Indica el mensaje que se mostrara al cerrar el programa
    def cerrar_programa():
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            root.destroy()

    def on_enter_pressed_buscar(self, event):
        Functions.buscar_juego(self)

    def on_enter_pressed_guardar(self, event):
        Functions.save(self)

root = tk.Tk()
app = Treeview(root)
root.mainloop()