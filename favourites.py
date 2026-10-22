FILE_NAME = "faves.txt"
FAVOURITE_TYPES = ["MOVIE", "SONG", "BOOK", "GAME"]


def load_favourites():
    favourites = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            details = line.strip().split("|")
            if len(details) == 5:
                try:
                    item_type = details[0]
                    title = details[1]
                    creator = details[2]
                    year = int(details[3])
                    rating = int(details[4])
                    if item_type in FAVOURITE_TYPES and title != "" and creator != "":
                        if 1 <= year <= 9999 and 1 <= rating <= 10:
                            favourites.append([item_type, title, creator, year, rating])
                except ValueError:
                    pass
        file.close()
    except FileNotFoundError:
        pass
    return favourites


def save_favourites(favourites):
    file = open(FILE_NAME, "w")
    for favourite in favourites:
        item_type = favourite[0]
        title = favourite[1]
        creator = favourite[2]
        year = favourite[3]
        rating = favourite[4]
        line = item_type + "|" + title + "|" + creator + "|" + str(year) + "|" + str(rating)
        file.write(line + "\n")
    file.close()


def get_number(message, minimum, maximum):
    while True:
        try:
            number = int(input(message))
            if minimum <= number <= maximum:
                return number
            print("Enter a number from", minimum, "to", maximum)
        except ValueError:
            print("Please enter a whole number.")


def get_text(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("This cannot be empty.")
        elif "|" in text:
            print("Do not use the | character.")
        else:
            return text


def choose_type():
    print("1. Movie  2. Song  3. Book  4. Game")
    choice = get_number("Choose type: ", 1, 4)
    return FAVOURITE_TYPES[choice - 1]


def add_favourite(favourites):
    print("\n--- ADD FAVOURITE ---")
    item_type = choose_type()
    title = get_text("Title: ")
    for favourite in favourites:
        if favourite[0] == item_type and favourite[1].lower() == title.lower():
            print("This favourite already exists.")
            return
    creator = get_text("Creator: ")
    year = get_number("Year: ", 1, 9999)
    rating = get_number("Rating (1-10): ", 1, 10)
    new_favourite = [item_type, title, creator, year, rating]
    favourites.append(new_favourite)
    save_favourites(favourites)
    print("Favourite added.")


def show_favourites(favourites):
    if len(favourites) == 0:
        print("No favourites found.")
        return
    print("\nNo. Type | Title | Creator | Year | Rating")
    for number in range(len(favourites)):
        favourite = favourites[number]
        print(number + 1, favourite[0], "|", favourite[1], "|",
              favourite[2], "|", favourite[3], "|", favourite[4])


def search_favourites(favourites):
    search_text = get_text("Enter title or part of title: ").lower()
    found_favourites = []
    for favourite in favourites:
        if search_text in favourite[1].lower():
            found_favourites.append(favourite)
    show_favourites(found_favourites)


def filter_favourites(favourites):
    chosen_type = choose_type()
    found_favourites = []
    for favourite in favourites:
        if favourite[0] == chosen_type:
            found_favourites.append(favourite)
    show_favourites(found_favourites)




def show_statistics(favourites):
    print("\nType | Number of items | Average rating")
    for item_type in FAVOURITE_TYPES:
        item_count = 0
        total_rating = 0
        for favourite in favourites:
            if favourite[0] == item_type:
                item_count = item_count + 1
                total_rating = total_rating + favourite[4]
        if item_count == 0:
            average_rating = 0
        else:
            average_rating = round(total_rating / item_count, 1)
        print(item_type, "|", item_count, "|", average_rating)


def edit_rating(favourites):
    show_favourites(favourites)
    if len(favourites) == 0:
        return
    title_to_edit = get_text("Enter exact title: ").lower()
    chosen_type = choose_type()
    for favourite in favourites:
        if favourite[0] == chosen_type and favourite[1].lower() == title_to_edit:
            new_rating = get_number("New rating (1-10): ", 1, 10)
            favourite[4] = new_rating
            save_favourites(favourites)
            print("Rating updated.")
            return
    print("Favourite not found.")


def delete_favourite(favourites):
    show_favourites(favourites)
    if len(favourites) == 0:
        return
    title_to_delete = get_text("Enter exact title: ").lower()
    chosen_type = choose_type()
    for favourite in favourites:
        if favourite[0] == chosen_type and favourite[1].lower() == title_to_delete:
            favourites.remove(favourite)
            save_favourites(favourites)
            print("Favourite deleted.")
            return
    print("Favourite not found.")


def main():
    favourites = load_favourites()
    print("Welcome to Favourites List!")
    print("Loaded", len(favourites), "favourites.")
    while True:
        print("\n--- FAVOURITES MENU ---")
        print("1. Add favourite")
        print("2. View all favourites")
        print("3. Search title")
        print("4. Filter by type")
        print("5. Statistics")
        print("6. Edit rating")
        print("7. Delete favourite")
        print("0. Save and exit")
        choice = get_number("Choose: ", 0, 8)
        if choice == 1:
            add_favourite(favourites)
        elif choice == 2:
            show_favourites(favourites)
        elif choice == 3:
            search_favourites(favourites)
        elif choice == 4:
            filter_favourites(favourites)
        elif choice == 5:
            show_statistics(favourites)
        elif choice == 6:
            edit_rating(favourites)
        elif choice == 7:
            delete_favourite(favourites)
        else:
            save_favourites(favourites)
            print("Data saved. Goodbye!")
            break


if __name__ == "__main__":
    main()
