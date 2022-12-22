import requests  # TO GET URL
from bs4 import BeautifulSoup  # TO PARSE AND ARRANGE DATA(S)

# Variables
choice = 0
limit = 0
book1 = {}
book2 = {}
distinct_words1 = {}
distinct_words2 = {}
commonWords = {}

Stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
              "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
              "she", "her", "hers", "herself", "it", "its", "itself", "they", "them",
              "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
              "that", "these", "those", "am", "is", "are", "was", "were", "be", "been",
              "being", "have", "has", "had", "having", "do", "does", "did", "doing",
              "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
              "while", "of", "at", "by", "for", "with", "about", "against", "between",
              "into", "through", "during", "before", "after", "above", "below", "to",
              "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how",
              "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
              "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s",
              "t", "can", "will", "just", "don", "should", "now", "has", "int"]  # I CREATE IT WITH SEARCH FOR STOPWORDS


# Functions
def main_menu():  # MENU

    print(" ")
    print(" >> 1- Download Books")
    print(" >> 2- Count one book's words")
    print(" >> 3- Compare two books words")
    print(" >> 4- Exit")

    is_choice = False
    global choice
    global limit
    global distinct_words1
    global distinct_words2

    while not is_choice:
        choice = int(input(" >> ENTER A CHOICE: "))
        if choice < 1 or choice > 4:
            is_choice = False
            print(" >> TRY AGAIN")
        else:
            is_choice = True

    if choice == 1:  # DOWNLOAD A BOOK
        book_name = " "
        while book_name != "Exit":
            book_name = input("Please enter your book name or enter 'Exit': ")
            if book_name != "Exit":
                download_book(book_name)
        main_menu()

    elif choice == 2:  # READ A BOOK
        limit_choice = (input("Enter the print limit: "))
        if limit_choice == "":
            limit = 20
        else:
            limit = int(limit_choice)

        book_name1 = input("Please enter your book's name (file): ")
        uncleaned_words = (read_file(book_name1 + ".txt"))
        book_words = count_words(clean_words(uncleaned_words))
        one_book_info(book_words, book_name1)

    elif choice == 3:  # COMPARE TWO BOOKS

        limit_choice = (input("Enter the print limit: "))
        if limit_choice == "":
            limit = 20
        else:
            limit = int(limit_choice)

        book_name1 = (input("Enter your 1. book's name: "))
        uncleaned_words1 = read_file(book_name1 + ".txt")
        book_name2 = (input("Enter your 2. book's name: "))
        uncleaned_words2 = read_file(book_name2 + ".txt")
        compare_(clean_words(uncleaned_words1), clean_words(uncleaned_words2))
        comparison_books_info(distinct_words1, distinct_words2, book_name1, book_name2)

    elif choice == 4:  # EXIT
        print(" ")
        print("Good Day")


def clean_words(words_):  # CLEANING WORDS FROM SYMBOLS AND STOPWORDS
    cleaned_words = []

    words_ = words_.replace(".", " ").replace("%", " ").replace("=", " ").replace(",", " ").replace(";", " ").replace \
        ("_", " ").replace(")", " ").replace("(", " ").replace("!", " ").replace("?", " ").replace("<", " ").replace(
        ">", " ").replace("/", " ").replace(
        "#", " ").replace("'", " ").replace('"', " ").replace("*", " ").replace(":", " ").replace("&", " ").replace("-",
                                                                                                                    " ")

    for word in (words_.split()):
        if " " in word:
            word = words_.replace(" ", '')
        if word not in Stop_words and (len(word) > 1):
            cleaned_words.append(word)
    cleaned_words.sort()

    return cleaned_words


def read_file(name):  # READING FILE
    FILE = open(name, "r", encoding="utf-8")
    script = FILE.read()
    script = script.lower()
    FILE.close()
    return script


def count_words(words):  # COUNTING WORDS
    temp_count = 0
    temp_word = " "
    our_words = {}
    word_count = {}

    for word in words:  # COUNTING WORDS
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

    for a in range(limit):  # SORTING WORDS UP TO THE ENTERED LIMIT
        for key in word_count.keys():
            if word_count[key] > temp_count and key not in our_words:
                temp_count = word_count[key]
                temp_word = key
        our_words[temp_word] = temp_count
        temp_count = 0
        temp_word = " "

    return our_words


def compare_(book_words1, book_words2):  # COMPARING TWO BOOKS
    global book1
    global book2
    global distinct_words1
    global distinct_words2
    global commonWords

    book1_words = []
    book2_words = []
    commonwords = []
    temp_count = 0
    temp_word = " "

    for word1 in book_words1:  # BOOK1 WORDS
        if word1 not in book1:
            book1[word1] = 1
        else:
            book1[word1] += 1

    for word2 in book_words2:  # BOOK2 WORDS
        if word2 not in book2:
            book2[word2] = 1
        else:
            book2[word2] += 1

    for WORD in book1:  # ADDING BOOK1 WORDS TO "BOOK1_WORDS"
        if WORD not in book2 and WORD not in book1_words:
            book1_words.append(WORD)
    book1_words.sort()

    for WORD in book2:  # ADDING BOOK2 WORDS TO "BOOK2_WORDS"
        if WORD not in book1 and WORD not in book2_words:
            book2_words.append(WORD)
    book2_words.sort()

    for WORD in book1:  # ADDING COMMON WORDS TO "COMMONWORDS"
        if WORD in book2 and WORD not in commonwords:
            commonwords.append(WORD)
    commonwords.sort()

    for a in range(limit):

        for WORDS in book1_words:  # DISTINCT WORDS OF BOOK1
            if (book1[WORDS]) > temp_count and WORDS not in distinct_words1:
                temp_count = (book1[WORDS])
                temp_word = WORDS
        distinct_words1[temp_word] = temp_count
        temp_count = 0
        temp_word = " "

        for WORDS in book2_words:  # DISTINCT WORDS OF BOOK2
            if (book2[WORDS]) > temp_count and WORDS not in distinct_words2:
                temp_count = (book2[WORDS])
                temp_word = WORDS
        distinct_words2[temp_word] = temp_count
        temp_count = 0
        temp_word = " "

        for WORDS in commonwords:  # COMMON WORDS
            if (book1[WORDS] + book2[WORDS]) > temp_count and WORDS not in commonWords:
                temp_count = (book1[WORDS] + book2[WORDS])
                temp_word = WORDS
        commonWords[temp_word] = temp_count
        temp_count = 0
        temp_word = " "


def one_book_info(words_, book_name1):  # SHOWING ONE BOOK INFO

    no = 1
    print(" ")
    print(" ")
    print(">>> Book1: ", book_name1)
    print(" ")
    print("NO \t WORD\t\t   FREQUENCY")
    print(" ")

    for key in words_.keys():  # MAKING INFORMATION APPEAR PROPERLY
        first_space = "\t"

        space = 12 - len(key)
        space2 = space * " "
        print(no, first_space, key, space2, words_[key])
        no = no + 1


def comparison_books_info(words1, words2, book_name1, book_name2):  # SHOW COMPARISON OF TWO BOOKS INFO

    no = 1
    print("\n>>> Book1: ", book_name1)
    print(">>> Book2: ", book_name2)
    print("\nCOMMON WORDS\n")
    print("NO\t\t WORD\t\t\t  FREQUENCY.1\t\t FREQUENCY.2\t\t TOTAL\n")

    for key in commonWords.keys():  # MAKING INFORMATION APPEAR PROPERLY

        space = 15 - len(key)
        space2 = space * " "
        print(no, "\t\t", key, space2, book1[key], "\t\t\t\t", book2[key], "\t\t\t\t", commonWords[key])
        no = no + 1

    # SHOWING BOOK1 DISTINCT WORDS
    no = 1
    print("\n>>> Book1: ", book_name1)
    print("\nDISTINCT WORDS\n")
    print("NO\t\t WORD\t\t\t\t   FREQUENCY\n")

    for key in words1.keys():  # MAKING INFORMATION APPEAR PROPERLY
        space = 20 - len(key)
        space2 = space * " "

        print(no, "\t\t", key, space2, distinct_words1[key])
        no = no + 1

    # SHOWING BOOK2 DISTINCT WORDS
    no = 1
    print("\n>>> Book2: ", book_name2)
    print("\nDISTINCT WORDS\n")
    print("NO\t\t WORD\t\t\t\t   FREQUENCY\n")

    for key in words2.keys():  # MAKING INFORMATION APPEAR PROPERLY
        space = 20 - len(key)
        space2 = space * " "

        print(no, "\t\t", key, space2, distinct_words2[key])
        no = no + 1


def download_book(book_name):  # DOWNLOADING A BOOK

    book = " "
    splitted_book_name = book_name.replace(" ", "_")

    wikiurl = requests.get('https://en.wikibooks.org/wiki/' + splitted_book_name + "/Print_version")
    wikiurl_2 = BeautifulSoup(wikiurl.content, "html.parser")

    all_site = wikiurl_2.find_all("div", {"class": "mw-parser-output"})

    for htmlseperator in all_site:  # TAKING ONLY TEXTS
        book += (" " + htmlseperator.text)

    if book == " ":  # IF WE CANNOT DOWNLOAD WITH "Print_version"
        wikiurl = requests.get('https://en.wikibooks.org/wiki/' + splitted_book_name + "/print_version")
        wikiurl_2 = BeautifulSoup(wikiurl.content, "html.parser")

        all_site = wikiurl_2.find_all("div", {"class": "mw-parser-output"})

        for htmlseperator in all_site:  # TAKING ONLY TEXTS
            book += (" " + htmlseperator.text)
        if book == " ":  # IF WE CANNOT DOWNLOAD WITH "print_version"

            wikiurl = requests.get('https://en.wikibooks.org/wiki/' + splitted_book_name + "Printable_version")
            wikiurl_2 = BeautifulSoup(wikiurl.content, "html.parser")

            all_site = wikiurl_2.find_all("div", {"class": "mw-parser-output"})

            for htmlseperator in all_site:  # TAKING ONLY TEXTS
                book += (" " + htmlseperator.text)
            if book == " ":
                print(" ")
                print("***You had entered a wrong book name!***")
                print(" ")
            else:
                file = open(book_name + ".txt", "w", encoding="utf-8")
                file.write(book)
                file.close()

        else:  # IF WE CAN DOWNLOAD WITH "print_version"
            file = open(book_name + ".txt", "w", encoding="utf-8")
            file.write(book)
            file.close()

    else:  # IF WE CAN DOWNLOAD WITH "Print_version"
        file = open(book_name + ".txt", "w", encoding="utf-8")
        file.write(book)
        file.close()


main_menu()