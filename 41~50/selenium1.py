from selenium import webdriver
driver=webdriver.Chrome(R"C:\Users\Nagata Kento\Downloads\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
driver.get('https://www.library.chiyoda.tokyo.jp/')

schedule_el= driver.find_elements_by_class_name('schedule-list01__text')
print([s.text for s in schedule_el])

#わからない