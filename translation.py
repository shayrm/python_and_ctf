# build a translation from AEIOU and aeiou which will be replaced by 'g'
'''
    BTW this is another why to make a long text 
    more than one line...
    and this is another one...
'''

def trans_g(phrase):
    # translate = "AEIOUaeiou" if not using the letter.lower()
    translate = "aeiou"
    translation = ""
    for letter in phrase:
        if letter.lower() in translate:
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(trans_g(input(" Enter a phrase to translate: ")))