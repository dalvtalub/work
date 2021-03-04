from django.shortcuts import render
from main.models import *
from django.db.models import Q
from django.http import JsonResponse
import datetime as dt


# before debugging write in terminal: set os.environ['DJANGO_SETTINGS_MODULE'] = 'САЙТ.settings'


def index(request):
    matches = []
    matches_now = []
    # all_matches = Matches.objects.order_by('time')
    # AJAX request: sort and view matches by team
    if request.is_ajax():
        team_name = request.POST['team'].title()
        try:
            team = Teams.objects.get(team=team_name)
            matches = Matches.objects.filter(Q(team1=team.id) | Q(team2=team.id))
            result = []
            for match in matches:
                result.append({
                    'team_name1': match.team1.team,
                    'team_name2': match.team2.team,
                    'time': match.time,
                    'url': f'team_lineup/{match.team1.team}__{match.team2.team}',
                })
            return JsonResponse({"result": result})
        except:
            return JsonResponse({"result": "Team is not exist"})
        # add matches and live matches
        # if match.team1.team == team:
        #     if match.time > dt.datetime.now(dt.timezone.utc):
        #         result.append(match)
        #     elif match.time <= dt.datetime.now(dt.timezone.utc) <= match.time + dt.timedelta(hours=1, minutes=30):
        #         matches_now.append(match)
        # if match.team2.team == team:
        #     if match.time > dt.datetime.now(dt.timezone.utc):
        #         matches.append(match)
        #     elif match.time <= dt.datetime.now(dt.timezone.utc) <= match.time + dt.timedelta(hours=1, minutes=30):
        #         matches_now.append(match)
    all_matches = Matches.objects.order_by('time')  # Match.objects.find(), order_by() for example: [:1]
    teams = Teams.objects.order_by('team')
    # view all matches and live matches
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
