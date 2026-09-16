#generate the random password ...
import random
sma_le = random.sample("abcdef",2)
cap_le =random.sample("ABCDEF",2)
numb = random.sample("123456",2)
spec = random.sample("@#$",2)

password = []
password.extend(sma_le)
password.extend(cap_le)
password.extend(numb)
password.extend(spec)
random.shuffle(password)
print("".join(password))
