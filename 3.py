vn=input()
li1=('a','A','e','E','i','I','o','O','u','U')
li2=('b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z')
if(vn in li1):
    print("Vowel")
elif(vn in li2):
    print("Consonant")
else:
    print("invalid")
