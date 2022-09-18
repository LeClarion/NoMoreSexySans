import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.naver.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["green", "pink"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "Nartuur입니다.")
write("description", "잘 부탁드립니다.")
write("button", "ㅗ")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "정보) "
  "샌즈": "섹시함",
  "파피루스": "귀여움",
  "나": "잘생김",
  "이 사이트에 접속한 ": "못생김;;;;;;"
}
information(informations)
