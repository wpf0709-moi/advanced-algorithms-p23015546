import time


# ==============================
# Transaction Entity Class
# ==============================
class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return (
            f"ID: {self.transaction_id} | "
            f"Customer: {self.customer_name} | "
            f"Product: {self.product_name} | "
            f"Amount: RM{self.amount:.2f} | "
            f"Date: {self.transaction_date}"
        )


# ==============================
# Sample Unsorted Transaction Data
# ==============================
def create_sample_transactions():
    return [
        Transaction(108, "Ali", "Wireless Mouse", 45.90, "2026-05-02"),
        Transaction(103, "Mei Ling", "Keyboard", 89.50, "2026-05-03"),
        Transaction(115, "Raj", "Monitor", 599.00, "2026-05-05"),
        Transaction(101, "Siti", "USB Cable", 18.90, "2026-05-01"),
        Transaction(112, "Jason", "Laptop Stand", 75.00, "2026-05-04"),
        Transaction(106, "Aina", "Webcam", 120.00, "2026-05-06"),
        Transaction(110, "Daniel", "Headphones", 150.00, "2026-05-07"),
        Transaction(104, "Nurul", "Power Bank", 99.90, "2026-05-08"),
        Transaction(114, "Kevin", "External Hard Drive", 320.00, "2026-05-09"),
        Transaction(102, "Farah", "Phone Charger", 35.00, "2026-05-10"),
        Transaction(109, "Hafiz", "Smartwatch", 250.00, "2026-05-11"),
        Transaction(107, "Chloe", "Bluetooth Speaker", 180.00, "2026-05-12"),
    ]


# ==============================
# Display Transactions
# ==============================
def display_transactions(transactions):
    if len(transactions) == 0:
        print("\nNo transactions available.")
        return

    print("\n==================== Transaction List ====================")
    for transaction in transactions:
        print(transaction)
    print("==========================================================")


# ==============================
# Merge Sort: Divide and Conquer
# ==============================
def merge_sort(transactions):
    # Base case: a list with 0 or 1 item is already sorted
    if len(transactions) <= 1:
        return transactions

    # Divide step: split the list into two halves
    middle = len(transactions) // 2
    left_half = transactions[:middle]
    right_half = transactions[middle:]

    # Conquer step: recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine step: merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    # Compare transaction IDs and add the smaller one first
    while i < len(left) and j < len(right):
        if left[i].transaction_id <= right[j].transaction_id:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining transactions from the left side
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Add remaining transactions from the right side
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# ==============================
# Binary Search
# ==============================
def binary_search(transactions, target_id):
    low = 0
    high = len(transactions) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_transaction = transactions[middle]

        if middle_transaction.transaction_id == target_id:
            return middle_transaction

        elif target_id < middle_transaction.transaction_id:
            high = middle - 1

        else:
            low = middle + 1

    return None


# ==============================
# Linear Search
# ==============================
def linear_search(transactions, target_id):
    for transaction in transactions:
        if transaction.transaction_id == target_id:
            return transaction
    return None


# ==============================
# Performance Comparison
# ==============================
def compare_search_performance(transactions):
    sorted_transactions = merge_sort(transactions)

    search_keys = [101, 106, 115, 999, 888, 103, 777]

    print("\n================ Search Performance Comparison ================")
    print(f"{'Search ID':<12}{'Binary Search Time (ns)':<28}{'Linear Search Time (ns)':<25}")
    print("-" * 70)

    total_binary_time = 0
    total_linear_time = 0

    for key in search_keys:
        start_binary = time.perf_counter_ns()
        binary_search(sorted_transactions, key)
        end_binary = time.perf_counter_ns()
        binary_time = end_binary - start_binary

        start_linear = time.perf_counter_ns()
        linear_search(sorted_transactions, key)
        end_linear = time.perf_counter_ns()
        linear_time = end_linear - start_linear

        total_binary_time += binary_time
        total_linear_time += linear_time

        print(f"{key:<12}{binary_time:<28}{linear_time:<25}")

    average_binary = total_binary_time / len(search_keys)
    average_linear = total_linear_time / len(search_keys)

    print("-" * 70)
    print(f"{'Average':<12}{average_binary:<28.2f}{average_linear:<25.2f}")

    if average_binary < average_linear:
        print("\nConclusion: Binary Search was faster on average.")
    else:
        print("\nConclusion: Linear Search was faster in this small test.")

    print("================================================================")


# ==============================
# Merge Sort Performance
# ==============================
def test_merge_sort_performance(transactions):
    print("\n================ Merge Sort Performance ================")
    print("Before sorting:")
    display_transactions(transactions)

    start_time = time.perf_counter_ns()
    sorted_transactions = merge_sort(transactions)
    end_time = time.perf_counter_ns()

    elapsed_time = end_time - start_time

    print("\nAfter sorting by Transaction ID:")
    display_transactions(sorted_transactions)

    print(f"\nMerge Sort execution time: {elapsed_time} ns")
    print("========================================================")

    return sorted_transactions


# ==============================
# Search Using Binary Search
# ==============================
def search_using_binary(transactions):
    try:
        sorted_transactions = merge_sort(transactions)

        target_id = int(input("Enter Transaction ID to search using Binary Search: "))

        start_time = time.perf_counter_ns()
        result = binary_search(sorted_transactions, target_id)
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time

        if result is not None:
            print("\nTransaction found using Binary Search:")
            print(result)
        else:
            print("\nTransaction not found using Binary Search.")

        print(f"Binary Search execution time: {elapsed_time} ns")

    except ValueError:
        print("Invalid input. Please enter a valid transaction ID.")


# ==============================
# Search Using Linear Search
# ==============================
def search_using_linear(transactions):
    try:
        target_id = int(input("Enter Transaction ID to search using Linear Search: "))

        start_time = time.perf_counter_ns()
        result = linear_search(transactions, target_id)
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time

        if result is not None:
            print("\nTransaction found using Linear Search:")
            print(result)
        else:
            print("\nTransaction not found using Linear Search.")

        print(f"Linear Search execution time: {elapsed_time} ns")

    except ValueError:
        print("Invalid input. Please enter a valid transaction ID.")


# ==============================
# Optional Feature: Insert Transaction
# ==============================
def insert_transaction(transactions):
    try:
        transaction_id = int(input("Enter Transaction ID: "))
        customer_name = input("Enter Customer Name: ")
        product_name = input("Enter Product Name: ")
        amount = float(input("Enter Amount: RM"))
        transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")

        new_transaction = Transaction(
            transaction_id,
            customer_name,
            product_name,
            amount,
            transaction_date
        )

        transactions.append(new_transaction)
        print("Transaction inserted successfully.")

    except ValueError:
        print("Invalid input. Please enter numbers for Transaction ID and Amount.")


# ==============================
# Time Complexity Table
# ==============================
def display_time_complexity():
    print("\n================ Time Complexity Analysis ================")
    print(f"{'Algorithm':<20}{'Best Case':<15}{'Average Case':<15}{'Worst Case':<15}")
    print("-" * 65)
    print(f"{'Merge Sort':<20}{'O(n log n)':<15}{'O(n log n)':<15}{'O(n log n)':<15}")
    print(f"{'Binary Search':<20}{'O(1)':<15}{'O(log n)':<15}{'O(log n)':<15}")
    print(f"{'Linear Search':<20}{'O(1)':<15}{'O(n)':<15}{'O(n)':<15}")
    print("===========================================================")


# ==============================
# Main Menu
# ==============================
def main():
    transactions = create_sample_transactions()

    while True:
        print("\n================ Online Shopping Transaction System ================")
        print("1. Display all transactions")
        print("2. Sort transactions using Merge Sort")
        print("3. Search transaction using Binary Search")
        print("4. Search transaction using Linear Search")
        print("5. Compare Binary Search and Linear Search performance")
        print("6. Insert new transaction")
        print("7. Display time complexity analysis")
        print("8. Exit")
        print("====================================================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            display_transactions(transactions)

        elif choice == "2":
            sorted_transactions = test_merge_sort_performance(transactions)
            transactions = sorted_transactions

        elif choice == "3":
            search_using_binary(transactions)

        elif choice == "4":
            search_using_linear(transactions)

        elif choice == "5":
            compare_search_performance(transactions)

        elif choice == "6":
            insert_transaction(transactions)

        elif choice == "7":
            display_time_complexity()

        elif choice == "8":
            print("Thank you for using the Transaction System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()