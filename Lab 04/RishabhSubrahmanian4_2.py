import re

def main():

    txt_read = open('input.txt', 'r')
    csv_write = open('output.csv', 'w')

    csv_write.write(f'Email,Subject,Confidence\n')
    email_pattern = '[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+'
    subject_pattern = 'r[0-9]+'
    confidence_pattern = '[0-9]+\.[0-9]+'

    for i in txt_read:
        if i.startswith('From: '):
            email_result = re.findall(email_pattern, str(i))[0]
            csv_write.write(f'{email_result},')
        if i.startswith('Subject: '):
            subject_result = re.findall(subject_pattern, str(i))[0]
            csv_write.write(f'{subject_result},')
        if i.startswith('X-DSPAM-Confidence:'):
            conf_result = re.findall(confidence_pattern, str(i))[0]
            csv_write.write(f'{float(conf_result):.4f}\n')

    txt_read.close()
    csv_write.close()


if __name__ == '__main__':
    main()
