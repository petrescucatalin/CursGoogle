def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    while True:
        operation = input("Introdu operatia (+, -, *, /, C sa stergi sau Q sa inchizi): ").strip().lower()

        if operation == 'q':
            print("Se inchide.")
            break

        if operation == 'c':
            print("Curatat.")
            continue

        if operation not in ('+', '-', '*', '/'):
            print("Operatie invalida. Incearca iar.")
            continue

        num1 = float(input("Primul nr: "))
        num2 = float(input("Al doilea nr: "))

        if operation == '+':
            print(f"Rezultat: {add(num1, num2)}")
        elif operation == '-':
            print(f"Rezultat: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Rezultat: {multiply(num1, num2)}")
        elif operation == '/':
            if num2 == 0:
                print("Nu se poate imparti la 0.")
            else:
                print(f"Rezultat: {divide(num1, num2)}")


if __name__ == "__main__":
    calculator()
