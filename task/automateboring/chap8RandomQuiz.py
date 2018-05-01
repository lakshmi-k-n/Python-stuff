import random

capitals = {'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())


for numm in range(len(capitals)):

    quizdata = open('capitalsquiz%s.txt' % (numm +1), 'w')
    file1 = open('capitalquiz_answers%s.txt' % (numm +1), 'w')
    quizdata.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (numm +1))
    quizdata.write('\n\n')

   
    states = list(capitals.keys())
    random.shuffle(states)

    
    for qnum in range(50):
        
        Trueans = capitals[states[qnum]]
        Falseans = list(capitals.values())
        del Falseans[Falseans.index(Trueans)]
        Falseans = random.sample(Falseans, 3)
        options = Falseans + [Trueans]
        random.shuffle(options)

  
        quizdata.write('%s. What is the capital of %s?\n' % (qnum + 1, states[qnum]))
        for i in range(4):
            quizdata.write('    %s. %s\n' % ('ABCD'[i], options[i]))
        quizdata.write('\n')

        file1.write('%s. %s\n' % (qnum + 1, 'ABCD'[options.index(Trueans)]))

    quizdata.close()
file1.close()
