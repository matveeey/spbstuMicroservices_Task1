import re

def process(raw_str):
    res = True

    str = re.sub(r'[^a-zA-Z0-9а-яА-Я]', '', raw_str) # the rule "removes" all the other symbols except the letters and digits

    if len(str) == 0:
        res = False
        return res

    str_rev = str[::-1]

    for sym, sym_rev in zip(str, str_rev):
        if sym != sym_rev:
            res = False
            break
    
    return res

def pali_check(str):
    if process(str):
        print(f'"{str}" is a palindrome!')
    else:
        print(f'"{str}" is not a palindrome!')

if __name__ == '__main__':
    pali_check("palindrome")
    pali_check("фыввы ф")
    pali_check("дед")
    pali_check(" turtle eltrut")
