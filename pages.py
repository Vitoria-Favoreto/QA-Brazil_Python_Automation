import helpers

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    # =========================
    # ENDEREÇOS
    # =========================

    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    # =========================
    # BOTÃO INICIAL
    # =========================

    initial_taxi_button = (
        By.XPATH,
        "//button[@type='button' and contains(text(), 'Chamar um táxi')]"
    )

    # =========================
    # TARIFA COMFORT
    # =========================

    comfort_tariff = (
        By.XPATH,
        "//div[contains(@class, 'tcard')]"
        "[.//div[contains(@class, 'tcard-title') and normalize-space()='Comfort']]"
    )

    comfort_active = (
        By.XPATH,
        "//div[contains(@class, 'tcard') and contains(@class, 'active')]"
        "[.//div[contains(@class, 'tcard-title') and normalize-space()='Comfort']]"
    )

    # =========================
    # TELEFONE
    # =========================

    phone_section = (
        By.XPATH,
        "//div[contains(@class, 'np-text') and normalize-space()='Número de telefone']"
    )

    phone_field = (By.ID, "phone")

    phone_next_button = (
        By.XPATH,
        "//button[contains(text(), 'Próximo')]"
    )

    phone_code_field = (By.ID, "code")

    confirm_phone_button = (
        By.XPATH,
        "//button[contains(text(), 'Confirmar')]"
    )

    # =========================
    # CARTÃO
    # =========================

    payment_method = (
        By.XPATH,
        "//div[contains(@class, 'pp-text') and normalize-space()='Método de pagamento']"
    )

    add_card_option = (
        By.XPATH,
        "//div[contains(@class, 'pp-title') and normalize-space()='Adicionar cartão']"
    )

    # Campos do cartão
    card_number_field = (
        By.XPATH,
        "//input[@id='number' and @name='number' and @placeholder='1234 0000 4321']"
    )

    card_code_field = (
        By.XPATH,
        "//input[@id='code' and @name='code' and @placeholder='12']"
    )

    add_card_button = (
        By.XPATH,
        "//button[contains(text(), 'Adicionar')]"
    )

    # X para fechar janela do cartão
    close_card_button = (
        By.CSS_SELECTOR,
        "button.close-button.section-close"
    )

    # =========================
    # COMENTÁRIO
    # =========================

    comment_field = (By.ID, "comment")

    # =========================
    # COBERTOR E LENÇÓIS
    # =========================

    blanket_switch_checkbox = (
        By.XPATH,
        "//div[contains(@class, 'r-sw-container')]"
        "[.//div[contains(@class, 'r-sw-label') "
        "and normalize-space()='Cobertor e lençóis']]"
        "//input[@type='checkbox']"
    )

    blanket_switch = (
        By.XPATH,
        "//div[contains(@class, 'r-sw-container')]"
        "[.//div[contains(@class, 'r-sw-label') "
        "and normalize-space()='Cobertor e lençóis']]"
        "//span[contains(@class, 'slider')]"
    )

    # =========================
    # SORVETE
    # =========================

    ice_cream_plus = (
        By.XPATH,
        "//div[contains(@class, 'r-counter')]"
        "[.//div[contains(@class, 'r-counter-label') "
        "and normalize-space()='Sorvete']]"
        "//div[contains(@class, 'counter-plus')]"
    )

    # =========================
    # BOTÃO FINAL
    # =========================

    call_taxi_button = (
        By.XPATH,
        "//button[contains(@class, 'smart-button')]"
    )

    # =========================
    # BUSCAR CARRO
    # =========================

    car_search_modal = (
        By.CLASS_NAME,
        "order-header-title"
    )

    # =========================
    # OVERLAY
    # =========================

    overlay = (
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
            EC.visibility_of_element_located(self.from_field)
        )

        from_input.clear()
        from_input.send_keys(address_from)

        to_input = self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        )

        to_input.clear()
        to_input.send_keys(address_to)

    # =========================
    # CHAMAR TÁXI
    # =========================

    def call_initial_taxi(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.initial_taxi_button)
        )

        button.click()

    # =========================
    # SELECIONAR COMFORT
    # =========================

    def select_comfort(self):

        comfort = self.wait.until(
            EC.visibility_of_element_located(self.comfort_tariff)
        )

        if "active" not in comfort.get_attribute("class"):
            comfort.click()

        self.wait.until(
            EC.visibility_of_element_located(self.comfort_active)
        )

    # =========================
    # TELEFONE
    # =========================

    def open_phone_form(self):

        phone_section = self.wait.until(
            EC.element_to_be_clickable(self.phone_section)
        )

        phone_section.click()

    def fill_phone_number(self, phone):

        phone_input = self.wait.until(
            EC.visibility_of_element_located(self.phone_field)
        )

        phone_input.clear()
        phone_input.send_keys(phone)

        next_button = self.wait.until(
            EC.element_to_be_clickable(self.phone_next_button)
        )

        next_button.click()

        code = helpers.retrieve_phone_code(self.driver)

        code_input = self.wait.until(
            EC.visibility_of_element_located(self.phone_code_field)
        )

        code_input.clear()
        code_input.send_keys(code)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.confirm_phone_button)
        )

        confirm_button.click()

    # =========================
    # ADICIONAR CARTÃO
    # =========================

    def add_card(self, card_number, card_code):

        # Abre o método de pagamento
        payment = self.wait.until(
            EC.element_to_be_clickable(self.payment_method)
        )

        payment.click()

        # Clica em Adicionar cartão
        add_card = self.wait.until(
            EC.element_to_be_clickable(self.add_card_option)
        )

        add_card.click()

        # Espera o campo NUMBER aparecer
        number_input = self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        )

        number_input.click()
        number_input.clear()
        number_input.send_keys(card_number)

        # Espera o campo CODE aparecer
        code_input = self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        )

        code_input.click()
        code_input.clear()
        code_input.send_keys(card_code)

        # Sai do campo para ativar o botão
        code_input.send_keys(Keys.TAB)

        # Clica em Adicionar
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )

        add_button.click()

        # Aguarda a janela do cartão desaparecer
        self.wait.until(
            EC.invisibility_of_element_located(self.card_number_field)
        )

    # =========================
    # COMENTÁRIO
    # =========================

    def fill_comment(self, comment):

        comment_input = self.wait.until(
            EC.visibility_of_element_located(self.comment_field)
        )

        comment_input.clear()
        comment_input.send_keys(comment)

    # =========================
    # COBERTOR E LENÇÓIS
    # =========================

    def order_blanket_and_sheets(self):

        # Se já estiver selecionado, não clica novamente
        checkbox = self.wait.until(
            EC.presence_of_element_located(
                self.blanket_switch_checkbox
            )
        )

        if checkbox.is_selected():
            return

        # Espera o overlay desaparecer
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.overlay)
            )
        except:
            pass

        # Scroll até o elemento
        switch = self.wait.until(
            EC.presence_of_element_located(self.blanket_switch)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            switch
        )

        # Usa JavaScript para evitar ElementClickInterceptedException
        self.driver.execute_script(
            "arguments[0].click();",
            switch
        )

        self.wait.until(
            lambda driver:
            driver.find_element(
                *self.blanket_switch_checkbox
            ).is_selected()
        )

    # =========================
    # SORVETES
    # =========================

    def add_ice_creams(self, quantity):

        # Espera overlay desaparecer
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.overlay)
            )
        except:
            pass

        plus_button = self.wait.until(
            EC.presence_of_element_located(self.ice_cream_plus)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            plus_button
        )

        for _ in range(quantity):

            plus_button = self.wait.until(
                EC.presence_of_element_located(self.ice_cream_plus)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                plus_button
            )

    # =========================
    # CHAMAR TÁXI FINAL
    # =========================

    def call_taxi(self):

        # Espera qualquer overlay desaparecer
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.overlay)
            )
        except:
            pass

        button = self.wait.until(
            EC.presence_of_element_located(self.call_taxi_button)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        # JavaScript evita o problema do overlay interceptar o clique
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # =========================
    # VERIFICAR BUSCA DO CARRO
    # =========================

    def call_taxi_and_check_modal(self):

        self.call_taxi()

        modal = self.wait.until(
            EC.visibility_of_element_located(
                self.car_search_modal
            )
        )

        assert modal.text == "Buscar carro"