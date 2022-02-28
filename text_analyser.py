TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

SEPARATOR = '-' * 30

# Dictionary creation and saved login data
username_password = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# Login sequence
username = input('Enter username: ')
password = input('Enter password: ')
print(SEPARATOR)
if username_password.get(username) == password:
    print(f'Welcome to app, {username}')
    print('We have 3 texts to be analyzed.')
    print(SEPARATOR)
else:
    print('Wrong username or password.')
    print(SEPARATOR)
    exit()

# If everything is OK, the user chooses which article he wants to analyze
while True:
    try:
        while True:
            choose_text = int(input('Enter a number btw. 1 and 3 to select: '))
            if choose_text > 3 or choose_text < 1:
                print('Wrong choice. Try it again')
            else:
                break
        words = list()
# Edit text, save to list and calculated word length. The whole analysis runs using for loops
        count_title = 0
        count_upper = 0
        count_lower = 0
        count_numeric = 0
        sum_str = 0
        for word in TEXTS[choose_text - 1].split():
            edit_word = word.strip(',.')
            words.append(edit_word)
            if word.istitle():
                count_title += 1
            if word.isupper() and word.isalpha():
                count_upper += 1
            if word.islower():
                count_lower += 1
            if word.isnumeric():
                count_numeric += 1
            if word.isdigit():
                sum_str = sum_str + int(word)
        print(f'There are {len(words)} words in the selected text.')
        print(f'There are {count_title} titlecase words.')
        print(f'There are {count_upper} uppercase words.')
        print(f'There are {count_lower} lowercase words.')
        print(f'There are {count_numeric} numeric strings.')
        print(f'The sum of all the numbers {sum_str}')
# Graphic display of how many words of a certain length are in the text.
        print(SEPARATOR)
        print('LEN|     OCCURRENCES     |NR.')
        print(SEPARATOR)
        words_occurrence = {}
        for word in words:
            len_w = len(word)
            if len_w not in words_occurrence:
                words_occurrence[len_w] = 0
            words_occurrence[len_w] = words_occurrence[len_w] + 1
        for key, value in sorted(words_occurrence.items()):
            occurrences = value * '*'
            print(f'{key:>3}| {occurrences:<18} | {value}')
        while True:
            next_text = input("Do you want to analyse next text? Type 'y' for yes or 'n' for no: ")
            if next_text == 'n':
                print('Thank you for using the app.')
                print('Quitting the program...')
                exit()
            elif next_text == 'y':
                break
            else:
                print('Wrong input. Try it again...')
    except ValueError:
        print(SEPARATOR)
        print('Wrong input. You can choose number only between 1 - 3 and value must be a number!')
        print(SEPARATOR)
