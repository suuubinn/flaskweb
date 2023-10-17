from utils import get_movie_info

def test_get_movie_info():
    # 샘플 url
    test_url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=185293"
    # 함수를 호출해서 값을 가져오기 - 파싱이 제대로 됐는지 확인
    title, image, desc = get_movie_info(test_url)
    print(title)
    print(image)
    print(desc)
    assert title == "내일의 기억"
    #assert image == "https://search.pstatic.net/common?type=o&size=174x242&quality=85&direct=true&src=https%3A%2F%2Fs.pstatic.net%2Fmovie.phinf%2F20210406_131%2F1617688160755B157W_JPEG%2Fmovie_image.jpg%3Ftype%3Dw640_2"
    