def main():
    with open('test.txt', 'w+') as file:
        print(f'Opened file: test.txt')
        while True:
            try:
                user_input = input('Enter a number: ')
                if user_input.lower().strip() == 'done':
                    print(f'Data stored to test.txt')
                    break
                elif int(user_input):
                    file.write(f'{user_input}\n')
                else:
                    raise ValueError
            except ValueError:
                print(f'Invalid input')
        file.seek(0)
        input_list = file.readlines()
        print(f'Minimum = {min(input_list)}', end='')
        print(f'Maximum = {max(input_list)}', end='')
        print(f'Count = {len(input_list)}')
        total = 0
        for i in input_list:
            total += int(i)
        print(f'Sum = {total}', end='')


if __name__ == '__main__':
    main()
