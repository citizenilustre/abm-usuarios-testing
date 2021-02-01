"""
Modulo que contiene funciones auxiliares para obtener datos relacionados a las tarjetas de credito
y a las operaciones relacionadas con las mismas
"""


class CardRateError(Exception):
    """
    Error custom para cuando no se puede calcular la tasa
    determinado por una tarjeta inexistente ingresada
    """
    pass


def diferent_cards(card_1, card_2):
    """
    Identifica si una tarjeta es diferente a otra
    :param card_1: card object
    :param card_2: card object
    :return: True si es diferente or False si son iguales
    """

    card_1_number = card_1.number
    card_2_number = card_2.number

    if card_1_number != card_2_number:
        return True
    else:
        return False


def get_unique_cards():
    """
    Obtiene todas las tarjetas unicas en el sistema
    """
    from tarjetas.models import Tarjetas

    tarjetas_unicas = Tarjetas.objects.all().values('name').distinct()

    return tarjetas_unicas


class Operations:
    """
    Se encarga de chequear las operaciones relacionadas con las tarjetas
    """

    def __init__(self, operation_value, card):
        """

        :param operation_value: el valor de la operacion
        :param card: la tarjeta con la que se realiza la operacion representada como un objeto
        """

        self.operation_value = operation_value
        self.card = card

    def is_valid_operation(self):
        """
        Verifica si el la operacion es valida a partir del valor de la operacion
        :return: True si es valida or False si no es valida
        """

        if self.operation_value < 100:
            return True
        else:
            return False

    def is_valid_credit_card(self):
        """
        Se encarga de corroborar si la tarjeta de credito es valida para operar
        :return: True si es valida para operar or False si no lo es
        """

        return self.card.check_validation()  # Metodo del modelo Tarjetas

    def get_card_rate(self):
        """
        A partir de la tarjeta de credito se obtiene la tasa de la misma
        :return: integer representando la tasa
        """
        from datetime import date
        card = self.card.name.lower()  # se evitan errores en mayusculas o minusculas

        today = date.today()
        year = today.year
        month = today.month

        if card == 'squa':
            rate = year / month  # Tasa a cobrar por squa
            return rate

        elif card == 'sco':
            rate = today.day * 0.5  # Tasa a cobrar por sco
            return rate

        elif card == 'pere':
            rate = month * 0.1  # Tasa a cobrar por pere
            return rate

        else:
            raise CardRateError('No se puede obtener la tasa de la tarjeta {}'.format(card))

    def get_operation_rate(self):
        """
        Obtiene la tasa de una operacion
        :return: diccionario con la marca, tasa y el importe de la operacion
        """

        rate = self.get_card_rate()
        billing = self.operation_value * rate

        billing_information = {
            'rate': rate,
            'card': self.card.name,
            'billing': billing
        }

        return billing_information
