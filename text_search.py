import re

def read_text_file(text_file):
    lines = file(text_file).readlines()
    return [line[:-1] for line in lines] 

def index_text(text_lines):
    index = {}
    i = 0
    for line in text_lines:
        words = re.split('[ .:)(?!-\'\"]+',line)
        for word in words:
            if word != '':
                index[word] = index.get(word, []) + [i]
        i += 1
    return index

def print_rows(word,text_index,text_lines):
    print ''
    i = 0
    last_line_id = -1
    for line_id in text_index.get(word, []):
        line =  text_lines[line_id]
        if not line_id == last_line_id:
            print '  [Line:' + (5 - len(str(line_id + 1))) * ' ' + str(line_id + 1) + 
']  
' + line
            print 16 * ' ' + build_pointers(word,line)
        i += 1
        last_line_id = line_id     
    if i>0:
        print '  "' + word + '" was found ' + str(i) + ' times.\n'
    else:
        print '  Nothing found for "' + word + '".\n'

def build_pointers(word,str):
    pointers = ''
    while len(str) > 0:
        offset =  str.find(word)
        if not offset == -1:
            pointers =  pointers + offset * ' ' + '^'
            str = str[offset + 1:]
        else:
            return pointers
    return pointers
    
def find_word(text_index,text_lines):
    print_rows(raw_input('\nSearch for: '),text_index,text_lines)
    find_word(text_index,text_lines)

f = str(raw_input('\nFilename: '))

text_lines = read_text_file(f)
text_index = index_text(text_lines)

find_word(text_index,text_lines)
