from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown
from . import util


def index(request):
    css = util.get_entry("CSS")
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
    return f'Article "{title}" not found. Try again'


def search(request):
    entry_list = util.list_entries()
    query = request.GET["q"]
    if query in entry_list:
        return HttpResponseRedirect(reverse(f"encyclopedia:wiki/{query}"))

    return render(request, "encyclopedia/index.html")
