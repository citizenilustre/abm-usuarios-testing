from django.db import models
from personas.models import Personas


class Tarjetas(models.Model):
    """
    Modelo que guarda los datos asociados a las tarjetas de credito
    """

    # Las opciones de tarjetas habilitadas para operar
    CARDS_OPTIONS = [
        ('SQUA', 'SQUA'),
        ('SCO', 'SCO'),
        ('PERE', 'PERE'),
    ]

    name = models.CharField(choices=CARDS_OPTIONS, verbose_name='Nombre', max_length=100)
    number = models.IntegerField(verbose_name='Numero de tarjeta')
    owner = models.CharField(verbose_name='Titular', max_length=150)
    person = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name='Persona')
    credit_limit = models.IntegerField(verbose_name='Limite de credito')
    expiration_date = models.DateField(verbose_name='Vencimiento de la tarjeta')
    rate = models.FloatField(verbose_name='Tasa')

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    class Meta:
        db_table = 'Tarjetas'

    def get_card_info(self):
        """
        Otiene la informacion relacionada a una tarjeta a partir de su numero
        :return: queryset como lista que contiene la info de la tarjeta
        """

        card = Tarjetas.objects.filter(number=self.number).values()

        return card

    def check_validation(self):
        """
        Chequea si la tarjeta es valida para operar a partir de su fecha de vencimiento
        :return: True or False
        """
        from datetime import date

        today = date.today()

        if self.expiration_date > today:
            return True
        else:
            return False




