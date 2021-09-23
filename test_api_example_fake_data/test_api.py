from unittest import main, TestCase
from unittest.mock import patch
import user_manage

# 이 테스트 코드는 접속자가 https://jsonplaceholder.typicode.com/users/1 에 Get으로 접속한다는 가정하에 동작하는 코드입니다.
class TestUserManger(TestCase):
    @patch("requests.get")
    def test_get_user(self, mock_get): #네트워크 연동없는 단위 테스트
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = { # 돌아오는 요청값을 미리 적고
            "name": "Test User",
            "email": "user@test.com",
        }

        user = user_manage.get_user(1)

        self.assertEqual(user["name"], "Test User") # 예상했던 작업이 일어났는지 검증해야 합니다..
        self.assertEqual(user["email"],"user@test.com")
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")

if __name__ == '__main__':
    main() #  테스트 스크립트에 명령행 인터페이스를 제공합니다. -v 를 넘기면 unittest.main()은 상세히 보여준다.