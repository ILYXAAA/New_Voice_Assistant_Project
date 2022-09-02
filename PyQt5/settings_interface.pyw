from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QCompleter, QMessageBox, QFileDialog, QDialog
import sys
import os.path
import pyttsx3
#print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '\\Scripts')
from Settings_ui import *
import torch
import sounddevice as sd
import time
from settings import Settings
import configparser

class Settings_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.settings = Ui_Settings_window()
        self.settings.setupUi(self)

        # Initialize from settings.ini
        self.init_all_items()

        self.settings.speaker_engine.currentTextChanged.connect(self.change_engine_items)
        self.settings.language.currentTextChanged.connect(self.change_engine_items)
        self.settings.line_region.textChanged.connect(self.check_city)
        self.settings.region.activated.connect(self.set_region)
        self.settings.test.clicked.connect(self.test_voice)
        self.settings.backup_to_mine.clicked.connect(self.return_engine)
        self.settings.reset.clicked.connect(self.reset_settings)
        self.settings.apply.clicked.connect(self.apply_changes)
        self.settings.choose_keepass_path.clicked.connect(self.browse_keepass_path)

        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")

        global data
        global cities_list
        cities_list = []
        with open(config['Settings']['program_path'] + '\\PyQt5\\list_of_cities.txt', 'r') as file:
            data = file.readlines()
        for i in range(len(data)):
            self.settings.region.addItem(data[i])
            cities_list.append(data[i])
        
        completer = QCompleter(cities_list, self.settings.line_region)
        self.settings.line_region.setCompleter(completer)

    def init_all_items(self):
        try:
            self.settings.region.clear()
            self.settings.pc_speed.clear()
            self.settings.speech_recognition_base.clear()
            self.settings.language.clear()
            self.settings.speaker_engine.clear()
            self.settings.sample_rate.clear()
            self.settings.model_id.clear()

            config = configparser.ConfigParser()
            config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
            self.settings.assistant_name.setText(config["Settings"]["assistant_name"])
            self.settings.person_name.setText(config["Settings"]["person_name"])
            self.settings.line_region.setText(config["Settings"]["region"])
            self.settings.program_path.setText(config["Settings"]["program_path"])
            self.settings.keepass_path.setText(config["Settings"]["keepass_path"])
            self.settings.pc_speed.addItems(['1', '2', '3', '4', '5', '6'])
            self.settings.pc_speed.setCurrentText(config["Settings"]["pc_speed"])
            self.settings.speech_recognition_base.addItems(['small_model', 'big_model'])
            self.settings.speech_recognition_base.setCurrentText(config["Settings"]["speech_recognition_base"])
            self.settings.vk_api.setText(config["Settings"]["vk_api"])
            self.settings.speaker_engine.addItems(['torch', 'pyttsx'])
            self.settings.speaker_engine.setCurrentText(config["Settings"]["speaker_engine"])
            self.settings.language.addItems(['ru', 'en'])
            self.settings.language.setCurrentText(config["Settings"]["language"])
            if self.settings.speaker_engine.currentText() == 'pyttsx':
                self.settings.speaker_voice.clear()
                tts = pyttsx3.init()
                voices = tts.getProperty('voices')
                if self.settings.language.currentText() == 'ru':
                    for voice in voices:
                        if 'Russian' in voice.name:
                            name = voice.name.replace('Microsoft', '')
                            name = name.replace('Desktop', '')
                            name = name.replace('Russian', '')
                            name = name.replace(' - ', '')
                            name = name.replace(' ', '')
                            self.settings.speaker_voice.addItem(name)
                elif self.settings.language.currentText() == 'en':
                    for voice in voices:
                        if 'English' in voice.name:
                            name = voice.name.replace('Microsoft', '')
                            name = name.replace('Desktop', '')
                            name = name.replace('English', '')
                            name = name.replace(' - ', '')
                            name = name.replace('(United States)', '')
                            name = name.replace(' ', '')
                            self.settings.speaker_voice.addItem(name)
                self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_pyttsx_voice"])

            elif self.settings.speaker_engine.currentText() == 'torch':
                self.settings.speaker_voice.clear()
                if self.settings.language.currentText() == 'ru':
                    self.settings.speaker_voice.addItems(['baya', 'aidar', 'kseniya', 'xenia'])
                    self.settings.model_id.addItem('ru_v3')
                if self.settings.language.currentText() == 'en':
                    self.settings.speaker_voice.addItems(['en_0', 'en_1', 'en_2', 'en_3'])
                    self.settings.model_id.addItem('v3_en')
                self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_torch_voice"])
                self.settings.sample_rate.addItems(['48000', '24000', '8000'])
                self.settings.sample_rate.setCurrentText(config["Settings"]["sample_rate"])
        except Exception as error:
            print(error)
            Settings.createConfig()
            self.init_all_items()

    def change_engine_items(self):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        self.settings.speaker_voice.clear()
        self.settings.sample_rate.clear()
        self.settings.model_id.clear()
        if self.settings.speaker_engine.currentText() == 'pyttsx':
            tts = pyttsx3.init()
            voices = tts.getProperty('voices')
            if self.settings.language.currentText() == 'ru':
                for voice in voices:
                    if 'Russian' in voice.name:
                        name = voice.name.replace('Microsoft', '')
                        name = name.replace('Desktop', '')
                        name = name.replace('Russian', '')
                        name = name.replace(' - ', '')
                        name = name.replace(' ', '')
                        self.settings.speaker_voice.addItem(name)
            elif self.settings.language.currentText() == 'en':
                for voice in voices:
                    if 'English' in voice.name:
                        name = voice.name.replace('Microsoft', '')
                        name = name.replace('Desktop', '')
                        name = name.replace('English', '')
                        name = name.replace(' - ', '')
                        name = name.replace('(United States)', '')
                        name = name.replace(' ', '')
                        self.settings.speaker_voice.addItem(name)
            self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_pyttsx_voice"])

        elif self.settings.speaker_engine.currentText() == 'torch':
            if self.settings.language.currentText() == 'ru':
                self.settings.speaker_voice.addItems(['baya', 'aidar', 'kseniya', 'xenia'])
                self.settings.model_id.addItem('ru_v3')
            if self.settings.language.currentText() == 'en':
                self.settings.speaker_voice.addItems(['en_0', 'en_1', 'en_2', 'en_3'])
                self.settings.model_id.addItem('v3_en')
            self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_torch_voice"])
            self.settings.sample_rate.addItems(['48000', '24000', '8000'])
            self.settings.sample_rate.setCurrentText(config["Settings"]["sample_rate"])

    def test_voice(self):
        if self.settings.speaker_engine.currentText() == 'pyttsx':
            tts = pyttsx3.init()
            voices = tts.getProperty('voices')
            tts.setProperty('voice', self.settings.language.currentText())
            for voice in voices:
                if self.settings.speaker_voice.currentText() in voice.name:
                    tts.setProperty('voice', voice.id)
            if self.settings.language.currentText() == 'ru':
                tts.say('Тестирование голосового помошника')
            elif self.settings.language.currentText() == 'en':
                tts.say('Testing voice')
            tts.runAndWait()
            
        elif self.settings.speaker_engine.currentText() == 'torch':
            if self.settings.language.currentText() == 'ru':
                words = 'Тестирование голосового помошника'
            if self.settings.language.currentText() == 'en':
                words = 'Testing voice assistant'
            config = configparser.ConfigParser()
            config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")

            language = self.settings.language.currentText()
            model_id = self.settings.model_id.currentText()
            sample_rate = int(self.settings.sample_rate.currentText())
            speaker = self.settings.speaker_voice.currentText()
            put_accent = bool(config["Settings"]["put_accent"])
            put_yo = bool(config["Settings"]["put_yo"])
            device = torch.device(config["Settings"]["device"])  # cpu or gpu

            model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_tts',
                                          language=language,
                                          speaker=model_id)
            model.to(device)

            audio = model.apply_tts(text=words + "..",
                                    speaker=speaker,
                                    sample_rate=sample_rate,
                                    put_accent=put_accent,
                                    put_yo=put_yo)

            sd.play(audio, sample_rate * 1.05)
            time.sleep((len(audio) / sample_rate) + 0.5)
            sd.stop()

    def browse_keepass_path(self):
        filen = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser(r'~\Downloads'),
                                            "KeePass2 base (*.kdbx)")
        self.settings.keepass_path.setText(filen[0])

    def check_city(self):
        self.settings.region.clear()
        for i in range(len(data)):
            if self.settings.line_region.text()[0:len(self.settings.line_region.text())].lower() == data[i][0:len(self.settings.line_region.text())].lower():
                self.settings.region.addItem(data[i])

    def set_region(self):
        self.settings.line_region.setText(self.settings.region.currentText())

    def return_engine(self):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        self.settings.speaker_voice.clear()
        self.settings.language.clear()
        self.settings.speaker_engine.clear()
        self.settings.sample_rate.clear()
        self.settings.model_id.clear()
        # Initialize from settings.ini
        try:
            self.settings.speaker_engine.addItems(['torch', 'pyttsx'])
            self.settings.speaker_engine.setCurrentText(config["Settings"]["speaker_engine"])
            self.settings.language.addItems(['ru', 'en'])
            self.settings.language.setCurrentText(config["Settings"]["language"])
            if self.settings.speaker_engine.currentText() == 'pyttsx':
                tts = pyttsx3.init()
                voices = tts.getProperty('voices')
                if self.settings.language.currentText() == 'ru':
                    for voice in voices:
                        if 'Russian' in voice.name:
                            name = voice.name.replace('Microsoft', '')
                            name = name.replace('Desktop', '')
                            name = name.replace('Russian', '')
                            name = name.replace(' - ', '')
                            name = name.replace(' ', '')
                            self.settings.speaker_voice.addItem(name)
                        elif self.settings.language.currentText() == 'en':
                            for voice in voices:
                                if 'English' in voice.name:
                                    name = voice.name.replace('Microsoft', '')
                                    name = name.replace('Desktop', '')
                                    name = name.replace('English', '')
                                    name = name.replace(' - ', '')
                                    name = name.replace('(United States)', '')
                                    name = name.replace(' ', '')
                                    self.settings.speaker_voice.addItem(name)
                    self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_pyttsx_voice"])

            elif self.settings.speaker_engine.currentText() == 'torch':
                if self.settings.language.currentText() == 'ru':
                    self.settings.speaker_voice.addItems(['baya', 'aidar', 'kseniya', 'xenia'])
                    self.settings.model_id.addItem('ru_v3')
                if self.settings.language.currentText() == 'en':
                    self.settings.speaker_voice.addItems(['en_0', 'en_1', 'en_2', 'en_3'])
                    self.settings.model_id.addItem('v3_en')
                self.settings.speaker_voice.setCurrentText(config["Settings"]["speaker_torch_voice"])
                self.settings.sample_rate.addItems(['48000', '24000', '8000'])
                self.settings.sample_rate.setCurrentText(config["Settings"]["sample_rate"])
        except Exception:
            Settings.createConfig()
            self.init_all_items()

    def reset_settings(self):
        try:
            Settings.createConfig()
            self.init_all_items()
            self.msg_info('Настройки успешно сброшены!')
        except Exception as error:
            print(str(error))

    def apply_changes(self):
        try:
            Settings.change_person_name(self.settings.person_name.text())
            Settings.change_assistant_name(self.settings.assistant_name.text())
            Settings.change_region(self.settings.line_region.text())
            Settings.change_program_path(self.settings.program_path.text())
            Settings.change_keepass_path(self.settings.keepass_path.text())
            Settings.change_vk_api(self.settings.vk_api.text())
            Settings.change_pc_speed(self.settings.pc_speed.currentText())
            Settings.change_speech_recognition_base(self.settings.speech_recognition_base.currentText())
            Settings.change_speaker_engine(self.settings.speaker_engine.currentText())
            Settings.change_language(self.settings.language.currentText())
            if self.settings.speaker_engine.currentText() == 'torch':
                Settings.change_sample_rate(self.settings.sample_rate.currentText())
                Settings.change_model_id(self.settings.model_id.currentText())
                Settings.change_speaker_torch_voice(self.settings.speaker_voice.currentText())
            elif self.settings.speaker_engine.currentText() == 'pyttsx':
                Settings.change_speaker_pyttsx_voice(self.settings.speaker_voice.currentText())
            self.msg_info('Настройки успешно установлены!')
            self.init_all_items()
        except Exception as error:
            print(str(error))

    def msg_warn(self, text):
        QMessageBox.warning(self, "Предупреждение ",
                            text, QMessageBox.Ok)

    def msg_crit(self, text):
        QMessageBox.critical(self, "Ошибка ",
                             text, QMessageBox.Ok)

    def msg_info(self, text):
        QMessageBox.information(self, "Информация ",
                                text, QMessageBox.Ok)



app = QtWidgets.QApplication(sys.argv)
myapp = Settings_window()
myapp.show()
sys.exit(app.exec_())
