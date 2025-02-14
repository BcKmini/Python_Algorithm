def get_change(cents):
    quarters = cents // 25 
    cents %= 25
    dimes = cents // 10  
    cents %= 10
    nickels = cents // 5  
    cents %= 5
    pennies = cents 
    
    return f"{quarters} {dimes} {nickels} {pennies}"

T = int(input()) 
for _ in range(T):
    C = int(input()) 
    print(get_change(C))