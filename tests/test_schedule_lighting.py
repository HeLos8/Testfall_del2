import pytest #pytest-ramverk som används för att skapa och köra testfall
from selenium import webdriver #importerar webdriver-modul från selenium för att automatisera webbläsarinteraktioner
from selenium.webdriver.common.by import By #importerar By-klassen som används för att identifiera element i webbsidan
from selenium.webdriver.support.ui import WebDriverWait #importerar WebDriverWait-klassen för att kunna vänta
#på ett villkor innan man fortsätter körning av koden
from selenium.webdriver.support import expected_conditions as EC #importerar modulen för förväntade villkor

@pytest.fixture #en funktion som körs innan/efter testfall, för setup/teardown testmiljön
def driver():
    _driver = webdriver.Chrome() #skapar en ny chrome webbläsarinstans
    _driver.implicitly_wait(10)
    _driver.get("http://localhost:5000") #öppnar webbläsaren på en angiven URL
    yield _driver #returnerar webdriver-objektet till testfallen
    _driver.quit() #stänger webbläsare och avslutar webdriver session

def test_schedule_lighting_on(driver):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "room-input-schedule")))
    room_input = driver.find_element(By.ID, "room-input-schedule") #lokaliserar fältet för rummet
    room_input.send_keys("bedroom") #bedroom skrivs in i fältet
    
    time_input = driver.find_element(By.ID, "time-input") #lokaliserar tidsinmatningsfältet
    time_input.send_keys("18:00") #sätter tiden till 18:00
    
    state_dropdown = driver.find_element(By.ID, "state-dropdown-schedule") #lokaliserar dropdown menyn för ljusets tillstånd
    state_dropdown.send_keys("on") #sätter den till "on"
    
    submit_button = driver.find_element(By.ID, "submit-schedule") #hittar knappen för schemaläggningsförfrågan
    submit_button.click() #klickar på knappen
    
    success_message = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "success-message"), "Scheduled on for bedroom at 18:00")
    ) #väntar för att se meddelandet på sidan, vilket betyder att schemat ställdes framgångsrikt

def test_schedule_lighting_off(driver):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "room-input-schedule")))
    room_input = driver.find_element(By.ID, "room-input-schedule")
    room_input.clear() #rummets inmatningsfält rensas
    room_input.send_keys("kitchen") #skriver in "kitchen"
    
    time_input = driver.find_element(By.ID, "time-input") #lokaliserar tidsinmatningsfältet
    time_input.clear() #rensar tidsinmatningen
    time_input.send_keys("22:00") #sätter tiden till 22:00
    
    state_dropdown = driver.find_element(By.ID, "state-dropdown-schedule") #lokaliserar dropdown fältet för state
    state_dropdown.send_keys("off") #sätter den till "off"
    
    submit_button = driver.find_element(By.ID, "submit-schedule") #lokaliserar schemaläggningsknappen
    submit_button.click() #klickar på knappen
    
    success_message = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "success-message"), "Scheduled off for kitchen at 22:00")
    ) #kontrollerar att meddelandet visar "Scheduled off for kitchen at 22:00"
