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


