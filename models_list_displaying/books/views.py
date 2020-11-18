from django.shortcuts import render
from books.models import Book


books = Book.objects.all()


# def books_view(request, pub_date=None):
#     if pub_date:
#         date_list = []
#         current_page, prev_page, next_page = None, None, None
#         items = Book.objects.filter(pub_date__exact=pub_date)
#         template = 'books/show_books.html'
#         for date in books.order_by('pub_date'):
#             if date.pub_date in date_list:
#                 continue
#             date_list.append(date.pub_date)
#         for i, v in enumerate(date_list):
#             if str(pub_date) in str(v):
#                 prev_page = date_list[i - 1]
#                 if i - 1 < 0:
#                     prev_page = None
#                 if i + 1 == len(date_list):
#                     next_page = None
#                 else:
#                     next_page = date_list[i + 1]
#         context = {'items': items,
#                    'current_page': pub_date,
#                    'prev_page': prev_page,
#                    'next_page': next_page}
#     else:
#         items = books
#         template = 'books/books_list.html'
#         context = {'items': items}
#     return render(request, template, context)


def books_view(request, pub_date=None):
    if pub_date:
        items = Book.objects.filter(pub_date__exact=pub_date)
        template = 'books/show_books.html'
        left_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
        left_date = None
        if left_book:
            left_date = left_book.pub_date
        right_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
        right_date = None
        if right_book:
            right_date = right_book.pub_date
        context = {'items': items,
                   'current_page': pub_date,
                   'prev_page': left_date,
                   'next_page': right_date}

    else:
        items = books
        template = 'books/books_list.html'
        context = {'items': items}
    return render(request, template, context)
