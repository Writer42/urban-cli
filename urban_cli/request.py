import requests
from requests import Response


def get_definition(word:str) -> Response: 
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term":word}

    headers = {
        "X-RapidAPI-Key": "0bec7d8db6mshb59170b100edffcp1c4824jsnfceaf6a343f3",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    return requests.request("GET", url, headers=headers, params=querystring)