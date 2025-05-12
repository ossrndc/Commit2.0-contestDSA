# Valentine Day Problem - Python Solution

def main():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        # Read X and Y for each test case
        X, Y = map(int, input().split())
        
        # Calculate and print how many chocolates Ayushman can buy
        print(X // Y)

# Call the main function
if __name__ == "__main__":
    main()