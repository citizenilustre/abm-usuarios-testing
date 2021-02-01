from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tarjetas.forms.tarjetas_form import TarjetasForm


@login_required
def abm_tarjetas(request):

    form = TarjetasForm()

    if request.method == 'POST':
        form = TarjetasForm(data=request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'tarjetas.html', {'form': form})



