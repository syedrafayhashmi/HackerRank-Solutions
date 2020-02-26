from selenium import webdriver

driver = webdriver.Chrome('R:/Python_Codes/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of user or Group: ")
msg = input("Enter Your Message: ")
count = int(input("Enter the number of messages: "))

input("Scan QR Code and hit any Key")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for x in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()