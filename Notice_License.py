import os

for root,dir,files in os.walk("/home/ubuntu/NOTICE_LICENSE"):
    for file in files:
        if file.startswith(('NOTICE','LICENSE')):
            print(f"{root}/{file}")
