import pytest


class Test:
    def test_1(self):
        '''
        에러를 발생시키고 별다른 조치 안 함
        '''
        def foo():
            raise NotImplementedError
        
        foo()

    def test_2(self):
        '''
        에러를 발생시키고 잘못된 에러를 예상함
        '''
        def foo():
            raise NotImplementedError

        with pytest.raises(ZeroDivisionError):
            foo()
    
    def test_3(self):
        '''
        에러를 발생시키고 올바른 에러를 강제함
        '''
        def foo():
            raise NotImplementedError

        with pytest.raises(NotImplementedError):
            foo()
    
    def test_4(self):
        '''
        에러를 발생시키고 타입을 명확히 확인함
        NotImplementedError는 RuntimeError의 서브 클래스
        '''
        def foo():
            raise NotImplementedError

        with pytest.raises(RuntimeError) as excinfo:
            foo()
        
        assert excinfo.type is RuntimeError
