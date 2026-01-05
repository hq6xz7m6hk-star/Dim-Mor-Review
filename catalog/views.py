from django.http import HttpResponse
from .models import Review
from django.shortcuts import render, redirect
from django.middleware.csrf import get_token

def catalog_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        Review.objects.create(
            name=name,
            email=email,
            text=text,
            checked=False
        )

        return redirect('/')

    reviews = Review.objects.all()

    # Получаем CSRF токен
    csrf_token = get_token(request)

    html = '<h1>Отзывы</h1>'

    if reviews:
        for review in reviews:
            html += f'<p><strong>{review.name}</strong> ({review.email})<br>'
            html += f'{review.text}<br>'
            html += f'Проверено: {"Да" if review.checked else "Нет"}</p><hr>'
    else:
        html += '<p>Отзывов пока нет</p>'

    html += '<h2>Добавить отзыв</h2>'
    html += '<form method="POST">'
    # Вставляем токен вручную
    html += f'<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">'
    html += '<p>Имя: <input type="text" name="name" required></p>'
    html += '<p>Email: <input type="email" name="email" required></p>'
    html += '<p>Отзыв:<br><textarea name="text" rows="5" cols="50" required></textarea></p>'
    html += '<button type="submit">Отправить отзыв</button>'
    html += '</form>'

    return HttpResponse(html)





