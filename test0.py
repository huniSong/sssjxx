from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'todo' in browser.title, "Brower title was " + browser.title
