import re

def slugified(s:str):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s


def dignify(n:int):
    return f"{n:,}"

def is_valid_email(email:str):
    pattern = r'^[\w\.-]@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False