from selenium import webdriver
import time
import app
from selenium.webdriver import ActionChains
from datetime import datetime
import time

# datetime.datetime.now() # datetime 모듈 안에 있는 datetime 클래스에 있는 now 메소드를 사용한다

driverPath = "C:/Users/ITPS/Desktop/driver/chromedriver.exe"

URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)

driver.implicitly_wait(10)

element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz.Knqxbd.tzLNed.Mfkobe > ul > li.uQeS5e.qKjvAb.iZhiic > a > span")
element.click()


element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz:nth-child(3) > c-wiz > div > div > div > div:nth-child(4) > div > a")
element.click()


element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.Z3lOXb > div.xwY9Zc > a")
element.click()


# 순위를 수집하는 코드
firstElementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(6) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div")

# 수집한 순위의 마지막 요소
# elementLis[0] = 1위 앱의 요소
# elementList[1] = 2위 앱의 요소
lastElement = firstElementList[-1]

# 마지막 요소로 스크롤을 이동시켜라
ActionChains(driver).move_to_element(lastElement).perform()
# 페이지에 들어가자마자 50위까지의 순위 수집
# 스크롤을 내려서 새롭게 불러온 순위 수집


# 51~200위까지
for i in range(1, 4): # 3번 돌려라
    time.sleep(1)
    elementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(6) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz")

    # 수집한 순위의 마지막 요소
    # elementLis[0] = 1위 앱의 요소
    # elementList[1] = 2위 앱의 요소
    lastElement = elementList[-1]

    # 마지막 요소로 스크롤을 이동시켜라
    ActionChains(driver).move_to_element(lastElement).perform()

# firstElemnetList = 1~ 50위까지 앱 요소
# elementList = 50~200위까지 앱 요소
elementList = firstElementList + elementList
appInfoList = []

# 앱의 데이터를 뽑아서 객체에 저장
for element in elementList:
    
    appName = element.find_element_by_css_selector(".WsMG1c.nnK0zc")
    appName = appName.text

    companyName = element.find_element_by_css_selector(".KoLSrc")
    companyName = companyName.text

    imgPath = element.find_element_by_css_selector(".T75of.QNCnCf")
    imgPath = imgPath.get_property("src") # 속성의 값을 가지고 올 수 있음

    star = element.find_element_by_css_selector("div.pf5lIe div") # div.pf5lIe 밑의 div 태그에서 찾아라
    star = star.get_attribute("aria-label")
    star = star[10:13]
    # property와 attribute 메소드의 차이?

    element.click()

    print("카테고리 수집")
    category = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(1) > c-wiz:nth-child(1) > div > div.D0ZKYe > div > div.sIskre > div > div.ZVWMWc > div:nth-child(1) > span:nth-child(2) > a")
    category = category.text

    print("리뷰 작성자의 수집")
    reviewPeople = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(1) > c-wiz:nth-child(1) > div > div.D0ZKYe > div > div.sIskre > div > div.dNLKff > c-wiz > span > span:nth-child(1)")
    reviewPeople = reviewPeople.text

    print("별점별 비율 수집")
    star5Rate = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(1) > span.L2o20d.P41RMc")
    star5Rate = star5Rate.get_attribute("style")

    star4Rate = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(2) > span.L2o20d.tpbQF")
    star4Rate = star5Rate.get_attribute("style")

    star3Rate = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(3) > span.L2o20d.Sthl9e")
    star3Rate = star5Rate.get_attribute("style")

    star2Rate = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(4) > span.L2o20d.rhCabb")
    star2Rate = star5Rate.get_attribute("style")

    star1Rate = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > div > div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(5) > span.L2o20d.A3ihhc")
    star1Rate = star5Rate.get_attribute("style")



    print("뒤로가기 순위 페이지로 돌아감")
    driver.back()

    appInfo = app.AppInfo(appName, companyName, imgPath, star, category, reviewPeople, star5Rate, star4Rate, star3Rate, star2Rate, star1Rate)
    appInfoList.append(appInfo)



# print("가져온 앱의 개수 = ", len(appInfoList))
#
# for appInfo in appInfoList:
#     print("%s / %s" % (appInfo.getAppNAme(), appInfo.getCompanyName()))

# 현재 탭을 닫아라 (현재 탭이 하나밖에 없으면 브라우저가 닫힘)


today = datetime.now()
# ex)20210407
today = today.strftime("%Y%m%d")

# with open("파일경로", "스트립", encoding=) as file:
# csv는 콤마(,)로 구분된 데이터를 넣음?(확장자)
# tsv는 탭으로 구분된 데이터를 넣는 확장자
with open("C:/Users/ITPS/Desktop/app_rank/"+today+".tsv", "w", encoding="UTF-8") as file:
    file.write("앱이름\t서비스회사\t앱이미지\t별점\t카테고리\t리뷰작성자의수\t별점5의비율\t별점4의비율\t별점3의비율\t별점2의비율\t별점1의비율\n")

    for appInfo in appInfoList:
        appName = appInfo.getAppName()
        companyName = appInfo.getCompanyName()
        imgPath = appInfo.getImgPath()
        star = appInfo.getStar()
        category = appInfo.category
        reviewPeople = appInfo.reviewPeople
        star5Rate = appInfo.star5Rate
        star4Rate = appInfo.star4Rate
        star3Rate = appInfo.star3Rate
        star2Rate = appInfo.star2Rate
        star1Rate = appInfo.star1Rate

        file.write(appName+"\t"+companyName+"\t"+imgPath+"\t"+star+"\t"+category+"\t"+reviewPeople+"\t"+star5Rate+"\t"+star4Rate+"\t"+star3Rate+"\t"+star2Rate+"\t"+star1Rate+"\n")

    # 문제가 생기는데 그 문제는 수업자료를 통해 알아보고 해결해 보기!
driver.close()
