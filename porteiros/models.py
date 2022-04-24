from django.db import models

class Porteiro(models.Model):
    nome_completo = models.CharField(
        verbose_name= "Nome Completo",
        max_length= 194,
    )

    CPF = models.CharField(
        verbose_name= "CPF",
        max_length= 11,
    )

    telefone = models.CharField(
        verbose_name= "Telefone de contato",
        max_length= 11,
    )