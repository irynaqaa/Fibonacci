import autopep8
import sys

def format_code(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            content = file.read()
            # Format the content using autopep8
            formatted_content = autopep8.fix_code(content)
            # Write the formatted content back to the file
            with open(file_path, 'w') as file:
                file.write(formatted_content)
        print(f'File {file_path} has been successfully formatted.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python code_formatting.py <file_path>')
    else:
        file_path = sys.argv[1]
        format_code(file_path)
