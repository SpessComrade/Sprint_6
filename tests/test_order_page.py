import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from TestData import OrderPageInputTexts

class TestpOrderPageTests:
    @allure.title('Тест заказа самоката')
    @pytest.mark.parametrize(
        "order_button, user_data, station, rent_data, period, color",
        [
            [
                MainPageLocators.order_button_top,
                OrderPageInputTexts.user_data_1,
                OrderPageLocators.metro_station_pp,
                OrderPageInputTexts.rent_data_1,
                OrderPageLocators.one_day_period_selector_option,
                OrderPageLocators.color_checkbox_gray,
            ],
            [
                MainPageLocators.order_button_top,
                OrderPageInputTexts.user_data_2,
                OrderPageLocators.metro_station_sb,
                OrderPageInputTexts.rent_data_2,
                OrderPageLocators.seven_days_period_selector_option,
                OrderPageLocators.color_checkbox_black,
            ],
        ],
    )
    def test_samokat_order(self, driver, order_button, user_data, station, rent_data, period, color):
        main_page = MainPage(driver)
        main_page.order_button_click(order_button)
        order_page = OrderPage(driver)
        order_page.fill_user_form(*user_data, station)
        order_page.click_next_button()
        order_page.fill_rent_form(*rent_data, period, color)
        order_page.click_order_button()
        order_page.wait_for_order_popup()
        order_page.click_yes_button()
        order_page.check_success_popup()