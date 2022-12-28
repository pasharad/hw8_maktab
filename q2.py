import re
user_input = 'TheFirstProgramingBootCamp'
x = re.sub(r'(\w)([A-Z])', r"\1 \2", user_input)
print(x)

