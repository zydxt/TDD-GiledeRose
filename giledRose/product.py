from giledRose.exceptions import SellInException, QualityException


class ProductBase:

    def __init__(self, name, sellIn, quality):
        self.name = name
        if not isinstance(sellIn, int) or sellIn <= 0:
            raise SellInException()
        self.sellIn = sellIn
        self.quality = quality
        if not isinstance(quality, int) or not 0 <= quality < 50:
            raise QualityException()

    def updateInfoAfterOneDay(self):
        self.quality = self.calculateQualityAfterOneDay()
        self.sellIn -= 1

    def calculateQualityAfterOneDay(self):
        raise NotImplementedError("Product should implement this method")

    def getDecreaseQualityToday(self):
        raise NotImplementedError("Product should implement this method")


class NormalProduct(ProductBase):

    def calculateQualityAfterOneDay(self):
        return max(0, self.quality - self.getDecreaseQualityToday())

    def getDecreaseQualityToday(self):
        return 1 if self.sellIn >= 0 else 2


class BackstagePass(ProductBase):

    def calculateQualityAfterOneDay(self):
        if self.sellIn <= 0:
            return 0
        else:
            return max(0, min(50, self.quality - self.getDecreaseQualityToday()))

    def getDecreaseQualityToday(self):
        if self.sellIn > 10:
            return -1
        elif self.sellIn > 5:
            return -2
        elif self.sellIn > 0:
            return -3
