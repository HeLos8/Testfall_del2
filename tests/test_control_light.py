import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    _driver = webdriver.Chrome()
    _driver.get("http://localhost:5000")
    yield _driver
    _driver.quit()

def test_control_light_on(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "room-input"))) #väntar 10s tills elementet är
    #synligt på sidan innan koden fortsätter.
    room_input = driver.find_element(By.ID, "room-input") #hittar textfältet för rumnamn
    room_input.send_keys("living room") #skriver in texten "living room" i textfältet

    state_dropdown = driver.find_element(By.ID, "state-dropdown") #hittar dropdown menyn för att välja
    #ljusets tillstånd
    state_dropdown.send_keys("on") #väljer "on" i dropdown menyn

    control_button = driver.find_element(By.ID, "control-button") #Hittar knappen för att aktivera ljuset
    control_button.click() #klickar på knappen

    status_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "status-message")) #väntar upp till 10s på att meddelandet ska visas
    ).text

    assert "Light in living room is on" in status_message #kontrollerar att den faktiska texten i statusmeddelandet innehåller
    #det förväntade värdet. Om inte den gör det så misslyckas testet.

def test_control_light_off(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "room-input"))) #väntar upp till 10s på att villkoret
    #uppfylls innan skriptet fortsätter
    room_input = driver.find_element(By.ID, "room-input") #hämtar element från sidan med ID "room-input"
    room_input.clear() #rensar ev befintlig text från textfältet.
    room_input.send_keys("living room") #simulerar en användare som skriver in texten "living room" i textfältet

    state_dropdown = driver.find_element(By.ID, "state-dropdown")
    state_dropdown.send_keys("off") #väljer alternativet "off" från dropdown menyn

    control_button = driver.find_element(By.ID, "control-button") #hämtar element "control-button" (knapp på webbsidan)
    control_button.click() #utför en musklickning på knappen
    
    status_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "status-message")) #säkerställer att status-message elementet finns på websidan   
    ).text

    assert "Light in living room is off" in status_message #kontrollerar att den hämtade texten innehåller "Light in living room is off"
