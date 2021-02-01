from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personas.forms.personas_form import PersonasForm


@login_required
def abm_personas(request):
    """
    Alta baja modificacion de personas
    :return: html con form renderizado
    """

    form = PersonasForm()

    if request.method == 'POST':
        form = PersonasForm(data=request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'personas.html', {'form': form})
