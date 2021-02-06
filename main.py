# instagram bot
from time import sleep

from selenium import webdriver
from sensible import mdp


class InstaBot:
    def __init__(self,username,mdp):
        self.userName = username
        #on definit le moteur de recherche que l'on va utiliser
        self.driver = webdriver.Chrome('C:/Users/uriel/chromedriver.exe')
        #on utilse la fonction get("url") pour accéder a la page web
        self.driver.get("https://www.instagram.com/?hl=fr")
        sleep(1) #maintient la page ouvere ( ne pas oublier de import time quand utiliser)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accepter')]").click()
        # xpath query qui fonctionne aussi pour les lien //a ou autre[contains(text(), 'Accepter')] et on ajoute la fonction click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.userName)  # la fonction send_keys() permet d'envoyer des informatons sur le site , dans le cas présent de remplir le champs username
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(mdp)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Plus tard')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Plus tard')]").click()


    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.userName)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        sleep(5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
             return arguments[0].scrollHeight;
             """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        sleep(2)
        names = [name.text for name in links if name.text != '']
        sleep(2)
        print(names)
        #self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        # done TypeError: 'WebElement' object is not iterable  -> utiliser webelement's' 
 


Bots = InstaBot('***********',mdp)
Bots.get_unfollowers()
