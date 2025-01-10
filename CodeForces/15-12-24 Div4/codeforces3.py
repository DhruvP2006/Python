t = int(input())  
while t > 0:
    m, a, b, c = map(int, input().split())  
    
    seated_in_row_1 = min(a, m)
    
    seated_in_row_2 = min(b, m)
    
    remaining_seats = 2 * m - (seated_in_row_1 + seated_in_row_2)
    
    seated_without_preference = min(c, remaining_seats)
    
    total_seated = seated_in_row_1 + seated_in_row_2 + seated_without_preference
    
    print(total_seated)
    
    t -= 1 
