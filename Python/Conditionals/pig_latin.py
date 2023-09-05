def translate(text):
    vowel_sounds = "aeiou"
    texts = ""
    for text in text.split():
        if text[0] in vowel_sounds:
            text += "ay"
        else: # if text[0] not in vowel_sounds:        
            if text[0] in "xy" and text[1] not in vowel_sounds:
                text += "ay"
            elif "qu" in text:
                text = text[text.index("u")+1:] + text[:text.index("u")+1] + "ay"
            elif text[1] not in vowel_sounds:
                if len(text) == 2 and text[1] == "y":
                    text = text[::-1] + "ay"
                elif text[2] == "y" or text[2] in vowel_sounds:
                    text = text[2:] + text[:2] +  "ay"
                else:
                    text = text[3:] + text[:3] + "ay"
            else:
                text = text[1:] + text[0] + "ay"
        texts += text + " "
    return texts.strip()