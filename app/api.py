from typing import Union
from fastapi import FastAPI
import datetime
import feedparser

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "service": "/rss/upworks-jobs/{parameter}?page={page_number}",
        "parameter": ["python", "datascraping", "airflow", "spark", "kafka", "machinelearning"],
        "page_number": ["10, 15, 20, 30"]
    }


@app.get("/rss/upworks-jobs/{skill}")
def read_item(skill: str, q: Union[str, None] = None, page: int = 10):
    url = ""
    data = []

    if skill == "python":
        url = f"https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&verified_payment_only=1&q=python&sort=recency&paging=0%3B{page}&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
    elif skill == "datascraping":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&q=data+scraping&verified_payment_only=1&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
    elif skill == "airflow":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&q=airflow&verified_payment_only=1&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
    elif skill == "spark":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&q=apache+spark&verified_payment_only=1&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
    elif skill == "kafka":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&q=kafka&verified_payment_only=1&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
    elif skill == "machinelearning":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&verified_payment_only=1&q=machine+learning&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"

    feed = feedparser.parse(url)

    for entry in feed.entries:
        dict_feed = {
            "job_id": datetime.datetime.now(),
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "published": entry.published,
        }
        data.append(dict_feed)

    return {"data": data}
