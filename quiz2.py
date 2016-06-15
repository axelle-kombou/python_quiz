# The following function uses the if statement to check if word is in sentence and returns true if it is the case, else returns false.
def word_in_sentence(sentence, word):
    if word in sentence:
        return True
    return False


# The following function displays the correct paragraph according to the chosen level
def get_sentence_level(level):
    if(level == 'easy'):
        return  '''The language __1__ has been an object-oriented language since it existed. So we can define __2__ to perform
a specific action. There are many built-in __2__  such as __3__ which allows to display on the screen.
To define a function you begin with the keyword __4__ .
'''
    elif(level == 'medium'):
        return '''A  __1__ in python is a sequence of characters. it is defined either with a __2__ quote or a double quotes.
However if you wish to have your__1__ span multiple lines you will need to use __3__ quotes. Creating a __1__ is
as simple as assigning a value to a __4__.
'''
    else:
        return '''In general, __1__ are executed sequentially: The first statement in a function is executed first,
followed by the second, and so on. There may be a situation when you need to __2__ a block of code several
number of times. A __3__ statement allows us to execute a statement or group of statements __4__ times.
'''

# The following function returns the correct answer for the corresponding level
def get_answers_level(level):
    if level == 'easy':
        return ['python', 'functions', 'print', 'def']
    elif level == 'medium':
        return ['string', 'single', 'triple', 'variable']
    else:
        return ['statements', 'execute', 'loop', 'multiple']


# The following function returns the correct introduction for each level printed before the actual test paragraph begins
def intro(level):
    if level == "easy":
            return '''You've chosen easy!

        You will get 5 guesses per problem
        '''
    elif level == "medium":
            return '''You've chosen medium!

        You will get 5 guesses per problem
        '''
    elif level == "hard":
            return '''You've chosen hard!

        You will get 5 guesses per problem
        '''

# The following function validates the level choice that the user inputs
def get_level():
    level = raw_input('''Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.
     ''')
    while level != 'easy' and level != 'medium' and level != 'hard':
        level = raw_input('''That's not an option!
Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.
 ''')
    print intro(level)
    return level

# the following function is the main one and it first display the sentence as long as the amount of try is less than 5.
# then it asks for the user answer
# if that answer is correct it replaces the question by their input
# if it's not correct we give them 5 tries
def guess_sentence(level, questions, sentence, answers):
    user_answer = ""
    i = 0
    end_game = False
    while(i < len(questions) and end_game == False):
        if(word_in_sentence(sentence[0], questions[i])):
            print sentence[0]
            user_answer = raw_input('Enter answer for ' + questions[i] + ' : ')
# if that answer is correct it replaces the question by their input
            if (user_answer == answers[i]):
                sentence[0] = sentence[0].replace(questions[i], user_answer)
                print '''Correct!
                '''
# if not correct we give them 5 tries
            else:
                end_game = check_bad_answer(sentence, questions[i], answers[i])
        i = i + 1

# This function gives the user 5 tries of bad answers and return correct if the user happens to enter the correct answer.

def check_bad_answer(sentence, question, answer) :
    nbr_try = 1
    while word_in_sentence(sentence[0], question) == True and nbr_try <= 5:
        nbr_try = nbr_try + 1
        print '''Try again!
        '''
        print sentence[0]
        user_answer = raw_input('Enter answer for ' + question + ' : ')
        if (user_answer == answer):
            sentence[0] = sentence[0].replace(question, user_answer)
            print '''Correct!
            '''
        if (nbr_try >= 5):
            return True
    return False



questions = ['__1__', '__2__', '__3__', '__4__']
level = get_level()
sentence = [get_sentence_level(level)]
answers = get_answers_level(level)


guess_sentence(level, questions, sentence, answers)






