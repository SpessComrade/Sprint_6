import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from TestData import MainPageTexts

class TestMainPageTests:
    @allure.title('Тест раздела FAQ')
    @pytest.mark.parametrize(
        "num, expected_text",
        [
            (0, MainPageTexts.answer_cost),
            (1, MainPageTexts.answer_more_scooters),
            (2, MainPageTexts.answer_rent_time),
            (3, MainPageTexts.answer_today),
            (4, MainPageTexts.answer_changes),
            (5, MainPageTexts.answer_charger),
            (6, MainPageTexts.answer_cancel),
            (7, MainPageTexts.answer_mkad),
        ],
    )
    def test_faq(self, driver, num, expected_text):
       main_page = MainPage(driver)
       answer_text = main_page.get_answer_text(num)
       assert answer_text == expected_text

class TestLogoClickTests:
    @allure.title('Переход со страницы заказа на главную страницу Самоката по клику на логотип Самокат')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.order_button_click(MainPageLocators.order_button_top)
        order_page = OrderPage(driver)
        order_page.click_samokat_logo()
        main_page.check_samokat_page_load()

    @allure.title('Переход с главной страницы на страницу Новостей Дзен по клику на логотип Яндекс')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.yandex_logo_click()
        main_page.switch_to_window()
        main_page.check_yandex_page_load()