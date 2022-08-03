"""
Create a knowledge trivia game called Bamboozled. First greet the user and explain the rules of the game.
Then ask the user series of 5 questions and store the information whether the answer was correct or not.
A the end of the game, return how many answers were correct and what prize the user won based on the number of
correct answers. For example: 0 correct answers - nothing, you got Bamboozled, 1 - a meatball sandwich, 2 - a pizza,
3 - a new pair of jeans, 4 - a Wacky Wango Card (a free ticket to try the trivia again), 5 - a Porsche.
"""
print("Welcome to 'Bamboozled' trivia game. Answer 5 questions and get a chance to win cool prizes.")
correct_answers = 0
answer_1 = input("1. How many symphonies did Beethoven compose?\n a) 9\n b) 10\n c) 11\n d) 12\nAnswer: ")
if answer_1 == "a":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'a'")
          
answer_2 = input("2. Which of the following disorders is the fear of being alone?\n a) Arachnophobia\n b) Acrophobia\n c) Agoraphobia \n d) Aerophobia\nAnswer: ")
if answer_2 == "c":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'c'")
    
answer_3 = input("3. What is the speed of sound?\n a) 120 km/h\n b) 1,200 km/h\n c) 400 km/h\n d) 700 km/h\nAnswer: ")
if answer_3 == "b":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'b'")
          
answer_4 = input("4. What do we call a newly hatched butterfly?\n a) A moth\n b) A butter\n c) A caterpillar\n d) A chrysalis\nAnswer: ")
if answer_4 == "c":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'c'")
    
answer_5 = input("5. The phrase: ”I think, therefore I am” was coined by which philosopher?\n a) Socrates\n b) Plato\n c) Aristotle\n d) Descartes\nAnswer: ")
if answer_5 == "d":
    correct_answers += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'd'")
 
congratulations = "The number of correct answers is {}. You won {}."         
if correct_answers == 5:
    print(congratulations.format(correct_answers,"a vacation to the moon"))
elif correct_answers == 4:
    print(congratulations.format(correct_answers,"an iPhone"))
elif correct_answers == 3:
    print(congratulations.format(correct_answers,"a meal in a restaurant of your choice"))
elif correct_answers == 2:
    print(congratulations.format(correct_answers,"a chocolate"))
elif correct_answers == 1:
    print(congratulations.format(correct_answers,"a candy"))
else:
    print(congratulations.format(correct_answers,"nothing"))

    