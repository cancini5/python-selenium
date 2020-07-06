#_*_coding: utf-8_*_

from selenium import webdriver
import time
from bs4 import BeautifulSoup


ytLiveChatUrl="https://www.youtube.com/live_chat?v=iBlqEQd86_Q&is_popout=1"
# start web browser
browser=webdriver.Firefox()

# get source code
browser.get(ytLiveChatUrl)
html = browser.page_source
time.sleep(2)

soup = BeautifulSoup(html, 'html.parser')
messages=soup.find_all("yt-live-chat-text-message-renderer")
for message in messages:
    content=message.find("div",{"id":"content"})
    author=content.find("span",{"id":"author-name"}).text
    message_content=content.find("span",{"id":"message"}).text
    
    print(author,message_content)





# close web browser
browser.close()