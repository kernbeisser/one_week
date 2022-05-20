

def the_big_cleanup(pr : str) -> str:
    # Remove the leading and trailing whitespace (new lines) from pr
    pr = pr.strip()


    # Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet waste" tests better than "dog poop"
    pr = pr.replace("dog poop", "pet waste")


    # We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)
    pr = pr.replace("Doody Calls", "DoodyCalls")


    # Our research shows that it's best to shout our press releases. Make the entire press release uppercased!
    pr = pr.upper()

    # Print out the updated press release with all of the above changes:
    return pr

def main():
    pr = """

Doody Calls, a nationwide leader in dog poop removal services, is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. Doody Calls currently cleans up dog poop in over 57 territories across 23 states and has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

    pr = the_big_cleanup(pr)
    print(pr)

if __name__ == '__main__':
    main()