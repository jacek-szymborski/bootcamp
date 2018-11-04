# def strip_line(line):
#     stripped_line = line.strip()
#     return stripped_line
#
# def wrong_email_format_at_sign(line):
#     if
#
# with open("dane/emails.txt") as f:
#     for line in f:
#         print(strip_line(line))

import sys

def validate_email(line):
    line = line.strip().lower()
    if line.count('@') == 1:
        return line
    else:
        return None


if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()

    with open(input_file) as f:
        for line in f:
            email = validate_email(line)
            if email:
                emails.add(email)
    with open(output_file,'w') as f:

        for email in sorted(emails):
            f.write(email+"\n")
else:
    print("malo parametrow")