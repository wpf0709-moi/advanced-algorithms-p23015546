import time  # Imports the time module so the program can measure search speed in nanoseconds.


# ==============================  
# Medicine Entity Class  
# ============================== 

class Medicine:  # Defines a class used to store one medicine record.

    def __init__(self, medicine_id, name, category, price, quantity):  # Runs automatically when a new Medicine object is created.
        self.medicine_id = medicine_id  # Stores the medicine's unique ID inside the object.
        self.name = name  # Stores the medicine's name inside the object.
        self.category = category  # Stores the medicine category, such as Tablet or Syrup.
        self.price = price  # Stores the medicine price.
        self.quantity = quantity  # Stores how many units are available in stock.


    def __str__(self):  # Defines how the medicine should look when printed as text.
        return (  # Starts returning a multi-line formatted string.
            f"ID: {self.medicine_id} | "  # Adds the medicine ID to the printed output.
            f"Name: {self.name} | "  # Adds the medicine name to the printed output.
            f"Category: {self.category} | "  # Adds the medicine category to the printed output.
            f"Price: RM{self.price:.2f} | "  # Adds the price formatted to 2 decimal places.
            f"Quantity: {self.quantity}"  # Adds the stock quantity to the printed output.
        )


# ==============================  
# Hash Table using Linear Probing 
# ============================== 

class HashTable:  # Defines a hash table class for storing medicines by ID.

    def __init__(self, size):  # Runs automatically when a new HashTable object is created.
        self.size = size  # Stores the number of buckets available in the hash table.
        self.table = [None] * size  # Creates an empty table where each bucket starts as None.


    def hash_function(self, key):  # Defines the function that converts a medicine ID into a bucket index.
        return key % self.size  # Uses modulo to keep the index within the table size.


    def insert(self, medicine):  # Defines how to add or update a medicine in the hash table.
        index = self.hash_function(medicine.medicine_id)  # Calculates the first bucket index for this medicine ID.
        original_index = index  # Saves the starting index so the program can detect a full loop.

        while self.table[index] is not None:  # Keeps checking while the current bucket is already occupied.
            if self.table[index].medicine_id == medicine.medicine_id:  # Checks whether the existing record has the same ID.
                self.table[index] = medicine  # Replaces the existing record with the new medicine details.
                print("Medicine record updated successfully.")  # Tells the user that an existing record was updated.
                return  # Stops the insert function after updating the record.

            index = (index + 1) % self.size  # Moves to the next bucket, wrapping back to 0 if needed.

            if index == original_index:  # Checks whether every bucket has been visited.
                print("Hash table is full. Cannot insert new medicine.")  # Tells the user there is no empty bucket.
                return  # Stops the insert function because insertion is impossible.

        self.table[index] = medicine  # Places the medicine in the first available empty bucket.
        print("Medicine inserted successfully.")  # Tells the user the new medicine was inserted.


    def search(self, medicine_id):  # Defines how to find a medicine by its ID in the hash table.
        index = self.hash_function(medicine_id)  # Calculates the first bucket index to search.
        original_index = index  # Saves the starting index so the search can stop after a full loop.

        while self.table[index] is not None:  # Keeps searching while the current bucket contains a record.
            if self.table[index].medicine_id == medicine_id:  # Checks whether the current medicine has the target ID.
                return self.table[index]  # Returns the matching medicine record.

            index = (index + 1) % self.size  # Moves to the next bucket using linear probing.

            if index == original_index:  # Checks whether the search has returned to the starting bucket.
                break  # Stops searching because the whole table has been checked.

        return None  # Returns None when no matching medicine is found.
    

    def display(self):  # Defines how to print the full hash table contents.
        print("\n========== Pharmacy Inventory Hash Table ==========")  # Prints a heading for the hash table display.
        for index, medicine in enumerate(self.table):  # Loops through each bucket with its index and stored value.
            if medicine is None:  # Checks whether the current bucket is empty.
                print(f"Bucket {index}: Empty")  # Prints that the current bucket has no medicine.
            else:  # Runs when the current bucket contains a medicine record.
                print(f"Bucket {index}: {medicine}")  # Prints the bucket number and medicine details.
        print("===================================================")  # Prints a closing line for the display section.


# ==============================  
# One-Dimensional Array Search
# ==============================
def linear_array_search(medicine_array, medicine_id):  # Defines a linear search function for the medicine list.
    for medicine in medicine_array:  # Checks each medicine one by one from the list.
        if medicine.medicine_id == medicine_id:  # Compares the current medicine ID with the target ID.
            return medicine  # Returns the medicine when a matching ID is found.
    return None  # Returns None if the loop finishes without finding the medicine.


# ==============================
# Sample Data
# ==============================
def create_sample_data():  # Defines a function that creates the starting medicine list.
    return [  # Returns a list containing Medicine objects.
        Medicine(101, "Paracetamol", "Tablet", 5.50, 100),  
        Medicine(112, "Cough Syrup", "Syrup", 12.90, 45),  
        Medicine(123, "Vitamin C", "Supplement", 18.00, 60),  
        Medicine(134, "Antacid", "Tablet", 7.50, 80),  
        Medicine(145, "Antibiotic Cream", "Cream", 15.00, 30),  
        Medicine(156, "Flu Tablets", "Tablet", 9.20, 70), 
        Medicine(167, "Eye Drops", "Drops", 11.40, 35), 
        Medicine(178, "Pain Relief Gel", "Gel", 13.80, 25),  
        Medicine(189, "Multivitamin", "Supplement", 25.00, 40),  
        Medicine(190, "Bandage Pack", "First Aid", 6.00, 90),
    ]


# ==============================  
# Performance Test  
# ============================== 
def performance_test(hash_table, medicine_array):  # Defines a function to compare search performance.
    search_keys = [101, 145, 190, 999, 888, 123, 777]  # Stores medicine IDs to test, including IDs that do not exist.

    print("\n========== Search Performance Comparison ==========")  # Prints the performance comparison heading.
    print(f"{'Search Key':<12}{'Hash Table Time (ns)':<25}{'Array Time (ns)':<20}")  # Prints aligned column headers.
    print("-" * 60)  # Prints a separator line 60 characters long.

    total_hash_time = 0  # Starts the total hash table search time at zero.
    total_array_time = 0  # Starts the total array search time at zero.

    for key in search_keys:  # Repeats the timing test for each search key.
        start_hash = time.perf_counter_ns()  # Records the start time before hash table searching.
        hash_table.search(key)  # Searches for the key in the hash table.
        end_hash = time.perf_counter_ns()  # Records the end time after hash table searching.
        hash_time = end_hash - start_hash  # Calculates how long the hash table search took.

        start_array = time.perf_counter_ns()  # Records the start time before array searching.
        linear_array_search(medicine_array, key)  # Searches for the key in the normal list.
        end_array = time.perf_counter_ns()  # Records the end time after array searching.
        array_time = end_array - start_array  # Calculates how long the array search took.

        total_hash_time += hash_time  # Adds this hash table search time to the running total.
        total_array_time += array_time  # Adds this array search time to the running total.

        print(f"{key:<12}{hash_time:<25}{array_time:<20}")  # Prints the search key and both measured times.

    average_hash_time = total_hash_time / len(search_keys)  # Calculates the average hash table search time.
    average_array_time = total_array_time / len(search_keys)  # Calculates the average array search time.

    print("-" * 60)  # Prints another separator line before the average row.
    print(f"{'Average':<12}{average_hash_time:<25.2f}{average_array_time:<20.2f}")  # Prints both average times.

    if average_hash_time < average_array_time:  # Checks whether the hash table average time is lower.
        print("\nConclusion: Hash Table search was faster on average.")  # Prints that the hash table was faster.
    else:  # Runs when the array search average is lower or equal.
        print("\nConclusion: Array linear search was faster on average in this small test.")  # Prints that array search was faster in this run.

    print("===================================================")  


# ==============================  
# Insert New Medicine 
# ============================== 
def insert_new_medicine(hash_table, medicine_array):  # Defines a function that asks the user for new medicine details.
    try:  # Starts error handling for invalid numeric input.
        medicine_id = int(input("Enter Medicine ID: "))  # Gets the medicine ID from the user and converts it to an integer.
        name = input("Enter Medicine Name: ")  # Gets the medicine name from the user.
        category = input("Enter Category: ")  # Gets the medicine category from the user.
        price = float(input("Enter Price: RM"))  # Gets the price from the user and converts it to a decimal number.
        quantity = int(input("Enter Quantity: "))  # Gets the stock quantity from the user and converts it to an integer.

        new_medicine = Medicine(medicine_id, name, category, price, quantity)  # Creates a new Medicine object using the user's input.

        hash_table.insert(new_medicine)  # Inserts the new medicine into the hash table.
        medicine_array.append(new_medicine)  # Adds the new medicine to the normal list as well.

    except ValueError:  # Runs if ID, price, or quantity cannot be converted to a number.
        print("Invalid input. Please enter numbers for ID, price, and quantity.")  # Shows an error message for invalid input.


# ==============================
# Search Medicine
# ==============================
def search_medicine(hash_table):  # Defines a function that asks the user which medicine ID to search for.
    try:  # Starts error handling for invalid ID input.
        medicine_id = int(input("Enter Medicine ID to search: "))  # Gets the search ID from the user and converts it to an integer.
        result = hash_table.search(medicine_id)  # Searches the hash table for the entered medicine ID.

        if result is not None:  # Checks whether a matching medicine was found.
            print("\nMedicine found:")  # Prints a success message before showing the record.
            print(result)  # Prints the medicine details using the Medicine __str__ method.
        else:  # Runs when the search result is None.
            print("\nMedicine not found.")  # Tells the user that no medicine matched the ID.

    except ValueError:  # Runs if the entered medicine ID is not a valid integer.
        print("Invalid input. Please enter a valid medicine ID.")  # Shows an error message for invalid ID input.


# ==============================  
# Main Menu  
# ============================== 
def main():  # Defines the main function where the program starts its main work.
    hash_table = HashTable(20)  # Creates a hash table with 20 available buckets.
    medicine_array = create_sample_data()  # Creates the starting list of sample medicines.

    for medicine in medicine_array:  # Loops through each sample medicine.
        hash_table.insert(medicine)  # Inserts each sample medicine into the hash table.

    while True:  # Starts an infinite loop so the menu keeps showing until the user exits.
        print("\n========== Pharmacy Inventory System ==========")  
        print("1. Display all medicines")
        print("2. Insert new medicine") 
        print("3. Search medicine by ID")
        print("4. Compare search performance")
        print("5. Exit")
        print("===============================================")  

        choice = input("Enter your choice (1-5): ")

        if choice == "1":  
            hash_table.display()  # Displays the full hash table.

        elif choice == "2":  
            insert_new_medicine(hash_table, medicine_array)  # Runs the insert medicine function.

        elif choice == "3":  
            search_medicine(hash_table)  # Runs the search medicine function.

        elif choice == "4":  
            performance_test(hash_table, medicine_array)  # Runs the performance comparison function.

        elif choice == "5": 
            print("Thank you for using the Pharmacy Inventory System.")  # Prints a goodbye message.
            break  # Stops the menu loop and ends the program.

        else:  
            print("Invalid choice. Please enter a number from 1 to 5.")  # Tells the user to enter a valid menu option.


if __name__ == "__main__":  # Checks whether this file is being run directly instead of imported.
    main()  # Calls the main function to start the program.
