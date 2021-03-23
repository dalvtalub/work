from django.shortcuts import render, redirect
from main.forms import ArticlesForm


def add_article(request):
    error = ''
    # checking POST request. If it's valid we add it to db
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles')  # after completing the addition - go to the galvanized page
        else:
            error = 'Error form'
    # if request.method == 'POST':
    #     form = ArticlesForm(request.POST)
    #     text = request.POST['text']
    #     if Articles.objects.filter(text=text).exists():
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/')  # after completing the addition - go to the galvanized page
    #         else:
    #             error = 'Error form'
    #     else:
    #         error = 'This article is exist'
    form = ArticlesForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'add_article/add_article.html', context)
