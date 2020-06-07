class SellInException(Exception):

    def __init__(self):
        super(SellInException, self).__init__("SellIn should be Integer greater than 0")


class QualityException(Exception):

    def __init__(self):
        super(QualityException, self).__init__("QualityException should be Integer between 0 to 50")
