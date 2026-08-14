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

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # =========================
    # SETUP DE CADA TESTE
    # =========================

    def setup_method(self):

        self.driver.get(data.URBAN_ROUTES_URL)

        self.page = UrbanRoutesPage(self.driver)

        self.page.set_route(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

    # =========================
    # PREPARAR PEDIDO
    # =========================

    def prepare_order(self):

        self.page.call_initial_taxi()

        assert self.page.is_order_form_visible()

        self.page.select_comfort()

        assert self.page.is_comfort_active()

    # =========================
    # 1 - DEFINIR ROTA
    # =========================

    def test_set_route(self):

        assert self.page.get_from_value() == data.ADDRESS_FROM
        assert self.page.get_to_value() == data.ADDRESS_TO

    # =========================
    # 2 - CHAMAR TÁXI INICIAL
    # =========================

    def test_call_initial_taxi(self):

        self.page.call_initial_taxi()

        assert self.page.is_order_form_visible()

    # =========================
    # 3 - SELECIONAR COMFORT
    # =========================

    def test_select_plan(self):

        self.page.call_initial_taxi()

        assert self.page.is_order_form_visible()

        self.page.select_comfort()

        assert self.page.is_comfort_active()

    # =========================
    # 4 - TELEFONE
    # =========================

    def test_fill_phone_number(self):

        self.prepare_order()

        self.page.open_phone_form()

        entered_phone = self.page.fill_phone_number(
            data.PHONE_NUMBER
        )

        assert entered_phone == data.PHONE_NUMBER

    # =========================
    # 5 - CARTÃO
    # =========================

    def test_fill_card(self):

        self.prepare_order()

        entered_card = self.page.add_card(
            data.CARD_NUMBER,
            data.CARD_CODE
        )

        assert entered_card == data.CARD_NUMBER

    # =========================
    # 6 - COMENTÁRIO
    # =========================

    def test_comment_for_driver(self):

        self.prepare_order()

        entered_comment = self.page.fill_comment(
            data.MESSAGE_FOR_DRIVER
        )

        assert entered_comment == data.MESSAGE_FOR_DRIVER

    # =========================
    # 7 - COBERTOR E LENÇÓIS
    # =========================

    def test_order_blanket_and_handkerchiefs(self):

        self.prepare_order()

        blanket_selected = self.page.order_blanket_and_sheets()

        assert blanket_selected is True

    # =========================
    # 8 - 2 SORVETES
    # =========================

    def test_order_2_ice_creams(self):

        self.prepare_order()

        ice_cream_count = self.page.add_ice_creams(2)

        assert ice_cream_count == 2

    # =========================
    # 9 - BUSCAR CARRO
    # =========================

    def test_car_search_model_appears(self):

        self.prepare_order()

        self.page.call_taxi()

        assert self.page.get_car_search_title() == "Buscar carro"