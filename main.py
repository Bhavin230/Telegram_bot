from turtle import update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
# from telethon import TelegramClient
updater = Updater("your_telegram_id",
                  use_context=True)
# api_id = '9974563'
# api_hash ='8e8b8c6029b3fb95d5c4908af0f5122d'
# client = TelegramClient('user', api_id, api_hash).start()

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Welcome to MENTOR TELE BOT
To find Something new press /Ready.""")


def Ready(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
        /help - If want to reach us
        /javaCourse - Java RoadMap
        /1CSE - 1st Semester Course Layout
        /2CSE - 2nd Semester Course Layout
        /3CSE - 3rd Semester Course Layout
        /4CSE - 4th Semester Course Layout
        /5CSE - 5th Semester Course Layout
    """)



def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/youtube - To get the youtube URL
/linkedin - To get the LinkedIn profile URL
/telegramUserName - To get telegramusername
/geeks - To get the GeeksforGeeks URL
/weather - To get the weather Report
/google - To get the Google URL""")


def pythonCourse(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/UdemyPython - Udemy python Course 
/GeeksForgeeksPython - Geeks For Geeks python crash Course
/python - Documentation for Python Language
""")


def javaCourse(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/UdemyJava - Udemy Java Course 
/GeeksForgeeksJava - Geeks For Geeks Java crash Course
/Java - Documentation for Java Language
	""")

def CSE1(update: Update, context: CallbackContext):
     update.message.reply_text("""Available Commands :-
/YoutubeC - Course For C  Language 
/GeeksForgeeks - Geeks For Geeks C crash Course
/C - Documentation for C Language
""")

def CSE2(update: Update, context: CallbackContext):
     update.message.reply_text("""Available Commands :-
/YoutubeCplus - Course For C++  Language
/GeeksForgeeks - Geeks For Geeks C++ crash Course
/Cplusplus - Documentation for C++ Language
""")

def CSE3(update: Update, context: CallbackContext):
     update.message.reply_text("""Available Commands :-
    /javaCourse - Java RoadMap
    /Web - Web Development
""")
def CSE4(update: Update, context: CallbackContext):
     update.message.reply_text("""Available Commands :-
        /pythonCourse - Python RoadMap
        /App - App Development

""")
def CSE5(update: Update, context: CallbackContext):
     update.message.reply_text("""Available Commands :-
        /Javapoint - CN


""")
def YoutubeC(update: Update, context: CallbackContext):
    update.message.reply_text(
        "YoutubeC URL =>https://www.youtube.com/watch?v=ZSPZob_1TOk&t=3s")
def javapoint(update: Update, context: CallbackContext):
    update.message.reply_text(
        "JavaPoint URL => https://www.javatpoint.com/computer-network-tutorial")
def YoutubeCplus(update: Update, context: CallbackContext):
    update.message.reply_text(
        "YoutubeCplus URL =>https://www.youtube.com/watch?v=j8nAHeVKL08&list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL")
def GeeksForgeeksC(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksC URL =>https://www.geeksforgeeks.org/c-programming-language/")
def GeeksForgeeksCplus(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksCplus URL =>https://www.geeksforgeeks.org/c-plus-plus/")
def C(update: Update, context: CallbackContext):
    update.message.reply_text(
        "C Language URL =>https://devdocs.io/c/")
def Cplus(update: Update, context: CallbackContext):
    update.message.reply_text(
        "C++ Language URL =>https://devdocs.io/cpp/")
def Web(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Web Development URL =>https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")
def App(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
App Development URL =>https://developer.android.com/studio/intro/?gclid=CjwKCAjw9LSSBhBsEiwAKtf0n5IPupPOc0xk2Jkpzo1cj-wS9dHPeQ_fH-i9vulv90n-UF6DQqMVfhoCGtEQAvD_BwE&gclsrc=aw.ds 

Flutter URL => https://flutter.dev/?gclid=CjwKCAjw9LSSBhBsEiwAKtf0nzK4xxEvrrx3tTrIMyZUNBJy-3FT1WB3aPzMnB8KXj-rq4PZbKykHxoCbS4QAvD_BwE&gclsrc=aw.ds
	""")
def UdemyPython(update: Update, context: CallbackContext):
    update.message.reply_text(
        "UdemyPyton URL =>https://www.udemy.com/courses/search/?q=python+programming&src=sac&kw=python")


def UdemyJava(update: Update, context: CallbackContext):
    update.message.reply_text(
        "UdemyJava URL =>https://www.udemy.com/courses/search/?q=java+programming&src=sac&kw=java")


def GeeksForgeeksPython(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksPython URL =>https://www.geeksforgeeks.org/python-programming-language/")


def GeeksForgeeksJava(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksJava URL =>https://www.geeksforgeeks.org/java/")


def python(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Python URL =>https://www.python.org/")


def Java(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Python URL =>https://docs.oracle.com/en/java/")


def telegramUserName(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''@BhavinKhunt
@RajKaneriya0408''')


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
            "LinkedIn URL => \
		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


def google(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Google => \
		https://www.google.co.in/")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def weather_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "WEATHER URL => https://weather.com/en-IN/weather/today/l/22.59,72.82?par=google")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Ready', Ready))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('pythonCourse', pythonCourse))
updater.dispatcher.add_handler(CommandHandler('1CSE', CSE1))
updater.dispatcher.add_handler(CommandHandler('2CSE', CSE2))
updater.dispatcher.add_handler(CommandHandler('3CSE', CSE3))
updater.dispatcher.add_handler(CommandHandler('4CSE', CSE4))
updater.dispatcher.add_handler(CommandHandler('YoutubeC', YoutubeC))
updater.dispatcher.add_handler(CommandHandler('YoutubeCplus', YoutubeCplus))
updater.dispatcher.add_handler(CommandHandler('GeeksForgeeks', GeeksForgeeksC))
updater.dispatcher.add_handler(CommandHandler('GeeksForgeeks', GeeksForgeeksCplus))
updater.dispatcher.add_handler(CommandHandler('C', C))
updater.dispatcher.add_handler(CommandHandler('Cplusplus', Cplus))
updater.dispatcher.add_handler(CommandHandler('Web', Web))
updater.dispatcher.add_handler(CommandHandler('App', App))
updater.dispatcher.add_handler(CommandHandler('5CSE', CSE5))
updater.dispatcher.add_handler(CommandHandler('Javapoint', javapoint))

updater.dispatcher.add_handler(CommandHandler('javaCourse', javaCourse))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler(
    'GeeksForgeeksPython', GeeksForgeeksPython))
updater.dispatcher.add_handler(CommandHandler(
    'GeeksForgeeksJava', GeeksForgeeksJava))
updater.dispatcher.add_handler(CommandHandler('UdemyPython', UdemyPython))
updater.dispatcher.add_handler(CommandHandler('UdemyJava', UdemyJava))
updater.dispatcher.add_handler(CommandHandler('Python', python))
updater.dispatcher.add_handler(CommandHandler('Java', Java))

updater.dispatcher.add_handler(CommandHandler('telegramUserName', telegramUserName))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(CommandHandler('weather', weather_url))
updater.dispatcher.add_handler(CommandHandler('google', google))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
# client.run_until_disconnected()
