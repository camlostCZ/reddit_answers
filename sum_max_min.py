"""
https://www.reddit.com/r/learnpython/comments/q2dlme/need_help_with_a_practice_problem/
"""

# Ask the user how many test scores they would like to enter.
answer = input("How many test scores you want to enter? ")
count = int(answer)     # Since input() returns a string, we need to convert it to an int

total = 0     # We have added 0 scores so far
mini = None  # Let's use some special value
maxi = None  # Let's use some special value

for each in range(count):
    # Repeat this code
    answer = input("Enter a score: ")
    score = int(answer)     # Again, convert string to int

    # Compute total + score and store it in sum again.
    # This increases sum by score, in fact.
    total = total + score
    print(f"DEBUG: sum = {total}")

    # If mini hasn't been set yet (has a special value)
    # or if score is lesser than mini, update mini:
    if mini == None or score < mini:
        mini = score
        print(f"DEBUG: mini updated to {mini}")

    # The same for maxi:
    if maxi == None or score > maxi:
        maxi = score
        print(f"DEBUG: maxi updated to {maxi}")

# After all score entered, let's print the result:
print(f"\nSum:     {total}")
print(f"Average: {total / count}")
print(f"Minimum: {mini}")
print(f"Maximum: {maxi}")
