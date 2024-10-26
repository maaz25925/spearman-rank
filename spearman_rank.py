import pandas as pd

# Input X & Y
X = list(map(int, input("Enter X: ").split()))
Y = list(map(int, input("Enter Y: ").split()))

# Create DataFrame
dataFrame = pd.DataFrame({"X": X, "Y": Y})

# Add ranking and difference columns
dataFrame["R1"] = dataFrame["X"].rank()
dataFrame["R2"] = dataFrame["Y"].rank()
dataFrame["D=R1-R2"] = dataFrame["R1"] - dataFrame["R2"]
dataFrame["D^2"] = dataFrame["D=R1-R2"] ** 2

print(dataFrame.to_string(index=False))
print("N:", dataFrame.shape[0])
print("∑D^2:", dataFrame["D^2"].sum())

# Calculate repeated values in R1 & R2
repeatedValuesInR1 = [x for x in dataFrame["R1"].value_counts() if x > 1]
repeatedValuesInR2 = [x for x in dataFrame["R2"].value_counts() if x > 1]

# Calculate tie correction for R1 and R2
correction_r1 = sum((m**3 - m) for m in repeatedValuesInR1) / 12
correction_r2 = sum((m**3 - m) for m in repeatedValuesInR2) / 12

# Spearman's rho formula
n = dataFrame.shape[0]
sum_d_squared = dataFrame["D^2"].sum()

if repeatedValuesInR1 or repeatedValuesInR2:
    # Display repeated values and their counts
    mCount = 1
    for value in repeatedValuesInR1 + repeatedValuesInR2:
        print(f"m{mCount} = {value}", end=", " if mCount < len(repeatedValuesInR1) + len(repeatedValuesInR2) else "\n")
        mCount += 1

    # Print the modified formula for rho with repeated values
    print("R = 1 - (6(∑D^2", end="")
    for i in range(1, len(repeatedValuesInR1) + len(repeatedValuesInR2) + 1):
        print(f" + (1/12)(m{i}^3 - m{i})", end="")
    print(") / (N^3 - N))")

    # Substitute and print the formula with actual values
    print(f"R = 1 - (6({sum_d_squared}", end="")
    for x in repeatedValuesInR1:
        print(f" + (1/12)({x}^3 - {x})", end="")
    for y in repeatedValuesInR2:
        print(f" + (1/12)({y}^3 - {y})", end="")
    print(f") / ({n}^3 - {n}))")

    # Calculate R with the correction terms in the numerator
    r = 1 - (6 * (sum_d_squared + correction_r1 + correction_r2) / (n**3 - n))
    print(f"R = {r}")
else:
    print("No repeated values found.")
    # Formula without tie correction
    print("R = 1 - (6(∑D^2) / (N^3 - N))")
    print(f"R = 1 - (6({sum_d_squared}) / ({n}^3 - {n}))")
    
    # Calculate R without tie correction
    r = 1 - (6 * sum_d_squared / (n**3 - n))
    print(f"R = {r}")
