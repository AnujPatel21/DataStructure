def char_replace(b, token= " ",r = '%20'):
    return [r if x == token else x for x in b]
s = "ab cd ef g "
char_replace(s)
# # # b = "20%".join(s.split(" "))
# # print a
# # print b
print s
b = list(s)
c = char_replace(b)
string1 = ''.join(c)
print string1
