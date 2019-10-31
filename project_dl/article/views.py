from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib import auth

from .forms import CommandForm
from .models import Article, Commands
# Create your views here.

def basic_one(request):
    view = 'basic_one'
    html = '<html><body>THIS IS %s VIEW</html></body>' % view
    return HttpResponse(html)

def template_two(request):
    view = 'template_two'
    t = get_template('myview.html')
    html = t.render({'name': view})
    return HttpResponse(html)

def template_three_simple(request):
    view = 'template_three'
    return render_to_response('myview.html', {'name' : view})

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all(),
                                                'username': auth.get_user(request).username})


def article(request, article_id=1):
    command_form = CommandForm
    args = {}
    args.update(csrf(request))  # Type of hackers attack
                                # Подделка данных
                                # Protected from attacks Create
                                # Token that consist unique characters
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Commands.objects.filter(comments_article_id=article_id)
    args['form'] = command_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:
        if str(article_id) in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(str(article_id), 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommandForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60) # session exists 60 seconds
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

