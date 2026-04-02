def outer(x):
    print("Enter Outer function")
    
    def inner(y):
        print("Enter Inner function")
        return x + y

    print("Exit Outer function")
    return inner

print(outer(1)(2))


# MECHANISM

"""
    1. Call outer(1) -> Prints "Enter Outer function"
    2. Define inner(y) -> Python saves x=1 into inner's closure
    3. Finish outer() -> Prints "Exit Outer function"
    4. Return inner function -> The function inner is handed back to the main code
    5. Call inner(2) -> Prints "Enter Inner function"
    6. Calculate x+y -> Uses the "remembered x=1" and the new y=2
    7. Return 3
"""