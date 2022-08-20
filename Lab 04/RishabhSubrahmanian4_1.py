import re


def main():

    read_file = open('input.txt', 'r')
    write_file = open('output.txt', 'w')
    pattern = '^X\-DSPAM-Confidence:'

    total = 0
    length = 0
    for line in read_file:
        result = re.match(pattern, line)

        if result:
            write_file.write(line)

            num_pattern = '[0]\.\d+'
            res = re.findall(num_pattern, line)[0]

            total += float(res)
            length += 1

    average = total / length

    write_file.write(f"{'-' * 50}\n")
    write_file.write(f'Total dspam confidence = {total:.2f}\n')
    write_file.write(f'Average dspam confidence = {average:.2f}\n')

    read_file.close()
    write_file.close()


if __name__ == '__main__':
    main()
