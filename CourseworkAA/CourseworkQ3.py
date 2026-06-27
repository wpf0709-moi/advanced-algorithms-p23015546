import time  # Imports the time module so the program can measure execution time in nanoseconds.
import threading  # Imports the threading module so the program can run tasks using multiple threads.


# ============================== 
# Factorial Function 
# ============================== 
def calculate_factorial(number):  # Defines a function that calculates the factorial of a given number.

    result = 1  # Starts the factorial result at 1 because factorial multiplication begins from 1.

    for i in range(1, number + 1):  # Loops from 1 up to and including the given number.
        result = result * i  # Multiplies the current result by the current loop value.

    return result  # Returns the final factorial value after the loop finishes.


# ==============================  
# Worker Function for Thread 
# ============================== 
def factorial_worker(number, results):  # Defines a worker function that calculates one factorial and stores it.
    results[number] = calculate_factorial(number)  # Saves the factorial result in the dictionary using the number as the key.


# ==============================  
# Multithreading Experiment  
# ============================== 
def run_multithreading_experiment(rounds=10):  # Defines a function that runs the threaded timing test for a set number of rounds.
    numbers = [50, 100, 200]  # Stores the numbers whose factorials will be calculated.
    times = []  # Creates an empty list to store the elapsed time for each round.

    print("\n================ Multithreading Factorial Experiment ================") 
    print(f"{'Round':<10}{'Time Taken (ns)':<20}")  # Prints aligned column headers for round number and time.
    print("-" * 35)  # Prints a separator line 35 characters long.

    for round_number in range(1, rounds + 1):  # Repeats the experiment from round 1 up to the chosen number of rounds.
        results = {}  # Creates an empty dictionary to store factorial results for this round.
        threads = []  # Creates an empty list to store the thread objects.

        start_time = time.perf_counter_ns()  # Records the start time before creating and running the threads.

        for number in numbers:  # Loops through each number that needs a factorial calculation.
            thread = threading.Thread(  # Creates a new thread object.
                target=factorial_worker,  # Tells the thread to run the factorial_worker function.
                args=(number, results)  # Passes the number and shared results dictionary to the worker function.
            )  
            threads.append(thread)  # Adds the new thread to the threads list so it can be tracked.
            thread.start()  # Starts running the thread.

        for thread in threads:  # Loops through every thread that was started.
            thread.join()  # Waits for the current thread to finish before continuing.

        end_time = time.perf_counter_ns()  # Records the end time after all threads have finished.
        elapsed_time = end_time - start_time  # Calculates the total time taken for this round.
        times.append(elapsed_time)  # Stores this round's elapsed time in the times list.

        print(f"{round_number:<10}{elapsed_time:<20}")  # Prints the round number and measured time.

    average_time = sum(times) / len(times)  # Calculates the average time across all rounds.

    print("-" * 35)  # Prints another separator line before the average row.
    print(f"{'Average':<10}{average_time:<20.2f}")  # Prints the average time formatted to 2 decimal places.
    print("=====================================================================")

    return times, average_time  # Returns all recorded times and the average time.


# ==============================  
# Non-Multithreading Experiment 
# ============================== 
def run_non_multithreading_experiment(rounds=10):  # Defines a function that runs the normal sequential timing test.
    numbers = [50, 100, 200]  # Stores the numbers whose factorials will be calculated.
    times = []  # Creates an empty list to store the elapsed time for each round.

    print("\n================ Non-Multithreading Factorial Experiment ================")
    print(f"{'Round':<10}{'Time Taken (ns)':<20}")  # Prints aligned column headers for round number and time.
    print("-" * 35)  # Prints a separator line 35 characters long.

    for round_number in range(1, rounds + 1):  # Repeats the experiment from round 1 up to the chosen number of rounds.
        results = {}  # Creates an empty dictionary to store factorial results for this round.

        start_time = time.perf_counter_ns()  # Records the start time before the calculations begin.

        for number in numbers:  # Loops through each number one at a time.
            results[number] = calculate_factorial(number)  # Calculates the factorial and stores it in the dictionary.

        end_time = time.perf_counter_ns()  # Records the end time after all calculations finish.
        elapsed_time = end_time - start_time  # Calculates the total time taken for this round.
        times.append(elapsed_time)  # Stores this round's elapsed time in the times list.

        print(f"{round_number:<10}{elapsed_time:<20}")  # Prints the round number and measured time.

    average_time = sum(times) / len(times)  # Calculates the average time across all rounds.

    print("-" * 35)  # Prints another separator line before the average row.
    print(f"{'Average':<10}{average_time:<20.2f}")  # Prints the average time formatted to 2 decimal places.
    print("=========================================================================")

    return times, average_time  # Returns all recorded times and the average time.


# ============================== 
# Display Factorial Results
# ============================== 
def display_factorial_results():  # Defines a function that displays factorial results for fixed numbers.
    numbers = [50, 100, 200]  # Stores the numbers whose factorials will be displayed.

    print("\n================ Factorial Results ================")

    for number in numbers:  # Loops through each number in the list.
        result = calculate_factorial(number)  # Calculates the factorial for the current number.
        print(f"\n{number}! =")  # Prints a label showing which factorial is being displayed.
        print(result)  # Prints the calculated factorial value.

    print("===================================================") 


# ==============================  
# Comparison Summary 
# ============================== 
def compare_results(thread_average, non_thread_average):  # Defines a function that compares the two average times.
    print("\n================ Experiment Comparison Summary ================")  # Prints the comparison summary heading.
    print(f"Average time with multithreading:     {thread_average:.2f} ns")  # Prints the average threaded time.
    print(f"Average time without multithreading:  {non_thread_average:.2f} ns")  # Prints the average non-threaded time.

    if thread_average < non_thread_average:  # Checks whether the threaded average time is lower.
        print("\nResult: Multithreading was faster in this experiment.")  # Prints that multithreading was faster.
    else:
        print("\nResult: Non-multithreading was faster in this experiment.")  # Prints that non-multithreading was faster.

    print("\nExplanation:") 
    print("Factorial calculation is a CPU-bound task.")  
    print("In CPython, the Global Interpreter Lock, also called GIL, allows only one thread")  
    print("to execute Python bytecode at a time. Because of this, multithreading may not")   
    print("improve the speed of CPU-heavy calculations and may even add thread overhead.")  
    print("================================================================")


# ==============================  
# Main Program  
# ==============================  
def main():  # Defines the main function where the program starts its main work.

    while True:  # Starts an infinite loop so the menu keeps showing until the user exits.
        print("\n================ Factorial Multithreading System ================")  
        print("1. Display factorial results for 50!, 100!, and 200!")  
        print("2. Run multithreading experiment")  
        print("3. Run non-multithreading experiment")  
        print("4. Run full comparison experiment") 
        print("5. Exit") 
        print("================================================================") 

        choice = input("Enter your choice (1-5): ") 

        if choice == "1": 
            display_factorial_results()  # Runs the function that prints 50!, 100!, and 200!.

        elif choice == "2":  
            run_multithreading_experiment()  # Runs the threaded factorial timing experiment.

        elif choice == "3":  
            run_non_multithreading_experiment()  # Runs the normal sequential factorial timing experiment.

        elif choice == "4":  
            thread_times, thread_average = run_multithreading_experiment()  # Runs threaded timing and stores its results.
            non_thread_times, non_thread_average = run_non_multithreading_experiment()  # Runs non-threaded timing and stores its results.
            compare_results(thread_average, non_thread_average)  # Compares both average times and prints the conclusion.

        elif choice == "5": 
            print("Thank you for using the Factorial Multithreading System.")  # Prints a goodbye message.
            break  # Stops the menu loop and ends the program.

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")  # Tells the user to enter a valid menu option.


if __name__ == "__main__":  # Checks whether this file is being run directly instead of imported.
    main()  # Calls the main function to start the program.
