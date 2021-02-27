from django.shortcuts import render
from main.models import Matches, Teams, Cards, Articles
import datetime as dt
from django.http import JsonResponse, HttpResponse


# before debugging write in terminal: set os.environ['DJANGO_SETTINGS_MODULE'] = 'САЙТ.settings'
def index(request):
    if request.method == 'POST':
        team = request.POST['team']
        matches = []
        matches_now = []
        all_matches = Matches.objects.order_by('time')
        for match in all_matches:
            if match.team1.team == team:
                if match.time > dt.datetime.now(dt.timezone.utc):
                    matches.append(match)
                elif match.time <= dt.datetime.now(dt.timezone.utc) <= match.time + dt.timedelta(hours=1, minutes=30):
                    matches_now.append(match)
            if match.team2.team == team:
                if match.time > dt.datetime.now(dt.timezone.utc):
                    matches.append(match)
                elif match.time <= dt.datetime.now(dt.timezone.utc) <= match.time + dt.timedelta(hours=1, minutes=30):
                    matches_now.append(match)
        context = {
            'matches': matches,
            'matches_now': matches_now,
        }
        return render(request, 'main/index.html', context)
    # after completing the addition - go to the galvanized page
    matches = []
    matches_now = []
    all_matches = Matches.objects.order_by('time')  # Match.objects.find(), order_by() for example: [:1]
    teams = Teams.objects.order_by('team')

    for match in all_matches:
        if match.time > dt.datetime.now(dt.timezone.utc):
            matches.append(match)
        elif match.time <= dt.datetime.now(dt.timezone.utc) <= match.time + dt.timedelta(hours=1, minutes=30):
            matches_now.append(match)
    context = {
        'matches': matches,
        'matches_now': matches_now,
        'teams': teams,
    }
    return render(request, 'main/index.html', context)


def about_us(request):
    cards = Cards.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'main/about_us.html', context)


def articles(request):
    articles = Articles.objects.all()
    content = {
        'articles': articles,
        'number': 0,
    }
    return render(request, 'main/articles.html', content)


def team_lineup(request, team1, team2):
    logos = Teams.objects.all()
    content = {
        'team1': team1,
        'team2': team2,
        'logos': logos,
    }
    return render(request, 'main/team_line-up.html', content)
