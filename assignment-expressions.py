# See: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions

arr = [ 1, 2, 3, 4 ]

if (n := len(arr) ) < 3:
    print("array is too short")

print(f"arr has {n} elements")


