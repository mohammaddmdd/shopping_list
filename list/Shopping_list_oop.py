# The get_close_matches() function returns a list of close matched strings \
# that satisfy the cutoff.
import csv
import logging
from difflib import get_close_matches as g
from typing import Tuple, Dict

from pandas import read_csv as read

logging.basicConfig(level=logging.DEBUG, filename='log.log',
                    format='%(asctime)s :%(levelname)s->%(name)s:\n%(msg)s'

                    )


class Item:
    def __init__(self) -> None:
        self.__items_in_list: Dict = {}

    @property
    def items_in_list(self):
        """Possibility to access private variable outside the class"""
        return self.__items_in_list

    @items_in_list.setter
    def items_in_list(self, keys: Tuple) -> None:
        """Ability to set private variable outside the class"""
        _key, _val = keys
        if not isinstance(_key, str):
            raise ValueError('only str')
        self.__items_in_list[_key] = _val

    @items_in_list.deleter
    def items_in_list(self) -> None:
        """Ability to delete private variable outside the class"""
        del self.__items_in_list

    def add_item(self, product: str, price: int) -> None:
        """Add product to the list."""
        if product not in self.__items_in_list:
            self.__items_in_list[product] = price
            logging.debug(product + " added.")
        else:
            logging.debug(product + " is already in the list.")

    def add_items(self, products: list, prices: list) -> None:
        """ Add more items to the shopping list """

        for product, price in zip(products, prices):
            self.add_item(product, price)


class Shoppinglist(Item):
    customer_name = 'mohammad'

    def show_items(self) -> None:
        """Shows list items"""
        logging.debug(self.items_in_list)

    def total_price(self) -> None:
        """Calculates the total of the list price"""
        total = len(self.items_in_list.keys()) * sum(
            self.items_in_list.values())

        logging.debug(total)

    def search_item(self) -> None:
        """Searches for the desired item with the ability to suggest"""
        search_me = input("Which item would you like to search ? ")
        if search_me in self.items_in_list:
            logging.debug(f' there is {search_me} in list')
            # g refers to the method get_close_matches and \
            # Return a list of the best “good enough” matches
        elif len(g(search_me, self.items_in_list)) > 0:
            action = input("Did you mean %s instead? [y or n] " % g(
                search_me, self.items_in_list))

            if action == "y":
                logging.debug('Please re-enter correctly')
                self.search_item()
            elif action == "n":
                logging.debug("The word doesn't exist, yet.")
        else:
            logging.debug(f'{search_me} is not in the list!!')

    def clear_list(self):
        """Clears the list"""
        if input("Clear your list? [y/n] ").lower().startswith("y"):
            self.__items_in_list = {}
            logging.debug("Your list has been cleared.")


food = Shoppinglist()
food.add_items(['apple', 'egg', 'carrot'], [50, 55, 65])
with open('mycsv.csv', 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['product', 'price'])
    for key in food.items_in_list.keys():
        cf.write("%s, %s\n" % (key, food.items_in_list[key]))
    cf.write("%s, %s\n" % ('----', '----'))

clothes = Shoppinglist()
clothes.add_items(['t-shirts', 'socks', 'socks'], [25, 35, 40])
with open('mycsv.csv', 'a', newline='') as cf:
    writer = csv.writer(cf)
    for key in clothes.items_in_list.keys():
        cf.write("%s, %s\n" % (key, clothes.items_in_list[key]))
df = read('mycsv.csv')
logging.debug(df)
# clothes.search_item()
# food.show_items()
# clothes.show_items()
# food.total_price()
# clothes.show_items()
# clothes.clear_list()
