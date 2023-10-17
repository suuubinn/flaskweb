import requests
from bs4 import BeautifulSoup

def get_movie_info(url_receive):
    headers = {
        # User-Agent는 접속한 클라이언트 정보
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # html 읽어오기
    data = requests.get(url_receive, headers=headers)
    # 파싱 준비
    soup = BeautifulSoup(data.text, 'html.parser')
    # 파싱
    title = soup.select_one('div.title_area.type_keep._title_area > h2 > span > strong').get_text()
    image = soup.select_one('div.cm_info_box > div.detail_info > a > img')['src']
    desc = soup.select_one('div.cm_info_box > div.detail_info > div > span').get_text()
    return title, image, desc
