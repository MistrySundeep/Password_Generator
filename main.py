import random


def shuffle(pw: str):
    tmp_list = list(pw)
    random.shuffle(tmp_list)
    return ''.join(tmp_list)


def initial_pw(cap: list, low: list, num: list, sym: list) -> str:
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


def generate_cap(size: int):
    # Temp list for generated values
    tmp_cap = []

    while tmp_cap.__len__() < size:
        upper_case = chr(random.randint(65, 90))
        tmp_cap.append(upper_case)
    return tmp_cap


def generate_low(size: int):
    tmp_low = []

    while tmp_low.__len__() < size:
        upper_case = chr(random.randint(97, 122))
        tmp_low.append(upper_case)
    return tmp_low


def generate_num(size: int):
    tmp_num = []

    while tmp_num.__len__() < size:
        upper_case = chr(random.randint(48, 57))
        tmp_num.append(upper_case)
    return tmp_num


def generate_symbol(size: int):
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


user_values = []

for i in range(4):
    user_num = int(input("Enter 4 numbers between 1 and 5: "))
    if user_num > 5:
        print("Please enter a number less than 5")
    else:
        user_values.insert(i, user_num)


capital = generate_cap(user_values[0])
lower = generate_low(user_values[1])
number = generate_num(user_values[2])
gen_symbol = generate_symbol(user_values[3])

unshuffled_pw = initial_pw(capital, lower, number, gen_symbol)
final_pw = shuffle(unshuffled_pw)
print(final_pw)

