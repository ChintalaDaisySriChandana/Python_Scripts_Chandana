import re

email_data="chandanaSRI <daisySRI123@gmail.com>, sri <sric@gmail.com>"

result= re.search(r"chan", email_data)
print(result)

result=re.findall(r"chan", email_data)
print(result)

result=re.search(r"chan[d,e]", email_data)
print(result)

result=re.search(r"chan[a-z]", email_data)
print(result)

result=re.search(r"chan[a-z]{2}", email_data)
print(result)

result=re.search(r"chan[a-z]+", email_data)
print(result)

result=re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

