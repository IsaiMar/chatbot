from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='Chatbot', read_only=True,
                logic_adapters=
['chatterbot.logic.MathematicalEvaluation',
                                'chatterbot.logic.BestMatch'])

list_trainer = ListTrainer(my_bot)
small_talk = ['hi there',
              'hi!',
              'how do you do',
              'how are you',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'wha\'s your name',
              'My name is Chatbot, ask me a math question.']

math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared']
math_talk_2 = ['2+2',
               '4 ask me a harder one.']
math_talk_3 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']
            
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2, math_talk_3):
        list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')