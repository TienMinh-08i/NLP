from typing import List

def parse_music_original(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    def count_beats(note: str) -> int:
        if note == 'o':
            return 4
        elif note == 'o|':
            return 2
        elif note == '.|':
            return 1
    if music_string == '':
        return []
    return list(map(count_beats, music_string.split(' ')))


def parse_music(music_string: str) -> List[int]:


    return_value = parse_music_original(music_string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # The postcondition asserts that if the input music_string is empty, the return_value is an empty list.
    # Otherwise, it asserts that the return_value is a list where each element corresponds to the correct beat count
    # for the respective note in the music_string, following the specified mapping: 'o' -> 4, 'o|' -> 2, '.|' -> 1.
    assert (music_string == "" and return_value == []) or \
           (music_string != "" and \
            return_value == list(map(lambda note: 4 if note == "o" else (2 if note == "o|" else 1), music_string.split(" "))))
    

    return return_value
