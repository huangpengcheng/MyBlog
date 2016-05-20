from django.shortcuts import render, get_object_or_404
from my_blog.models import Article, Article_Tag, Article_genre
from django.shortcuts import redirect
from django.utils import timezone
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def article(request):
    article = Article.objects.all()
    tags = Article_Tag.objects.all()
    genres = Article_genre.objects.all()
    return render(request, 'index.html', { 'article': article,'tags':tags,'genres': genres})

def show_article_content(request, id):
    #article_content = Article.objects.get(id=int(id)).content
    article = get_object_or_404(Article,id=int(id))
    return render(request, 'article_content.html', {'article': article})

@login_required(login_url='/login/')
def create_article(request):
    if request.method == "POST":
        Article.objects.create(title=request.POST['title'], content=request.POST['content'], pub_date=timezone.now(),update_time=timezone.now(),tag=get_object_or_404(Article_Tag,id=int(request.POST['tag'])),genre=get_object_or_404(Article_genre,id=int(request.POST['gen'])) )
        return redirect('/')

    else:
        tags = Article_Tag.objects.all()
        gen = Article_genre.objects.all()
        return render(request, 'create_article.html', {'tags':tags,'gen':gen})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')        
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def show_tag(request,tag_id):
    tag = get_object_or_404(Article_Tag,id=int(tag_id))
    article = tag.article_set.all()
    tags = Article_Tag.objects.all()
    genres = Article_genre.objects.all()
    return render(request, 'index.html', { 'article': article,'tags':tags,'genres':genres})

def show_genre(request, genre_id):
    genre = get_object_or_404(Article_genre, id=int(genre_id))
    article = genre.article_set.all()
    genres = Article_genre.objects.all()
    tags = Article_Tag.objects.all()
    return render(request, 'index.html', {'article': article,'genres':genres,'tags':tags})
