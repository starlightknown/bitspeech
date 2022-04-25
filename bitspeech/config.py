import os


class Config:
    """Configuration settings for the bitspeech Flask app."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "placeholder-secret-key")
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgres://xoehhrqcdxqdac:26c77c72005e69895878be54444feecd5e3f87f92a05149e08b54a92bdc12e89@ec2-34-194-158-176.compute-1.amazonaws.com:5432/da81aph83o5l17
")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
