import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestDuckDuckGoCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup
        options = Options()
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls._open_calculator()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def _open_calculator(self):
        self.driver.get("https://duckduckgo.com/")
        search_input = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_input.clear()
        search_input.send_keys("calculator")
        search_input.send_keys(Keys.ENTER)
        self.wait.until(EC.presence_of_element_located((By.ID, "display")))
    
    def _refresh_page(self):
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located((By.ID, "display")))

    def _click_button(self, value):
        btn = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//button[@value='{value}']")))
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(0.1)

    def _get_display_value(self):
        display = self.driver.find_element(By.ID, "display")
        return display.text

    def test_a_somar_dois_numeros_diferentes(self):
        self._refresh_page()
        # Exercise SUT
        self._click_button("2")
        self._click_button("+")
        self._click_button("3")
        self._click_button("=")
        resultado = self._get_display_value()
        
        # Verificação
        self.assertTrue(resultado == "5")

    def test_b_multiplicar_e_dividir(self):
        self._refresh_page()
        # Exercise SUT
        self._click_button("5")
        self._click_button("×")
        self._click_button("6")
        self._click_button("÷")
        self._click_button("1")
        self._click_button("0")
        self._click_button("=")
        resultado = self._get_display_value()

        # Verificação
        self.assertTrue(resultado == "3")

    def test_c_duas_operacoes_com_subtracao(self):
        self._refresh_page()
        # Exercise SUT
        self._click_button("8")
        self._click_button("-")
        self._click_button("3")
        self._click_button("×")
        self._click_button("2")
        self._click_button("=")
        resultado = self._get_display_value()

        # Verificação
        self.assertTrue(resultado == "2")

    def test_d_tres_operacoes_e_historico(self):
        self._refresh_page()
        # Exercise SUT
        self._click_button("1")
        self._click_button("+")
        self._click_button("2")
        self._click_button("=")
        resultado_1 = self._get_display_value()

        self._click_button("×")
        self._click_button("3")
        self._click_button("=")
        resultado_2 = self._get_display_value()

        self._click_button("-")
        self._click_button("4")
        self._click_button("=")
        resultado_3 = self._get_display_value()

        # Verificação
        self.assertTrue(resultado_1 == "3")
        self.assertTrue(resultado_2 == "9")
        self.assertTrue(resultado_3 == "5")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertTrue("1 + 2" in body_text)
        self.assertTrue("3 × 3" in body_text)
        self.assertTrue("9" in body_text)
        self.assertTrue("4" in body_text)


if __name__ == "__main__":
    unittest.main()
