from playwright.sync_api import Page, expect

class CartPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"
        
    def  click_checkout(self):
       self.page.get_by_role("link", name="Proceder al Pago").click()
    
    def remove_product(self, product_name):
        self.page.get_by_role("button", name=f"Eliminar {product_name} del").click()

    def verify_item_not_visible(self, product_name):
         expect(self.page.get_by_text(product_name)).not_to_be_visible()
    
    def verify_item_visible(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def verify_summary(self, price, vat, shipping, total):
        summary = self.page.get_by_label("Resumen del Pedido")
        expect(summary.get_by_text(price)).to_be_visible()
        expect(summary.get_by_text(vat)).to_be_visible()
        expect(summary.get_by_text(shipping)).to_be_visible()
        expect(summary.get_by_text(total)).to_be_visible()

    ###KARELIA

    def __init__(self, page: Page):
        self.page = page
        self.url_product = "https://web-qa.dev.adalab.es/products"
        self.plant_name = "Sansevieria"
        self.pot_name = "maceta de barro"

    def visit_product(self):
        self.page.goto(self.url_product)
    
    def fill_name_plant_and_add(self):
        self.page.get_by_role("searchbox", name="Nombre").fill(self.plant_name)
        self.page.get_by_role("button", name="Añadir Sansevieria al carrito").click()
    
    def clear_filter(self):
        self.page.get_by_role("button", name="Quitar filtros y ver todos").click()
    
    def fill_name_pot_and_add(self):
        self.page.get_by_role("searchbox", name="Nombre").fill(self.pot_name)
        self.page.get_by_role("button", name="Añadir Maceta de Barro Grande").click()
    
    def click_on_cart(self):
        self.page.get_by_role("link", name="Carrito de compra").click()

    def verify_details_plant(self):
        expect(self.page.get_by_role("heading", name="Sansevieria")).to_be_visible()
        expect(self.page.get_by_text("Plantas")).to_be_visible()
        expect(self.page.get_by_text("22.00 €")).to_be_visible()
    
    def verify_details_pot(self):
        expect(self.page.get_by_role("heading", name="Maceta de Barro Grande")).to_be_visible()
        expect(self.page.get_by_text("Macetas")).to_be_visible()
        expect(self.page.get_by_text("10.50 €")).to_be_visible()

    def verify_summary_details(self):
        self.page.get_by_role("heading", name="Resumen del Pedido")
        expect(self.page.get_by_text("32.50 €")).to_be_visible()
        expect(self.page.get_by_text("6.83 €")).to_be_visible()
        expect(self.page.get_by_text("5.00 €")).to_be_visible()
        expect(self.page.get_by_text("44.33 €")).to_be_visible()

    def empty_cart(self):
        self.page.get_by_role("button", name="Vaciar Carrito").click()
        expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()

    





