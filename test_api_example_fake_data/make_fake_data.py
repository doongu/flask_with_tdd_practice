from faker import Faker
from faker.providers import internet

# api에 테스트 해보기 위한 데이터 생성 부분입니다.
# 어떤 필요한 데이터들을 생성해서 test를 해볼 것인가?를 주된 관점으로 작성해보았습니다.
# 서버에 대한 API 요청을 테스트 해볼 것이기에, 이에 필요한 요소들을 정리해보겠습니다.
'''
1. 파라메타 (GET, POST, PUT, DELETE 4개)
2. uri 에서 url을 뺀 부분 ( path 부분 )
4. port 번호
3. 2번에서 추출한 값을 http://localhost:포트번호/path 로 지정하고, 이 uri들을 저장
5. 3번에서 저장한 값을 GET, POST, PUT, DELETE에 맞게 요청이 올바른지 에 대한 TDD 진행

ex) http://localhost:80/main 으로 POST요청이 들어온 것은 200error 외에는 전부 400 Bad Request로 처리.
'''
fake = Faker('ko_KR')
fake.add_provider(internet)
print(fake.uri())