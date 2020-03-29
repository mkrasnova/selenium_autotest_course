from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
with open("test.txt", "w") as file:
    content = file.write("automation by python")  # create test.txt file

try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    elements = browser.find_elements_by_class_name('form-control')
    for element in elements:
        element.send_keys("Мой ответ")
    browser.find_element_by_id('file').send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
