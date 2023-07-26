lang=['russ','eng','chin','polsk','ukr','shwed']
print(lang)
lang.insert(3,'rom')
print(lang)
lang.insert(-1,'port')
print(lang)
lang.append('norg')
print(lang)
lang.remove('eng')
print(lang)
print(sorted(lang))
print(lang)
print(sorted(lang,reverse=True))
print(lang)
lang_popped=lang.pop(-1)
print(lang_popped)
del lang[0]
print(lang)
message=("I'd like to study "+lang_popped+'.')
print(message)
for lang in lang:
    print(cool)



