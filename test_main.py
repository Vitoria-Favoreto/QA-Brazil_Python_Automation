import data
import helpers

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print(
                "Não foi possível conectar ao Urban Routes. "
                "Verifique se o servidor está ligado e ainda em execução."
            )

        # Necessário para recuperar o código do telefone.
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {
            "performance": "ALL"
        }

        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # =========================
    # 1 - DEFINIR ROTA
    # =========================

    def test_set_route(self):

        page = UrbanRoutesPage(self.driver)

        page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

    # =========================
    # 2 - CHAMAR TÁXI INICIAL
    # =========================

    def test_call_initial_taxi(self):

        page = UrbanRoutesPage(self.driver)

        page.call_initial_taxi()

    # =========================
    # 3 - SELECIONAR COMFORT
    # =========================

    def test_select_plan(self):

        page = UrbanRoutesPage(self.driver)

        page.select_comfort()

    # =========================
    # 4 - TELEFONE
    # =========================

    def test_fill_phone_number(self):

        page = UrbanRoutesPage(self.driver)

        page.open_phone_form()

        page.fill_phone_number(
            data.PHONE_NUMBER
        )

    # =========================
    # 5 - CARTÃO
    # =========================

    def test_fill_card(self):

        page = UrbanRoutesPage(self.driver)

        page.add_card(
            data.CARD_NUMBER,
            data.CARD_CODE
        )

    # =========================
    # 6 - COMENTÁRIO
    # =========================

    def test_comment_for_driver(self):

        page = UrbanRoutesPage(self.driver)

        page.fill_comment(
            data.MESSAGE_FOR_DRIVER
        )

    # =========================
    # 7 - COBERTOR E LENÇÓIS
    # =========================

    def test_order_blanket_and_handkerchiefs(self):

        page = UrbanRoutesPage(self.driver)

        page.order_blanket_and_sheets()

    # =========================
    # 8 - 2 SORVETES
    # =========================

    def test_order_2_ice_creams(self):

        page = UrbanRoutesPage(self.driver)

        page.add_ice_creams(2)

    # =========================
    # 9 - CHAMAR TÁXI E VERIFICAR
    # =========================

    def test_car_search_model_appears(self):

        page = UrbanRoutesPage(self.driver)

        page.call_taxi_and_check_modal()