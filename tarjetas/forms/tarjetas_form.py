from django.forms import ModelForm, widgets
from tarjetas.models import Tarjetas


class TarjetasForm(ModelForm):
    """
    Model Form para ingresar tarjetas al sistema
    """

    class Meta:
        model = Tarjetas
        fields = [
            'name',
            'number',
            'owner',
            'person',
            'credit_limit',
            'expiration_date',
            'rate',
        ]

        widgets = {
            'expiration_date': widgets.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date'
                }
            ),
        }
