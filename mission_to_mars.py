
# coding: utf-8

# In[117]:


# Import BeautifulSoup for parsing and splinter to navigate site
from splinter import Browser
from bs4 import BeautifulSoup
import os


# In[118]:


# Load Chromedriver and prep the browser
filepath = {'executable_path': './chromedriver'}
browser = Browser('chrome', **filepath)


# In[119]:


## NASA MARS NEWS. Title and Paragraph.


# In[120]:


# Visit the NASA news URL to collect the latest News Title and Paragraph
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)


# In[121]:


# Scrape page into BeautifulSoup
news = BeautifulSoup(browser.html, 'html.parser')


# In[122]:


# Collect the latest News Title
news_item = news.find('div', class_='content_title')


# In[123]:


news_title = news_item.text
news_title


# In[124]:


# Collectthe latest Paragraph
news_para = news.find('div', class_='article_teaser_body').text


# In[125]:


# Display the Paragraph
news_para


# In[126]:


# JPL MARS SPACE IMAGES.


# In[127]:


# Visit the JPL Mars URL to begin scraping to collect image
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[128]:


browser.visit(image_url)


# In[129]:


# Click Full Image Button
full_image_element = browser.find_by_id('full_image')
full_image_element.click()


# In[130]:


# Click More Info Button
more_info_element = browser.find_link_by_partial_text('more info')
more_info_element.click()


# In[131]:


# Create new BeautifulSoup Object
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[132]:


# Display Image URL link for hi res image.
img_url = img_soup.find('figure', class_='lede').find('img')['src']
img_url


# In[133]:


# Adding the complete link to the hi res image listed above.
base_url = f"https://www.jpl.nasa.gov{img_url}"


# In[134]:


# Display the complete link of the image.
base_url


# In[135]:


# MARS WEATHER
# Visit the Mars Weather Twitter Account and Scrap the Latest Mars Weather Tweet.
# tweepy not needed


# In[136]:


# get mars weather from mars twitter
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[137]:


weather_html = browser.html
weather_soup = BeautifulSoup(html3, 'html.parser') 


# In[138]:


tweets = weather_soup.find_all('p', 'tweet-text')


# In[139]:


weather_tweet = ''
for tweet in tweets:
    if tweet.text.split()[0] == 'Sol':
        weather_tweet = tweet.text
        print(tweet.text)
        break


# In[140]:


weather_tweet


# In[141]:


# MARS FACTS
# Use Pandas to scrape the table containing facts about the planer including Diameter, Mass, etc.


# In[142]:


# Visit the website to gather Mars Facts.
facts_url = 'http://space-facts.com/mars/'
browser.visit(facts_url)


# In[143]:


# Place Data Into a DataFrame,convert the Data to a HTML Table String.
import pandas as pd
fact_list = pd.read_html(facts_url)
facts_df = fact_list[0]
facts_table = facts_df.to_html(header=False, index=False)
print(facts_table)  


# In[144]:


# MARS HEMISPHERES Visit the USGS Astrogeology site to obtain high resolution images for each of Mars' hemispheres.


# In[145]:


# Go to USGS website
usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(usgs_url)
# URL Data and sends to BeautifulSoup
usgs_html = browser.html                            
usgs_soup = BeautifulSoup(usgs_html, 'html.parser') 
hemisphere_image_urls = []                                                   # Creates empty list

products = usgs_soup.find('div', class_='result-list')                       # finds products
hemispheres = products.find_all('div', class_='item')                        # finds hemispheres
# Loops gathering Data:
for hemisphere in hemispheres:                                               # iterates through hemispheres
    title = hemisphere.find('div', class_='description')
    
    title_text = title.a.text                                                # extracts cleaned title
    title_text = title_text.replace(' Enhanced', '')
    browser.click_link_by_partial_text(title_text)                           # (automated) click
    
    usgs_html = browser.html                                                 # acquires response from URL
    usgs_soup = BeautifulSoup(usgs_html, 'html.parser')                                 # sends response to beautiful soup
# Extracts Image URL.
    image = usgs_soup.find('div', class_='downloads').find('ul').find('li')  # extracts image url
    img_url = image.a['href']
# Adds Dictionary to the List   
    hemisphere_image_urls.append({'title': title_text, 'img_url': img_url})  # adds dictionary to list  
    
    browser.click_link_by_partial_text('Back')                               # (automated) click back


# In[146]:


# Display the List of Dictionaries:
hemisphere_image_urls                                                        # displays list of dictionaries


# In[147]:


# Close Browser
browser.quit()

