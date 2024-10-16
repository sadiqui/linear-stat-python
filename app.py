import sys
from numpy import polyfit
from scipy.stats import pearsonr

# Read file and parse data into list of integers
def read_data(file):
    with open(file, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    return data

def main(file):
    y = read_data(file)
    x = list(range(len(y)))
    
    # Linear regression
    a, b = polyfit(x, y, 1)

    # Pearson Correlation
    r, _ = pearsonr(x, y)

    print(f"Linear Regression Line: y = {a:.6f}x + {b:.6f}")
    print(f"Pearson Correlation Coefficient: {r:.10f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 app.py <file_name>")
    else:
        main(sys.argv[1])
