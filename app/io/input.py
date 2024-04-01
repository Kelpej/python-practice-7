import pandas as pd


def read_input(prompt: str) -> str:
    """
    Read input from the user
    :param prompt:
    :return:
    """
    return input(f'{prompt}:')


def read_file(file: str) -> str:
    """
    Read file content
    :param file: path to file
    :return: file content
    """
    with open(file, 'r') as f:
        return f.read()


def read_file_pandas(file: str) -> pd.DataFrame:
    return pd.read_csv(file)
