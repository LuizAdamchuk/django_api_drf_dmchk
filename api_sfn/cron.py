import requests
from api_sfn.models import CronJob, Article


def mapperResponse(data):
    objs = [
    Article(
        site_id=l['id'],
        title=l['title'],
        imageUrl=l['imageUrl'],
        url=l['url'],
        newsSite=l['newsSite'],
        summary=l['summary']
    )
    for l in data
    ]
    return objs

def paginationList(page,limit):
    PARAMS = {'_limit':limit, '_start':page}
    URL = "https://api.spaceflightnewsapi.net/v3/articles"
    response = requests.get(url = URL, params = PARAMS)
    data = response.json()
    objs = mapperResponse(data)
    return objs

def getCount():
    URL = "https://api.spaceflightnewsapi.net/v3/articles/count"
    response = requests.get(url = URL)
    data = response.json()
    return data

def multipleRequests(total):
    for x in range(1000, total, 1000):
        articlesList = paginationList(x-999, x)
        try:
            Article.objects.bulk_create(articlesList)
        except:
            continue

def my_scheduled_job():
    totalArticlesSFNAPI = getCount()
    totalArticlesDMCHKAPI =CronJob.objects.last().quantity if CronJob.objects.last() else 0
    if totalArticlesDMCHKAPI  != totalArticlesSFNAPI:
        requests = totalArticlesSFNAPI - totalArticlesDMCHKAPI
        CronJob.objects.create(quantity=totalArticlesSFNAPI)
        if requests > 300:
            multipleRequests(totalArticlesSFNAPI)
        else:
            articlesList = paginationList(1, requests)
            Article.objects.bulk_create(articlesList)



    

