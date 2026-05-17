def word_counter(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_counter(text):
    characters = list(text.lower())
    character_dict = {}
    for character in characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict
