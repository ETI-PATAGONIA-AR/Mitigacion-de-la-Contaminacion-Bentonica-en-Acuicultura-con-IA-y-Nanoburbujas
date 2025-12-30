import cv2
import numpy as np
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import datetime
import os

class SistemaMonitoreoCompleto:
    def __init__(self, model_path):
        self.model = YOLO(model_path) if os.path.exists(model_path) else None
        self.root = tk.Tk()
        self.root.title("Analizador de Lodo y Peces (DEMO) - ETI Patagonia")
        self.root.geometry("450x300")
        self.root.configure(bg="#34495e")
        self.current_frame = None 

        tk.Label(
            self.root,
            text="Seleccione el modo de análisis:",
            fg="white",
            bg="#34495e",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Analizar Cámara en Vivo",
            command=lambda: self.procesar(0),
            width=30,
            bg="#27ae60",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Analizar Archivo MP4/AVI",
            command=self.elegir_video_archivo,
            width=30,
            bg="#2980b9",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Analizar Foto Estática (JPG/PNG)",
            command=self.elegir_foto_archivo,
            width=30,
            bg="#f39c12",
            fg="white"
        ).pack(pady=5)
        
        tk.Button(
            self.root,
            text="Herramienta: Etiquetar Lodo Manualmente",
            command=self.etiquetar_manual,
            width=30,
            bg="#e74c3c",
            fg="white"
        ).pack(pady=20)

    def elegir_video_archivo(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi"), ("All files", "*.*")]
        )
        if ruta:
            self.procesar(ruta)

    def elegir_foto_archivo(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png"), ("All files", "*.*")]
        )
        if ruta:
            frame = cv2.imread(ruta)
            if frame is not None:
                self.analizar_foto(frame)

    def analizar_foto(self, frame):
        frame_resultado = self.aplicar_analisis(frame)
        cv2.imshow("Resultado de Analisis de Foto", frame_resultado)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def procesar(self, fuente):
        cap = cv2.VideoCapture(fuente)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            self.current_frame = frame.copy()
            frame_resultado = self.aplicar_analisis(frame)

            cv2.imshow(
                "Monitoreo en Tiempo Real (Q para salir / Clic en Etiquetar)",
                frame_resultado
            )

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        cap.release()
        cv2.destroyAllWindows()
        
    def aplicar_analisis(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

        if self.model:
            results = self.model(gray_bgr, conf=0.4, verbose=False)
            res_plotted = results[0].plot()   # <<< FIX REAL
        else:
            res_plotted = frame.copy()

        gray_final = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(
            gray_final, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        kernel = np.ones((7, 7), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        total_lodo_pixeles = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > 2000:
                total_lodo_pixeles += cv2.contourArea(cnt)
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(res_plotted, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(
                    res_plotted,
                    "MANTO LODO",
                    (x, y - 15),
                    0,
                    0.6,
                    (0, 0, 255),
                    2
                )

        self.generar_reporte_log(frame, total_lodo_pixeles)
        return res_plotted
    
    def generar_reporte_log(self, frame, total_lodo_pixeles):
        height, width, _ = frame.shape
        area_total = height * width
        porcentaje_cobertura = (total_lodo_pixeles / area_total) * 100
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = {
            "Timestamp": [timestamp],
            "Area Total Pixels": [area_total],
            "Pixeles Lodo Detectado": [total_lodo_pixeles],
            "Porcentaje Cobertura (%)": [round(porcentaje_cobertura, 2)]
        }

        df = pd.DataFrame(log_entry)
        
        if not os.path.isfile("reporte_acuicultura.csv"):
            df.to_csv("reporte_acuicultura.csv", index=False, mode="a", header=True)
        else:
            df.to_csv("reporte_acuicultura.csv", index=False, mode="a", header=False)

    def etiquetar_manual(self):
        if self.current_frame is None:
            messagebox.showwarning(
                "Advertencia",
                "Inicia el análisis de cámara/video primero para capturar un frame."
            )
            return

        messagebox.showinfo(
            "Etiquetado Manual",
            "Dibuja un rectangulo alrededor del lodo/coliforme no detectado y presiona ENTER/ESPACIO."
        )
        
        bbox = cv2.selectROI(
            "Seleccionar Coliforme No Reconocido",
            self.current_frame,
            fromCenter=False
        )

        cv2.destroyWindow("Seleccionar Coliforme No Reconocido")
        
        if bbox != (0, 0, 0, 0):
            self.guardar_etiqueta(bbox, self.current_frame)
            messagebox.showinfo(
                "Guardado",
                f"Etiqueta guardada en 'dataset_manual/'. Coordenadas: {bbox}"
            )

    def guardar_etiqueta(self, bbox, frame):
        if not os.path.exists("dataset_manual"):
            os.makedirs("dataset_manual/images")
            os.makedirs("dataset_manual/labels")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        img_name = f"lodo_{timestamp}.jpg"
        label_name = f"lodo_{timestamp}.txt"
        
        cv2.imwrite(os.path.join("dataset_manual/images", img_name), frame)
        
        x, y, w, h = bbox
        img_h, img_w, _ = frame.shape

        x_center = (x + w / 2) / img_w
        y_center = (y + h / 2) / img_h
        width_norm = w / img_w
        height_norm = h / img_h
        
        with open(os.path.join("dataset_manual/labels", label_name), "w") as f:
            f.write(f"0 {x_center} {y_center} {width_norm} {height_norm}\n")

if __name__ == "__main__":
    app = SistemaMonitoreoCompleto("yolo11n-seg-fish-trained.pt")
    app.root.mainloop()
