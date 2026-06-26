import time
import threading


# ==============================
# Factorial Function
# ==============================
def calculate_factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


# ==============================
# Worker Function for Thread
# ==============================
def factorial_worker(number, results):
    results[number] = calculate_factorial(number)


# ==============================
# Multithreading Experiment
# ==============================
def run_multithreading_experiment(rounds=10):
    numbers = [50, 100, 200]
    times = []

    print("\n================ Multithreading Factorial Experiment ================")
    print(f"{'Round':<10}{'Time Taken (ns)':<20}")
    print("-" * 35)

    for round_number in range(1, rounds + 1):
        results = {}
        threads = []

        start_time = time.perf_counter_ns()

        for number in numbers:
            thread = threading.Thread(
                target=factorial_worker,
                args=(number, results)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        print(f"{round_number:<10}{elapsed_time:<20}")

    average_time = sum(times) / len(times)

    print("-" * 35)
    print(f"{'Average':<10}{average_time:<20.2f}")
    print("=====================================================================")

    return times, average_time


# ==============================
# Non-Multithreading Experiment
# ==============================
def run_non_multithreading_experiment(rounds=10):
    numbers = [50, 100, 200]
    times = []

    print("\n================ Non-Multithreading Factorial Experiment ================")
    print(f"{'Round':<10}{'Time Taken (ns)':<20}")
    print("-" * 35)

    for round_number in range(1, rounds + 1):
        results = {}

        start_time = time.perf_counter_ns()

        for number in numbers:
            results[number] = calculate_factorial(number)

        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        print(f"{round_number:<10}{elapsed_time:<20}")

    average_time = sum(times) / len(times)

    print("-" * 35)
    print(f"{'Average':<10}{average_time:<20.2f}")
    print("=========================================================================")

    return times, average_time


# ==============================
# Display Factorial Results
# ==============================
def display_factorial_results():
    numbers = [50, 100, 200]

    print("\n================ Factorial Results ================")

    for number in numbers:
        result = calculate_factorial(number)
        print(f"\n{number}! =")
        print(result)

    print("===================================================")


# ==============================
# Comparison Summary
# ==============================
def compare_results(thread_average, non_thread_average):
    print("\n================ Experiment Comparison Summary ================")
    print(f"Average time with multithreading:     {thread_average:.2f} ns")
    print(f"Average time without multithreading:  {non_thread_average:.2f} ns")

    if thread_average < non_thread_average:
        print("\nResult: Multithreading was faster in this experiment.")
    else:
        print("\nResult: Non-multithreading was faster in this experiment.")

    print("\nExplanation:")
    print("Factorial calculation is a CPU-bound task.")
    print("In CPython, the Global Interpreter Lock, also called GIL, allows only one thread")
    print("to execute Python bytecode at a time. Because of this, multithreading may not")
    print("improve the speed of CPU-heavy calculations and may even add thread overhead.")
    print("================================================================")


# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("\n================ Factorial Multithreading System ================")
        print("1. Display factorial results for 50!, 100!, and 200!")
        print("2. Run multithreading experiment")
        print("3. Run non-multithreading experiment")
        print("4. Run full comparison experiment")
        print("5. Exit")
        print("================================================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_factorial_results()

        elif choice == "2":
            run_multithreading_experiment()

        elif choice == "3":
            run_non_multithreading_experiment()

        elif choice == "4":
            thread_times, thread_average = run_multithreading_experiment()
            non_thread_times, non_thread_average = run_non_multithreading_experiment()
            compare_results(thread_average, non_thread_average)

        elif choice == "5":
            print("Thank you for using the Factorial Multithreading System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()