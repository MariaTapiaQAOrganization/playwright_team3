from playwright.sync_api import Page, expect


class CheckoutPage:                  #MARIA
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/checkout"
    
    def fill_name(self, name):
        name_input = self.page.get_by_placeholder("María González")
        name_input.wait_for(state="visible")
        name_input.fill(name)

    def fill_email(self, email):
        email_input = self.page.get_by_placeholder("maria@example.com")
        email_input.wait_for(state="visible")
        email_input.fill(email)

    def fill_address(self, address):
        address_input = self.page.get_by_placeholder("Rúa da Raíña, 25, Lugo, 27001")
        address_input.wait_for(state="visible")
        address_input.fill(address)

    def fill_card(self, card_number):
        card_input = self.page.get_by_placeholder("4242 4242 4242 4242")
        card_input.wait_for(state="visible")
        card_input.fill(card_number)


    def complete_purchase (self):          #MARIA 
        self. page.get_by_role("button", name="Completar Compra").click()

    def verify_checkout_page(self):         #MARIA
         expect(self.page).to_have_url("https://web-qa.dev.adalab.es/checkout")

    def verify_card_error_message (self):
          expect(self.page.get_by_text("Tarjeta de crédito no válida.")).to_be_visible()

    
    def verify_order_summary_product(self, product_name):   #GRIMANESA
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def verify_order_summary_prices(self, price, vat, shipping, total):  #GRIMANESA
        summary = self.page.get_by_label("Resumen del Pedido")

        expect(summary.get_by_text(price)).to_be_visible()
        expect(summary.get_by_text(vat)).to_be_visible()
        expect(summary.get_by_text(shipping)).to_be_visible()
        expect(summary.get_by_text(total)).to_be_visible()


