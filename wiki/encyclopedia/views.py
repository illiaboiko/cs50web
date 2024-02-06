from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def show_article(request, title):
    article = util.get_entry(title)
    if article == None:
        article = no_article(title)
    
    return render(
        request,
        "encyclopedia/article.html",
        {"article": markdown(article), "title": title.capitalize()},
    )

def no_article(title):
    return f"Article \"{title}\" not found. Try again"