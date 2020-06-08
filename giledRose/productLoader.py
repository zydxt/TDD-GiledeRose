import json

from .productFactory import productFactory


def productLoader():
    with open("productInfo.json", 'r') as jsonFile:
        infoList = json.loads(jsonFile.read())
        return [productFactory(info["name"], info["sellIn"], info["quality"], info["type"]) for info in infoList]
