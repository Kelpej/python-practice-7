from datetime import datetime


def log(message: str):
    """
    Log a message with a timestamp
    :param message: a message to log
    :return: None
    """

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] - {message}')


def write_file(file: str, content: str):
    """
    Write content to a file
    :param file: path to file
    :param content: content to write
    :return: None
    """

    with open(file, 'w') as f:
        f.write(content)
