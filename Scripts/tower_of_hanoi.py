def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        return print("move disk " + str(n) + " from " + source + " to " + destination)
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("move disk " + str(n) + " from " + source + " to " + destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)


tower_of_hanoi(3, "A", "C", "B")