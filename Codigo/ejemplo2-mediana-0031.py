# EJEMPLO 2. Eliminación de ruido con filtro Mediano
import cv2

# Cargar la imagen
imagen = cv2.imread("Imagenes/ELEFANTE-0031.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original-0031", imagen)
cv2.imshow("Imagen con filtro de mediana-0031", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "Resultados/ELEFANTE_mediana_0031.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("Resultados/ELEFANTE_mediana_0031.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()