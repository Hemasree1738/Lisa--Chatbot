import random

jokes = [
    ("Why did the solar panel go to school?", "Because it wanted to be brighter! 💡"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs! 🐛"),
    ("Why did the computer go to the doctor?", "Because it had a virus! 🤒"),
    ("What do you call a fish without eyes?", "A fsh! 🐟"),
    ("Why can't your nose be 12 inches long?", "Because then it would be a foot! 👃"),
]
name = input("Before we start, What is your name: ")
print(f"Hello {name}, I'm Lisa")
print("How may I help you today!")

choice = 1
while(choice == 1):
    user_command = input("enter your response: ")
    words = user_command.split(" ")
    for word in words: 
        if(word.lower() == "hello" or word.lower()=="how"):
            print(f"I am fine. Glad you asked {name}!❤️\n")
            print("How are you doing ? 😊")
            break
        elif(word.lower() == "bye"):
            print("It was nice talking to you. Come for help!")
            choice = 0
            break
        elif "not fine" in user_command.lower() or "sad" in user_command.lower():
            print("Sorry to hear that, Do you want to hear a joke to pump your mood")
            user_command = user_command = input("enter your response: ")
            wrds = user_command.split(" ")
            for wrd in wrds:
                if(wrd.lower() == "yes"):
                    joke = random.choice(jokes)
                    print(joke)
                elif(wrd.lower() == "no"):
                    print("Okay!")
                    break
        elif(word.lower() == "time"):
            import datetime
            now = datetime.datetime.now()
            print(f"Now, the time is {now.strftime('%H:%M')}")
            break
        elif word.lower() == "age":
            print("I am a chatbot so I don't have an age! 😄")
            break
