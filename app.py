import csv

# Function to validate user credentials
def login():
    stored_user_id = "user@example.com"  # Replace with your actual user ID
    stored_password = "password123"  # Replace with your actual password

    user_id = input("Enter User ID (email): ")
    password = input("Enter Password: ")

    if user_id == stored_user_id and password == stored_password:
        print("Login successful!\n")
        return True
    else:
        print("Incorrect email or password.\n")
        return False

# Function to get participant details
def get_participant_details():
    participants = []
    num_participants = int(input("Enter the number of participants: "))

    for i in range(num_participants):
        name = input(f"Enter the name of participant {i + 1}: ")
        email = input(f"Enter the email of participant {i + 1}: ")
        mobile = input(f"Enter the mobile number of participant {i + 1}: ")
        participants.append({
            "name": name,
            "email": email,
            "mobile": mobile,
            "expenses": 0
        })

    return participants

# Function to get expense details
def get_expenses():
    expense_amount = float(input("Enter the expense amount: "))
    description = input("Enter the expense description: ")
    return expense_amount, description

# Function to choose a split method
def choose_split_method(participants, total_expense):
    split_method = input("Choose split method (Equal, Exact, Percentage): ").strip().lower()

    if split_method == "equal":
        for participant in participants:
            participant["expenses"] += total_expense / len(participants)

    elif split_method == "exact":
        for participant in participants:
            amount = float(input(f"Enter the exact amount spent by {participant['name']}: "))
            participant["expenses"] += amount

    elif split_method == "percentage":
        total_percentage = 0
        for participant in participants:
            percentage = float(input(f"Enter the percentage for {participant['name']}: "))
            total_percentage += percentage
            participant["expenses"] += (percentage / 100) * total_expense

        if total_percentage != 100:
            print("Error: Percentages do not add up to 100.")
            return None

    else:
        print("Invalid split method.")
        return None

    return participants

# Function to create and display the balance sheet
def generate_balance_sheet(participants, total_expense, description):
    print("\nBalance Sheet:")
    total_expenses = sum(participant["expenses"] for participant in participants)

    # Display balance sheet
    for participant in participants:
        print(f"{participant['name']} owes: {participant['expenses']:.2f}")

    print(f"\nTotal expenses for all users: {total_expenses:.2f}")

    # Offer to download the balance sheet
    download_balance_sheet(participants, total_expense, total_expenses, description)

# Function to download the balance sheet as CSV
def download_balance_sheet(participants, total_expense, total_expenses, description):
    download = input("\nWould you like to download the balance sheet? (yes/no): ").strip().lower()

    if download == "yes":
        filename = "balance_sheet.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Write headers
            writer.writerow(["Participant Name", "Email", "Mobile", "Owed Amount (in $)"])

            # Write participant details and their expenses
            for participant in participants:
                writer.writerow([participant["name"], participant["email"], participant["mobile"], f"{participant['expenses']:.2f}"])

            # Write total expense details
            writer.writerow([])
            writer.writerow(["Total Expense:", f"{total_expense:.2f}"])
            writer.writerow(["Description:", description])
            writer.writerow(["Total Amount Owed by All Users:", f"{total_expenses:.2f}"])

        print(f"\nBalance sheet successfully saved as '{filename}'.")
    else:
        print("\nDownload canceled.")

# Main function
def main():
    if not login():
        return

    participants = get_participant_details()
    total_expense, description = get_expenses()
    participants = choose_split_method(participants, total_expense)

    if participants:
        generate_balance_sheet(participants, total_expense, description)

# Run the application
if __name__ == "__main__":
    main()
