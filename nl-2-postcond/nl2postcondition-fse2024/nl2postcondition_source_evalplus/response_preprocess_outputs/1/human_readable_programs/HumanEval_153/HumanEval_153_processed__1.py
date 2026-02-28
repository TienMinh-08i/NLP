def Strongest_Extension_original(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    def strength(s: str) -> int:
        CAP, SM = (0, 0)
        for ch in s:
            if ch.isupper():
                CAP += 1
            if ch.islower():
                SM += 1
        return CAP - SM
    max_strength = max(map(strength, extensions))
    for e in extensions:
        if strength(e) == max_strength:
            return class_name + '.' + e


def Strongest_Extension(class_name, extensions):


    return_value = Strongest_Extension_original(class_name, extensions)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that the returned value is correctly formatted as ClassName.StrongestExtensionName,
    # and that the chosen extension is indeed the strongest one based on the CAP-SM metric,
    # adhering to the tie-breaking rule (first occurrence in the list wins).
    assert (
        # 1. The return value must start with the class name followed by a dot.
        return_value.startswith(class_name + ".") and
        # 2. Extract the extension name part from the return value.
        # The walrus operator (:=) assigns the extracted extension to 'chosen_extension' for later use.
        (chosen_extension := return_value[len(class_name) + 1:]) and
        # 3. The extracted extension must be present in the original list of extensions.
        chosen_extension in extensions and
        # 4. Get the index of the chosen extension for tie-breaking comparison.
        # The walrus operator assigns the index to 'chosen_idx'.
        (chosen_idx := extensions.index(chosen_extension)) and
        # 5. Verify that no other extension is "stronger" or comes earlier with the same strength.
        # This is checked by iterating through all extensions and their indices.
        all(
            # For each extension 'e' at its index 'i' in the list:
            # It must either have a strictly lower strength than the chosen_extension,
            strength(e) < strength(chosen_extension) or
            # Or, if it has the same strength, it must appear at or after the chosen_extension's index.
            # This condition handles the tie-breaking rule.
            (strength(e) == strength(chosen_extension) and i >= chosen_idx)
            for i, e in enumerate(extensions)
        )
    )

    return return_value
