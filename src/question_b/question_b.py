#write functions here, don't add input('') statements here!

def five_numbers():
    numbers = []
    print("Please enter 5 numbers, one at a time each followed by enter")
    for i in range(5):
        get_numbers = int(input("Enter a number: "))
        numbers.append(get_numbers)
    print("Lowest number: " + str(min(numbers)))
    print("Highest number: " + str(max(numbers)))
    total = 0
    for j in range(5):
        total += numbers[j]
    print("Total of the numbers: " + str(total))
    average = total / 5
    print("Average of the numbers: " + str(average))