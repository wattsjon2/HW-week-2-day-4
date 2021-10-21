import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cart():

    def __init__(self,cart_list):
        self.cart_list = cart_list

    def addItem(self):
        new_item = input('What would you like to add? ')
        if new_item in self.cart_list.keys():
            add_again = input('This is already in the cart, would you like to change the quantity? yes/no ')
            if add_again.lower() == "yes":
                new_item_quant = input('How many would you like instead? ')
                if new_item_quant.isdigit() == False or new_item_quant == "0":
                    print("please enter a valid quantity")
                else:
                    cur_quant = self.cart_list.get(new_item)
                    self.cart_list[new_item] = new_item_quant
                    print(f"The quantity of {new_item} has been changed from {cur_quant} to {new_item_quant}")

        else:        
            new_item_quant = input('How many would you like to add? ')
            new_item.lower()
            if new_item_quant.isdigit() == False or new_item_quant == "0":
                print("please enter a valid quantity")
            else:
                self.cart_list[new_item] = new_item_quant
                if new_item_quant == "1":
                    print(f"{new_item_quant} {new_item} has been added to the cart")
                else:
                    print(f"{new_item_quant} {new_item}s has been added to the cart")


    def viewCart(self):
        if self.cart_list == {}:
            print("The cart is empty")
        else:
            print("Here is your current cart")
            print("item             item quantity")
            for key, value in self.cart_list.items():
                    print('{0:<17}{1:<4}'.format(key,value))


    def delItem(self):
        if self.cart_list == {}:
            print("The cart is empty")
        else:
            print("Here is your current cart")
            print("item             item quantity")
            for key, value in self.cart_list.items():
                    print('{0:<17}{1:<4}'.format(key,value))  
            del_item = input('What would you like to delete? ')
            del_item.lower()
            if del_item not in self.cart_list.keys():
                print("please type an item in the cart")
            else:
                del_quant = self.cart_list.get(del_item)
                if int(del_quant) > 1:
                    del_all = input(f'There are {del_quant} of {del_item} in the cart. Would you like to delete all {del_quant}? yes/no ')
                    if del_all.lower() == "yes":
                        del self.cart_list[del_item]
                        print(f"{del_item} has been removed from the cart")
                    else:
                        del_update = input(f"How many {del_item} would you like in the cart instead? ")
                        if del_update.isdigit() == False or del_update == "0":
                            print("please enter a valid quantity")
                        else:
                            self.cart_list[del_item] = del_update
                            print(f"The quantity of {del_item} has been changed from {del_quant} to {del_update}")
                else:
                    del self.cart_list[del_item]
                    print(f"{del_item} has been removed from the cart")

def run():
    my_cart = Cart({})
    while True:
        response = input("What would you like to do? add/show/delete/quit ")
        if response.lower() == 'quit':
            break
        
        elif response.lower() == "add":
            my_cart.addItem()

        elif response.lower() == "show":
            my_cart.viewCart()

        elif response.lower() == "delete":
            my_cart.delItem()
        
        else:
            print("please select a valid response")

run()
