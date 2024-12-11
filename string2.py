s = "I am a student"
print(len(s))

s = "I am a student"
print(s.replace('student', 'teacher'))

address = "123 suhana apt, marathali, Bangalore"
print(address)
print(address.replace("apt", "Apartment"))

text = "BRB, TTYL, LOL"
print(text.replace("BRB", "Be right back").replace("TTYL", "talk to you letter").replace("LOL", "Laughing out loud"))

text = "Hello, World"
print(text.lower())
print(text.upper())
print(text.title())

text1 = "I am A Student"
print(text1.swapcase())
print(text1.capitalize())

sentence = "I am a student at azad"
print("am" in sentence)

sentence = "I am a student at azad"
search_word = "am"
if search_word in sentence:
    print("The search word is present")
else:
    print("Not")
    
username = "Shyam"
greeting = f"hello {username}, how are you?"
print(greeting)