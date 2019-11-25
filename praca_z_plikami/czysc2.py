import sys
try:
    input_file = sys.argv[1]
except IndexError:
    input_file = None

try:
    output_file = sys.argv[2]
except IndexError:
    output_file = None

def read_data(input_file):
    with open("dane/"+input_file) as in_file:
    data = in_file.read().splitlines()

def clean_data()
cleaned_emails = set()
for email in data:
    if email.count("@") == 1:
        cleaned_emails.add(email.strip().lower())

cleaned_emails = list(cleaned_emails)
cleaned_emails.sort()

print(cleaned_emails)

