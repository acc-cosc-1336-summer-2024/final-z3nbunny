#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table():
    multiplication_table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        multiplication_table.append(row)
    return multiplication_table

def display_multiplication_table(multiplication_table):
    for row in multiplication_table:
        row_string = ""
        for value in row:
            row_string += str(value) + " "
        print(row_string.strip())