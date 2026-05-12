from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = "Catálogo de Productos"
        self.url = "https://web-qa.dev.adalab.es/products"



    def verify_products_title(self):  #KARELIA
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verify_products_url(self):   #KARELIA
        expect(self.page).to_have_url(self.url)


    def verify_product_category(self):   #KARELIA
        expect(self.page.get_by_label(self.title).get_by_role("list")).to_contain_text("Plantas")

    def verify_product_name(self):   #KARELIA
        expect(self.page.get_by_label(self.title).get_by_role("list")).to_contain_text("Ficus Lyrata")

    def verify_product_price(self):   #KARELIA
        expect(self.page.get_by_label(self.title).get_by_role("list")).to_contain_text("35.00 €")

    def visit_product(self):   #KARELIA
        self.page.goto(self.url)

    def fill_name_manzana(self):   #KARELIA
        self.page.get_by_role("searchbox", name="Nombre").fill("manzana")

    def message_no_results(self):    #KARELIA
        expect(self.page.get_by_text("No se encontraron productos")).to_be_visible()




    def open_products_page(self): #GRIMANESA
        self.page.goto(self.url)

    def search_product(self, product_name): #GRIMANESA
        search_input = self.page.get_by_placeholder("Buscar productos...")
        search_input.wait_for(state="visible")
        search_input.fill(product_name)

    def filter_by_category(self, category):  #GRIMANESA
        self.page.get_by_label("Categoría").select_option(category)

    def filter_by_min_price(self, min_price):  #GRIMANESA
        self.page.get_by_placeholder("Min €").fill(min_price)

    def filter_by_max_price(self, max_price):  #GRIMANESA
        self.page.get_by_placeholder("Max €").fill(max_price)
    
    def add_product_to_cart(self, product_name):  #GRIMANESA
        self.page.get_by_label(f"Añadir {product_name} al carrito").click()

    def clear_filter(self):
        self.page.get_by_role("button", name="Quitar filtros y ver todos").click()

    def go_to_cart(self):  #MARIA
        self.page.get_by_role("link", name="Carrito de compra").click() 

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

 