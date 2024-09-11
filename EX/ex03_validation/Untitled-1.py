old_pass = "eva1970" # == "0791ave"
new_pass = "0791ave"
matching_value = 0

for i in reversed(old_pass):
    for x in new_pass:
        if x == i:
            matching_value += 1
    else:
        matching_value -= 1

if matching_value == 0:
    print(True)
else:
    print(len(old_pass) / matching_value < 0.5)
