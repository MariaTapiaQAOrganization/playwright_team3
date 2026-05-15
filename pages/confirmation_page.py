
from playwright.sync_api import Page, expect


class ConfirmationPage:  #GRIMANESA

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"
    
    def verificar_compra_realizada(self):
        expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()