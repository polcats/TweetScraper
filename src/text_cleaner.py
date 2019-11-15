
import re
import wordninja

def clean_text(text):
    text =  " ".join(text.splitlines()) # remove line breaks
    text =  re.sub(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)", "", text) #remove links
    text =  re.sub(r"(\<(/?[^>]+)>)", '', text) #remove tags
    text =  re.sub(r"(#|@)\w+", "", text)  #hashtags/mentions
    text =  re.sub(r'[^A-Za-z0-9\s]', '', text) #non letter/space
    text =  re.sub(r'\s{2,}', ' ', text) # more than 1 space
    text =  text.strip() # leading/tail spaces
    text =  text.lower()
    # text =  " ".join(wordninja.split(text))

    return text


