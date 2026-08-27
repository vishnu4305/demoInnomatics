def hype_man(name,skill):
    print(f"Make some noise for {name}, the absolute master of {skill}!")
hype_man("Alex", "coding")

def check_age(age):
    if age >= 12 :
        print("Enjoy the ride!")
    else:
        print("Sorry, maybe next year.")
check_age(15)
        
def vowel_vacuum(text):
    new_s = ""
    for i in text.lower():
        if i not in "aeiou":
            new_s += i
    print(new_s)
vowel_vacuum("Python is awesome")
            
def calculate_total(cart_prices: list[float]) :
    total = 0
    discount = 10
    for i in cart_prices:
        total += i 
        if total > 100 :
            total -= discount
    print(f"Your total today is {total}")
    

calculate_total([25.50, 40.00, 50.00])
    
def emojify(sentence: str, emoji_dict: dict[str, str]) -> str:
    new_s = ""
    for word in sentence.split():
        if word in emoji_dict:
            new_s += emoji_dict[word] + " "
        else:
            new_s +=word + " "
    print(new_s)
        
emojify("I am so happy to eat pizza and code python",{"happy": "😊", "pizza": "🍕", "python": "🐍"})



def print_shopping_list(recipe1:list[str],recipe2:list[str] ):
    new_s = recipe1 +recipe2
    print(set(new_s))
print_shopping_list(["flour", "sugar",
"eggs"], ["eggs", "butter", "sugar", "vanilla"])


def check_anagram(word1: str, word2: str):

    w1 = sorted(word1.lower().replace(" ", ""))
    w2 = sorted(word2.lower().replace(" ", ""))

    if w1 == w2:
        print("Yes, those are anagrams!")
    else:
        print("Nope, not an anagram.")

check_anagram("Clint Eastwood", "Old West Action")

