from django.db import models
from django.contrib.auth.models import User

class Feriado(models.Model):
    nome = models.CharField(max_length=100)  
    data = models.DateField(unique=True)
    ponto_facultativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.data}"
    def __str__(self):
        return f"{self.nome} - {self.data}"

class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Sala {self.numero}"

class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome} - {self.turno.nome}"

class Aula(models.Model):
    STATUS_CHOICES = [
        ('caminho', 'A caminho'),
        ('ausente', 'Ausente'),
        ('presente', 'Presente'),
    ]
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ausente')

    
    def __str__(self):
        return f"Aula em {self.data} - {self.professor.nome} - {self.status}"
