def average(*args):
    total = sum(args)
    return total / len(args) if len(args) > 0 else 0

avg = average(2, 4, 6, 8)
print(f"Average: {avg}")
