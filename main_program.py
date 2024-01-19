from admin_operations import admin_operations
from user_operations import user_operations

def main():
    user_type = input("Are you an admin or a user? Enter 'admin' or 'user': ").lower()

    if user_type == "admin":
        admin_operations()
    elif user_type == "user":
        user_operations()
    else:
        print("Invalid user type. Please enter 'admin' or 'user'.")

if __name__ == "__main__":
    main()
