# Nathan Quick
# 02/24/2025

class Product:
    # a constructor that initializes 3 attributes
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name                          # attribute 1
        self.price = price                        # attribute 2
        self.discountPercent = discountPercent    # attribute 3

    # a method that uses two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def __str__(self):
        return self.name + "|"  + str(self.price) + "|" + \
               str(self.discountPercent)


class LineItem:
    def __init__(self, product=None, quantity=1):
            self.product = product
            self.quantity = quantity

    def getTotal(self):
        return self.product.price * self.quantity

class Quality:
    def __init__(self, rating=0, review='', reviewNum=0):
        self.rating = rating
        self.review = review
        self.reviewNum = reviewNum
    
    def getRating(self):
       return self.rating
        
    def getReview(self):
        return self.review
        
    def getTotalReviews(self):
        return self.reviewNum