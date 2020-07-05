import csv
import os
import json


# Ques1 Create a variable, paragraph, that has the following content:
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."

var = """
    Python is a great language!", said Fred. "I don't ever remember
# having this much fun before.
"""
print(var)


# Ques2 Write an if statement to determine whether a variable holding a year
# is a leap year.

def leapyr(year):
    if year % 4 == 0 and year % 100 != 0:
        return (year, "is a Leap Year")
    elif year % 100 == 0:
        return (year, "is not a Leap Year")
    elif year % 400 == 0:
        return (year, "is a Leap Year")
    else:
        return (year, "is not a Leap Year")


year_inp = int(input("enter a year\t"))
print(leapyr(year_inp))


# Ques3 Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

def anagram(para):
    list3 = para.split()
    new_list = []
    print(list3)
    for word1 in list3:
        for word2 in list3:
            if word1 != word2 and (sorted(word1) == sorted(word2)):
                new_list.append(word1)
    return new_list


paragraph = "dog god cat "
print(anagram(paragraph))

# Ques4 Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


def list_sort(lst):
    new_list = ['Aakash']
    id1 = id(new_list)
    print("id of the list: " + str(id1))
    new_list.append(lst)
    id2 = id(new_list)
    print("id of the appended list:" + str(id2))
    if id1 == id2:
        print("The id has not changed")
    else:
        print("The id has changed")
    return new_list


list_inp = input("enter the items\t")
print(list_sort(list_inp))


# Ques5 Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.


def tup_sort(l):
    return sorted(l,  reverse=False)

people = []
tup5 = ('Aakash', 'Dangol', 23)
people.append(list(tup5))

while True:

    fname = input("enter first name\t")
    lname = input("enter last name \t")
    age = input("enter age\t")
    new_tup = (fname, lname, age)
    people.append(list(new_tup))
    inp1 = input("do u want to continue?\t")
    if inp1 == 'y':
        continue
    else:
        break

print(tup_sort(people))


# Ques6 Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

def john(l):
    length6 = len(l)
    print(l)
    for i in range(length6):
        if l[i] == 'John':
            print("Found")
            break
        else:
            print("not found")
    return "Finished"


list6 = []
while True:
    inp6 = input("enter items in list\t")
    if inp6 == 'end':
        break
    else:
        list6.append(inp6)

print(john(list6))


# Ques7 Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.


def avg(l):
    length7 = len(l)
    age7 = 0
    print(l)
    avg_age = 0
    for tup in l:
        if tup[2] == "None":
            break
        else:
            avg_age += int(tup[2])
            age7 += 1
    print(avg_age)
    return avg_age/age7


list_tup = []
while True:
    fname = input("enter first name\t")
    lname = input("enter last name \t")
    age = input("enter age\t")
    new_tup = (fname, lname, age)
    list_tup.append(new_tup)
    inp1 = input("do u want to continue?\t")
    if inp1 == 'y':
        continue
    else:
        break
print(avg(list_tup))


# Ques8 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(n):
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                return "False"
            else:
                return "True"
    else:
        return "False"


inp8 = int(input("enter a num\t"))
print(is_prime(inp8))


# Ques9 Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def bin(seq, num):
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if num == seq[mid]:
            return seq.index(num)
        elif num < seq[mid]:
            high = mid - 1
        else:
            low = mid +1
    return '-1'


seq_list = []
while True:
    sequence = int(input("enter inputs\t"))
    seq_list.append(sequence)
    confirm = input("do u want to continue? Y? N?\t")
    if confirm == 'N':
        break
    else:
        continue
inp9 = int(input("enter a num to search\t"))

new_list = sorted(seq_list)
print(new_list)
print(bin(new_list, inp9))


# Ques10 Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def cases(case):
    snake_case = [case[0].lower()]
    snake_case2 = [case[0].lower()]
    for c in case[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            snake_case.append('_')
            snake_case2.append('-')
            snake_case.append(c.lower())
            snake_case2.append(c.lower())
        else:
            snake_case.append(c)
            snake_case2.append(c)

    print(''.join(snake_case))
    print(''.join(snake_case2))
    return "Complete"


camel_case = input("enter camel case sentence\t")
print(cases(camel_case))


# Ques11 Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?


def extension(extent):
    filename = "Readme.txt"
    length_ext = len(filename)
    count1 = 0
    count2 = 0
    for c1 in filename:
        if c1 != '.':
            count1 += 1
        else:
            break
    result1 = slice(count1+1, length_ext)

    for c2 in extent:
        if c2 != '.':
            count2 += 1
        else:
            break
    result2 = slice(0, count2)

    return filename[result1], extent[result2]


ext = input("enter the sentence\t")
print(extension(ext))
print("Yes my code does work on filename with arbitrary length")

# Yes my code does work on filename with arbitrary length


# Ques12 Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


def is_palindrome(pal):
    if pal[::-1] == pal:
        return "Palindrome"
    else:
        return "Not Palindrome"


pal_inp = input("enter a word\t")
print(is_palindrome(pal_inp))


# Ques13 Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21


def csv_file():
    path = '/python/Insights/AssignmentII'

    fields = ('Name', 'Address', 'Age')
    filename = input("Enter file name: ")+'.csv'
    csv13 = os.path.join(path, filename)
    list13 = []
    count = int(input("Enter number of items to be written in File:\t"))
    for i in range(0, count):
        data  = input("Enter Name , Address , Age:\t")
        my_tuple = tuple(data.split())
        list13.append(my_tuple)
    print(list13)
    with open(csv13, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(fields)
        writer.writerows(list13)


csv_file()


# Ques14 Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.


def read_file():

    file14 = input("Enter filename to be read")
    filename = file14 + '.csv'

    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        list14 = list(reader)

    print(list14)


read_file()


# Ques15 Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class customer():

    def __init__(self, balance, name, address, phone, sex):
        self.balance = balance
        self.name = name
        self.address = address
        self.phone = phone
        self.sex = sex

    def information(self):
        print("Name: " + self.name)
        print("Address: " + self.address)
        print("Phone Number: " + self.phone)
        print("Sex: " + self.sex)
        return "Information"

    def checkBalance(self):
        return ("Balance: ", self.balance)

    def deposit(self, deposit_amt):
        # deposit_amt = int(input("Enter amount to be deposited: "))
        self.balance = self.balance + deposit_amt
        return ("New Balance: ", self.balance)

    def withdraw(self, withdraw_amt):
        if (self.balance >= withdraw_amt):
            self.balance = self.balance - withdraw_amt
            return ("New Balance: ", self.balance)
        else:
            return ("Low balance")


o = customer(10000, "Aakash Dangol", "KTM", '9843608958', "M")
while True:
    print("Welcome to Banking system!\n ")
    print("Actions: \n")
    print("1. View Information")
    print("2.Check Balance")
    print("3.Deposit.")
    print("4.Withdraw")
    choice = input("Enter choices\t")
    if choice == '1':
        print(o.information())
    elif choice == '2':
        print(o.checkBalance())
    elif choice == '3':
        withdraw_amt = int(input("Enter the amount to be withdrawn: "))
        print(o.withdraw(withdraw_amt))
    elif choice == '4':
        deposit_amt = int(input("Enter amount to be deposited: "))
        print(o.deposit(deposit_amt))
    else:
        print("Invalid choice.")

    exit = input("Do u want to continue? Y/N?\t")
    if exit == "Y":
        continue
    else:
        print("Thank You")
        break

# Ques16 Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class batman():
    def __init__(self, name, sex, abilities, friends, villains, gadgets, secret):
        self.name = name
        self.sex = sex
        self.abilities = abilities
        self.friends = friends
        self.villains = villains
        self.gadgets = gadgets
        self.secret = secret


    def info(self):
        print(self.name)
        print(self.sex)
        print("""
            Batman has been Gotham's protector for decades, CEO of Wayne Enterprises,
            Patriarch of the Bat Family and veteran member of the Justice League.
            Batman is a superhero co-created by artist Bob Kane and writer Bill Finger
            and published by DC Comics. The character made his first appearance in Detective Comics #27
            (May, 1939). Batman is the secret identity of Bruce Wayne. Witnessing the murder
            of his parents as a child leads him to train himself to physical and intellectual
            perfection and don a bat-themed costume in order to fight crime. Batman operates in
            Gotham City, assisted by various supporting characters including his sidekick Robin
            and his butler Alfred Pennyworth, and fights an assortment of villains influenced by
            the characters' roots in film and pulp magazines. Unlike most superheroes, he does not
            possess any superpowers; he makes use (to the best that he can) of intellect, detective
            skills, science and technology, wealth, physical prowess, and intimidation in his war on crime.
        """)
        return "Batman"

    def ab(self):
        print(self.abilities, """
        1) Genius-level intelligence
        2) Master detective
        3) Master escapologist
        4) Peak human physical condition
        5) Master martial artist
        6) Access to high tech equipment
        """)
        return "Batman"

    def fren(self):
        print(self.friends, """
                    1) Superman
                    2) Wonder Woman
                    3) Flash
                    4) Aquaman
                    5) Martian Manhunter
                    6) Green Lantern
                    7) Cyborg
                    8) Hawkman
                    9) Commissioner Gordan
                    10) Shazam
                    """)
        return "Batman"

    def vil(self):
        print(self.villains,  """
                1) Ra's Al Ghul
                2) Bane
                3) Joker
                4) Deathstroke
                5) Harley Quinn
                6) Deadshot
                7) Solomon Grundy
                8) Copper Head
                9) Two Face
                10) Penguin
                    """)
        return "Batman"

    def gad(self):
        print(self.gadgets, """
                1) The Batarang
                2) Grappling Gun
                3) Utility Belt
                4) Batmobile Remote Control
                5) Cell Phone Sonar Device
                6) Kyptonite Ring
                7) Hell Armor Batsuit
                    """)
        return "Batman"

    def sec(self):
        return self.secret


b = batman("Batman", "M", "abilities", "friends", "villains", "gadgets", "I AM BATMAN!!!")

while True:
    print("WELCOME TO THE GOTHAM CITY!!!\n")
    print("Enter your choice")
    print("1: INFORMATION")
    print("2: ABILITIES")
    print("3: FRIENDS")
    print("4: VILLAINS")
    print("5: GADGETS")
    print("6: SECRET MESSAGE FROM BATMAN")
    c = input("enter choice\t")
    if c == '1':
        print(b.info())
    elif c == '2':
        print(b.ab())
    elif c == '3':
        print(b.fren())
    elif c == '4':
        print(b.vil())
    elif c == '5':
        print(b.gad())
    elif c == '6':
        print(b.sec())
    else:
        print("Invalid Choice")

    end = input("Do you want to continue? Y/N?\t")
    if end == "Y":
        continue
    else:
        print("You either die a hero, or live long enough to see yourself become a villain.")
        break

# Ques17 Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if(y == 0):
        return print("Infinte.")
    else:
        return x/y



while True:
    print("Select operator.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choices\t")
    num1 = int(input("Enter first number\t"))
    num2 = int(input("Enter second number\t"))
    if choice == '1':
        print(add(num1, num2))

    elif choice == '2':
        print(subtract(num1, num2))

    elif choice == '3':
        print(multiply(num1, num2))

    elif choice == '4':
        print(divide(num1, num2))
        break
    else:
        print("Invalid choice")

    cont = input("do u want to continue?? Press Y for yes, press N for no\t")
    if cont == "Y":
        continue
    else:
        break


# Ques18 Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

print("Dictionaries: ")
person = {"name": "Aakash", "age": 23}
print(person)
print("Converting to JSON: \n")
person_dict = json.dumps(person, indent=2)
print(person_dict)

print("Now, converting into dictionaries from JSON\n")
json_string = json.loads(person_dict)
print(json_string)


# Ques19 Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


class validity():

    def valid(self, str):
        stack =[]
        char = {"(":")","{":"}","[":"]"}
        for paranthesis in str:
            if paranthesis in char:
                stack.append(paranthesis)
            elif len(stack) == 0 or char[stack.pop()]!=paranthesis:
                return False
        return len(stack) == 0


print("(){}[] IS VALID?: ", validity().valid("(){}[]"))
print("()[{}] IS VALID?: ", validity().valid("()[{}]"))
print("(){[] IS VALID?: ", validity().valid("(){[]"))



# Ques20 Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class sum:
    def zero_sum(self, numbers):
        numbers = sorted(numbers)
        result = []
        i = 0
        while i <= len(numbers)-2:
            j = i + 1
            k = len(numbers)-1
            while j < k:
                if numbers[i] + numbers[j] + numbers[k] < 0:
                    j += 1
                elif numbers[i] + numbers[j] + numbers[k] > 0:
                    k -= 1
                else:
                    result.append([numbers[i],numbers[j],numbers[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and numbers[j] == numbers[j-1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k+1]:
                        k -= 1
            i += 1
            while i < len(numbers)-2 and numbers[i] == numbers[i-1]:
                i += 1
        return result
print(sum().zero_sum([-25,-10,-7,-3,2,4,8,10]))

