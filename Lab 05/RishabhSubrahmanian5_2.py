import os.path


def main():
    email_dict = {}
    while True:
        try:
            file_name = input('Input file name: ').strip()
            with open('files/' + file_name, 'r') as file:
                for i in file:
                    if i.startswith('From:'):
                        email_result = i.split()[1]
                        email_dict[email_result] = email_dict.get(email_result, 0) + 1
                output_file = input('Output file name: ').strip()
                break
        except IOError:
            print('File does not exist!')

    while os.path.isfile('files/' + output_file):
        new_file_question = input('Overwrite existing file (y/n): ').strip().lower()
        while new_file_question not in ['y', 'n']:
            new_file_question = input('Enter (y/n): ').strip().lower()
        if new_file_question == 'y':
            break
        elif new_file_question == 'n':
            new_output_file = input('New output file name: ').strip()
            if new_output_file == output_file:
                continue

    with open('files/' + output_file, 'w') as file:
        for key, value in email_dict.items():
            file.write(f'{key} - {value}\n')

    print('Data stored!')


if __name__ == '__main__':
    main()
