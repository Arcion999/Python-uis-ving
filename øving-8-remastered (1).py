class Questions:
    def __init__(self, question:str, answer:int, choice:list):
        self.question = question
        self.answer = answer
        self.choice = choice
    
    def control(self, answer):
        return answer -1 == self.answer
    
    def __str__(self):
        return f"{self.question} \n 0: {self.answer[0]} \n 1: {self.choice[1]}"\
             f"\n 2: {self.choice[2]} \n 3: {self.choice[3]}"
    
    def korrekt_svar_tekst(self, riktig_svar):
        return f"Riktig svar er {self.riktig_svar}"
    
def hent_sporsmaal():
    liste_spor = []
    with open("sporsmaalsfil.txt", "r", encoding= "UTF-8") as fila:
        for linje in fila:
            linje = linje.split(":")
            
            question = linje[0]
            answer = int(linje[1])
            choice = linje[2]
            
            choice = choice.strip("[\n] ")
            choice = choice.split(",")
            
            spor = Questions(question, answer, choice)
            
            liste_spor.append(spor)
    
    return liste_spor


score_1 = 0
score_2 = 0


if __name__=='__main__':
    x = hent_sporsmaal()
    teller = 0
    
    for i in x:
        print(i)
        svar_1 = int(input("Spiller 1: "))
        svar_2 = int(input("Spiller 2: "))
        print()
        print(f"Riktig svar er {i.Correct}.")
        
        if i.control(svar_1):
            score_1 += 1
            print("Spiller 1: Riktig!")
        else:
            print("Spiller 1: Feil")
        
        if i.control(svar_2):
            score_2 += 1
            print(svar_2)
            print("Spiller 2: Riktig!")
        else:
            print("Spiller 2: Feil")
        print()
        print()


print(f"Spiller 1: score{score_1}")
print(f"Spiller 2: score{score_2}")
