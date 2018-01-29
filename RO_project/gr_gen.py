import random

ascii_letters = 'ABCDEFGHILMNOPQRST'
#abcdefghijklmnopqrstuvwxyz
#0123456789
f = open("graph/graph_ppt.txt", "w")

for i in ascii_letters[:len(ascii_letters)-1]:
	f.write(i + ",")
f.write(ascii_letters[len(ascii_letters)-1] + '\n')

h = 0
for i in ascii_letters:
	h+=1
	for j in ascii_letters[h:]:
		f.write(str(random.randint(1,30)) + ' ' + i + ' ' + j + '\n')
f.close()
