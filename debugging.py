def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Write a number: "))
    print(divisors(num))
    print("program finish")


if __name__ == "__main__":
    run()