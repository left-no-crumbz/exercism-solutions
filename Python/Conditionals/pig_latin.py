def translate(text):
    vowel_sounds = "aeiou"
    
    special_vowels = ["xr", "yt", "yg"]
    modified = []
    
    for text in text.split():
        if text[0] in vowel_sounds or text[0:2] in special_vowels:
            modified.append(text + "ay")
            continue
        for pos in range(1, len(text)):
            if text[pos] in vowel_sounds + "y":
                pos+=1 if text[pos-1] == 'q' and text[pos] == 'u' else 0 
                modified.append(text[pos:] + text[:pos] + "ay")
                break
    return " ".join(modified)