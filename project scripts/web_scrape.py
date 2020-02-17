import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.imdb.com/title/tt0145487')
# print(response.content)
#print(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.find(class_='cast_list'))
print(soup.find(text='Budget:').parent.parent)
budget = soup.find(text='Budget:').parent.parent
print(budget)
budget_val = budget.find('h4').next_sibling
b = ''
for n in budget_val:
    if(n.isdigit()):
        b = b + n

print(b)
# table = soup.find_all(class_='cast_list')
# print(table.find_all('a'))