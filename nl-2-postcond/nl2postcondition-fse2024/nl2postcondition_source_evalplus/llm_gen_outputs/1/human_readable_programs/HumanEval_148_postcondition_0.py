# The postcondition verifies that if either input planet is not a valid name, the function returns an empty tuple.
# Otherwise, it verifies that the returned value is a tuple containing all planets located between the two input planets (exclusive),
# sorted by their proximity to the sun, regardless of the order in which the input planets were provided.
planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
assert ((planet1 not in planets_list or planet2 not in planets_list) and return_value == ()) or \
       ((planet1 in planets_list and planet2 in planets_list) and \
        return_value == tuple(planets_list[min(planets_list.index(planet1), planets_list.index(planet2)) + 1 : \
                                           max(planets_list.index(planet1), planets_list.index(planet2))]))


