from django.shortcuts import render, redirect
from main.forms import ArticlesForm
from main.models import Articles


def add_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # after completing the addition - go to the galvanized page
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


# def add_article(request):
#     error = ''
#     if request.method == 'POST':
#         form = MatchesForm(request.POST)
#         team1 = request.POST['team1']
#         team2 = request.POST['team2']
#         if Teams.objects.filter(team=team1).exists() and Teams.objects.filter(team=team2).exists():
#             if form.is_valid():
#                 form.save()
#                 return redirect('/')  # after completing the addition - go to the galvanized page
#             else:
#                 error = 'Error form'
#         else:
#             error = 'One of these teams is not exist'
#
#     form = MatchesForm()
#     context = {
#         'form': form,
#         'error': error,
#     }
#     return render(request, 'add_article/add_article.html', context)
