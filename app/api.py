from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import feedparser

app = FastAPI()


# class Item(BaseModel):
#     title: str
#     url: str


@app.get("/")
def read_root():

    return {"service": "/rss/{parameter}", "parameter": ["python", "datascraping", "airflow", "spark", "kafka", "machinelearning"]}


@app.get("/rss/{skill}")
def read_item(skill: str):
    url = ""
    dict_feed = {
        "title": [],
        "link": [],
        "summary": [],
        "published": [],
    }
    if skill == "python":
        url = "https://www.upwork.com/ab/feed/jobs/rss?location=Americas%2CEurope%2COceania&verified_payment_only=1&q=python&sort=recency&paging=0%3B10&api_params=1&securityToken=d76b00a86ffa60baeb01da154db76acbc3e3fb340eb668f28c222bb46639c8703ab081313822496c9034327bdea763a7d925b795c8689537c032172bc7d66703&userUid=1183197118515154944&orgUid=1183197118523543553"
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
        dict_feed["title"].append(entry.title)
        dict_feed["link"].append(entry.link)
        dict_feed["summary"].append(entry.summary)
        dict_feed["published"].append(entry.published)

    return {"title": dict_feed["title"], "link": dict_feed["link"], "summary": dict_feed["summary"],
            "published": dict_feed["published"]}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
