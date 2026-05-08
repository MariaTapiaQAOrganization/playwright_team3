from playwright.sync_api import Page, expect

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/contact"

    def open_contact_page(self):
         self.page.goto(self.url)

    def fill_contact_name(self, name):
        self.page.get_by_role("textbox", name="Nombre *").fill(name)
    
    def fill_contact_email(self,email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_contact_message(self,message):
        self.page.get_by_role("textbox", name="Mensaje *").fill(message)
    
    def press_send_contact(self):
        self.page.get_by_role("button", name="Enviar Mensaje").click()

    def verify_message_form(self,text):
        expect(self.page.get_by_role("heading", name=text)).to_be_visible()
