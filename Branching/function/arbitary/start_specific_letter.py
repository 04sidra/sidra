def start_specific_letter(word,letter):
    for i in word:
        if not i.startswith(letter):
            return False
    return True
w=input("enter the word :").split()
l=input("enter the letter to check :")
if start_specific_letter(w,l):
    print('yes')
else:
    print('Not')    



 