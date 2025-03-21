import json
import os

# File to store library data
data_file = 'library.txt'

# Load library from file
def load_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

# Save library to file
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input('Enter the book title: ')
    author = input('Enter the author: ')
    year = input('Enter the publication year: ')
    genre = input('Enter the genre: ')
    read = input('Have you read this book? (yes/no): ').strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully!\n")

# Remove a book from the library
def remove_book(library):
    title = input('Enter the title of the book to remove: ').strip()
    updated_library = [book for book in library if book['title'].lower() != title.lower()]
    
    if len(updated_library) < len(library):
        save_library(updated_library)
        print(f"Book '{title}' removed successfully!\n")
    else:
        print(f"Book '{title}' not found in the library.\n")
    
    return updated_library

# Search for books by title or author
def search_library(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        search_by = 'title'
    elif choice == '2':
        search_by = 'author'
    else:
        print("Invalid choice!\n")
        return
    
    search_term = input(f'Enter the {search_by}: ').strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]
    
    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}'.\n")

# Display all books in the library
def display_all_books(library):
    if library:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("The library is empty.\n")

# Display statistics of the library
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Main function to display menu and handle user choices
def main():
    library = load_library()
    
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
