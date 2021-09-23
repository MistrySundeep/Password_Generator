import random
# The use of the 'chr()' function in this script lets us take the random int and convert it to its Ascii equivalent


def generate_cap(size: int):
    # Creates a list of capital letters
    # Ascii value of random number generated determines the letter stored in list
    # A list holding these capital letters is returned
    tmp_cap = []

    while tmp_cap.__len__() < size:
        upper_case = chr(random.randint(65, 90))
        tmp_cap.append(upper_case)
    return tmp_cap


def generate_low(size: int):
    # Creates a list of lowercase letters
    # Ascii value of random number generated determines the letter stored in list
    # A list holding these lowercase letters is returned
    tmp_low = []

    while tmp_low.__len__() < size:
        upper_case = chr(random.randint(97, 122))
        tmp_low.append(upper_case)
    return tmp_low


def generate_num(size: int):
    # Creates a list of numbers
    # Ascii value of random number generated determines the number stored in list
    # A list holding these numbers is returned
    tmp_num = []

    while tmp_num.__len__() < size:
        upper_case = chr(random.randint(48, 57))
        tmp_num.append(upper_case)
    return tmp_num


def generate_symbol(size: int):
    # Creates a list of numbers
    # Ascii value of random number generated determines the symbol stored in list
    # A list holding these symbols is returned
    tmp_symbol = []

    while tmp_symbol.__len__() < size:
        choice = random.randint(0, 3)
        if choice == 0:
            random_symbol = chr(random.randint(32, 47))
            tmp_symbol.append(random_symbol)
        elif choice == 1:
            random_symbol = chr(random.randint(58, 64))
            tmp_symbol.append(random_symbol)
        elif choice == 2:
            random_symbol = chr(random.randint(91, 96))
            tmp_symbol.append(random_symbol)
        else:
            random_symbol = chr(random.randint(123, 126))
            tmp_symbol.append(random_symbol)

    return tmp_symbol


def initial_pw(cap: list, low: list, num: list, sym: list) -> str:
    # Based on the previously generated lists, we iterate through each and create a single string holding all values
    # from the lists and returns it
    tmp_pw = ''
    for c in cap:
        tmp_pw += c
    for l in low:
        tmp_pw += l
    for n in num:
        tmp_pw += n
    for s in sym:
        tmp_pw += s
    return tmp_pw


def shuffle(pw: str):
    # Takes the returned string from the 'initial_pw()' function and casts the string to a list
    # From this we then use random.shuffle() to shuffle the order of the items of the password
    # We then return a string containing the shuffled password
    tmp_list = list(pw)
    random.shuffle(tmp_list)
    return ''.join(tmp_list)


def run():
    # First asks for the user to enter 4 numbers between 1 and 4, validating each input
    # If the input is valid it is then appended to a list
    user_values = []
    counter = 0
    while counter < 5:
        try:
            user_num = int(input("Please enter a value between 1 and 4: "))
        except ValueError:
            print("Sorry, try another value")
            continue
        else:
            if user_num > 4:
                print("Your value is too big, try again")
            else:
                user_values.append(user_num)
                counter += 1

    # It then use the values from the previously created list to represent how many caps, lowercase, number and symbols
    # the user wants in their password
    capital = generate_cap(user_values[0])
    lower = generate_low(user_values[1])
    number = generate_num(user_values[2])
    gen_symbol = generate_symbol(user_values[3])

    # We then create an initial password (String) from the previously generated lists
    unshuffled_pw = initial_pw(capital, lower, number, gen_symbol)

    # Shuffle the inital password to create the final password
    final_pw = shuffle(unshuffled_pw)

    # Print the final results to the console
    print(final_pw)


run()
