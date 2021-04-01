import requests

url = ''
param_dic= {}

# fullURL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=161967'
fullURL = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
fullURL = fullURL.split("?")

try:
    url = fullURL[0]
    parameter = fullURL[1]

    parameter = parameter.split("&")


    for param in parameter:
        param = param.split("=")
        print(param)

        param_dic[param[0]] = param[1]

except IndexError:
    print("파라미터가 없는 URL입니다.")


# print(param_dic)

response = requests.get(url, param_dic)
print(response.text)

# file = open("C:/Users/ITPS/Desktop/wow.txt", "w")
# file.write(response.text)
# file.close()

