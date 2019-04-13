import random


def dis():
    print("you'll be taught addition for today")


def gen():
    firstno = random.randint(1, 10)
    secondno = random.randint(1, 10)
    return [firstno, secondno]


def add(firstno, secondno):
    return firstno + secondno


def getcheck(result):
    answer = int(input("what is the answer"))
    while True:
        if answer == result:
            print("correct")
            break
        print("Incorrect")
        answer = int(input("what is the answer"))

    # print("the answer is {}".format(result))


def main():
    dis()
    while True:
        randomlist = gen()
        result = add(randomlist[0], randomlist[1])
        print(randomlist[0], " + ", randomlist[1], " = ___")
        check = getcheck(result)


main()
