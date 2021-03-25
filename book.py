#!/usr/bin/env python3

class Order:
    "Order contains id, buy or sell type, quantity and price"

    def __init__ (self, id, order_type, quantity, price):
        self.id = id
        self.order = order_type
        self.quantity = quantity
        self.price = price

    def __repr__ (self):
        return f"{self.order} {self.quantity}@{self.price} id={self.id}"

class Book:
    "Book contains the list of orders"

    def __init__ (self, name):
        self.num_order = 0
        self.sell_orders = []
        self.buy_orders = []
        self.name = name

    def insert_buy (self, quantity, price):
        self.num_order += 1
        new_order = Order (self.num_order, "BUY", quantity, price)
        print("--- Insert", new_order, "on", self.name)

        # Insertion at last position
        n = len(self.buy_orders)
        if (n == 0) or (self.buy_orders[n-1].price >= new_order.price):
            self.buy_orders.append(new_order)

        # Insertion in the beginning or in the middle
        else:
            for i, elt in enumerate(self.buy_orders):
                if new_order.price > elt.price:
                    self.buy_orders.insert(i,new_order)
                    break;

        self.compare_orders()
        self.bookprint()

    def insert_sell (self, quantity, price):
        self.num_order += 1
        new_order = Order (self.num_order, "SELL", quantity, price)
        print("--- Insert", new_order, "on", self.name)

        # Insertion at last position
        n = len(self.sell_orders)
        if (n == 0) or (self.sell_orders[n-1].price <= new_order.price):
            self.sell_orders.append(new_order)

        # Insertion in the beginning or in the middle
        else:
            for i, elt in enumerate(self.sell_orders):
                if new_order.price < elt.price:
                    self.sell_orders.insert(i,new_order)
                    break;

        self.compare_orders()
        self.bookprint()

    def bookprint (self):
        print ("Book on " + self.name)
        for elt in self.sell_orders:
            print("       ", elt)
        for elt in self.buy_orders:
            print("       ", elt)
        print ("-------------------------")

    def compare_orders(self):

        # check if there are enough orders in the book
        if (len(self.sell_orders)==0) or (len(self.buy_orders)==0):
            return

        # check if orders are available to swap
        if self.sell_orders[0].price <= self.buy_orders[0].price:
            swap_price = self.buy_orders[0].price
            swap_quantity = min (self.buy_orders[0].quantity, self.sell_orders[0].quantity)

            # book of orders purge
            if self.buy_orders[0].quantity < self.sell_orders[0].quantity:
                self.buy_orders.pop(0)
                self.sell_orders[0].quantity -= swap_quantity
            else:
                self.sell_orders.pop(0)
                self.buy_orders[0].quantity -= swap_quantity
                if self.buy_orders[0].quantity == 0:
                    self.buy_orders.pop(0)

            print (f'Execute {swap_quantity} at {swap_price} on {self.name}')

            # use of recursivity in case there are other swaps to do
            self.compare_orders()
