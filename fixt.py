import pytest
import uuid


@pytest.fixture(scope="function")
def gen_f():
    return uuid.uuid1()


@pytest.fixture(scope="class")
def gen_c():
    return uuid.uuid1()


@pytest.fixture(scope="module")
def gen_m():
    return uuid.uuid1()


class TestA():
    def test1(self, gen_f, gen_c, gen_m):
        print(f'Func: {gen_f}')
        print(f'Class: {gen_c}')
        print(f'Module: {gen_m}\n')
        assert True

    def test2(self, gen_f, gen_c, gen_m):
        print(f'Func: {gen_f}')
        print(f'Class: {gen_c}')
        print(f'Module: {gen_m}\n')
        assert True


class TestB():
    def test3(self, gen_f, gen_c, gen_m):
        print(f'Func: {gen_f}')
        print(f'Class: {gen_c}')
        print(f'Module: {gen_m}\n')
        assert True

    def test4(self, gen_f, gen_c, gen_m):
        print(f'Func: {gen_f}')
        print(f'Class: {gen_c}')
        print(f'Module: {gen_m}\n')
        assert True

