import json
import os

from .productFactory import productFactory


def productLoader():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "productInfo.json"), 'r') as jsonFile:
        infoList = json.loads(jsonFile.read())
        return [productFactory(info["name"], info["sellIn"], info["quality"], info["type"]) for info in infoList]
