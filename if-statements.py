
is_male = True
is_tall = True

if is_male or is_tall:
    print("or--You are a male or tall or both")
else:
    print("or--You are neither male nor tall")

if is_male and is_tall:
    print("and--You are a tall male")
elif is_male and not is_tall:
    print("and--You are a short male")
elif not is_male and is_tall:
    print("and--You are not a male, but are tall")
else:
    print("and--You are not a male and not tall")
