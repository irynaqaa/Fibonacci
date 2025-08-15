import os
from pydantic import BaseSettings
from configparser import ConfigParser


class Settings(BaseSettings):
    authlib_client_id: str
    authlib_client_secret: str
    authlib_access_token_url: str
    authlib_authorize_url: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Configuration:
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.config.read(config_file)
    def get_config(self, section, key):
        return self.config.get(section, key)
