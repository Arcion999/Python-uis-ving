
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
    def sjekk(self, answer):
        if self.answer == answer:
            return True
        
    def __str__(self):
             return("the correct answer is "+ self.answer)
    

question_prompts = [
    "What pogramming language are you using?\n(a) Python\n(b) Matlab\n(c) Java\n\n",
    "What is the strongest metal?\n(a) steel\n(b) tungsten\n(c) Titanium\n\n",
    "How cold is absolute 0 in celsius?\n(a) -273\n(b) -438\n(c) -157\n\n"    
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        print(question)
        if question.sjekk(answer):
            score += 1
            
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)
