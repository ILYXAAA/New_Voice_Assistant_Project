import configparser
import os
class Settings:
    def __init__(self):
        try:
            config = configparser.ConfigParser()
            config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        except Exception:
            self.createConfig()
            self.__init__()

        self.speaker_engine = config["Settings"]["speaker_engine"]
        self.assistant_name = config["Settings"]["assistant_name"]
        self.program_path = config["Settings"]["program_path"]
        self.language = config["Settings"]["language"]
        self.model_id = config["Settings"]["model_id"]
        self.sample_rate = config["Settings"]["sample_rate"]
        self.speaker_torch_voice = config["Settings"]["speaker_torch_voice"]
        self.speaker_pyttsx_voice = config["Settings"]["speaker_pyttsx_voice"]
        self.put_accent = config["Settings"]["put_accent"]
        self.put_yo = config["Settings"]["put_yo"]
        self.device = config["Settings"]["device"]
        self.speech_recognition_base = config["Settings"]["speech_recognition_base"]
        self.region = config["Settings"]["region"]
        self.keepass_path = config["Settings"]["keepass_path"]
        self.vk_api = config["Settings"]["vk_api"]
        self.pc_speed = config["Settings"]["pc_speed"]
        self.pyowm_key = config["Settings"]["pyowm_key"]
        self.country = config["Settings"]["country"]

    @staticmethod
    def createConfig():
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "assistant_name", "Default")
        config.set("Settings", "person_name", "Default")
        config.set("Settings", "program_path", os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
        config.set("Settings", "language", "ru")
        config.set("Settings", "model_id", "ru_v3")
        config.set("Settings", "sample_rate", "48000")
        config.set("Settings", "speaker_torch_voice", "baya")
        config.set("Settings", "speaker_pyttsx_voice", "Irina")
        config.set("Settings", "put_accent", "True")
        config.set("Settings", "put_yo", "True")
        config.set("Settings", "device", "cpu")
        config.set("Settings", "speaker_engine", "pyttsx")
        config.set("Settings", "speech_recognition_base", "small_model")
        config.set("Settings", "region", "Default")
        config.set("Settings", "keepass_path", "Default")
        config.set("Settings", "vk_api", "Default")
        config.set("Settings", "pc_speed", "6")
        config.set("Settings", "pyowm_key", "Default")
        config.set("Settings", "country", "Default")

        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_assistant_name(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "assistant_name", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_person_name(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "person_name", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_program_path(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "program_path", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_language(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "language", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_model_id(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "model_id", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_sample_rate(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "sample_rate", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_speaker_pyttsx_voice(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "speaker_pyttsx_voice", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_speaker_torch_voice(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "speaker_torch_voice", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini",
                  "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_put_accent(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "put_accent", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_put_yo(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "put_yo", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_device(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "device", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_speaker_engine(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "speaker_engine", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_speech_recognition_base(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "speech_recognition_base", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_region(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "region", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_keepass_path(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "keepass_path", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_vk_api(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "vk_api", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_speaker_engine(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "speaker_engine", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_pc_speed(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "pc_speed", new)
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_pyowm_key(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "pyowm_key", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini", "w") as config_file:
            config.write(config_file)

    @staticmethod
    def change_country(new):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini")
        config.set("Settings", "country", new.lower())
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + "\\settings.ini",
                  "w") as config_file:
            config.write(config_file)

