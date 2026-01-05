from django.http import HttpResponse
from .models import Review


def catalog_page(request):
    reviews = Review.objects.all()

    # Формируем HTML без шаблона
    html = '<h1>Каталог отзывов</h1>'

    if reviews:
        for review in reviews:
            html += f'<p><strong>{review.name}</strong> ({review.email})<br>'
            html += f'{review.text}<br>'
            html += f'Проверено: {"Да" if review.checked else "Нет"}</p><hr>'
    else:
        html += '<p>Отзывов пока нет</p>'

    return HttpResponse(html)