from crud_operations import *

def admin_operations():
    # Load datasets
    db1 = load_dataset(DB1_FILE)
    db2 = load_dataset(DB2_FILE)

    # Join datasets
    joined_dataset = join_datasets(db1, db2)
    
    # Ask whether the user is admin or user
    
        # If admin, prompt for username and password
    admin_username = input("Enter your username (admin): ")
    admin_password = input("Enter your password (admin): ")

    if admin_username == ADMIN_USERNAME and admin_password == ADMIN_PASSWORD:
            print("Admin access granted. You can perform CRUD operations.")
            while True:
                print("\nSelect operation:")
                print("1. Read entries")
                print("2. Create entry")
                print("3. Update entry")
                print("4. Delete entry")
                print("5. Query entries")
                print("0. Exit")
                username="admin"
                choice = input("Enter your choice: ")

                if choice == "1":
                    read_entries(joined_dataset)
                elif choice == "2":
                    #username = input("Enter the username for the new entry: ")
                    create_entry(joined_dataset, username)
                elif choice == "3":
                    #username = input("Enter your username: ")
                    update_entry(joined_dataset, username)
                elif choice == "4":
                    #username = input("Enter your username: ")
                    delete_entry(joined_dataset, username)
                elif choice == "5":
                    query_entries(joined_dataset)
                elif choice == "0":
                    # Save changes before exiting
                    commit_changes(db1, db2, joined_dataset)
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Try again.")
    else:
            print("Invalid username or password. Access denied.")

if __name__ == "__main__":
    admin_operations()
