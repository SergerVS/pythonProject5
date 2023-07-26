
person={}
person = {'name' : 'Ivan Petrov'}
print(person)
person['age'] = 25
person['email']='serovsv'
person['phone']=322
print(person)
print(person.keys())
print(person.values())
person.pop('phone')
print(person)