import re

kody = set()
maile = set()
daty = set()

p_kod = re.compile("\d{2}-\d{3}")
p_mail = re.compile('[\w\.\-]+@+[\w\.-]+')
p_data = re.compile('\d{2} \w{3} \d{4}')

with open('dane/input.txt') as f:
    data = f.read()
    print(p_kod.findall(data))
    print(p_mail.findall(data))
    print(p_data.findall(data))

    # for line in data:
    #     if p_kod.findall(data):
    #         kody.add(p_kod)
    #     if p_mail.findall(data):
    #         maile.add(p_mail)
    #     if p_data.findall(data):
    #         daty.add(p_data)
