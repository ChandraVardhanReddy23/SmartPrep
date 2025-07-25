import requests
from datetime import datetime
from .models import CodeforcesContest, LeetcodeContest
from django.http import HttpResponse
def fetch_codeforces_ratings(handle):
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    res = requests.get(url)
    saved_contests = []
    if res.status_code == 200:
        data = res.json()
        if data['status'] == 'OK':
            for c in data['result']:
                obj, created = CodeforcesContest.objects.update_or_create(
                    handle=handle,
                    contest_name=c['contestName'],
                    defaults={
                        'rank': c['rank'],
                        'old_rating': c['oldRating'],
                        'new_rating': c['newRating'],
                        'timestamp': datetime.fromtimestamp(c['ratingUpdateTimeSeconds'])
                    }
                )
                saved_contests.append(obj)
    return saved_contests

def fetch_leetcode_rating(username):
    url = "https://leetcode.com/graphql/"
    query = {
        "operationName": "userContestRankingInfo",
        "variables": {"username": username},
        "query": """
        query userContestRankingInfo($username: String!) {
            userContestRanking(username: $username) {
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
            }
        }
        """
    }
    res = requests.post(url, json=query)
    if res.status_code == 200:
        data = res.json()
        if data.get('data') and data['data'].get('userContestRanking'):
            r = data['data']['userContestRanking']
            obj, created = LeetcodeContest.objects.update_or_create(
                handle=username,
                defaults={
                    'attended_contests': r['attendedContestsCount'],
                    'rating': r['rating'],
                    'global_ranking': r['globalRanking'],
                    'total_participants': r['totalParticipants'],
                    'top_percentage': r['topPercentage']
                }
            )
            return obj
    return None
def fetch_and_save_data(user):
    user_profile = user.userprofile
    cf_handle = user_profile.codeforces_handle
    lc_handle = user_profile.leetcode_handle
    fetch_codeforces_ratings(cf_handle)
    fetch_leetcode_rating(lc_handle)
    return HttpResponse("Data fetched and saved successfully.")

