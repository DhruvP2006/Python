numbers = [1, -2, 3, 4, -5, 6, 0, 7, 8]

for num in numbers:
    if num < 0:  
        continue  
    if num == 0:  
        print("Encountered zero, exiting the loop.")
        break  
    print(f"Odd number: {num}" if num % 2 != 0 else f"Even number: {num}")
