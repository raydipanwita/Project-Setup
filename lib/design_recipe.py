def design_recipe(text):
    
    words_per_min = 200
    time_to_read = text/words_per_min
    return time_to_read

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
