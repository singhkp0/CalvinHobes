from selenium import webdriver
import pyautogui
import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os, sys, csv
import smtplib
from email import Encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

chromedriver = "C://Users//Kamal//Desktop//chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()
chrome_options.add_argument("test-type")
#chrome_options.add_argument("user-data-dir=C:/Users/kamaldeep.singh/AppData/Local/Google/Chrome/UserData")
chrome_options.add_argument("user-data-dir=C:/Users/Kamal/AppData/Local/Google/Chrome/UserData")
browser = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)
browser.get('http://www.gocomics.com/calvinandhobbes')
comic=browser.find_elements_by_tag_name('img')
#browser.get(comic[3].get_attribute('src'))

import urllib
urllib.urlretrieve(comic[4].get_attribute('src'), "C:/Users/Kamal/Desktop/CH/CH_%s.jpg" %datetime.datetime.now().strftime("%Y%m%d"))

gmail_user = "k******@gmail.com"
gmail_pwd = "*****"

strFrom ='<kamal23444@gmail.com>'
#strTo = ' thomas.kurian@tredence.com, pankaj.gupta@tredence.com, vjk01101991@gmail.com, chirag.jain@tredence.com,bijay.mohapatra@tredence.com' # Receivers Email ID
strTo = 'vjk01101991@gmail.com'

attachment = "C:/Users/Kamal/Desktop/CH/CH_%s.jpg" %datetime.datetime.now().strftime("%Y%m%d")

msg = MIMEMultipart()
msg["To"] = 'aakshi.sharma1010@gmail.com'
msg["From"] = 'kamal23444@gmail.com'
msg["Subject"] = 'Happy Comic of the Day'

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % ('Good Morning', attachment), 'html')  
msg.attach(msgText)   # Added, and edited the previous line

fp = open(attachment, 'rb')                                                    
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

# Send the email (this example assumes SMTP authentication is required)
mailServer = smtplib.SMTP("smtp.gmail.com:587")
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.set_debuglevel(1)
mailServer.sendmail(gmail_user, strTo.split(',') , msg.as_string())
# Should be mailServer.quit(), but that crashes...
mailServer.close()
print 'done'
browser.close()
sys.exit()
