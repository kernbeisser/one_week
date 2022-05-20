# imports as needed
"""
WELCOME TO OUR USELESS STORE!
*****************************
what item are you purchasing?  taco
what is the price of taco?  2.5
how many taco are you buying?  5

Added 5 taco(s) to shopping cart
Subtotal: $12.5
"""

def some_func():
    welcome = """WELCOME TO OUR USELESS STORE!\n*****************************"""

    print(f"{welcome}")
    item = input("what item are you purchasing? ")
    price = float(input("what is the price of taco?  "))
    how_may = int(input("how many taco are you buying?  "))
    total = price * how_may
    print(f"Added {how_may} {item}(s) to shopping cart")
    print(f"Subtotal: ${total}")


def main():
    some_func()

if __name__ == '__main__':
    main()
