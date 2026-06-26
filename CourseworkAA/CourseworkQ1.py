import time


# ==============================
# Medicine Entity Class
# ==============================
class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.medicine_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Price: RM{self.price:.2f} | "
            f"Quantity: {self.quantity}"
        )


# ==============================
# Hash Table using Linear Probing
# ==============================
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.medicine_id)
        original_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                print("Medicine record updated successfully.")
                return

            index = (index + 1) % self.size

            if index == original_index:
                print("Hash table is full. Cannot insert new medicine.")
                return

        self.table[index] = medicine
        print("Medicine inserted successfully.")

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)
        original_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == original_index:
                break

        return None

    def display(self):
        print("\n========== Pharmacy Inventory Hash Table ==========")
        for index, medicine in enumerate(self.table):
            if medicine is None:
                print(f"Bucket {index}: Empty")
            else:
                print(f"Bucket {index}: {medicine}")
        print("===================================================")


# ==============================
# One-Dimensional Array Search
# ==============================
def linear_array_search(medicine_array, medicine_id):
    for medicine in medicine_array:
        if medicine.medicine_id == medicine_id:
            return medicine
    return None


# ==============================
# Sample Data
# ==============================
def create_sample_data():
    return [
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
def performance_test(hash_table, medicine_array):
    search_keys = [101, 145, 190, 999, 888, 123, 777]

    print("\n========== Search Performance Comparison ==========")
    print(f"{'Search Key':<12}{'Hash Table Time (ns)':<25}{'Array Time (ns)':<20}")
    print("-" * 60)

    total_hash_time = 0
    total_array_time = 0

    for key in search_keys:
        start_hash = time.perf_counter_ns()
        hash_table.search(key)
        end_hash = time.perf_counter_ns()
        hash_time = end_hash - start_hash

        start_array = time.perf_counter_ns()
        linear_array_search(medicine_array, key)
        end_array = time.perf_counter_ns()
        array_time = end_array - start_array

        total_hash_time += hash_time
        total_array_time += array_time

        print(f"{key:<12}{hash_time:<25}{array_time:<20}")

    average_hash_time = total_hash_time / len(search_keys)
    average_array_time = total_array_time / len(search_keys)

    print("-" * 60)
    print(f"{'Average':<12}{average_hash_time:<25.2f}{average_array_time:<20.2f}")

    if average_hash_time < average_array_time:
        print("\nConclusion: Hash Table search was faster on average.")
    else:
        print("\nConclusion: Array linear search was faster on average in this small test.")

    print("===================================================")


# ==============================
# Insert New Medicine
# ==============================
def insert_new_medicine(hash_table, medicine_array):
    try:
        medicine_id = int(input("Enter Medicine ID: "))
        name = input("Enter Medicine Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: RM"))
        quantity = int(input("Enter Quantity: "))

        new_medicine = Medicine(medicine_id, name, category, price, quantity)

        hash_table.insert(new_medicine)
        medicine_array.append(new_medicine)

    except ValueError:
        print("Invalid input. Please enter numbers for ID, price, and quantity.")


# ==============================
# Search Medicine
# ==============================
def search_medicine(hash_table):
    try:
        medicine_id = int(input("Enter Medicine ID to search: "))
        result = hash_table.search(medicine_id)

        if result is not None:
            print("\nMedicine found:")
            print(result)
        else:
            print("\nMedicine not found.")

    except ValueError:
        print("Invalid input. Please enter a valid medicine ID.")


# ==============================
# Main Menu
# ==============================
def main():
    hash_table = HashTable(20)
    medicine_array = create_sample_data()

    for medicine in medicine_array:
        hash_table.insert(medicine)

    while True:
        print("\n========== Pharmacy Inventory System ==========")
        print("1. Display all medicines")
        print("2. Insert new medicine")
        print("3. Search medicine by ID")
        print("4. Compare search performance")
        print("5. Exit")
        print("===============================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hash_table.display()

        elif choice == "2":
            insert_new_medicine(hash_table, medicine_array)

        elif choice == "3":
            search_medicine(hash_table)

        elif choice == "4":
            performance_test(hash_table, medicine_array)

        elif choice == "5":
            print("Thank you for using the Pharmacy Inventory System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()