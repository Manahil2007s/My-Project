class CarShop:

    def __init__(self, stock):
        self.stock = stock

    def displayCars(self):
        print('Total Cars:', self.stock)

    def sellCars(self, quantity):
        if quantity <= 0:
            print("Enter a positive value.")
        elif quantity > self.stock:
            print("Not enough cars in stock.")
        else:
            self.stock -= quantity
            print(f"{quantity} car(s) sold.")
            print("Cars left in stock:", self.stock)
while True:
    obj=CarShop(10000)
    uc=int(input('''
    1 Display Stocks
    2 Rent a Car
    3 Exit
        '''))
    if uc==1:
        obj.displayCars()
    elif uc==2:
        n=int(input("Enter the QTY---"))
        obj.sellCars(n)
    else:
        break

