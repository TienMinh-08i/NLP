def bf_original(planet1, planet2):
    """
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    i1, i2 = (planets.index(planet1), planets.index(planet2))
    if i1 > i2:
        i1, i2 = (i2, i1)
    return tuple(planets[i1 + 1:i2])


def bf(planet1, planet2):


    return_value = bf_original(planet1, planet2)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that if either input planet is not a valid name, the function returns an empty tuple.
    # Otherwise, it verifies that the returned value is a tuple containing all planets located between the two input planets (exclusive),
    # sorted by their proximity to the sun, regardless of the order in which the input planets were provided.
    planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    assert ((planet1 not in planets_list or planet2 not in planets_list) and return_value == ()) or \
           ((planet1 in planets_list and planet2 in planets_list) and \
            return_value == tuple(planets_list[min(planets_list.index(planet1), planets_list.index(planet2)) + 1 : \
                                               max(planets_list.index(planet1), planets_list.index(planet2))]))

    return return_value
