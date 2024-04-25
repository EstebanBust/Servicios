import openpyxl
from django.shortcuts import render
from servicios.models import Vehiculo, Dotacion, TipoDeDispositivo, Funcionario
import os

def listar_datos(request):
    # Obtener la ruta del archivo Excel
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, 'DISTRIBUCIÓN 23-04-2024.xlsx')

    # Cargar el libro de trabajo de Excel
    workbook = openpyxl.load_workbook(filename)

    # Seleccionar la hoja de trabajo
    sheet = workbook.active

    # Obtener los nombres de las columnas desde la primera fila del archivo Excel
    column_names = [cell.value for cell in sheet[1]]

    # Mapear los nombres de las columnas a los campos de los modelos
    column_mapping = {
        'Marca': 'marca',
        'Modelo': 'modelo',
        'Placa': 'placa',
        'Sigla': 'sigla',
        'Tipo de Dispositivo': 'tipo',
        'Nombre Dotacion': 'nombre',
        'Nombre Funcionario': 'nombres',
        'Apellidos Funcionario': 'apellidos',
        'Grado': 'grado',
        'Codigo': 'codigo',
        'Cemep': 'cemep',
        'Extra': 'extra'
    }

    # Iterar sobre las filas de la hoja de cálculo y crear instancias de modelos
    for row in sheet.iter_rows(min_row=2, values_only=True):
        tipo_dispositivo_values = {}
        dotacion_values = {}
        vehiculo_values = {}
        funcionario_values = {}

        # Iterar sobre los valores de las columnas y asignarlos a los diccionarios correspondientes si están presentes en el archivo Excel
        for column_name, column_mapping_key in column_mapping.items():
            if column_name in column_names:
                column_index = column_names.index(column_name)
                if column_mapping_key == 'tipo':
                    tipo_dispositivo_values[column_mapping_key] = row[column_index]
                elif column_mapping_key == 'nombre':
                    dotacion_values[column_mapping_key] = row[column_index]
                elif column_mapping_key in ['marca', 'modelo', 'placa', 'sigla']:
                    vehiculo_values[column_mapping_key] = row[column_index]
                elif column_mapping_key in ['nombres', 'apellidos', 'grado', 'codigo', 'cemep', 'extra']:
                    funcionario_values[column_mapping_key] = row[column_index]

        # Verificar si todos los valores requeridos están presentes para un tipo de dato
        if all(value for value in tipo_dispositivo_values.values()):
            tipo_dispositivo, _ = TipoDeDispositivo.objects.get_or_create(**tipo_dispositivo_values)

            if all(value for value in dotacion_values.values()):
                dotacion_values['tipo'] = tipo_dispositivo
                dotacion, _ = Dotacion.objects.get_or_create(**dotacion_values)

                if all(value for value in vehiculo_values.values()):
                    vehiculo_values['dotacion'] = dotacion
                    vehiculo = Vehiculo.objects.create(**vehiculo_values)

                if all(value for value in funcionario_values.values()):
                    funcionario_values['dotacion'] = dotacion
                    funcionario = Funcionario.objects.create(**funcionario_values)

    # El resto del código permanece igual

    # Obtener los datos para pasarlos al contexto si es necesario
    funcionarios = Funcionario.objects.all()

    # Pasar los datos al contexto
    return render(request, 'xlsxScraper/scraper1.html', {'funcionarios': funcionarios})