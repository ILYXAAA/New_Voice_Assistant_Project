import sys
from fuzzywuzzy import fuzz
sys.path.append('Scripts/')
sys.path.append('PyQt5/')
sys.path.append('Dictionaries/')
from response_rebuilder import *
from listen import *
from check_engine import *
from weather import *
from Sound import Sound
from settings import Settings
import keyboard
import random
from threading import Thread
Settings = Settings()

def main():
    # Инициализация команд
    commands = {'change_person_name': change_person_name,
                'change_assistant_name': change_assistant_name,
                'make_settings_recovery': make_settings_recovery,
                'make_settings_backup' : make_settings_backup,
                'hello': hello,
                'exit_program': exit_program,
                'no_problem': no_problem,
                'show_settings_panel' : show_settings_panel,
                'close_window': close_window,
                'say_my_name': say_my_name,
                'weather': weather,
                'volume_mute':volume_mute,
                'volume_max':volume_max,
                'volume_up':volume_up,
                'volume_down':volume_down,
                'set_volume':set_volume}

    with open('Dictionaries/commands_dictionary.json', 'r') as f:
        global commands_dictionary
        commands_dictionary = json.load(f)
    with open('Dictionaries/words_dictionary.json', 'r') as f:
        global words_and_answers_dictionary
        words_and_answers_dictionary = json.load(f)

    # Проверка движка
    global speak_engine
    speak_engine = check_engine()
    speak_engine['say']("Здравствуйте")

    while True:
        # Подгрузка конфиг файла
        global config
        config = configparser.ConfigParser()
        config.read("settings.ini")
        response = listen()
        print(f'response = {response}')

        if config['Settings']['assistant_name'] in response:
            while len(response) != 0:
                if response == config['Settings']['assistant_name']:
                    speak_engine['say']("Слушаю вас!")
                    response = listen()
                if config['Settings']['assistant_name'] in response:
                    response = response.replace(config['Settings']['assistant_name'], '')

                response = clarify_response(response)
                print(f'response after clarifying = {response}\n')

                for resp in response:
                    task = ''
                    maximum = 0
                    for i in range(len(list(commands_dictionary))):
                        for j in range(len(commands_dictionary[list(commands_dictionary)[i]])):
                            if fuzz.token_sort_ratio(resp, commands_dictionary[list(commands_dictionary)[i]][j]) > maximum:
                                maximum = fuzz.token_sort_ratio(resp, commands_dictionary[list(commands_dictionary)[i]][j])
                                task = list(commands_dictionary)[i]
                    print(f'function is: {task} with {maximum}%')

                    if maximum > 60:
                        config = configparser.ConfigParser()
                        config.read("settings.ini")
                        try:
                            stop_process = Thread(target=stop_event, args=(config,))
                            stop_process.start()
                            commands[task](resp)
                        except Exception as error:
                            print(error)
                            speak_engine['say'](error)
                    else:
                        if maximum >=40 and maximum < 60:
                            speak_engine['say'](f'К сожалению, не смогла распознать команду, которую вы сказали, попробуйте повторить или сказать её по-другому. '
                                            f'Если хотите поговорить, вы в любой момент можете сказать, {config["Settings"]["assistant_name"]}, давай поговорим')
                        elif maximum < 40:
                            speak_engine['say']('Угу')


                response = listen()


def stop_event(config):
    while True:
        response = listen()
        if 'стоп' in response and config['Settings']['assistant_name'] in response:
            print('ПЕРЕЗАПУСКАЮСЬ')
            os.execv(sys.executable, ['python'] + sys.argv)


def change_person_name(response):
    with open('Dictionaries/names.txt', 'r') as f:
        names = f.readlines()
    names = [line.rstrip() for line in names]
    new_name = response.split()[-1]
    c = 0
    for name in names:
        if ' ' + name + ' ' in ' ' + response + ' ':
            new_name = name
            c = 1
            break
    if c == 0:
        speak_engine['say'](
            f"К сожалению, я не смогла найти имя, {new_name}, в словаре имён. Хотите добавить его в словарь, а потом установить данное имя?")
        answer = listen()
        for yes_word in words_and_answers_dictionary['yes_words']:
            if yes_word in answer:
                with open('Dictionaries/names.txt', 'a') as file:
                    file.write(f'{new_name}\n')
                speak_engine['say'](
                    f"Добавила имя, {new_name}, в словарь имён.")

        config = configparser.ConfigParser()
        config.read("settings.ini")
        if config["Settings"]["person_name"] != new_name:
            speak_engine['say']('Хорошо, имя не устанавлиаем и не записываем.')
            return

    if ' моё ' not in ' ' + response + ' ' and ' твоё ' not in ' ' + response + ' ' and ' меня ' not in ' ' + response + ' ' and ' тебя ' not in ' ' + response + ' ' and ' своё ' not in ' ' + response + ' ':
        speak_engine['say']("Чьё имя хотите изменить?")
        answer = listen()

        if 'твоё' in answer in answer:
            Settings.change_assistant_name(new_name)
            speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила своё имя на {new_name}")
        elif 'моё' in answer or 'своё' in answer:
            Settings.change_person_name(new_name)
            speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила ваше имя на {new_name}")

    else:
        Settings.change_person_name(new_name)
        speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила ваше имя на {new_name}")


def change_assistant_name(response):
    with open('Dictionaries/names.txt', 'r') as f:
        names = f.readlines()
    names = [line.rstrip() for line in names]
    new_name = response.split()[-1]
    c = 0
    for name in names:
        if ' ' + name + ' ' in ' ' + response + ' ':
            new_name = name
            c = 1
            break
    if c == 0:
        speak_engine['say'](
            f"К сожалению, я не смогла найти имя, {new_name}, в словаре имён. Хотите добавить его в словарь, а потом установить данное имя?")
        answer = listen()
        c = 0
        for yes_word in words_and_answers_dictionary['yes_words']:
            if yes_word in answer:
                with open('Dictionaries/names.txt', 'a') as file:
                    file.write(f'{new_name}\n')
                speak_engine['say'](
                    f"Добавила имя, {new_name}, в словарь имён.")
                c = 1
                break

        if c == 0:
            speak_engine['say']('Хорошо, имя не устанавлиаем и не записываем.')
            return


    if 'моё' not in response and 'твоё' not in response and 'меня' not in response and 'тебя' not in response and 'своё' not in response:
        speak_engine['say']("Чьё имя хотите изменить?")
        answer = listen()

        if 'твоё' in answer:
            Settings.change_assistant_name(new_name)
            speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила своё имя на {new_name}")
        elif 'моё' in answer or 'своё' in answer:
            Settings.change_person_name(new_name)
            speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила ваше имя на {new_name}")

    else:
        Settings.change_assistant_name(new_name)
        speak_engine['say'](f"{random.choice(words_and_answers_dictionary['done_words'])}. сменила своё имя на {new_name}")

def show_settings_panel(response):
    try:
        speak_engine['say']('Открываю')
        os.startfile(r'PyQt5\settings_interface.pyw')
    except Exception as error:
        print(error)
        speak_engine['say'](error)

def close_window(response):
    speak_engine['say']('Ок')
    keyboard.send('ALT+F4')

def say_my_name(response):
    speak_engine['say'](f'Вас зовут, {config["Settings"]["person_name"]}')

def make_settings_backup(response):
    try:
        with open('settings.ini', 'r') as file:
            data = file.read()
        with open('Backups/settings_backup.ini', 'w') as file:
            file.write(data)
        speak_engine['say'](f'{random.choice(words_and_answers_dictionary["done_words"])}')
    except Exception as error:
        speak_engine['say'](error)


def make_settings_recovery(response):
    try:
        with open('Backups/settings_backup.ini', 'r') as file:
            data = file.read()
        with open('settings.ini', 'w') as file:
            file.write(data)
        speak_engine['say'](f'{random.choice(words_and_answers_dictionary["done_words"])}')
    except Exception as error:
        speak_engine['say'](error)

def weather(response):
    speak_engine['say'](get_weather())

def volume_mute(response):
    Sound.mute()

def volume_max(response):
    Sound.volume_max()

def volume_up(response):
    Sound.volume_up()
    Sound.volume_up()
    Sound.volume_up()
    Sound.volume_up()
    Sound.volume_up()

def volume_down(response):
    Sound.volume_down()
    Sound.volume_down()
    Sound.volume_down()
    Sound.volume_down()
    Sound.volume_down()

def set_volume(response): # От 0 до 100
    response = response.split()
    for word in response:
        try:
            print(word)
            word = int(word)
            if word <= 100:
                Sound.volume_set(word)
                speak_engine['say'](f'{random.choice(words_and_answers_dictionary["done_words"])}')
            else:
                speak_engine['say']('Громкость может быть от 0 до 100')
        except Exception as error:
            pass


def hello(response):
    speak_engine['say'](f"{random.choice(words_and_answers_dictionary['hello_words'])}, {config['Settings']['person_name']}")
def no_problem(response):
    speak_engine['say'](f"{random.choice(words_and_answers_dictionary['no_problem_words'])}")
def exit_program(response):
    speak_engine['say'](f"{random.choice(words_and_answers_dictionary['goodbye_words'])}, {config['Settings']['person_name']}")
    os._exit(0)

if __name__ == '__main__':
    main()
