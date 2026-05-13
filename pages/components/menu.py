from playwright.sync_api import Page, expect

class Menu:

    def __init__(self, page: Page):
        self.page = page
        self.menu_about_us = "Quiénes Somos"
        self.menu_products = "Productos"
        self.menu_contact = "Contacto"
    
    def visit_menu_about_us(self):
        self.page.get_by_role("link", name=self.menu_about_us).click()

    def visit_menu_products(self):
        self.page.get_by_role("link", name=self.menu_products).click()

    def visit_menu_contact(self):
        self.page.get_by_role("link", name=self.menu_contact).click()