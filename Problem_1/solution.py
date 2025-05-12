# Function to calculate number of notebooks
def count_notebooks(pulp_weight):
    pages = pulp_weight * 1000  # 1 kg pulp makes 1000 pages
    notebooks = pages // 100  # 1 notebook consists of 100 pages
    return notebooks

# Number of test cases
T = int(input())  

# Process each test case
for _ in range(T):
    N = int(input())  # Weight of pulp in kg
    print(count_notebooks(N))