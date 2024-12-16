'''
Main: restaurant.py
'''

__author__ = "8367998, Thalheim, 7077348, Pasichnyk"

class Order:
    '''
    Creates order for the table with the chosen products.
    '''

    def __init__(self):
        self.items = []
        self.special_requests = []

    def add_item(self, product, special_request):
        '''
        Adds a product to the order.
        '''
        # Adds product to the list of items.
        # Adds tuple of product and special request to list of special requests
        self.items.append(product)
        if special_request:
            self.special_requests.append((product, special_request))
        return self.items

    def remove_item(self, product):
        '''
        Removes a product from order..
        '''
        try:
            self.items.remove(product)
        except Exception as e:
            print(f"The following error occured: {e}.")

        return self.items

    def total(self, products):
        '''
        Calculates the total of the products.
        '''
        total = 0
        # Checks for every item in self.items,
        # if it can be found in products dict.
        # If found, it reads price and calculates the sum of all item prices.
        for item in self.items:
            if item in products:
                total += products[item]
        return total
