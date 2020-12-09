def counter():
    counter.count += 1
    return counter.count


counter.count = 0

if __name__ == "__main__":
    print(counter())
    print(counter())
