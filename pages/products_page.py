from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"