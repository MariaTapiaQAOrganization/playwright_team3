
from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage

def test_contact_submit_the_form_with_all_required_fields_filled_out(page: Page): #TEST MARIA

    contact_page = ContactPage(page)

    print("Given user visit contact page")  
    contact_page.open_contact_page()

    print("When the user enters Marta Diaz in the name field")
    contact_page.fill_contact_name("Marta Diaz")

    print("And the user enters test_automation@test.com in the email field")
    contact_page.fill_contact_name("test_automation@test.com")
    
    print("And the user enters Test message in the message field")
    contact_page.fill_contact_message("Test message")

    print("And the user clicks on the submit button")
    contact_page.press_send_contact()

    print("Then the user should see the success message “¡Mensaje enviado con éxito!”")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")




def test_contact_required_message_empty(page: Page):
    page.goto("https://web-qa.dev.adalab.es/contact")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()


def test_contact_invalid_email(page: Page):
    page.goto("https://web-qa.dev.adalab.es/contact")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("email")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()


def test_contact_submit_the_form_with_required_name_field_left_empty(page: Page): #TEST MARIA
    
    contact_page = ContactPage(page)

    print("Given user visit contact page")  
    contact_page.open_contact_page()

    print("When the user enters test@gmail.com in the email field")
    contact_page.fill_contact_name("test@gmail.com")
    
    print("And the user enters Test message in the message field")
    contact_page.fill_contact_message("test message")
    
    print("And the user clicks on the submit button")
    contact_page.press_send_contact()

    print("Then the user should see the error message “El nombre es obligatorio”")
    contact_page.verify_message_form("El nombre es obligatorio")


def test_contact_submit_the_form_with_required_email_field_left_empty(page: Page): #TEST MARIA

    contact_page= ContactPage(page)

    print("Given user visit contact page")
    contact_page.open_contact_page()

    print("When the user enters Marta Diaz in the name field")
    contact_page.fill_contact_name("Marta Diaz")

    print("And the user enters Test message in the message field")
    contact_page.fill_contact_message("test message")

    print("And the user clicks on the submit button")
    contact_page.press_send_contact()

    print("Then the user should see the error message “El email es obligatorio”")
    contact_page.verify_message_form("El email es obligatorio")
