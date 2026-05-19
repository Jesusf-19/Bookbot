from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

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

def sort_on(char_count: CharacterCount) -> int:
    return char_count["num"]

def dict_sort(char_counts: dict[str, int]) -> list[CharacterCount]:
    sorted_list = []
    for char, num in char_counts.items():
        sorted_list.append({"char": char, "num": num})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list