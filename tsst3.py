fr_names=['iv','pol','lora','pav','greg']
print(fr_names[3].title())
print(fr_names[-1].upper())
print(fr_names.count('iv'))
message=('Hi , '+fr_names[0].title()+','+'  '+'how are you?')
print(message)
message_2=('Morning,'+fr_names[2].title()+','+' '+'wont you fack?')
print(message_2)
message_3=('Such a fine day ,'+fr_names[-1].upper()+','+' '+"go home?" )
print(message_3)
fr_names.sort()
print(fr_names)
fr_names.sort(reverse=True)
print(fr_names)
print('Here is original')
print(fr_names)
print('Here is sorted')
print(sorted(fr_names))
print('ytre is original again')
print(fr_names)
fr_names.reverse()
print(fr_names)
len(fr_names)
