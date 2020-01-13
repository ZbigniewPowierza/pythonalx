import re

text = "11 02 1980   11 15 1980"
# xxx pattern = re.compile("11|12+")

x_pattern = re.compile("\d{2} \d{2} \d{4}")
xxx_pattern = re.compile("((\d{2} 0[1-9]|10|11|12) \d{4})")
print(x_pattern.findall(text))
print(xxx_pattern.findall(text))

daty_pattern = "[0-3][0-9] \w{3} \d{4}"
pna_pattern = "\d{2}-\d{3}"
pna_pattern1 = "(\d{2}-)\(d{3})"
pna_pattern2 = "((\d{2}-)\(d{3}))"
email_pattern = "[\w-]+@[\w.]+"



with open ("input.txt") as f:
    text = f.read()

daty = re.compile(daty_pattern)
print(daty.findall(text))

pna = re.compile(pna_pattern)
print(pna.findall(text))

email_pattern = re.compile(email_pattern)
print(email_pattern.findall(text))
