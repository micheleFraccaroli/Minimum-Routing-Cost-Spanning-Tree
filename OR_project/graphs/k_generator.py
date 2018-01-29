
ascii_letters = 'abcdefghijklm'
not_used = "nopqruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
def main():
	f = open("graph_random.txt","w")
	for ch in ascii_letters[:len(ascii_letters)-1]:
		f.write(ch+",")
	f.write(ascii_letters[len(ascii_letters)-1]+"\n")
	i =0
	for ch in ascii_letters:
		i+=1
		for ch2 in ascii_letters[i:]:
			f.write(str(random.randint(8,30))+" "+ch+" "+ch2+"\n")
	f.close()

if __name__ == '__main__':
	main()