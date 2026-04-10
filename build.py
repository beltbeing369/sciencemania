
import json
import os

def build_site():
    articles_html = ""
    article_files = [f for f in os.listdir('articles') if f.endswith('.json')]
    
    # 1. 기사 파일들을 읽어서 리스트에 담기
    data_list = []
    for file in article_files:
        with open(f'articles/{file}', 'r', encoding='utf-8') as f:
            data_list.append(json.load(f))
    
    # 2. 최신순 정렬
    data_list.sort(key=lambda x: x['date'], reverse=True)
    
    # build.py의 3번 기사 변환 부분 수정
for art in data_list:
    img_tag = f'<img src="{art.get("image", "")}" style="max-width:100%">' if art.get("image") else ""
    articles_html += f"""
    <div class="article">
        <h2>{art['title']}</h2>
        {img_tag}
        <p class="date">{art['date']} | 작성자: {art['author']}</p>
        <p>{art['content']}</p>
    </div>
    """
    
    # 4. 템플릿 파일 읽기
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 5. {{ ARTICLES }} 부분을 기사 내용으로 교체
    final_html = template.replace('{{ ARTICLES }}', articles_html)
    
    # 6. 최종 index.html 저장
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    build_site()
