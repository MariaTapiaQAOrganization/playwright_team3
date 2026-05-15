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

    ###KARELIA.  

    def __init__(self, page: Page):
        self.page = page
        self.utl = "https://web-qa.dev.adalab.es/products"

    def open_product_page(self):
        self.page.goto(self.url)
    
    def search_product(self, product_name):
        self.page.get_by_role("searchbox", name="Nombre").fill(product_name)
    
    def add_product_to_cart(self, product_name):
        self.page.get_by_role("button", name="Añadir " + product_name+" al carrito").click()
    
    def clear_filter(self):
        self.page.get_by_role("button", name="Quitar filtros y ver todos").click()
    
    def search_product(self, product_name):
        self.page.get_by_role("searchbox", name="Nombre").fill(product_name)

    
    def click_on_cart(self):
        self.page.get_by_role("link", name="Carrito de compra").click()

    def verify_item_visible_all(self, product_name, category, price):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()
        expect(self.page.get_by_text(category)).to_be_visible()
        expect(self.page.get_by_text(price)).to_be_visible()

    def empty_cart(self):
        self.page.get_by_role("button", name="Vaciar Carrito").click()
        expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()

    def click_finish_purchase(self):
        self.page.get_by_role("link", name="Finalizar Compra").click()





