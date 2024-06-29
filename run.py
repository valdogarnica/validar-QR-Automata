import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image
from curp import automata
from validar_qr import validarQR


def generar_qr():
    curp = curp_caja.get()
    r = automata(curp)
    if r:
        # Datos que deseas codificar en el código QR
        data = curp
    else:
        messagebox.showerror("ERROR", f"Ingresa una curp Valida: {curp}")
    # Crear una instancia de la clase QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agregar datos al objeto QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Crear una imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    messagebox.showinfo("QR Generado", f"QR Generado correctamente para {curp}")
    # guarda y muestra la imagen
    img.save("qr/" + curp + ".png")
    img.show()

def comprobar_qr():
    try:
        y = validarQR()
        re = automata(y)
        if re:
            print(y)
            messagebox.showinfo("Exito", f"ACCESO PERMITIDO: {y}")
        else:
            messagebox.showerror("ERROR", f"ACCESO DENEGADO: Intenta de Nuevo")
    except:
        print("Error no se puede validar el codigo")

ventana = tk.Tk()
ventana.title("PAGINA DE PRINCIPAL")
# TITULO DE LA VENTANA 
titulo = tk.Label(ventana, text="GENERAR CODIGO QR")
titulo.grid(row=0, column=3, padx=10, pady=5)

#BODY 
#LABEL
curp = tk.Label(ventana, text="INGRESA TU CURP: ")
curp.grid(row=2, column=1, padx=10, pady=5)
#INPUT CAJA
curp_caja = tk.Entry(ventana)
curp_caja.grid(row=2, column=2, padx=10, pady=5)



#BOTONES
generar = tk.Button(ventana, text="GENERAR QR", fg='white', bg='green', command=generar_qr)
generar.grid(row=6, column=2, padx=10, pady=100)

boton_validar_qr = tk.Button(ventana, text="VALIDAR QR", fg='white', bg='blue', command=comprobar_qr)
boton_validar_qr.grid(row=6, column=3, padx=10, pady=100)

#VENTANA
ventana.geometry('600x400+50+50')
ventana.resizable(True, True)
ventana.mainloop()