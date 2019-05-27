import allure, pytest


class TestAbc(object):
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试步骤01")
    def test_01(self):
        print("test_01")
        allure.attach("测试标题", "具体内容")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试步骤02")
    def test_02(self):
        print("test_02")

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是测试步骤03")
    def test_03(self):
        print("test_03")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是测试步骤04")
    def test_04(self):
        print("test_04")

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是测试步骤05")
    def test_05(self):
        print("test_05")
