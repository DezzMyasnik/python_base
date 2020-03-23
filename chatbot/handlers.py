import re


re_name = re.compile(r'^[\w\-\s]{3,40}')
re_email = re.compile(r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+\b')

def handle_name(text, context):
    match = re.match(re_name,text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_email(text, context):
    match = re.findall(re_email,text)
    if len(match) > 0:
        context['email'] = match[0]
        return True
    else:
        return False