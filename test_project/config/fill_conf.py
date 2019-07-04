import configparser
import os

path = os.path.join(os.getcwd(),'config/' "local.conf")
config = configparser.RawConfigParser()

config.add_section("main")
config.set("main", "SECRET_KEY", "2_d#0azac!z=0#vrjwz-ttun78apobg062)26yxg8i46nea#19")
config.set("main", "DEBUG", "True")



with open(path, "w") as config_file:
    config.write(config_file)