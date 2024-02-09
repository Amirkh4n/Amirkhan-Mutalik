def solve(numheads, numlegs):
    num_chickens = 0
    num_rabbits = 0

    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None, None

if __name__ == "__main__":
    numheads = 35
    numlegs = 94
    chickens, rabbits = solve(numheads, numlegs)
    if chickens is not None and rabbits is not None:
        print(f"Number of chickens: {chickens}")
        print(f"Number of rabbits: {rabbits}")
    else:
        print("No solution found.")
