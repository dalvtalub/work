from main.models import Teams, Matches
import random
import datetime
import django.db


# create matches for the year ahead. Condition: all teams have to play two matches with each others.
def run():
    for team1 in Teams.objects.all():
        for team2 in Teams.objects.all():
            try:
                if team1 == team2:
                    continue
                else:
                    match1 = Matches(team1=team1, team2=team2, time=data())
                    match2 = Matches(team1=team2, team2=team1, time=data())
                    match1.save()
                    match2.save()
            except django.db.utils.IntegrityError:
                continue


# create random date and time of match
def data():
    start_date = datetime.datetime.today()
    end_date = start_date + datetime.timedelta(days=365)
    end_date = end_date.toordinal()
    start_date = start_date.toordinal()
    random_day = datetime.datetime.fromordinal(random.randint(start_date, end_date))
    return random_day


run()
