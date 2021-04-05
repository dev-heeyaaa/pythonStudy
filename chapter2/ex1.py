from selenium import webdriver
import time

driverPath = "C:/Users/ITPS/Desktop/driver/chromedriver.exe"

URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)


#  selenium의 기본 대기시간은 0초

# selenium의 기본 대기 시간을 10초로 설정
driver.implicitly_wait(10)

# elementList = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
# print(elementList)
#
# for element in elementList:
#     print(element)

# element = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]')
# # xpath도 상대평가가 있다
# # xpath 그냥 상대적 xpath
# # full xpath는 절대
#
# print(element)
#
# element = driver.find_elements_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]')
# print(element)
#
element = driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(3)')

element.click()

time.sleep(2)
# 클릭 후 2초 쉬어라

print("현제 페이지에서 뒤로 가기")
driver.back()
time.sleep(2)

print("현재 페이지에서 앞으로 가기")
driver.forward()
time.sleep(2)

print("현재 페이지에서 새로고침")
driver.refresh()
time.sleep(2)

print("현재 페이지에서 스크린샷 저장")
driver.save_screenshot("save.png")
time.sleep(2)

# 현재 탭이 닫히는 것! (현재 보고있는 탭을 닫음)
# 브라우저 내 탭이 하나였다면 탭을 닫으면서 브라우저도 닫힘
print("브라우저 닫기")

driver.close()

# # 브라우저 자체를 아예 닫아버림 (탭이 여러개 있었으면 강제로 다 닫힘)
# driver.quit()

#

# 계속 오류가 나면 다른 태그네임으로 찾든지 아이디로 찾든지...
# print("=============== ===============")
# # 두 번째 요소들을 1. css 선택자 2. xpath를 사용해서 요소를 선택하고 출력하세요
# elementList2 = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
# for element2 in elementList2:
#     print(element2)
# print("=============== ===============")
# elementList3 = driver.find_elements_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div')
# for element3 in elementList3:
#     print(element3)

# 드라이버 객체: 현재 페이지와 관련된 정보를 가지고 있음