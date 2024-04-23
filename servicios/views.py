from django.shortcuts import render

def my_view(request):
    if request.method == 'GET':
        # Acción para solicitudes GET
        return render(request, 'mi_app/get_template.html')

    elif request.method == 'POST':
        # Acción para solicitudes POST
        data = request.POST  # Si se envía un formulario POST
        # Si se envía un JSON en el cuerpo de la solicitud
        # data = json.loads(request.body)
        
        # Supongamos que esperamos un parámetro 'nombre'
        nombre = data.get('nombre')
        if nombre:
            # Se renderiza una plantilla diferente para las solicitudes POST
            return render(request, 'mi_app/post_template.html', {'nombre': nombre})
        else:
            return render(request, 'mi_app/error_template.html', status=400)
