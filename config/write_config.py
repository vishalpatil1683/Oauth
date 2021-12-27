# from configparser import Configparser
from configparser import ConfigParser
# Config file object
config = ConfigParser()
# Section
config.add_section('power-bi-config')

#setting Values

config.set('power-bi-config','client_id','cb76af0e-ce74-4ac7-8485-578f0c8e08b8')

config.set('power-bi-config','client_secret','j3id3jkNe036QSM9wpFme5fM+gO98TW4hOEJmSkJIwc=')

config.set('power-bi-config','redirect_uri','https://localhost/redirect')

# client_id = "cb76af0e-ce74-4ac7-8485-578f0c8e08b8"
# client_secret = "j3id3jkNe036QSM9wpFme5fM+gO98TW4hOEJmSkJIwc="
# redirect_uri = "https://localhost/redirect"

with open(file='config/config.ini', mode='w+') as f:
    config.write(f)