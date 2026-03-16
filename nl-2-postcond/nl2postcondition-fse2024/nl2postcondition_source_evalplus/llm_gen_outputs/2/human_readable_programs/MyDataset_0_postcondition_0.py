# The return_value is a callable decorator that returns the class it is applied to, provided the input name is a string.
assert isinstance(name, str) and callable(return_value) and (lambda cls: return_value(cls) is cls)(type('DummyAccessor', (), {}))


