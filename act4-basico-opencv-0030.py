# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import win32gui
import win32con
import win32api
print(" -*-*-*-*-* Cepeda Darrell NC 0030 *-*-*-*-*-")
# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")  # Imprime el título de la sección en la consola.
imgcarro_rojo = cv2.imread('carrorojo.jpg')  # Lee la imagen 'sample_image.jpg' y la guarda como matriz en 'img'.

if imgcarro_rojo is None:  # Verifica si la variable 'img' está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'sample_image.jpg'. Revisa el nombre y ubicación.")  # Muestra mensaje de error.
    sys.exit()  # Detiene inmediatamente la ejecución del programa para evitar fallos posteriores.
else:  # Si la imagen sí se cargó correctamente...
    print("Imagen cargada exitosamente.")  # Confirma en consola que la imagen está lista.

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN 0030")  # Imprime el título de la segunda sección.
height, width, channels = imgcarro_rojo.shape  # Extrae el alto (filas), ancho (columnas) y canales de color de la matriz.
print(f"Dimensiones de la imagen: {width}x{height} píxeles")  # Muestra el ancho por el alto en consola.
print(f"Número de canales de color: {channels}")  # Muestra cuántos canales tiene (3 para BGR: Azul, Verde, Rojo).
print(f"Tipo de dato de la imagen: {imgcarro_rojo.dtype}")  # Muestra el tipo de dato (uint8 = enteros de 0 a 255).
print(f"Total de datos/píxeles: {imgcarro_rojo.size}")  # Muestra la cantidad total de valores numéricos en la matriz.

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL del carro rojo")  # Imprime el título de la tercera sección.
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")  # Instrucción para el usuario.
cv2.imshow('img_carro rojo Original 0030', imgcarro_rojo)  # Abre una ventana llamada 'Imagen Original' y muestra la imagen cargada.
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.