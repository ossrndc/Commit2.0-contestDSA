# Max Triangle Problem - Python Solution

def main():
    # Read the number of test cases
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        # Check if it's possible to form a non-degenerate triangle
        if N < 3:
            print(-1)
        else:
            # Try to form a triangle with the largest three sticks: N, N-1, and N-2
            if N - 1 + N - 2 > N:
                print(N + (N - 1) + (N - 2))  # The perimeter of the largest valid triangle
            else:
                print(-1)  # No valid triangle can be formed with these sticks

# Call the main function
if __name__ == "__main__":
    main()
