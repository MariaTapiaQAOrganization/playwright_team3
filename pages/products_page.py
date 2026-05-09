from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
    
    def open_products_page(self): #GRIMANESA
        self.page.goto(self.url)

    def search_product(self, product_name): #GRIMANESA
        self.page.get_by_placeholder("Buscar productos...").fill(product_name)

    def filter_by_category(self, category):  #GRIMANESA
        self.page.get_by_label("Categoría").select_option(category)

    def filter_by_min_price(self, min_price):  #GRIMANESA
        self.page.get_by_placeholder("Min €").fill(min_price)

    def filter_by_max_price(self, max_price):  #GRIMANESA
        self.page.get_by_placeholder("Max €").fill(max_price)
    
    def add_product_to_cart(self, product_name):  #GRIMANESA
        self.page.get_by_label(f"Añadir {product_name} al carrito").click()

    def click_checkout(self):  #GRIMANESA
        self.page.get_by_role("link", name="Finalizar Compra").first.click()

    def click_proceed_to_payment(self):  #GRIMANESA
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def fill_checkout_form(self, name, email, address, card):  #GRIMANESA
        self.page.get_by_placeholder("María González").fill(name)
        self.page.get_by_placeholder("maria@example.com").fill(email)
        self.page.get_by_placeholder("Rúa da Raíña, 25, Lugo, 27001").fill(address)
        self.page.get_by_placeholder("4242 4242 4242 4242").fill(card)

    def complete_purchase(self):  #GRIMANESA
        self.page.get_by_role("button", name="Completar Compra").click()

    def verify_success_message(self, text):  #GRIMANESA
        expect(self.page.get_by_text(text)).to_be_visible()