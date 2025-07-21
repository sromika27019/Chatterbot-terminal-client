# I create a Django management command so I can chat in the terminal.

from django.core.management.base import BaseCommand
from chatterbot import ChatBot               # I import the core ChatBot class
from chatterbot.trainers import ChatterBotCorpusTrainer  # I import the trainer

class Command(BaseCommand):
    help = 'I launch a terminal chat session with ChatterBot.'

    def handle(self, *args, **options):
        # I instantiate my bot with the BestMatch logic adapter
        chatbot = ChatBot(
            'TerminalBot',
            logic_adapters=[
                'chatterbot.logic.BestMatch'
            ]
        )

        # I train the bot on the English corpus (only the first run takes time)
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train('chatterbot.corpus.english')

        # I let the user know how to exit
        self.stdout.write(self.style.SUCCESS(
            'Chat session started — type "exit" or Ctrl-C to quit.'
        ))

        try:
            # I loop forever, reading user input and printing bot responses
            while True:
                user_input = input('You: ')
                # I break out when the user types exit or quit
                if user_input.strip().lower() in ('exit', 'quit'):
                    break
                # I get the bot’s response and print it
                response = chatbot.get_response(user_input)
                self.stdout.write(f'Bot: {response}')
        except (KeyboardInterrupt, EOFError):
            # I handle Ctrl-C / EOF gracefully
            self.stdout.write('\nGoodbye!')
