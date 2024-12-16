'''
restaurant.py
'''

from Team.invoice import Invoice
from Team.order import Order
from Team.product import Product

__author__ = "8367998, Thalheim, 7077348, Pasichnyk"


class Restaurant:
    '''
    Creates the whole system with help of the modules.
    '''
    def __init__(self):
        self.products = self.load_products()
        self.tables = {}
        self.invoice_counter = 0

    def load_products(self):
        '''
        Reads the available products from the CSV
        '''
        menu = Product("", 0)
        return menu.read_products()

    def show_available_products(self):
        '''
        Shows the menu with product names and prices.
        '''
        print("\nOur products:")
        for product_name, price in self.products.items():
            print(f"- {product_name}: {price:.2f}€")

    def create_table(self, table_number):
        '''
        Creates a new table for every order in the system..
        '''

        # Checks if table already exists.
        if table_number in self.tables:
            print(f"Table {table_number} already exists!")
        else:

            # Creates table in dictionary.
            try:
                new_order = Order()
                self.tables[table_number] = new_order
                print(f"Table {table_number} was created..")

            except Exception as e:
                print(f"The following error occured: {e}")

    def remove_table(self, table_number):
        '''
        Removes table in the system after paying.
        '''

        # Checks if table exists.
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist")
        else:

            # Deletes table from dictionary.
            del self.tables[table_number]
            print(f"Table {table_number} got removed.")

    def show_order_for_table(self, table_number):
        '''
        Shows the order of a table.
        '''

        # Checks if table exists.
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist.")
            return

        table = self.tables[table_number]
        print(f"Table {table_number} - Order:")

        # Checks if there are products in dictionary with this table.
        if not table.items:
            print("No products in order for this table.")
        else:

            # Prints all products of order
            for item in table.items:
                print(f"- {item}")


    def add_product_to_order(self, table_number, product, special_request):
        '''
        Adds a product to an order
        '''

        # Checks if table exists.
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist.")
            return

        # Shows menu.
        try:
            self.show_available_products()
        except Exception as e:
            print(f"The following error occured: {e}")

        # Checks if special request.
        if special_request:

            # Checks if product in menu.
            if product in self.products:
                extra = special_request
            else:

                # If no special request.
                print(f"{product} not found.")
                return
        else:
            # If no special request, extra is None.
            extra = None

        # Adds product (and special request) to order.
        try:
            self.tables[table_number].add_item(product, extra)
            print(f"{product} was added to order of table {table_number}.")
        except Exception as e:
            print(f"The following error occured: {e}")


    def remove_product_from_order(self, table_number, product):
        '''
        Removes product from order.
        '''

        # Checks if table exists.
        if table_number not in self.tables:
            print(f"table {table_number} does not exist..")
            return

        # Checks if product is in order.
        if product not in self.tables[table_number].order.items:
            print(f"{product} is not found in order of table {table_number}.")
            return

        # Removes item from order.
        try:
            self.tables[table_number].remove_item(product)
            print(f"{product} was removed from order of table {table_number}.")
        except Exception as e:
            print(f"The following error occured: {e}")

    def create_invoice(self, table_number):
        '''
        Creates and saves an invoice for a table's order.
        '''

        # Checks if table exists.
        if table_number not in self.tables:
            print(f"Table {table_number} does not exist.")
            return

        order = self.tables[table_number]
        total_price = order.total(self.products)

        invoice = Invoice(self.invoice_counter, table_number, total_price)

        # Generates invoice with help of invoice.py
        # Given invoice_id, table_number and total_price
        try:
            invoice.generate_invoice(self.invoice_counter, table_number, order)
        except Exception as e:
            print(f"The following error occured: {e}")

        # Sets invoice counter one up, so that each invoice has a new id.
        self.invoice_counter += 1
        print(f"Invoice for table {table_number} has been created.")


if __name__ == "__main__":
    restaurant = Restaurant()
