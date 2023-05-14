from .models import Article
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import Http404
import sqlite3
from .forms import SignUpForm
from django.contrib import messages

def sign_in(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'registration.html')

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def article(request):
    return render(request, 'article.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":

            # Создаем подключение к БД.
            conn = sqlite3.connect('db.sqlite3')
            # Создаем курсор
            cursor = conn.cursor()

            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                cursor.execute("SELECT title FROM articles_article WHERE title = {0}".format(form["title"]))

                if cursor.fetchone():
                    form['errors'] = u"Такая статья уже есть в системе, придумайте другое название."
                    return render(request, 'create_post.html', {'form': form})

                else:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    #form['errors'] = u"Статья добавлена"
                    #return render(request, 'create_post.html', {'form': form})
                    return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})

            conn.close()
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404

def sign_up1(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})
