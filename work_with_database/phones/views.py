from django.shortcuts import render
from phones.models import Phone

phones = Phone.objects.all()


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        context = {'items': phones.order_by('name')}
    elif sorting == 'min_price':
        context = {'items': phones.order_by('price')}
    elif sorting == 'max_price':
        context = {'items': phones.order_by('-price')}
    elif not sorting:
        context = {'items': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    items = Phone.objects.get(slug__exact=slug)
    context = {'items': items}

    return render(request, template, context)
