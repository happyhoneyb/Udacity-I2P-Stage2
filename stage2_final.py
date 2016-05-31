#This game tests a player's knowledge of world capitals.
#The player will be given a paragraph related to world capitals and asked to fill-in-the blanks.
#There are three levels -- easy, medium, and hard.  Each level has four questions.
#The player has three chances to provide the corrct answer before it will be provided.
#The player may repeat the game once gameplay ends.


def IsCorrect(answer, capital):
    """Return true if player's response is correct."""
    if answer == capital:
        return True
    return False


sentence = " "

def CorrectedSentence(sentence, blank, capital):
    """Return corrected sentence replacing blank with capital."""
    sentence = sentence.replace(blank, capital)
    return sentence

capital = []
blank = ['___1___', '___2___', '___3___', '___4___']
answer = 'nada'


def play_level(sentence, blank, answer, capital):
    """Print corrected sentence for each blank if player answers correctly or after three tries."""
    print sentence
    i = 0
    for number in blank:
        answer = raw_input("Which city is " + str(i+1) +"? ").title()
        t = 1
        while IsCorrect(answer, capital[i]) == False and t < 3:
            print "Try again."
            answer = raw_input("Which city is " + str(i+1) +"? ").title()
            t += 1
        if IsCorrect(answer, capital[i]) == True or t >= 3:
            sentence = CorrectedSentence(sentence, number, capital[i])
            print sentence
        i += 1
    return "Thank you for playing."


def ChooseLevel_Capital(level):
    """Return correct answers used for comparing player's answers based on chosen level of difficulty."""
    if level == 'easy':
        capital = ['Tokyo', 'London', 'Moscow', 'Beijing']
    elif level == 'medium':
        capital = ['Ottawa', 'Jakarta', 'Canberra', 'Brasilia']
    elif level == 'hard':
        capital = ['Abuja','Tallinn','Tegucigalpa','Tashkent']
    else:
        capital = ['Tokyo', 'London', 'Moscow', 'Beijing']
    return capital


def ChooseLevel_Sentence(level):
    """Return fill-in-the-blank quiz to ask player based on chosen level of difficulty.  Choose easy level if level chosen is not understood."""
    if level == 'easy':
        sentence = """ ___1___, the capital of Japan, is the world's largest metropolitan area.
        The capital of Great Britain, ___2___, is also the first city to host the modern Summer Olympic games three times.
        The capital of Russia is ___3___, although at one point before the Russian Revolution of 1917, it had been Saint Petersburg.
        The name ___4___, the capital of China, means "Northern Capital", and is meant to distinguish it from Nanjing, the "Southern Capital" during the Ming Dynasty."""
    elif level == 'medium':
        sentence = """Many Americans do not know that the capital of their northern neighbor Canada is ___1___.
        ___2___, the capital of Indonesia, is nicknamed "the Big Durian", aka the New York City (the Big Apple) of Indonesia.
        Many outside Australia think that its capital is Sydney or Melbourne, but it is actually ___3___.
        In 1960, ___4___ became the capital of Brazil; it is a planned city founded specifically for this purpose."""
    elif level == 'hard':
        sentence = """The capital of Nigeria is ___1___ since 1991 and the city was built specifically for that purpose.
        ___2___, the capital of Estonia, boasts the highest number of startups per person in Europe.
        If you're visiting ___3___, the capital of Honduras, be forewarned that it has what is considered one of the most difficult airports in the world to land a plane.
        The capital of Uzbekistan, ___4___, was destroyed by Genghis Khan in 1219 but rebuilt and prospered from the Silk Road."""
    else:
        sentence = """We'll start with the EASY level.
        ___1___, the capital of Japan, is the world's largest metropolitan area.
        The capital of Great Britain, ___2___, is also the first city to host the modern Summer Olympic games three times.
        The capital of Russia is ___3___, although at one point before the Russian Revolution of 1917, it had been Saint Petersburg.
        The name ___4___, the capital of China, means "Northern Capital", and is meant to distinguish it from Nanjing, the "Southern Capital" during the Ming Dynasty."""
    return sentence


def play_game(sentence, blank, answer, capital):
    """Play game of fill-in-the-blanks with capital cities using clues provided.  Prompt user to repeat game when finished."""
    print """Hello.  This game will test your knowledge of world capital cities.  There are three levels of difficulty and four questions per level.  After three wrong answers, the correct answer will be provided.  Please begin by choosing a level."""
    level = raw_input("Which level would you like to play?  Easy, Medium, or Hard?  ").lower()
    capital = ChooseLevel_Capital(level)
    sentence = ChooseLevel_Sentence(level)
    print play_level(sentence, blank, answer, capital)
    again = raw_input("Would you like to play again? Yes or no? ").lower()
    if again == 'yes':
        return play_again(sentence, blank, answer, capital)
    else:
        return "Thank you for playing.  Good bye!"


def play_again(sentence, blank, answer, capital):
    """Repeat the game."""
    return play_game(sentence, blank, answer, capital)


print play_game(sentence, blank, answer, capital)
