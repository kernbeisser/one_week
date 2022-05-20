# imports as needed

def some_func():
    try:
        age = float(input("Age? "))
        return age * 365
    except:
        pass


def main():
    days = some_func()
    print(f"you are {days} days old")

if __name__ == '__main__':
    main()
