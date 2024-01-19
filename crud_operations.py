import csv

# Database setup
DB1_FILE = "db1.csv"
DB2_FILE = "db2.csv"

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# Function to load dataset
def load_dataset(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        dataset = list(reader)
    return dataset

# Function to save dataset to CSV file
def save_dataset(file_path, joined_dataset):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = joined_dataset[0].keys() if joined_dataset else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        if joined_dataset:
            writer.writeheader()
        writer.writerows(joined_dataset)


# Function to query entries based on user input
def query_entries(joined_dataset):
    print("\nQuery Entries:")
    print("1. Filter by country")
    print("2. Filter by date range")
    print("3. Filter by inflation range")
    print("0. Back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        country = input("Enter the country to filter: ")
        filtered_entries = [entry for entry in joined_dataset if entry["country"].lower() == country.lower()]
        display_entries(filtered_entries)
    elif choice == "2":
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        filtered_entries = [entry for entry in joined_dataset if start_date <= entry["date"] <= end_date]
        display_entries(filtered_entries)
    elif choice == "3":
        min_inflation = float(input("Enter the minimum inflation: "))
        max_inflation = float(input("Enter the maximum inflation: "))
        filtered_entries = [entry for entry in joined_dataset if (min_inflation <= float(entry["Inflation"] ) and float(entry["Inflation"]) <= max_inflation)]
        display_entries(filtered_entries)
    elif choice == "0":
        return
    else:
        print("Invalid choice. Try again.")

# Function to display entries in a tabular format
def display_entries(entries):
    if not entries:
        print("No matching entries found.")
    else:
        fieldnames = entries[0].keys()
        print("\nDisplaying Entries:")
        print("| " + " | ".join(fieldnames) + " |")
        print("|" + "-" * (len(" | ".join(fieldnames)) + len(fieldnames) - 1) + "|")
        for entry in entries:
            print("| " + " | ".join(str(entry[field]) for field in fieldnames) + " |")

# Modify the main loop in admin_operations


# Function to join datasets based on 'Id'
def join_datasets(db1, db2):
    # Perform inner join on 'Id'
    joined_dataset = []
    for entry1 in db1:
        for entry2 in db2:
            if entry1['id'] == entry2['id']:
                joined_entry = {**entry1, **entry2}  # Merge dictionaries
                joined_dataset.append(joined_entry)
                break  # Assuming 'Id' is unique, no need to continue searching

    return joined_dataset

# Function to commit changes to datasets
def commit_changes(db1, db2, joined_dataset):
    # Update db1 and db2 with changes from joined_dataset
    for entry in joined_dataset:
        # Assuming 'Id' is unique
        for i, entry1 in enumerate(db1):
            if entry1['id'] == entry['id']:
                db1[i] = entry
                break

        for i, entry2 in enumerate(db2):
            if entry2['id'] == entry['id']:
                db2[i] = entry
                break

    # Save changes to respective CSV files
    save_dataset(DB1_FILE, db1)
    save_dataset(DB2_FILE, db2)
    
    
# CRUD functions
def read_entries(joined_dataset):
    for entry in joined_dataset:
        print(entry)

def create_entry(joined_dataset, username):
    
    if not joined_dataset:
        new_id = 1
    else:
        
        new_id = int(max(entry["id"] for entry in joined_dataset) )+ 1

    new_entry = {
        "id": new_id,  # Auto-increment id
        "Open": float(input("Enter Open: ")),
        "High": float(input("Enter High: ")),
        "Low": float(input("Enter Low: ")),
        "Close": float(input("Enter Close: ")),
        "Inflation": float(input("Enter Inflation: ")),
        "country": input("Enter Country: "),
        "ISO3": input("Enter ISO3: "),
        "date": input("Enter Date: "),
        "username": username  # Store the username with the entry
    }
    joined_dataset.append(new_entry)
    print("Entry created successfully.")
    
def update_entry(joined_dataset, username):
    country = input("Enter Country of the entry to update: ")
    date = input("Enter Date of the entry to update: ")

    for entry in joined_dataset:
        if entry["country"] == country and entry["date"] == date and entry["username"] == username:
            entry["Open"] = float(input("Enter new Open: "))
            entry["High"] = float(input("Enter new High: "))
            entry["Low"] = float(input("Enter new Low: "))
            entry["Close"] = float(input("Enter new Close: "))
            entry["Inflation"] = float(input("Enter new Inflation: "))
            entry["ISO3"] = input("Enter new ISO3: ")
            print("Entry updated successfully.")
            return
    print("Entry not found or you don't have permission to update.")
    
def delete_entry(joined_dataset, username):
        country = input("Enter Country of the entry to delete: ")
        date = input("Enter Date of the entry to delete: ")

        for entry in joined_dataset:
            if entry["country"] == country and entry["date"] == date and entry["username"] == username:
                joined_dataset.remove(entry)
                print("Entry deleted successfully.")
                return
        print("Entry not found or you don't have permission to delete.")