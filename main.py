import app.io.input as input
import app.io.output as output

if __name__ == '__main__':
    output.log('Hello, World!')

    name = input.read_input('What is your name?')
    output.write_file(name, 'Hello, World!')

    content = input.read_file(name)
    output.log(content)

    df = input.read_file_pandas('resources/data.csv')
    output.log(df.head())
