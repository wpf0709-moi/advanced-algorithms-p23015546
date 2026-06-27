import time  # Imports the time module so the program can measure execution time in nanoseconds.


# ==============================  
# Transaction Entity Class 
# ============================== 
class Transaction:  # Defines a class used to store one transaction record.

    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):  # Runs when a new Transaction object is created.
        self.transaction_id = transaction_id  # Stores the unique transaction ID inside the object.
        self.customer_name = customer_name  # Stores the customer's name inside the object.
        self.product_name = product_name  # Stores the purchased product name inside the object.
        self.amount = amount  # Stores the transaction amount or price.
        self.transaction_date = transaction_date  # Stores the date when the transaction happened.


    def __str__(self):  # Defines how the transaction should appear when printed.
        return (  # Starts returning a multi-line formatted string.
            f"ID: {self.transaction_id} | "  # Adds the transaction ID to the printed output.
            f"Customer: {self.customer_name} | "  # Adds the customer name to the printed output.
            f"Product: {self.product_name} | "  # Adds the product name to the printed output.
            f"Amount: RM{self.amount:.2f} | "  # Adds the amount formatted to 2 decimal places.
            f"Date: {self.transaction_date}"  # Adds the transaction date to the printed output.
        )


# ============================== 
# Sample Unsorted Transaction Data
# ==============================
def create_sample_transactions():  # Defines a function that creates the starting list of transactions.

    return [  # Returns a list containing Transaction objects.
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
def display_transactions(transactions):  # Defines a function to display all transactions in a list.

    if len(transactions) == 0:  # Checks whether the transaction list is empty.
        print("\nNo transactions available.")  # Tells the user there are no transactions to display.
        return  # Stops the function early because there is nothing to print.

    print("\n==================== Transaction List ====================")
    for transaction in transactions:  # Loops through every transaction in the list.
        print(transaction)  # Prints the transaction using the Transaction __str__ method.
    print("==========================================================")


# ============================== 
# Merge Sort: Divide and Conquer 
# ============================== 
def merge_sort(transactions):  # Defines a recursive merge sort function for transaction records.

    # Base case: a list with 0 or 1 item is already sorted  # Explains why the next condition stops recursion.
    if len(transactions) <= 1:  # Checks whether the list is already small enough to be sorted.
        return transactions  # Returns the list unchanged because no sorting is needed.


    # Divide step: split the list into two halves  # Explains that merge sort first breaks the list apart.
    middle = len(transactions) // 2  # Finds the middle index using integer division.
    left_half = transactions[:middle]  # Creates a list containing everything before the middle index.
    right_half = transactions[middle:]  # Creates a list containing everything from the middle index onward.


    # Conquer step: recursively sort both halves  # Explains that each smaller half is sorted separately.
    sorted_left = merge_sort(left_half)  # Recursively sorts the left half.
    sorted_right = merge_sort(right_half)  # Recursively sorts the right half.


    # Combine step: merge the two sorted halves  # Explains that the sorted halves are joined together.
    return merge(sorted_left, sorted_right)  # Returns one sorted list made from both sorted halves.


def merge(left, right):  # Defines a helper function that combines two sorted lists.

    sorted_list = []  # Creates an empty list to store the merged sorted result.
    i = 0  # Starts the index pointer for the left list at the first item.
    j = 0  # Starts the index pointer for the right list at the first item.

    # Compare transaction IDs and add the smaller one first  # Explains the main comparison step in merging.
    while i < len(left) and j < len(right):  # Repeats while both lists still have items left to compare.
        if left[i].transaction_id <= right[j].transaction_id:  # Checks whether the current left transaction ID is smaller or equal.
            sorted_list.append(left[i])  # Adds the current left transaction to the sorted result.
            i += 1  # Moves the left pointer to the next transaction.

        else:  # Runs when the current right transaction ID is smaller.
            sorted_list.append(right[j])  # Adds the current right transaction to the sorted result.
            j += 1  # Moves the right pointer to the next transaction.

    # Add remaining transactions from the left side  # Explains that leftover left items are already sorted.
    while i < len(left):  # Repeats while there are still unused items in the left list.
        sorted_list.append(left[i])  # Adds the remaining left transaction to the result.
        i += 1  # Moves to the next remaining left transaction.


    # Add remaining transactions from the right side  # Explains that leftover right items are already sorted.
    while j < len(right):  # Repeats while there are still unused items in the right list.
        sorted_list.append(right[j])  # Adds the remaining right transaction to the result.
        j += 1  # Moves to the next remaining right transaction.

    return sorted_list  # Returns the fully merged and sorted list.


# ==============================  
# Binary Search 
# ============================== 
def binary_search(transactions, target_id):  # Defines a function to find a transaction ID using binary search.
    low = 0  # Sets the lowest search index to the start of the list.
    high = len(transactions) - 1  # Sets the highest search index to the end of the list.

    while low <= high:  # Keeps searching while the search range is still valid.
        middle = (low + high) // 2  # Finds the middle index of the current search range.
        middle_transaction = transactions[middle]  # Gets the transaction located at the middle index.


        if middle_transaction.transaction_id == target_id:  # Checks whether the middle transaction is the target.
            return middle_transaction  # Returns the matching transaction record.


        elif target_id < middle_transaction.transaction_id:  # Checks whether the target ID is smaller than the middle ID.
            high = middle - 1  # Moves the search range to the left half.


        else:  # Runs when the target ID is larger than the middle ID.
            low = middle + 1  # Moves the search range to the right half.

    return None  # Returns None when the target ID is not found.


# ============================== 
# Linear Search  
# ============================== 
def linear_search(transactions, target_id):  # Defines a function to find a transaction ID using linear search.

    for transaction in transactions:  # Loops through each transaction from start to end.
        if transaction.transaction_id == target_id:  # Checks whether the current transaction has the target ID.
            return transaction  # Returns the matching transaction record.
    return None  # Returns None if no matching transaction is found.


# ============================== 
# Performance Comparison  
# ============================== 
def compare_search_performance(transactions):  # Defines a function to compare search performance.
    sorted_transactions = merge_sort(transactions)  # Sorts the transactions first because binary search needs sorted data.

    search_keys = [101, 106, 115, 999, 888, 103, 777]  # Stores transaction IDs to test, including IDs that do not exist.

    print("\n================ Search Performance Comparison ================") 
    print(f"{'Search ID':<12}{'Binary Search Time (ns)':<28}{'Linear Search Time (ns)':<25}")  # Prints aligned column headers.
    print("-" * 70)  # Prints a separator line 70 characters long.

    total_binary_time = 0  # Starts the total binary search time at zero.
    total_linear_time = 0  # Starts the total linear search time at zero.

    for key in search_keys:  # Repeats the timing test for each search ID.
        start_binary = time.perf_counter_ns()  # Records the start time before binary search.
        binary_search(sorted_transactions, key)  # Searches for the key using binary search.
        end_binary = time.perf_counter_ns()  # Records the end time after binary search.
        binary_time = end_binary - start_binary  # Calculates how long binary search took.


        start_linear = time.perf_counter_ns()  # Records the start time before linear search.
        linear_search(sorted_transactions, key)  # Searches for the key using linear search.
        end_linear = time.perf_counter_ns()  # Records the end time after linear search.
        linear_time = end_linear - start_linear  # Calculates how long linear search took.


        total_binary_time += binary_time  # Adds this binary search time to the running total.
        total_linear_time += linear_time  # Adds this linear search time to the running total.

        print(f"{key:<12}{binary_time:<28}{linear_time:<25}")  # Prints the search ID and both measured times.


    average_binary = total_binary_time / len(search_keys)  # Calculates the average binary search time.
    average_linear = total_linear_time / len(search_keys)  # Calculates the average linear search time.

    print("-" * 70)  # Prints another separator line before the average row.
    print(f"{'Average':<12}{average_binary:<28.2f}{average_linear:<25.2f}")  # Prints both average times.


    if average_binary < average_linear:  # Checks whether binary search was faster on average.
        print("\nConclusion: Binary Search was faster on average.")  # Prints that binary search was faster.
    else:  # Runs when linear search is faster or equal in this test.
        print("\nConclusion: Linear Search was faster in this small test.")  # Prints that linear search was faster in this run.

    print("================================================================")


# ============================== 
# Merge Sort Performance 
# ============================== 
def test_merge_sort_performance(transactions):  # Defines a function to display and time merge sort.
    print("\n================ Merge Sort Performance ================")
    print("Before sorting:")  # Labels the unsorted transaction list.
    display_transactions(transactions)  # Displays the transactions before sorting.

    start_time = time.perf_counter_ns()  # Records the start time before merge sort.
    sorted_transactions = merge_sort(transactions)  # Sorts the transactions by transaction ID.
    end_time = time.perf_counter_ns()  # Records the end time after merge sort.

    elapsed_time = end_time - start_time  # Calculates how long merge sort took.

    print("\nAfter sorting by Transaction ID:")  # Labels the sorted transaction list.
    display_transactions(sorted_transactions)  # Displays the transactions after sorting.

    print(f"\nMerge Sort execution time: {elapsed_time} ns")  # Prints the measured merge sort execution time.
    print("========================================================") 

    return sorted_transactions  # Returns the sorted list so it can be reused.


# ==============================  
# Search Using Binary Search  
# ============================== 
def search_using_binary(transactions):  # Defines a function that lets the user search by binary search.
    try:  # Starts error handling for invalid numeric input.
        sorted_transactions = merge_sort(transactions)  # Sorts the transactions first because binary search requires sorted data.

        target_id = int(input("Enter Transaction ID to search using Binary Search: "))  # Gets the target ID from the user as an integer.

        start_time = time.perf_counter_ns()  # Records the start time before binary search.
        result = binary_search(sorted_transactions, target_id)  # Searches the sorted list for the target ID.
        end_time = time.perf_counter_ns()  # Records the end time after binary search.

        elapsed_time = end_time - start_time  # Calculates how long the binary search took.

        if result is not None:  # Checks whether a matching transaction was found.
            print("\nTransaction found using Binary Search:")  # Prints a success message.
            print(result)  # Prints the matching transaction details.
        else:  # Runs when the search result is None.
            print("\nTransaction not found using Binary Search.")  # Tells the user no matching transaction was found.

        print(f"Binary Search execution time: {elapsed_time} ns")  # Prints the measured binary search time.

    except ValueError:  # Runs if the user enters something that is not a valid integer.
        print("Invalid input. Please enter a valid transaction ID.")  # Shows an error message for invalid ID input.


# ==============================  
# Search Using Linear Search 
# ==============================  
def search_using_linear(transactions):  # Defines a function that lets the user search by linear search.
    try:  # Starts error handling for invalid numeric input.
        target_id = int(input("Enter Transaction ID to search using Linear Search: "))  # Gets the target ID from the user as an integer.

        start_time = time.perf_counter_ns()  # Records the start time before linear search.
        result = linear_search(transactions, target_id)  # Searches the list one item at a time.
        end_time = time.perf_counter_ns()  # Records the end time after linear search.

        elapsed_time = end_time - start_time  # Calculates how long the linear search took.

        if result is not None:  # Checks whether a matching transaction was found.
            print("\nTransaction found using Linear Search:")  # Prints a success message.
            print(result)  # Prints the matching transaction details.
        else:  # Runs when the search result is None.
            print("\nTransaction not found using Linear Search.")  # Tells the user no matching transaction was found.

        print(f"Linear Search execution time: {elapsed_time} ns")  # Prints the measured linear search time.

    except ValueError:  # Runs if the user enters something that is not a valid integer.
        print("Invalid input. Please enter a valid transaction ID.")  # Shows an error message for invalid ID input.


# ============================== 
# Insert Transaction  
# ============================== 
def insert_transaction(transactions):  # Defines a function that asks the user for new transaction details.
    try:  # Starts error handling for invalid numeric input.
        transaction_id = int(input("Enter Transaction ID: "))  
        customer_name = input("Enter Customer Name: ")  
        product_name = input("Enter Product Name: ") 
        amount = float(input("Enter Amount: RM"))  
        transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ") 

        new_transaction = Transaction(  # Starts creating a new Transaction object from the user's input.
            transaction_id,  # Passes the entered transaction ID into the Transaction object.
            customer_name,  # Passes the entered customer name into the Transaction object.
            product_name,  # Passes the entered product name into the Transaction object.
            amount,  # Passes the entered amount into the Transaction object.
            transaction_date  # Passes the entered transaction date into the Transaction object.
        )

        transactions.append(new_transaction)  # Adds the new transaction to the transaction list.
        print("Transaction inserted successfully.")  # Tells the user the transaction was added.

    except ValueError:  # Runs if the transaction ID or amount cannot be converted to a number.
        print("Invalid input. Please enter numbers for Transaction ID and Amount.")  # Shows an error message for invalid numeric input.


# ============================== 
# Time Complexity Table 
# ==============================
def display_time_complexity():  # Defines a function to print algorithm time complexities.
    print("\n================ Time Complexity Analysis ================")  # Prints the time complexity heading.
    print(f"{'Algorithm':<20}{'Best Case':<15}{'Average Case':<15}{'Worst Case':<15}")  # Prints aligned table column headers.
    print("-" * 65)  # Prints a separator line 65 characters long.
    print(f"{'Merge Sort':<20}{'O(n log n)':<15}{'O(n log n)':<15}{'O(n log n)':<15}")  # Prints merge sort complexity for all cases.
    print(f"{'Binary Search':<20}{'O(1)':<15}{'O(log n)':<15}{'O(log n)':<15}")  # Prints binary search complexity for all cases.
    print(f"{'Linear Search':<20}{'O(1)':<15}{'O(n)':<15}{'O(n)':<15}")  # Prints linear search complexity for all cases.
    print("===========================================================")


# ==============================  
# Main Menu  
# ==============================  
def main():  # Defines the main function where the program starts its main work.
    transactions = create_sample_transactions()  # Creates the starting list of sample transactions.

    while True:  # Starts an infinite loop so the menu keeps showing until the user exits.
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
            display_transactions(transactions)  # Displays every transaction in the current list.

        elif choice == "2":
            sorted_transactions = test_merge_sort_performance(transactions)  # Sorts the transactions and shows sort timing.
            transactions = sorted_transactions  # Updates the main transaction list to the sorted list.

        elif choice == "3":
            search_using_binary(transactions)  # Runs the binary search input and result function.

        elif choice == "4":
            search_using_linear(transactions)  # Runs the linear search input and result function.

        elif choice == "5":
            compare_search_performance(transactions)  # Compares binary search and linear search timing.

        elif choice == "6":
            insert_transaction(transactions)  # Runs the insert transaction function.

        elif choice == "7":
            display_time_complexity()  # Displays the Big O time complexity table.

        elif choice == "8":
            print("Thank you for using the Transaction System.")  # Prints a goodbye message.
            break  # Stops the menu loop and ends the program.

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")  # Tells the user to enter a valid menu option.


if __name__ == "__main__":  # Checks whether this file is being run directly instead of imported.
    main()  # Calls the main function to start the program.
