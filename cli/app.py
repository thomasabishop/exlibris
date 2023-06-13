import json 

def seek_user_confirmation(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input, please enter 'yes' or 'no'.")


prompts = [
    "Enter title",
    "Enter author",
    "Enter publication date",
    "Enter year you read the book"
]

keys = ["Title", "Author", "Publication_date", "Date_read"]

book = {}

for key, prompt in zip(keys,prompts): 
    book[key] = input(prompt + ": ")

book_json = json.dumps(book, indent=4)

if seek_user_confirmation("Are you happy with the entry? (yes/no): \n"  + book_json + "\n"):
    print("user accepts")
else: 
    print("user denies ")


