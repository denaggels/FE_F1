from pathlib import Path
import boto3
from dotenv import load_dotenv
import os

def get_path_to_data():
    """Return path to data."""
    return Path('Data/')


def get_raw_data_path():
    """Return path to raw data."""
    return get_path_to_data() / 'RawData'


def get_tidy_data_path():
    """Return path to tidy data."""
    return get_path_to_data() / 'TidyData'


def get_dynamo_recouce():
    load_dotenv()
    session = boto3.Session(aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
                             aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"))
    dynamo_resource = session.resource('dynamodb', region_name='eu-west-1')
    return dynamo_resource