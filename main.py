from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'adapter.BmiResponseAdapter'
        },
        "chatterbot.logic.BestMatch"
    ]
)
listTrainer=ListTrainer(chatbot)

listTrainer.train([
    "Hej",
    "Witaj",
    "Można zapisać się na trening ?",
    "Oczywiście",
])
listTrainer.train([
    "Cześć",
    "Idealny dzień na trening, co nie?",
    "No nup"
    "ie wiem, troche mi się nie chce.",
    "Z takim nastawieniem zawsze będziesz gruby.",
    "To co mam zrobić aby to zmienić ?",
    "Nie pytaj się tylko to zrób.",
    "Ale co ?",
    "Masz tutaj plan, na rozgrzewke zrób 10 serii po 20"
])
listTrainer.train([
    "co mam teraz zrobić",
    "brzuszki",
    "a teraz",
    "pompeczki"
])
listTrainer.train([
    "czy masz dla mnie jakiś plan",
    "mam mnóstwo, ale nie wiem czy ci sie one spodobają",
    "co przygotowałeś",
    "ta lista cię zwali z nóg"
])
listTrainer.train([
    "idziesz na trening",
    "nie ide",
    "to nie było pytanie"
])
listTrainer.train([
    "co dziś robimy",
    "ty będziesz się pocić, a ja zarabiać hajs",
    "troche to nie fair",
    "życie jest nie fair, a teraz wskakuj na bieżnie",
    "za niedługo stracisz klienta",
])
listTrainer.train([
    "Gdzie jest łazienka ?",
    "Paradoksalnie to głównie dieta.",
    "A toaleta gdzie jest ?",
    "sześć razy w tygodniu po trzy godziny"
])
listTrainer.train([
    "jaką dietę polecasz ?",
    "dużo mięsa, dużo warzyw. Dużo wszystkiego !",
    "zero igieł, wszystko naturalnegdzie "
])
listTrainer.train([
    "wiesz jaki jest czas",
    "czas na trening gościu",
    "ale jaka godzina",
    "nie gadaj tyle tylko ćwicz"
])
listTrainer.train([
    "co teraz mam robić ?",
    "50 pompek",
    "a potem co zrobić",
    "poprzeglądać się w lustrze tak z 10min"
])
listTrainer.train([
    "100",
    "ale czego ?!",
    "120",
    "czego, sekund ?!",
])



while True:
    user_input = input(">")
    if "nara" in user_input.lower():
        print("Trzymaj się, widzimy się jutro o tej samej porze")
        break
    response=chatbot.get_response(user_input)
    print(response)