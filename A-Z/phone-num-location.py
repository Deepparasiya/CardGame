import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


num = str(input("Enter the number: "))
pn = phonenumbers.parse(num, "CH")

print(geocoder.description_for_number(pn, "en"))


servnbr = phonenumbers.parse(num, "RO")

print(carrier.name_for_number(servnbr, "en"))

# +919619229780