def apply_operation(value, operation):
    if operation == '@':
        return value * 3
    elif operation == '%':
        return value + 5
    elif operation == '#':
        return value - 7


def process_math_expression(expression):
    parts = expression.split()
    value = float(parts[0]) 
    operations = parts[1:]   
    
    for op in operations:
        value = apply_operation(value, op)
    
    return f"{value:.2f}"  

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        result = process_math_expression(data[i])
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
