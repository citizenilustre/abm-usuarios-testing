from django.forms import ModelForm, widgets
from personas.models import Personas


class PersonasForm(ModelForm):
    """
    Model Form para ingresar personas al sistema
    """

    class Meta:
        model = Personas
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'dni',
        ]
