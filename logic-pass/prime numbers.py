start_number = int(input("enter the start of the range: "))
end_number = int(input("enter the end of the range: "))

prime_numbers = []
is_prime = bool

for i in range(start_number, end_number + 1):
    is_prime = True
    if (i == 1):
        continue
    else:
        for j in range(2 , i):
            if i == 2:
                break
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)


print(prime_numbers) 
