import random


words = [
    {"french": "bonjour", "english": "hello"},
    {"french": "merci", "english": "thank you"},
    {"french": "oui", "english": "yes"},
    {"french": "non", "english": "no"},
    {"french": "s'il vous plaît", "english": "please"},
    {"french": "excusez-moi", "english": "excuse me"},
    {"french": "pardon", "english": "sorry"},
    {"french": "au revoir", "english": "goodbye"},
    {"french": "salut", "english": "hi"},
    {"french": "bien", "english": "well"},
    {"french": "mal", "english": "badly"},
    {"french": "très", "english": "very"},
    {"french": "peu", "english": "little"},
    {"french": "plus", "english": "more"},
    {"french": "moins", "english": "less"},
    {"french": "ici", "english": "here"},
    {"french": "là", "english": "there"},
    {"french": "je", "english": "I"},
    {"french": "tu", "english": "you (singular informal)"},
    {"french": "il", "english": "he"},
    {"french": "elle", "english": "she"},
    {"french": "nous", "english": "we"},
    {"french": "vous", "english": "you (plural or formal)"},
    {"french": "ils", "english": "they (masculine)"},
    {"french": "elles", "english": "they (feminine)"},
    {"french": "être", "english": "to be"},
    {"french": "avoir", "english": "to have"},
    {"french": "faire", "english": "to do"},
    {"french": "aller", "english": "to go"},
    {"french": "dire", "english": "to say"},
    {"french": "pouvoir", "english": "can"},
    {"french": "vouloir", "english": "to want"},
    {"french": "savoir", "english": "to know"},
    {"french": "voir", "english": "to see"},
    {"french": "demander", "english": "to ask"},
    {"french": "parler", "english": "to speak"},
    {"french": "prendre", "english": "to take"},
    {"french": "mettre", "english": "to put"},
    {"french": "donner", "english": "to give"},
    {"french": "devoir", "english": "must"},
    {"french": "venir", "english": "to come"},
    {"french": "passer", "english": "to pass"},
    {"french": "croire", "english": "to believe"},
    {"french": "aimer", "english": "to love"},
    {"french": "falloir", "english": "to have to"},
    {"french": "trouver", "english": "to find"},
    {"french": "laisser", "english": "to leave"},
    {"french": "penser", "english": "to think"},
    {"french": "regarder", "english": "to watch"},
    {"french": "arriver", "english": "to arrive"},
    {"french": "appeler", "english": "to call"},
    {"french": "partir", "english": "to leave"},
    {"french": "utiliser", "english": "to use"},
    {"french": "finir", "english": "to finish"},
    {"french": "manger", "english": "to eat",}

]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['french']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()