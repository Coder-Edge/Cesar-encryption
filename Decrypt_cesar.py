
# list_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
#     , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# for x in range(len(list_letter)):
#     list_letter.append(list_letter[x])
#
# message = input("Entrez votre message : ")
# clef = int(input("Entrez votre cle : "))
#
# def encrypte_cesar(lettre,liste,clef):
#     for i in range(len(liste)):
#         if lettre == ' ':
#             return ' '
#         elif liste[i] == lettre:
#             return str(list_letter[i+clef])
#
#     return '?'
#
#
#
# for clef in range(1,26):
#     encrypte_message = str()
#     for letter in message:
#         encrypte_message += encrypte_cesar(letter,list_letter,clef)
#     print(encrypte_message)

# Descrypte with a key

list_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M' , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for x in range(len(list_letter)):
    list_letter.append(list_letter[x])

message = input("Entrez votre message : ")
clef = int(input("Entrez votre cle : "))* (-1)

def encrypte_cesar(lettre,liste,clef):
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste[i] == lettre:
            return str(list_letter[i+clef])

    return '?'

encrypte_message = str()

for letter in message:
    encrypte_message += encrypte_cesar(letter,list_letter,clef)

print(encrypte_message)



