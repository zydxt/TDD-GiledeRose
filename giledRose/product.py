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
