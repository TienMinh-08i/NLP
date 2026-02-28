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
    
    # The postcondition ensures that the length of the return_value matches the number of notes in the music_string and that each element in the return_value correctly represents the beat count of the corresponding note ('o' is 4, 'o|' is 2, and '.|' is 1).
    assert len(return_value) == (len(music_string.split(" ")) if music_string else 0) and all(v == (4 if n == 'o' else 2 if n == 'o|' else 1 if n == '.|' else None) for n, v in zip(music_string.split(" ") if music_string else [], return_value))
    

    return return_value
