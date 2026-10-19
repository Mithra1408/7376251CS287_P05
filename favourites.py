def add_favourite(items):
    print("\n--- ADD FAVOURITE ---")
    kind = choose_type()
    title = get_text("Title: ")

    for item in items:
        if item[0] == kind and item[1].lower() == title.lower():
            print("This favourite already exists.")
            return

    creator = get_text("Creator: ")
    year = get_number("Year: ", 1, 9999)
    rating = get_number("Rating (1-10): ", 1, 10)
    items.append([kind, title, creator, year, rating])
    save_data(items)
    print("Favourite added.")


def show_items(items):
    if len(items) == 0:
        print("No favourites found.")
        return

    print("\nNo. Type | Title | Creator | Year | Rating")
    for i in range(len(items)):
        item = items[i]
        print(i + 1, item[0], "|", item[1], "|", item[2],
              "|", item[3], "|", item[4])
def show_menu():
    print("\n--- FAVOURITES LIST ---")
    print("1. Add favourite")
    print("2. View all favourites")
    print("3. Search by title")
    print("4. Filter by type")
    print("5. Top 5 favourites")
    print("6. Show statistics")
    print("7. Edit rating")
    print("8. Delete favourite")
    print("9. Exit")