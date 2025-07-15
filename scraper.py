import os, requests, bs4

res = requests.get('https://news.ycombinator.com')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Select only the main story titles and their links
titles = soup.select('.titleline a')

with open('titles.txt', 'w', encoding='utf-8') as file:
    for i, title in enumerate(titles, 1):
        text = title.get_text(strip=True)
        url = title['href']
        file.write(f"{i}. {text} ({url})\n")

os.startfile('titles.txt')  # This will open the file in the default text editor on Windows

print("Titles saved to titles.txt! Star on github if you liked it!")