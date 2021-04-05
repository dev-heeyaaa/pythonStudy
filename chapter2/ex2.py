from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driverPath = "C:/Users/ITPS/Desktop/driver/chromedriver.exe"

URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)

driver.implicitly_wait(10)

# element 상황마다 계속 업데이트
elementList = driver.find_elements_by_css_selector(".WHE7ib.mpg5gc")
for element in elementList:
    elementName = element.find_element_by_css_selector(".WsMG1c.nnK0zc") # .이 붙으면 클래스 선택자 # 앱의 이름을 갖고있는 엘리먼트를 찾고
    elementName = elementName.text # 그 엘리멘트가 갖고있는 이름을 엘리먼트에 저장
    print(elementName, "페이지에 접속") # 무슨 내용인지 이해가 좀???

    element.click()
    time.sleep(1)

    driver.back()


# print("id =  ",element.id)
# print("tag name = ",element.tag_name)
# print("locaton = ",element.location)
# print("element.location_once_scrolled_into_view = ",element.location_once_scrolled_into_view)
# print("size = ",element.size)
# print("rect = ",element.rect)
# print("text = ", element.text)
# print("parent = ",element.parent)
#
# # attribute 나 property나 element의 속성값
# print(element.get_attribute("href"))
# print(element.get_property("class"))
#
# print(element.is_displayed())
# print(element.is_enabled())
# print(element.is_selected())
#
# # driver는 현재 페이지를 elememt는 내가 선택한 요소를!
#
# print(element.value_of_css_property("position"))
# print(element.screenshot("element.png"))

# 검색어 영역을 선택해서 검색하기
# element.send_keys("네이버")
# time.sleep(1)
#
# # element = driver.find_element_by_css_selector("#gbqfb > span")
# # element.submit() # 검색 버튼을 선택해서 클릭
# element.send_keys(Keys.ENTER)
# time.sleep(1)

# 검색 영역에 코리아 교육 그룹이라고 입력하고 해당 앱을 검색하고자 함

# element.send_keys(Keys.BACKSPACE)
# element.send_keys(Keys.BACKSPACE)
# element.send_keys(Keys.BACKSPACE)
#
# element = driver.find_element_by_css_selector("#gbqfq")
# # element.clear()
# element.send_keys("코리아교육그룹")
# time.sleep(1)
#
# element.send_keys(Keys.ENTER) # 엔터
# time.sleep(1)

