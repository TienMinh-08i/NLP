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


