# On his eighteenth birthday, Jose decided he was going to move out and live in a boarding house. He packed his luggage in boxes and found a suitable ad for an apartment for rent. He starts carrying his luggage in parts because he can't do it all at once. He has limited free space in his new home where he can arrange things so that the place is livable.
# Write a program that calculates the free volume of Jose's apartment that remains after he has moved his luggage.
# Each carton has exact dimensions: 1m x 1m x 1m.
# Login
# The user enters the following data on separate lines:
# 1. Width of free space - integer;
# 2. Length of free space - integer;
# 3. Height of free space - integer;
# 4. On the next lines (until the "Done" command is received) - number of boxes that are transported to the accommodation - whole numbers
# The program should finish reading data on a "Done" command or if free space runs out.
# Exit
# Print one of the following lines to the console:
# - If you get to the "Done" command and there is still free space:
# "{number of free cubic meters} Cubic meters left."
# - If free space runs out before the "Done" command is received:
# "No more free space! You need {number of missing cubic meters} Cubic meters more."

width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
used_volume = 0
boxes_count = 0
while True:
    command = input()
    if command == "Done":
        break
    else:
        boxes_count += 1
        used_volume += int(command)
    if used_volume > total_volume:
        print(f"No more free space! You need {used_volume - total_volume} Cubic meters more.")
        exit()
remaining_volume = total_volume - used_volume
print(f"{remaining_volume} Cubic meters left.")
