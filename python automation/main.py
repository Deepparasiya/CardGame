import requests
from colorama import Fore, Back, Style

requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text

r = requests.get("https://manageengine.com/", verify=False)
print(format_text('status code is: ', r.status_code))
print(format_text('Header is: ', r.headers))
print(format_text('Cookies are: ', r.cookies))
print(format_text('Text is: ', r.text))