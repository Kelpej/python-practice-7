import pandas as pd


def read_input(prompt: str) -> str:
    return input(f'{prompt}:')


def read_file(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def read_file_pandas(file: str) -> pd.DataFrame:
    return pd.read_csv(file)
