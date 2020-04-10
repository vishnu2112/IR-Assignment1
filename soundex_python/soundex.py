
def soundex(name):

    

    soundexcoding = [' ', ' ', ' ', ' ']
    soundexcodingindex = 1

    #           ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mappings = "01230120022455012623010202"

    soundexcoding[0] = name[0].upper()

    for i in range(1, len(name)):

         c = ord(name[i].upper()) - 65

         if c >= 0 and c <= 25:

             if mappings[c] != '0':

                 if mappings[c] != soundexcoding[soundexcodingindex-1]:

                     soundexcoding[soundexcodingindex] = mappings[c]
                     soundexcodingindex += 1

                 if soundexcodingindex > 3:

                     break

    if soundexcodingindex <= 3:
        while(soundexcodingindex <= 3):
            soundexcoding[soundexcodingindex] = '0'
            soundexcodingindex += 1

    return ''.join(soundexcoding)
