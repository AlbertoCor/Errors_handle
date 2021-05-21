def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Write a number: "))
        if num == 0:
            raise ValueError
        print(divisors(num))
        print("program finish")
    except ValueError:
        print("Introduce a number diferent from 0 or another number and try again >:V")


if __name__ == "__main__":
    run()