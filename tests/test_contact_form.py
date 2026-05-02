
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page


def test_contact_required_message_empty(page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()
    

def test_contac_submit_the_form_with_all_required_fields_filled_out(page):
    print("Given the user open contact web Contáctanos | Vida Verde" )
    page.goto("https://web-qa.dev.adalab.es/contact")
    print ("When the user enters Marta Diaz in the name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print ("And the user enters test_automation@test.com in the email field")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And submit the form")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print ("Then the user should see the message 'Message sent'")
    expect(page.get_by_text("¡Mensaje enviado con éxito!")).to_be_visible()


def test_contact_submit_the_form_with_required_name_field_left_empty(page):
    print("Given the user open contact web Contáctanos | Vida Verde" )
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user enters test_automation@test.com in the email field")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And submit the form")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print ("Then the user should see the error message 'The name is required'")   
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()

def test_contact_submit_the_form_with_required_email_field_left_empty(page):
    print("Given the user open contact web Contáctanos | Vida Verde" )
    page.goto("https://web-qa.dev.adalab.es/contact")
    print ("When the user enters Marta Diaz in the name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And submit the form")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print ("Then the user should see the error message 'The email is required'")   
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()

