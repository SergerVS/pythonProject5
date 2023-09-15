ponchos= []
ponchos.append('peper')
ponchos.append('chily')
ponchos.append('chik')
ponchos.append('meat')
ponchos.append('sea')
ponchos.append('choko')
print(ponchos)
friend_ponchos=ponchos [:]
print(friend_ponchos)
ponchos.append('feyh')
friend_ponchos.append('silk')
print(ponchos)
print(friend_ponchos)
print('My favourite ponchos are :')
for poncho in ponchos :
    print(poncho.title())
print('My friend,s favourite ponchos are :')
for friend_poncho in friend_ponchos :
    print(friend_poncho.title())
print('My friend,s favourite ponchos are :' )
print(friend_ponchos)