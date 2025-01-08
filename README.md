# Get work timetable information (groupware)

## 사용방법
.env.example을 복사해서 .env 파일로 만들기
아이디 패스워드 입력하기
```text
ID=[MYID]
PASSWORD=[MYPASSWORD]
```

### 의존성 설치
python 3.11 이상 설치
``` bash
pip install poetry
poetry install
poetry shell
```
### 실행
```bash
python timetable.py
```

현재 raw data만 json 형태로 츨력됩니다. 추가적으로 파싱 해야함.
standardWeek의 dailList에 이번주 출/퇴근 정보가 있는 것까지 파악된 상태 


