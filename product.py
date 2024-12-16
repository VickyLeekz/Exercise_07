'''
Main: restaurant.py
'''

import csv

__author__ = "8367998, Thalheim, 7077348, Pasichnyk"

class Product:
    '''
    Initialisiert ein Produkt.
    '''

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
        self.products = {}

    def read_products(self, filename='food.csv'):
        '''
        Reads products from csv file.
        '''
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)

                # Because of header it should skip the first row.
                next(reader)

                # Reads from each line just first and last column, because rest is irrelevant.
                # Adds all entries to the dictionary.
                # Key: name of product.
                # Value: price of product.
                for row in reader:
                    if len(row) == 4:
                        name, _, _, price = row
                        self.products[name] = float(price)
        except Exception as e:
            print(f"The following error occured: {e}")

        return self.products
