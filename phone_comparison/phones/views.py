from django.shortcuts import render
from phones.models import Phone

phones = Phone.objects.all()


def show_catalog(request):
    template = 'catalog.html'
    context = {'items': phones}
    return render(
        request,
        template,
        context
    )
