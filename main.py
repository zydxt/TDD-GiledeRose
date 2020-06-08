from pprint import pprint
from sys import argv
from giledRose.productLoader import productLoader


def main():
    days = int(argv[1]) if argv and len(argv) > 1 else 0
    productList = productLoader()
    for day in range(days):
        for p in productList:
            p.updateInfoAfterOneDay()
        print("经过{day}天".format(day=day + 1).center(80, "*"))
        pprint([p.toDict() for p in productList])
    print("END".center(83, "*"))


if __name__ == '__main__':
    main()
