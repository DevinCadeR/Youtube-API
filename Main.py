from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI

app = FastAPI()

def CheckYTSubs(ChannelID):
    ProductLink = f"https://www.youtube.com/channel/{ChannelID}"
    Result = requests.get(ProductLink, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"})

    Doc = BeautifulSoup(Result.text, "html.parser").prettify()
    R = str(Doc).split("subscribers")[:-1]
    Q = str(R).split("simpleText")[-1]
    Z = str(Q).split('"')[2]
    A = str(Z).split(" ")[0]
    return A

def CheckYTTotalViews(ChannelID):
    ProductLink = f"https://www.youtube.com/channel/{ChannelID}/about"
    Result = requests.get(ProductLink, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"})

    Doc = BeautifulSoup(Result.text, "html.parser").prettify()
    R = str(Doc).split("views")[:-1]
    Q = str(R).split("simpleText")[-1]
    Z = str(Q).split('"')[2]
    A = str(Z).split(" ")[0]
    return A

@app.get("/subs/{ID}")
def subs(ID: str):
    X = ""
    try:
        X = CheckYTSubs(ID)
    except:
        X = "Invalid Channel ID"
    return {"content": X}

@app.get("/views/{ID}")
def views(ID: str):
    X = ""
    try:
        X = CheckYTTotalViews(ID)
    except:
        X = "Invalid Channel ID"
    return {"content": X}