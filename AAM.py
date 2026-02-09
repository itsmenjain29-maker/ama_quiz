#--> We can later add age restriction and age verfication to use this quiz bot
#Assuming the user cooperates :)
#Ask about me
def methods(text):
    return text.strip().title()

print("Hello! User, Welcome to AAM.")

name = input("So User, what do you want me to call you? ")
name = methods(name)

print(f"Hello! {name}.")
print("Let's start the AAM.")

#Q1
hobby = input("Q. What is your hobby? ")
hobby = methods(hobby)

print(f"So your hobby is {hobby}. Interesting...")
print("Your next question is-")

#Q2
subject = input("Q. What is your favourite subject? ")
subject = methods(subject)

print(f"{subject} is an interesting subject.") 
print("So your next question is-")

#Q3
num = input("Q. What is your favourite number? ")
num = int(num.strip())

print(f"Oh! My favourite number is also {num}.")

#Maths Ques
print("Now some Maths questions! Use calculator only for addition.")

#Q4
input("What's 22*11+3969? ")
x = float(input("x = "))
y = float(input("y = "))
print(f"answer: {x + y:.2f}")

print(f"Thanks for playing this game, {name}.")
rating = input("How much would you like to rate us out of 5 star? ")

print(f"{rating}/5 star. Thanks for your valuable feedback.")