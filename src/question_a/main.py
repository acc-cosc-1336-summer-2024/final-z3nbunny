#add import
from question_a import create_multiplication_table, display_multiplication_table

def multiplication_loop():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        cont = input("Keep generating? (y/n): ").strip().lower()
        if cont != 'y':
            break

multiplication_loop()