import requests
from bs4 import BeautifulSoup
import pandas as pd

# 豆瓣电影TOP250的基础URL
base_url = 'https://movie.douban.com/top250'

# 定义一个函数来获取页面内容
def get_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print('请求页面失败:', response.status_code)
        return None

# 定义一个函数来解析页面内容
def parse_page_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    movie_list = soup.find_all('div', class_='item')
    movies = []
    for movie in movie_list:
        title = movie.find('span', class_='title').get_text()
        rating = movie.find('span', class_='rating_num').get_text()
        # director = movie.find('p', class_='').find('a').text
        movies.append({'title': title, 'rating': rating})
    return movies

# 定义一个函数来保存数据到CSV文件
def save_to_csv(movies):
    df = pd.DataFrame(movies)
    df.to_csv('douban_top250.csv', index=False, encoding='utf_8_sig')

# 主函数，用于运行爬虫
def main():
    movies = []
    print("豆瓣 top250 爬取开始...")
    for i in range(0, 250, 25):  # 豆瓣电影TOP250分为10页，每页25部电影
        url = f'{base_url}?start={i}&filter='
        html = get_page_content(url)
        if html:
            # print('第一页OK')
            movies.extend(parse_page_content(html))
    save_to_csv(movies)
    print('爬取完成，数据已保存到douban_top250.csv')


# 运行主函数
if __name__ == '__main__':
    main()
