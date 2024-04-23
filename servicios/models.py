from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=20, blank=True)
    sigla = models.CharField(max_length=20)
    dotacion = models.ForeignKey('Dotacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class Escuadron(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    sigla = models.CharField(max_length=100)
    # Otros campos relevantes para el escuadrón

    def __str__(self):
        return self.nombre if self.nombre else "Escuadron"

class TipoDeDispositivo(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dotacion(models.Model):
    tipo = models.ForeignKey(TipoDeDispositivo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    # Otros campos relevantes para la dotación

    def __str__(self):
        return f"{self.tipo} - {self.nombre}"

class Funcionario(models.Model):
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    grado = models.CharField(max_length=100, blank=True)
    codigo = models.CharField(max_length=20, blank=True)
    cemep = models.CharField(max_length=20, blank=True)
    extra = models.CharField(max_length=20, blank=True)
    dotacion = models.ForeignKey(Dotacion, on_delete=models.CASCADE, null=True, blank=True)
    # Otros campos relevantes para los datos de la persona

    def __str__(self):
        return f"{self.grado}{self.nombres} {self.apellidos}" if self.nombres and self.apellidos else "Funcionario"

class Servicio(models.Model):
    fecha = models.DateField()
    funcionarios = models.ManyToManyField(Funcionario)
    # Otros campos relevantes para el servicio

    def __str__(self):
        return f"Servicio del {self.fecha}"

