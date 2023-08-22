
def encryt_message():

    list_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for x in range(len(list_letter)):
        list_letter.append(list_letter[x])

    message = input("Tape your message : ")
    clef = int(input("Put the key : "))

    def encrypte_cesar(lettre, liste, clef):
        for i in range(len(liste)):
            if lettre == ' ':
                return ' '
            elif liste[i] == lettre:
                return str(list_letter[i + clef])

        return '?'

    encrypt_message = str()

    for letter in message:
        encrypt_message += encrypte_cesar(letter, list_letter, clef)

    print(encrypt_message)


