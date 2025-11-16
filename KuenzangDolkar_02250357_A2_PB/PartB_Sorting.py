def Bubble_sort(arr):   
    n = len(arr)        
    for i in range(n):      
        swapped = False    
        for j in range(0, n-i-1):       
            if arr[j] > arr[j+1]:       
                arr[j], arr[j+1] = arr[j+1], arr[j]     
                swapped = True      
        if not swapped:    
            break
    return arr     
def Insertion_sort(arr):
    n = len(arr)        
    for i in range(1, n):       
        key = arr[i]       
        j = i - 1       
        while j >= 0 and key < arr[j]:     
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key        
    return arr      

def Quick_sort(arr, calls = 0):
    calls += 1      
    if len(arr) <= 1:       
        return arr, calls
    else:
        pivot = arr[len(arr) // 2]      
        left = [x for x in arr if x < pivot]      
        middle = [x for x in arr if x == pivot]     
        right = [x for x in arr if x > pivot]       
        left_sorted, calls = Quick_sort(left, calls)
        right_sorted, calls = Quick_sort(right, calls)
        
        return left_sorted + middle + right_sorted, calls

# --- Main Menu Function ---
def menu():
    # Hardcoded lists for sorting examples
    student_names =["Chado", "Dolkar", "Kuenzang", "Dupchu", "Tashi", "Dorji", "Jigme", "Tandin", "Wangchuk", "Lhamo", "Tshewang", "Pema", "Wangmo", "Lekdhen", "Chimi"]
    test_scores_unsorted = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 60]
    book_prices = [450, 230, 678, 125, 890, 345, 210, 999, 410, 505, 150, 275, 320, 199, 600]

    while True:
        print("\n=== Sorting Algorithms Menu ===")      
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice (1-4): ").strip()   

        # --- Option 1: Bubble Sort ---
        if choice == "1":
            print("Original:", student_names)      
            sorted_names = Bubble_sort(student_names)   
            print("Sorted:", sorted_names)      

            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":        
                print("Thank you for using the sorting program!")
                break
        
        # --- Option 2: Insertion Sort ---
        elif choice == "2":
            print("Original scores:", test_scores_unsorted)     
            sorted_scores = Insertion_sort(test_scores_unsorted)    
            print("Performing Insertion Sort...")       
            print("Sorted scores:", sorted_scores)  
           
            top5 = sorted_scores[-5:][::-1] 
            print("Top 5 Scores:")
            for i, score in enumerate(top5, start=1):     
                print(f"{i}. {score}")

            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":
                print("Thank you for using the sorting program!")
                break

        # --- Option 3: Quick Sort ---
        elif choice == "3":
            print("Original prices:", book_prices)     
            sorted_prices, calls = Quick_sort(book_prices)     
            print("Sorted prices:", sorted_prices)      
            print("Recursive calls:", calls)    

            again = input("Would you like to perform another sort? (y/n): ").strip().lower()
            if again != "y":
                print("Thank you for using the sorting program!")
                break
        # --- Option 4: Exit ---
        elif choice == "4":
            print("Exiting program. Thank you for using the search program!")
            break
        # --- Invalid Option ---
        else:
            print("Invalid choice. Please select a valid option (1-4).")

menu()
