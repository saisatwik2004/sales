from django.shortcuts import render
from .forms import SaleForm

def sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SaleForm()
    return render(request, 'sales_form.html', {'form': form})
