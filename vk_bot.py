
from rutermextract import TermExtractor
import krTime


class VKan:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id

        self._COMMANDS = ["ПРИВЕТ", "ПОКА", "АНАЛИЗ", 'НАЧАТЬ']


    def analiz(self,message):

        if message.upper() == self._COMMANDS[0]:
            return f"Данный бот создан для отбора ключевых слов из вашего будущего поста для упрощения составления хэштегов, пожалуйста введите команду 'анализ' для дальнейших инструкций!"

        # Пока
        elif message.upper() == self._COMMANDS[1]:
            return f"До свидания!"

        if   message.upper() == self._COMMANDS[2]:
            return f"Пришли мне текст для анализа"
        elif message.upper() != self._COMMANDS[2]:
            term_extractor = TermExtractor()
            text = message
            with open('2.txt', 'w') as ikar:
                ikar.write(f'Наиболее подходящее время публикацции в часах:{krTime.time} \n Вот ваши ключевые слова для поста:\n')
                for term in term_extractor(text):
                    ikar.write(term.normalized)
                    ikar.write('\n')
            with open ('2.txt') as lar:
                return lar.read(),

        else:
            return f'Не заню'
