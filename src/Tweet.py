import re 

class Tweet():

    def __init__(self, target, id, date, flag, author, content):
        self.target = target
        self.id = id
        self.date = date
        self.flag = flag 
        self.author = author
        self.content = content

    def clean_up_content(self):
        self.content = re.sub(r'(@[a-zA-Z0-9]+)', '@', self.content)
        self.content = re.sub(r'([!?".:;,])', r' \1 ', self.content)
        self.content = re.sub(r'(\$ ?\d+\.\d+)', '$XX', self.content)
        self.content = re.sub(r'([0-9]{1,2}\%)', 'XX%', self.content)
        self.content = re.sub(r'https?://\S+|www\.\S+', '', self.content)
        self.content = self.content.replace(',', '')