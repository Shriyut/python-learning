import re

test_string = "prefix#ACCT-000000#suffix"
pattern=r"^[^#]*#ACCT-000000#"
if re.match(pattern, test_string):
    print("Match found!")
else:
    print("No match.")