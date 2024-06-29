import cv2
from pyzbar import pyzbar

def validarQR():
    cap = cv2.VideoCapture(0)
    barcode_data = ""
    barcode_detected = False

    while cap.isOpened() and not barcode_detected:
        ret, frame = cap.read()
        if not ret:
            break
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            barcode_value = barcode.data.decode("utf-8")
            cv2.putText(frame, barcode_value, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Guardar el valor del código de barras en una variable
            barcode_data = barcode_value
            #print(f"Código de barras detectado: {barcode_data}")
            
            # Marcar que se ha detectado un código de barras
            barcode_detected = True

            # Reproducir el sonido
            #mixer.music.play()

        cv2.imshow("lector de código de barras", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return barcode_data

