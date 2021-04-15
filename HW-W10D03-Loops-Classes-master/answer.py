disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
for i in disney_characters:
    if "u" in i:
        print(i, "U are so Uniquely U!")
    elif "i" in i:
        print(i,"I bet you're Impressively Intelligent!")
    elif "o" in i:
        print(i,"O My! How Original!")
    else :
        print("Ehh, a's and e's are so ordinary.")


temperature = 90

while temperature > 75:
    print(f"the temperature is {temperature} - crank the AC!!")
    temperature -= 3 

if temperature == 75:
        print(f"{temperature}. Ahh, that's better.")