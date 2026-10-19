"""
Media Collection Manager
CIS106 Final Project

About this application:
    This program keeps a list of movies, TV shows, and books. The user can
    add an item, delete an item, or view all items from a simple menu.
    Every time the list changes, it is saved to a file called
    "collection.txt" so the results can be opened and read later.

Functions:
    main()        - where the application starts; runs the menu loop
    menu()        - shows the menu options and returns the user's choice
    add_item()    - asks for an item's details and adds it to the list
    delete_item() - removes an item from the list by its number
    view_items()  - shows every item in the list
    save_items()  - writes the list to collection.txt
"""

FILE_NAME = "collection.txt"


def menu():
    """Show the menu options and return the choice the user types in."""
    print("\n===== Media Collection Manager =====")
    print("1. Add an item")
    print("2. Delete an item")
    print("3. View items")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    return choice


def add_item(collection):
    """Ask the user for the type, title, and year, then add the item to the list."""
    media_type = input("Type (Movie, Show, or Book): ")
    title = input("Title: ")
    year = input("Year: ")

    item = {"type": media_type, "title": title, "year": year}
    collection.append(item)
    save_items(collection)
    print(title + " was added.")


def view_items(collection):
    """Show every item in the list with a number next to it."""
    if len(collection) == 0:
        print("Your collection is empty.")
        return

    print("\n#   Type      Title                         Year")
    print("------------------------------------------------")
    for i in range(len(collection)):
        item = collection[i]
        print(f"{i + 1:<4}{item['type']:<10}{item['title']:<30}{item['year']}")


def delete_item(collection):
    """Show the list, ask which item number to delete, and remove it."""
    if len(collection) == 0:
        print("Your collection is empty. Nothing to delete.")
        return

    view_items(collection)
    number = input("Enter the number of the item to delete: ")

    if number.isdigit() and 1 <= int(number) <= len(collection):
        removed = collection.pop(int(number) - 1)
        save_items(collection)
        print(removed["title"] + " was deleted.")
    else:
        print("That is not a valid item number.")


def save_items(collection):
    """Write every item in the list to the output file, one item per line."""
    file = open(FILE_NAME, "w")
    file.write("My Media Collection\n")
    file.write("-------------------\n")
    for item in collection:
        file.write(item["type"] + " | " + item["title"] + " | " + item["year"] + "\n")
    file.close()


def main():
    """Start the application and keep showing the menu until the user quits."""
    collection = []
    running = True

    while running:
        choice = menu()

        if choice == "1":
            add_item(collection)
        elif choice == "2":
            delete_item(collection)
        elif choice == "3":
            view_items(collection)
        elif choice == "4":
            save_items(collection)
            print("Your collection was saved to " + FILE_NAME + ". Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


main()
