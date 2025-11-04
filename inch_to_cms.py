headline = "you can change into inch to cms"
width = 50
print(headline.center(width))

def inch_to_cms(inch):
    return inch*2.54

c = int(input("Enter your number for inch: "))

print(f"the cms is {inch_to_cms(c)}")
print()

headline = "you can change into cms to inch"
width = 50
print(headline.center(width))

def cms_to_inch(cms):
    return cms*0.393701

i = int(input("Enter your cms: "))

print(f"your inch is {cms_to_inch(i)}")