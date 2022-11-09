from chatterbot.logic import LogicAdapter
import re

class BmiResponseAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.waga = 0
        self.wzrost = 0

    def can_process(self, statement):
        wzrost_reg2 = re.compile(r'((mam)\s*(\d+[,\.]?\d*))|(\d+[,\.]?\d*)\s*(wzrostu|wysokości|cm|m)', re.I)
        waga_reg = re.compile(r'((ważę|waże)\s+\d+)|(\d+\s*kg)', re.I)

        wzrost = wzrost_reg2.search(statement.text)
        waga = waga_reg.search(statement.text)

        if re.search(r'bmi', statement.text, re.I):
            return True

        if waga != None:
            waga_str = re.search(r'\d+', waga.group())
            self.waga = int(waga_str[0])

        if wzrost != None:
            wzrost_str = re.search(r'\d+[,\.]?\d*', wzrost.group()).group()
            wzrost_str = wzrost_str.replace(',', '.')
            self.wzrost = float(wzrost_str)

        if waga != None or wzrost != None:
            print('waga: {}, wzrost: {}'.format(self.waga, self.wzrost))
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement

        if self.waga == 0:
            return Statement(text='ile ważysz ?')
        if self.wzrost == 0:
            return Statement(text='ile masz wzrostu ?')
        if self.wzrost >10:
            self.wzrost /= 100

        bmi = self.waga / (self.wzrost * self.wzrost)
        bmi = bmi.__round__(2)


        self.wzrost = 0
        self.waga = 0

        if bmi < 18.5:
            rezultat = 'Musisz jeść więcej'
        elif bmi <25:
            rezultat = 'Jesteś w normie'
        elif bmi <23:
            rezultat = 'Przydało by się schudnąć'
        elif bmi <35:
            rezultat = 'Łooo panie, marsz na siłke'
        else:
            rezultat = 'RIP twoje serducho'

        return Statement(text='{}. Twoje bmi wynosi {}'.format(rezultat, bmi ))
