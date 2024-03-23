import re

def process(filter, src):
    dst = []
    for str in src:
        if (not filter(str)):
            dst.append(str)
    return dst

if __name__ == '__main__':
    # kill strings with spaces
    filter0 = lambda s : False if s.find(' ') == -1 else True

    # starts with 'a'
    filter1 = lambda s : True if s[0] == 'a' or s[0] == 'A' else False
    
    # len less 5
    filter2 = lambda s : False if len(s) > 5 else True

    test_arr = ['string 1',
                'string2',
                'astring',
                'stra',
                'asdasd']
    
    print(f'source array: {test_arr}')
    print(f'without strings with spaces: {process(filter0, test_arr)}')
    print(f'without "A" in the beginning: {process(filter1, test_arr)}')
    print(f'without strings with length less than 5: {process(filter2, test_arr)}')