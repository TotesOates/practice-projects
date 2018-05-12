import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#Creates 35 different quizzes
for quizNum in range(35):
    quizFile = open('capitalquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquizkey%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\nDate:\n')
    quizFile.write('State Capital Quiz %s' % (quizNum + 1))
    quizFile.write('\n\n')
#shuffles the questions so all quizzes are different
    states = list(capitals.keys())
    random.shuffle(states)
#randomly writes all 50 states on a quiz
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
#randomly places one of the correct capitals in question
    for i in range(4):
        quizFile.write(' %s. %s \n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()

