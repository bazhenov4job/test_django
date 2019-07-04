import configparser
import os

path = os.path.join(os.getcwd(),'config/' "local.conf")
config = configparser.RawConfigParser()

config.add_section("main")
config.set("main", "SECRET_KEY", "2_d#0azac!z=0#vrjwz-ttun78apobg062)26yxg8i46nea#19")
config.set("main", "DEBUG", "True")

config.add_section("admin")
config.set("admin", "admin_username", "admin")
config.set("admin", "admin_email", "admin@geekshop.local")
config.set("admin", "admin_password", "admin")
config.set("admin", "admin_age", 30)

with open(path, "w") as config_file:
    config.write(config_file)