"""
https://www.reddit.com/r/learnpython/comments/pz03ci/having_trouble_still_new/
"""

# Phase One - Input

# Read 10 values
READ_COUNT = 10

source = []
for i in range(READ_COUNT):
    value = float(input(f"Temperature for day {i} [in °C]: "))
    source.append(value)

# Print the entire array
print(f"List of temperatures in °C:")
for each_item in source:
    print(each_item, end="  ")
print()


# Phase two - Data processing, i.e. conversion
fahr = []
# Since we want to process each item in the source,
# we use another for loop.
for each_item in source:
    new_value = each_item * 1.8 + 32.0  # Convert to Fahrenheits
    fahr.append(new_value)

# Print the entire array
print(f"List of temperatures °F:")
for each_item in fahr:
    print(each_item, end="  ")
print()


# Phase Three - Count cold, warm and hot days

# Since we should decide the thresholds, let's do it now:
# - cold < 8°C
# - warm <= 24°C
# - hot > 24°C
# I use degrees of Celsius as these are used in my country.

THRESHOLD_COLD = 8.0
THRESHOLD_HOT = 24.0

stats = [0, 0, 0]   # A list to count number of occurences of cold, warm, hot
for each_item in source:
    if each_item < THRESHOLD_COLD:
        stats[0] += 1
    elif each_item > THRESHOLD_HOT:
        stats[2] += 1
    else:
        stats[1] += 1

# Print the result
    words = ["cold", "warm", "hot"]
    for i in range(len(stats)):
        print(f"Number of {words[i]} days:  {stats[i]}")
