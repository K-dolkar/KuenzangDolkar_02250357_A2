def Linear_search(arr, target):    
    comparisons = 0            
    for i, val in enumerate(arr):          
        comparisons += 1       
        if val == target:       
            return i + 1, comparisons      
    return None, comparisons         

def Binary_search(arr, target):     
    left, right = 0, len(arr) - 1       
    comparisons = 0        
    while left <= right:        
        mid = (left + right) // 2            
        comparisons += 1            
        if arr[mid] == target:      
            return mid + 1, comparisons        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            return None, comparisons       
def Menu():
    # 20 student IDs (Unsorted)
    student_ids = [1001, 1005, 1003, 1008, 1002, 1007, 1004, 1010, 1006, 1009,
                   1011, 1015, 1013, 1018, 1012, 1014, 1017, 1020, 1016, 1019]
    # 20 scores (Sorted)
    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98,
                     100, 102, 105, 108, 110]
    while True:
        print("\n----Searching Algorithm Menu----")  
        print("Select a search operation (1-3):")     
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. exit the program")

        choice = input("Enter your choice (1-3): ").strip() 

        if choice == "1":    # --- Option 1: Linear Search ---
            while True:
                print("Searching in the list :", student_ids)     
                try:        # Ask user for the target ID to search
                    target = int(input("Enter the ID that you want to search: ").strip())
                except ValueError:      
                    print("Invalid input. Please enter a valid integer student ID.")
                    continue     
                position, comparisions = Linear_search(student_ids, target) 
                if position is not None:   
                    print(f"   Result: Student ID {target} found at position {position} with {comparisions} comparisons.")
                else:
                    print(f"   Result: Student ID {target} not found after {comparisions} comparisons.")
                    # Ask user if they want try again
                again = input("Do you want to try again? (y/n): ").strip().lower()
                if again != "y":    
                    break
                # Ask user if they want to perform another search
            another = input("Would you like to perform another search? (y/n): ").strip().lower()
            if another != "y":      
                print("Thank you for using the search program!")
                break

        elif choice == "2":     # --- Option 2: Binary Search ---
            while True:
                print(f"Sorted scores:{sorted_scores}")   
                try:    
                    target = int(input("Enter the score that you want to search: ").strip())
                except ValueError:      
                    print("Invalid input. Please enter a valid integer score.")
                    continue        
                position, comparisions = Binary_search(sorted_scores, target)   
                if position is not None:        
                    print(f"   Result: Score {target} found at position {position} with {comparisions} comparisons.")
                else:
                    print(f"   Result: Score {target} not found after {comparisions} comparisons.")
                again = input("Do you want to try again? (y/n): ").strip().lower()
                if again != "y":    
                    break
            another = input("Would you like to perform another search? (y/n): ").strip().lower()
            if another != "y":      
                print("Thank you for using the search program!")
                break
            elif choice == "3":
                print("Exiting program. Thank you for using the search program!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")

Menu()  
