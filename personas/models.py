from django.db import models


class Personas(models.Model):
    """
    Modelo que define a las personas que utilizan el servicio de credito
    """
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellido', max_length=100)
    direccion = models.CharField(verbose_name='Direccion', max_length=400)
    dni = models.IntegerField(verbose_name='Dni', unique=True)

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)

    class Meta:
        db_table = 'Personas'

    def get_related_credit_cards(self):
        """
        Obtiene todas las terjetas de credito relacionadas a una persona
        :return: credit cards
        """

        return self.tarjetas_set.all()
