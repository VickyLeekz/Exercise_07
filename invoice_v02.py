'''
Main: restaurant.py
'''
from datetime import datetime

__author__ = "8367998, Thalheim, 7077348, Pasichnyk"


class Invoice:
    '''
    Creates invoice for the table with their orders and mapps it to the table
    '''

    def __init__(self, invoice_id, table, total):
        self.invoice_id = invoice_id
        self.table = table
        self.total = total

    def generate_invoice(self, invoice_id, table, order):
        """
           This function creates an invoice for the table with their orders.
           It also creates a .txt file in the main directory, with the name, that
           cotntains the invoice number.
        """

        for i in range(1, table+1):
            invoice_id = i
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d_%H:%M:%S")
            path = "C:/Users/Anna/Documents/Uebung7_Team_work/invoice"

            # Creates .txt file and fills it with information about Table and order.
            try:
                with open(fr"{path}_{i}_{formatted_now}.txt", "w", encoding="utf-8") as f:
                    f.write("Invoice ID: " + str(invoice_id))
                    f.write("\n")
                    f.write("Table Number: " + str(table))
                    f.write("\n")
                    f.write("Order number: " + str(order))

                    # Writes every item name and price in the file.
                    for item in self.table.order.items():
                        f.write(f"{item.name}- {item.price:.2f}â‚¬\n")

                    # Writes total of order down.
                    f.write("\nGesamt: {self.total:.2f}â‚¬\n}")
                f.close()

            except Exception as e:
                print(f"The following error occured: {e}")
