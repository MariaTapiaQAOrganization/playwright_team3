
from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage


def test_contact_submit_the_form_with_all_required_fields_filled_out(page: Page): #TEST MARIA

    contact_page = ContactPage(page)

    print("Given user visit contact page")  
    contact_page.open_contact_page()

    print("When the user enters Marta Diaz in the name field")
    contact_page.fill_contact_name("Marta Diaz")

    print("And the user enters test@gmail.com in the email field")
    contact_page.fill_contact_email("test@gmail.com")
    
    print("And the user enters Test message in the message field")
    contact_page.fill_contact_message("Test message")

    print("And the user clicks on the submit button")
    contact_page.press_send_contact()

    print("Then the user should see the success message “¡Mensaje enviado con éxito!”")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")


def test_contact_required_message_empty(page: Page): #GRIMANESA
    
    contact_page = ContactPage(page)

    print("Given the user navigates to the contact page")
    contact_page.open_contact_page()

    print("when the user fills the requeried name with Marta Díaz")
    contact_page.fill_contact_name("Marta Díaz")

    print("and fills the required email field with test@gmail.com")
    contact_page.fill_contact_email("test@gmail.com")

    print("and clicks submit")
    contact_page.press_send_contact()

    print("then should see and error message el mensaje es obligatorio")
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()


def test_contact_invalid_email(page: Page): #GRIMANESA

    contact_page = ContactPage(page)

    print("Given the user navigates to the contact page")
    contact_page.open_contact_page()

    print("when the user fills the requeried name with Marta Díaz")
    contact_page.fill_contact_name("Marta Diaz")

    print("and fills the required email field with email")
    contact_page.fill_contact_email("email")

    print("And the user enters Mensaje de prueba in the message field")
    contact_page.fill_contact_message("Mensaje de prueba")

    print("and clicks submit")
    contact_page.press_send_contact()

    print("Then should see an error message el formato de email no es válido")
    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()



def test_contact_submit_the_form_with_required_name_field_left_empty(page: Page): #TEST MARIA
    
    contact_page = ContactPage(page)

    print("Given user visit contact page")  
    contact_page.open_contact_page()

    print("When the user enters test@gmail.com in the email field")
    contact_page.fill_contact_email("test@gmail.com")
    
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
