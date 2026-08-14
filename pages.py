import helpers

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    # =========================
    # ENDEREÇOS
    # =========================

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    # =========================
    # BOTÃO INICIAL
    # =========================

    INITIAL_TAXI_BUTTON = (
        By.XPATH,
        "//button[@type='button' and contains(text(), 'Chamar um táxi')]"
    )

    # =========================
    # TARIFA COMFORT
    # =========================

    COMFORT_TARIFF = (
        By.XPATH,
        "//div[contains(@class, 'tcard')]"
        "[.//div[contains(@class, 'tcard-title') "
        "and normalize-space()='Comfort']]"
    )

    COMFORT_ACTIVE = (
        By.XPATH,
        "//div[contains(@class, 'tcard') and contains(@class, 'active')]"
        "[.//div[contains(@class, 'tcard-title') "
        "and normalize-space()='Comfort']]"
    )

    # =========================
    # TELEFONE
    # =========================

    PHONE_SECTION = (
        By.XPATH,
        "//div[contains(@class, 'np-text') "
        "and normalize-space()='Número de telefone']"
    )

    PHONE_FIELD = (By.ID, "phone")

    PHONE_NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Próximo')]"
    )

    PHONE_CODE_FIELD = (By.ID, "code")

    CONFIRM_PHONE_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Confirmar')]"
    )

    # =========================
    # CARTÃO
    # =========================

    PAYMENT_METHOD = (
        By.XPATH,
        "//div[contains(@class, 'pp-text') "
        "and normalize-space()='Método de pagamento']"
    )

    ADD_CARD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'pp-title') "
        "and normalize-space()='Adicionar cartão']"
    )

    CARD_NUMBER_FIELD = (
        By.XPATH,
        "//input[@id='number' and @name='number' "
        "and @placeholder='1234 0000 4321']"
    )

    CARD_CODE_FIELD = (
        By.XPATH,
        "//input[@id='code' and @name='code' "
        "and @placeholder='12']"
    )

    ADD_CARD_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Adicionar')]"
    )

    CLOSE_CARD_BUTTON = (
        By.CSS_SELECTOR,
        "button.close-button.section-close"
    )

    # =========================
    # COMENTÁRIO
    # =========================

    COMMENT_FIELD = (By.ID, "comment")

    # =========================
    # COBERTOR E LENÇÓIS
    # =========================

    BLANKET_SWITCH_CHECKBOX = (
        By.XPATH,
        "//div[contains(@class, 'r-sw-container')]"
        "[.//div[contains(@class, 'r-sw-label') "
        "and normalize-space()='Cobertor e lençóis']]"
        "//input[@type='checkbox']"
    )

    BLANKET_SWITCH = (
        By.XPATH,
        "//div[contains(@class, 'r-sw-container')]"
        "[.//div[contains(@class, 'r-sw-label') "
        "and normalize-space()='Cobertor e lençóis']]"
        "//span[contains(@class, 'slider')]"
    )

    # =========================
    # SORVETE
    # =========================

    ICE_CREAM_PLUS = (
        By.XPATH,
        "//div[contains(@class, 'r-counter')]"
        "[.//div[contains(@class, 'r-counter-label') "
        "and normalize-space()='Sorvete']]"
        "//div[contains(@class, 'counter-plus')]"
    )

    ICE_CREAM_COUNT = (
        By.XPATH,
        "//div[contains(@class, 'r-counter')]"
        "[.//div[contains(@class, 'r-counter-label') "
        "and normalize-space()='Sorvete']]"
        "//*[contains(@class, 'counter-value')]"
    )

    # =========================
    # BOTÃO FINAL
    # =========================

    CALL_TAXI_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'smart-button')]"
    )

    # =========================
    # BUSCAR CARRO
    # =========================

    CAR_SEARCH_MODAL = (
        By.CLASS_NAME,
        "order-header-title"
    )

    # =========================
    # OVERLAY
    # =========================

    OVERLAY = (
        By.CSS_SELECTOR,
        ".overlay"
    )

    # =========================
    # CONSTRUTOR
    # =========================

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # ROTA
    # =========================

    def set_route(self, address_from, address_to):

        from_input = self.wait.until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        )

        from_input.clear()
        from_input.send_keys(address_from)

        to_input = self.wait.until(
            EC.visibility_of_element_located(self.TO_FIELD)
        )

        to_input.clear()
        to_input.send_keys(address_to)

    def get_from_value(self):

        from_input = self.wait.until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        )

        return from_input.get_attribute("value")

    def get_to_value(self):

        to_input = self.wait.until(
            EC.visibility_of_element_located(self.TO_FIELD)
        )

        return to_input.get_attribute("value")

    # =========================
    # CHAMAR TÁXI INICIAL
    # =========================

    def call_initial_taxi(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.INITIAL_TAXI_BUTTON)
        )

        button.click()

    def is_order_form_visible(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.COMFORT_TARIFF)
        ).is_displayed()

    # =========================
    # SELECIONAR COMFORT
    # =========================

    def select_comfort(self):

        comfort = self.wait.until(
            EC.visibility_of_element_located(self.COMFORT_TARIFF)
        )

        if "active" not in comfort.get_attribute("class"):
            comfort.click()

        self.wait.until(
            EC.visibility_of_element_located(self.COMFORT_ACTIVE)
        )

    def is_comfort_active(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.COMFORT_ACTIVE)
        ).is_displayed()

    # =========================
    # TELEFONE
    # =========================

    def open_phone_form(self):

        phone_section = self.wait.until(
            EC.element_to_be_clickable(self.PHONE_SECTION)
        )

        phone_section.click()

    def fill_phone_number(self, phone):

        phone_input = self.wait.until(
            EC.visibility_of_element_located(self.PHONE_FIELD)
        )

        phone_input.clear()
        phone_input.send_keys(phone)

        # Guarda o valor digitado antes de fechar o formulário.
        entered_phone = phone_input.get_attribute("value")

        next_button = self.wait.until(
            EC.element_to_be_clickable(self.PHONE_NEXT_BUTTON)
        )

        next_button.click()

        code = helpers.retrieve_phone_code(self.driver)

        code_input = self.wait.until(
            EC.visibility_of_element_located(self.PHONE_CODE_FIELD)
        )

        code_input.clear()
        code_input.send_keys(code)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_PHONE_BUTTON)
        )

        confirm_button.click()

        return entered_phone

    # =========================
    # CARTÃO
    # =========================

    def add_card(self, card_number, card_code):

        # Abre o método de pagamento.
        payment = self.wait.until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD)
        )

        payment.click()

        # Clica em Adicionar cartão.
        add_card = self.wait.until(
            EC.element_to_be_clickable(self.ADD_CARD_OPTION)
        )

        add_card.click()

        # Campo do número do cartão.
        number_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)
        )

        number_input.click()
        number_input.clear()
        number_input.send_keys(card_number)

        # Guarda o valor para o teste verificar.
        entered_card = number_input.get_attribute("value")

        # Campo do código.
        code_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE_FIELD)
        )

        code_input.click()
        code_input.clear()
        code_input.send_keys(card_code)

        # Sai do campo para ativar o botão.
        code_input.send_keys(Keys.TAB)

        # Clica em Adicionar.
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_CARD_BUTTON)
        )

        add_button.click()

        # Aguarda a janela do cartão desaparecer.
        self.wait.until(
            EC.invisibility_of_element_located(self.CARD_NUMBER_FIELD)
        )

        return entered_card

    # =========================
    # COMENTÁRIO
    # =========================

    def fill_comment(self, comment):

        comment_input = self.wait.until(
            EC.visibility_of_element_located(self.COMMENT_FIELD)
        )

        comment_input.clear()
        comment_input.send_keys(comment)

        return comment_input.get_attribute("value")

    # =========================
    # COBERTOR E LENÇÓIS
    # =========================

    def order_blanket_and_sheets(self):

        checkbox = self.wait.until(
            EC.presence_of_element_located(
                self.BLANKET_SWITCH_CHECKBOX
            )
        )

        # Se já estiver selecionado, não clica novamente.
        if checkbox.is_selected():
            return True

        # Espera o overlay desaparecer.
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except Exception:
            pass

        # Scroll até o elemento.
        switch = self.wait.until(
            EC.presence_of_element_located(self.BLANKET_SWITCH)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            switch
        )

        # JavaScript evita ElementClickInterceptedException.
        self.driver.execute_script(
            "arguments[0].click();",
            switch
        )

        self.wait.until(
            lambda driver:
            driver.find_element(
                *self.BLANKET_SWITCH_CHECKBOX
            ).is_selected()
        )

        return self.driver.find_element(
            *self.BLANKET_SWITCH_CHECKBOX
        ).is_selected()

    # =========================
    # SORVETES
    # =========================

    def add_ice_creams(self, quantity):

        # Espera o overlay desaparecer.
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except Exception:
            pass

        plus_button = self.wait.until(
            EC.presence_of_element_located(self.ICE_CREAM_PLUS)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            plus_button
        )

        for _ in range(quantity):

            plus_button = self.wait.until(
                EC.presence_of_element_located(self.ICE_CREAM_PLUS)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                plus_button
            )

        return self.get_ice_cream_count()

    def get_ice_cream_count(self):

        counter = self.wait.until(
            EC.visibility_of_element_located(self.ICE_CREAM_COUNT)
        )

        return int(counter.text)

    # =========================
    # CHAMAR TÁXI FINAL
    # =========================

    def call_taxi(self):

        # Espera qualquer overlay desaparecer.
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except Exception:
            pass

        button = self.wait.until(
            EC.presence_of_element_located(self.CALL_TAXI_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        # JavaScript evita problema de overlay interceptando o clique.
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # =========================
    # VERIFICAR BUSCA DO CARRO
    # =========================

    def get_car_search_title(self):

        modal = self.wait.until(
            EC.visibility_of_element_located(
                self.CAR_SEARCH_MODAL
            )
        )

        return modal.text