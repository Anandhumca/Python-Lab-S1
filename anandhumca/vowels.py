word=input("Enter A Word:")
vowels=['a','e','i','o','u']
wordvowels=[]
for x in word:
    if(x in vowels and x not in wordvowels):
        wordvowels.append(x)
print("vowels in",word,"are:",wordvowels)
