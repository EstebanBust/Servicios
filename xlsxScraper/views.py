from django.shortcuts import render
import openpyxl
import os


from django.shortcuts import render
import openpyxl

def listar_datos(request):
    # Cambiar el nombre del archivo si deseas que sea dinámico
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, 'DISTRIBUCIÓN 23-04-2024.xlsx')
    workbook = openpyxl.load_workbook(filename)
    
    # Seleccionar la primera hoja de cálculo (puedes cambiar el índice si es necesario)
    sheet = workbook.active
    
    # Lista para almacenar los datos de las filas
    datos = []
    
    # Iterar sobre las filas de la hoja de cálculo y agregarlas a la lista de datos
    for row in sheet.iter_rows(values_only=True):
        datos.append(row)
    
    # Renderizar la plantilla HTML y pasar los datos al contexto
    return render(request, 'xlsxScraper/scraper1.html', {'datos': datos})