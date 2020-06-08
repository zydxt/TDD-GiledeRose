from .product import NormalProduct, BackstagePass

productTypeMap = {"normal": NormalProduct, "backstagePass": BackstagePass}


def productFactory(name, sellIn, quality, productType):
    if productType not in productTypeMap:
        raise TypeError("ProductType should be normal or backstagePass")
    return productTypeMap[productType](name, sellIn, quality)
