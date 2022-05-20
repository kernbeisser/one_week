
def string_basics():
    first = "Nico"
    last = "Hulkenberg"

    # - Create a variable called "full_name" that combines first and last with a space between them.  
    # - Print it out
    full_name = f"{first} {last}"
    print(full_name)

    # - Create an "initials" variable that holds the first character of first followed by the first character of last. 
    # - Print it out
    initials = f"{first[0]}{last[0]}"
    print(initials)

    # - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
    # - Print it out
    initials_2 = f"{first[0]}.{last[0]}."
    print(initials_2)


    # Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
    # Print it out 
    nickname = last[:4]
    print(nickname)

def main():
    string_basics()

if __name__ == '__main__':
    main()
