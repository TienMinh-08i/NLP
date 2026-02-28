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
    
    
    # The postcondition checks three things:
    # 1. The length of the returned list matches the number of notes in the input string (handling the empty string explicitly and splitting by single spaces).
    # 2. All elements in the returned list are valid beat counts (1, 2, or 4).
    # 3. Each beat count in the returned list corresponds correctly to its respective note in the input string according to the specified mapping.
    assert (
        # Condition 1: Check if the length of the return_value matches the number of notes in music_string.
        # The parse_music function explicitly returns [] for an empty string.
        # For non-empty strings, it splits by " ".
        len(return_value) == (
            0 if music_string == "" else len(music_string.split(" "))
        )
        and
        # Condition 2: Check if all elements in the return_value are valid beat counts (1, 2, or 4).
        # This implicitly catches cases where `count_beats` might return None for unrecognized notes.
        all(map(lambda beat: beat in [1, 2, 4], return_value))
        and
        # Condition 3: Check if each note in the input string maps to its correct beat value in the return_value.
        # We zip the split notes with the returned beats and verify each pair against the defined mapping.
        all(map(lambda item: (item[0] == "o" and item[1] == 4) or
                               (item[0] == "o|" and item[1] == 2) or
                               (item[0] == ".|" and item[1] == 1),
                zip(music_string.split(" "), return_value)))
    )
    

    return return_value
