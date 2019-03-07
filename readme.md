# apply.likelion Crawling Source

* bs4 하고 selenium 써서 셋팅이 필요

## Getting Started

### 1. Install chrome driver

* 조금 길어서, 구글링 or 예전에 작성 해둔 것  <a href="https://github.com/Nuua-1team/TripadvisorCrawler">첨부 </a>

### 2. Install bs4 , selenium

```bash
pip3 install bs4 selenium
```

### 3. _id , _password setting

##### 프로젝트 폴더 안에 ```env.py``` 를 만들고 그안에 계정 정보를 입력

```python
_id = "your@email"
_password = "password"
```

### 4. Run

```bash
python3 parser.py
```



