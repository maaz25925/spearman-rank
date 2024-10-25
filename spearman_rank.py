import pandas as pd

# Input X & Y
X: list[int] = list(map(int, input("Enter X: ").split()))
Y: list[int] = list(map(int, input("Enter Y: ").split()))

# Create DataFrame
# Add X & Y columns
dataFrame: pd.DataFrame = pd.DataFrame({"X": X, "Y": Y})

# Add more columns
dataFrame["R1"] = dataFrame["X"].rank()
dataFrame["R2"] = dataFrame["Y"].rank()
dataFrame["D=R1-R2"] = dataFrame["R1"] - dataFrame["R2"]
dataFrame["D^2"] = dataFrame["D=R1-R2"] ** 2

print(dataFrame.to_string(index=False))
print("N:", dataFrame.shape[0])
print("∑D^2:", dataFrame["D^2"].sum())

# Calculate repeated values in R1 & R2
repeatedValuesInR1: list[int] = [x for x in dataFrame["R1"].value_counts() if x > 1]
repeatedValuesInR2: list[int] = [x for x in dataFrame["R2"].value_counts() if x > 1]

# Calculate R according to the formula
if repeatedValuesInR1 or repeatedValuesInR2:
    mCount = 1
    while mCount <= len(repeatedValuesInR1):
        print(f"m{mCount} = {repeatedValuesInR1[mCount - 1]}", end=", ")
        mCount += 1
    index = 0
    while mCount <= len(repeatedValuesInR1) + len(repeatedValuesInR2):
        print(f"m{mCount} = {repeatedValuesInR2[index]}", end="")
        index += 1
        mCount += 1
        if mCount == len(repeatedValuesInR1) + len(repeatedValuesInR2) + 1:
            print()
        else:
            print(", ", end="")
    # Print formula for R with repeated values
    print("R = 1 - (6(∑D^2", end="")
    # m[i] will be printed as per the number of total values repeated in the rank columns
    for i in range(1, len(repeatedValuesInR1) + len(repeatedValuesInR2) + 1):
        print(f" + (1/12)(m{i}^3 - m{i})", end="")
    print(") / (N^3 - N))")
    print(f"R = 1 - (6({dataFrame['D^2'].sum()})", end="")
    for x in repeatedValuesInR1:
        print(f" + (1/12)({x}^3 - {x})", end="")
    for y in repeatedValuesInR2:
        print(f" + (1/12)({y}^3 - {y})", end="")
    print(f") / ({dataFrame.shape[0]}^3 - {dataFrame.shape[0]}))")
    r: float = 1 - (6 * dataFrame["D^2"].sum() / (dataFrame.shape[0] ** 3 - dataFrame.shape[0]))
    print(f"R = {r}")
else:
    print("No repeated values found")
    # Print formula for R without repeated values
    print("R = 1 - (6(∑D^2) / (N^3 - N))")
    print(f"R = 1 - (6({dataFrame['D^2'].sum()}) / ({dataFrame.shape[0]}^3 - {dataFrame.shape[0]}))")
    r: float = 1 - (6 * dataFrame["D^2"].sum() / (dataFrame.shape[0] ** 3 - dataFrame.shape[0]))
    print(f"R = {r}")
