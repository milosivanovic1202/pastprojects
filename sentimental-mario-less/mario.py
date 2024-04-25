from cs50 import get_int

x = get_int("What height do you want the pyramids to be? ")

while x < 1 or x > 8:
    print("Error : allowed height is from 1 to 8.")
    x = get_int("What height do you want the pyramids to be?")

# x = 3 -> range(x) can be 0,1,2 but not 3!
for i in range(x):
    # print(f"{i}, {x}")
    # for j in range(x):
    print(" " * (x - i - 1), end="")
    print("#" * (i + 1))
    # print("#" * (i+1),"b" * (i+1) )
