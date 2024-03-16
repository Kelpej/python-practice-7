from datetime import datetime


def log(message: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] - {message}')


def write_file(file: str, content: str):
    with open(file, 'w') as f:
        f.write(content)
