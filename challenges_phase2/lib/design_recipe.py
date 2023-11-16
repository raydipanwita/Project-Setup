def design_recipe(text):
    words = text.split()
    wordcount = len(words)
    return wordcount / 200


def design_recipe2(word):
    if word[0].isupper() and word[-1] in {"." ,"!" , "?" }: 
        return True
    else:
        return False
    
def design_recipe3(word3):
    track = "#TODO"
    if track in word3:
        return True
    else:
        return False
