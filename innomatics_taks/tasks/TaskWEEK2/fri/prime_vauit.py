while True:

    user_input = int(input("Enter a passkey (Prime Number above 10): "))
    if user_input <= 10:
        print("Passkey must be greater than 10!")
        continue
    count = 0
    for i in range(1, user_input + 1):
        if user_input % i == 0:
            count += 1
    if count == 2:
        print("Vault unlocked!")
        for i in range(user_input, 0, -1):
            print(i)
        break
    else:
        print("Not a prime number")