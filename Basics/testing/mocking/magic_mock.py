from unittest.mock import Mock, MagicMock

# a magic mock supports magic methods(dunder methods) but mock does not
# better to use magic mock by default

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock)) # throws TypeError
print(len(magic_mock))
print(magic_mock[1000])
print(magic_mock.__len__)
magic_mock.__len__.return_value = 50
print(len(magic_mock))