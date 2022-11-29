from coffee_machine import CoffeeMachine
from sugar_strips import SugarStrips
from cups_pile import Cup, PileOfCups

def select_cup_size():
    return input('\n\nSelect Cup Size: \n\n1- Small\n2- Medium\n3- Big\n\n>>> ')

def take_sugar_strip():
    return input('\n\nDo you want one sugar strip: \n\n1- yes\n2- no\n\n>>> ')

def serve_coffee():
    print("\n\n===================\nserving coffee\n===================\n\n")

def main():
    pile_of_small_cups = PileOfCups(5)
    pile_of_medium_cups = PileOfCups(5)
    pile_of_big_cups = PileOfCups(5)

    sugar_strips_container =  SugarStrips(5)

    coffee_machine = CoffeeMachine(5)
    while True:
        print("\n\nWelcome to you local coffee vending machine :)")
        print("\nto exit press ctrl + c")
        cup_selection = select_cup_size()

        if cup_selection == "1":
            if not pile_of_small_cups.has_cups(): 
                print('\n\nSorry, there is not more cups of this size')
                return 0
            
            pile_of_small_cups.get_cup()

        elif cup_selection == "2":
            if not pile_of_medium_cups.has_cups(): 
                print('\n\nSorry, there is not more cups of this size')
                return 0
            
            pile_of_medium_cups.get_cup()

        elif cup_selection == "3":
            if not pile_of_big_cups.has_cups(): 
                print('\n\nSorry, there is not more cups of this size')
                return 0
            
            pile_of_big_cups.get_cup()

        else:
            print('\n\nSorry, this is not a valid cups size')
            return 0

        sugar_strip_selection = take_sugar_strip()

        if sugar_strip_selection == "1":
            if not sugar_strips_container.has_sugar_strip():
                print("\n\nSorry, there is not sugar left")
                return 0
            
            sugar_strips_container.get_sugar_strip()
            print("\n\nsugar taken")

        elif sugar_strip_selection == "2":
            print("\n\nNot sugar taken")

        else:
            print('\n\nSorry, this is not a valid option')
            print("\n\nNot sugar taken")

        print("\n\nEverything is ready...")

        serve_coffee()

        if not coffee_machine.has_coffe_grains():
            print("\n\nSorry, there is not coffee left")
            return 0

        print("\n\nCoffee is served, Enjoy :)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Enjoy ~~~")