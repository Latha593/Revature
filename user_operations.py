from crud_operations import *

def user_operations():
    # Load datasets
    db1 = load_dataset(DB1_FILE)
    db2 = load_dataset(DB2_FILE)

    # Join datasets
    joined_dataset = join_datasets(db1, db2)

    # User operations
    print("User access granted.")
    while True:
                print("Select operation:")
                print("1. Display Data")
                print("2. Query Entries")
                print("0. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    read_entries(joined_dataset)
                elif choice == "2":
                    query_entries(joined_dataset)
                elif choice == "0":
                    # Save changes before exiting
                    commit_changes(db1, db2, joined_dataset)
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    user_operations()
