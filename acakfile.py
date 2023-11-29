def input():
    import random
    file = open('random.txt','w')
    for a in range(1,101):
        value = random.randint(0,400)
        if a != 100:
            file.write(f"{value}\n")
        else:
            file.write(f"{value}")
    file.close()

def output1():
    file2 = open('random.txt','r')
    nums = file2.read()
    gan = 0
    gen = 0
    nol = 0
    global numbers
    numbers = [int(x) for x in nums.split()]
    for x in numbers:
        if x % 2:
            gan += 1
        elif x == 0:
            nol += 1
    gen = 100 - gan - nol
    file2.close()

    file4 = open('outputrandom.txt','w')
    file4.write(f"|----------------|--------|\n")
    file4.write(f"| jenis bilangan | Jumlah |\n")
    file4.write(f"| ganjil         | {gan}     |\n")
    file4.write(f"| genap          | {gen}     |\n")
    file4.write(f"| nol            | {nol}      |\n")
    file4.write(f"|----------------|--------|\n")
    file4.close()

def output2():
    file3 = open('sortedrandom.txt','w')
    c = sorted(numbers)
    n = 0
    for j in range(1,101):
        k = 0
        for b in c:
            if k == n:
                if j != 100:
                    file3.write(f"{b}\n")
                else:
                    file3.write(f"{b}")
            k += 1
        n += 1
    file3.close()
    

input()
output1()
output2()