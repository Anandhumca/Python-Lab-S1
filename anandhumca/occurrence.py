sentence=input("Enter The Sentence:")
words=sentence.split()
counts=dict()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)
