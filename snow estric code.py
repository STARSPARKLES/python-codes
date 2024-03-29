print("\t\t** ** ** * ** * ** * * ** *Snow Poem* ** * *  * ** * * * ** *\n")
string="words fell from the sky today I watched them snowin'"
stringend="and as they settled on the ground,they turned into this poem."
author="Brian Bilston"
wordend=stringend.split()
words=string.split()
w= " ".join(wordend)
s="\t"
snowrate=int(input("HOW MANY SNOW DO YOU WANT "))
for j in range(snowrate):
    for i in words:
        t=(s*len(i))
        print(t,"*")
print("*** *** * *** *** ****  ** * ** *** * * * *** *** * **** *")
print(w)
print("_____________")
print(author)
print("**  **  *  *  * *  * * ** ")