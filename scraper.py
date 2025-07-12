import os, requests, bs4

res = requests.get('news.ycombinator.com')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

titles = soup.select(".title")
with open('titles.txt', 'w') as file:
    i = 0
    for title in titles:
        file.write(f"{i+1}.{title.get_text()} \n")
        i+=1

os.startfile('titles.txt')  # This will open the file in the default text editor on Windows
# Note: os.startfile() is specific to Windows. For cross-platform compatibility, consider using:

print("Titles saved to titles.txt")
