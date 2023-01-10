shift=(ord('a')-ord('e'))


def Decryption_through_statistics(text):
    def create_letter_stats_percent(text):
        dictionary={}
        counter=0
        with open (text,'r') as f:
            for word in f:
                word=word.strip().lower()
                for c in word:
                    if ord(c)>122:
                        dictionary[c]=0
                    elif ord(c)>96:
                        dictionary[c]=dictionary.get(c,0)+1
                        counter+=1
        stat=sorted(dictionary)
        for key in stat:
            dictionary[key]=(dictionary[key]/counter*100)
            print(key,'=',dictionary[key],'%')
        for key in stat:
            a=max(dictionary,key=dictionary.get)
        print(a)
    create_letter_stats_percent("english_cipher.txt")

    def cesar_crypt(Text,Shift):
        output=""
        with open (Text,'r') as Text:
            f=(Text.read())
            for letter in f:
                number=ord(letter)
                space=' '
                if number==32:
                    output+=space
                else:
                    shiftednumber=((ord(letter)+Shift-97)%26+97)
                    shiftedtext=chr(shiftednumber)
                    output+=shiftedtext
            print(output)
    cesar_crypt("english_cipher.txt",-shift)

Decryption_through_statistics("english_cipher.txt")