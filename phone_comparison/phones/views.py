from django.shortcuts import render
from phones.models import Phone

phones = Phone.objects.all().select_related('special')


def show_catalog(request):
    template = 'catalog.html'
    context = {'items': phones}
    return render(
        request,
        template,
        context
    )

for item in phones:
    print(item.name, item.special.property_n1)
