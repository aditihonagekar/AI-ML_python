#this is a giraffe language, where vowels are converted to 'g'. example - dog -> dgg

def translate(phrase):
    translation=""
    for words in phrase:
        if words in "AEIOUaeiou":
            translation=translation+'g'
        else:
            translation=translation+words
    return translation
print(translate(input("enter phrase:")))
