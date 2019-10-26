from django.http import HttpResponse, Http404
from .models import *
# from django.template import loader
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):

    latest_articles = Article.objects.order_by('-article_date')

    """Using render() to laod the template"""
    return render(request, "myFirstApp/index.html", {'latest_articles':latest_articles})

    """Using loader.get_template(context, request)"""
    #template = loader.get_template('myFirstApp/index.html')
    #context = {
    #    'latest_articles':latest_articles,
    #}
    return HttpResponse(template.render(context,request))

    """Using simple HttpResponse()"""
    ans = '<br>'.join([a.article_name for a in latest_articles])
    return HttpResponse(
    "<center><b><h2> <br><br>More beautiful outpus is coming <br>The list of articles<br> %s <h2></b></center>"%ans
    )

def article(request, article_id):
    """Using get_object_or_404() shortcut to return PNF 404"""
    art = get_object_or_404(Article, pk=article_id)
    print(type(art), art)
    return render(request, "myFirstApp/article.html", {"article":art})

    # try:
    #     article = Article.objects.get(pk=article_id)
    # except:
    #     """using Http404() to raise an exception of page not found"""
    #     raise Http404("No such article by id %i" %article_id)
    #
    #     """Using simple HttpResponse to say that there is no such article by given id"""
    #     return HttpResponse("No Such Article")
    return HttpResponse("This article’s desciption is %s" % article.article_text)

def search(request, article_text):
    search_res = list(Article.objects.filter(article_text__contains=article_text).values_list("article_text"))
    try:
        for i in search_res:
            articles = articles + "<h3>%i: "%(search_res.index(i)+1) + str(*i) + "</h3><br>"
        return HttpResponse("<h2>This is the result of search</h2> %s" % articles)
    except:
        return HttpResponse("No such articles")

def archive(request):
    return HttpResponse("This are the articles for the last N years/months/days <br>")

def showComments(request, article_id):
    return HttpResponse("This is all comments to this article %i" % article_id)
