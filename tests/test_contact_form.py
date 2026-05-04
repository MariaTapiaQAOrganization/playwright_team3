
import pytest
from playwright.sync_api import Page, expect


def test_contact_required_message_empty(page: Page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()


@pytest.mark.skip(reason="Skipped due to known bug KAN-15: Contact page accepts invalid email formats and submits the form successfully - https://equipo3qa.atlassian.net/browse/KAN-15")
def test_contact_invalid_email(page: Page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("testgmail.com")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("¡Mensaje enviado con éxito!")).not_to_be_visible()


def test_contact_submit_the_form_with_all_required_fields_filled_out(page: Page):
    print("Given user visit contact page")  
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user enters Marta Diaz in the name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And the user enters test_automation@test.com in the email field")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And the user enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And the user clicks on the submit button")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("¡Mensaje enviado con éxito!")).to_be_visible()


def test_contact_submit_the_form_with_required_name_field_left_empty(page: Page):
    print("Given user visit contact page")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user enters test_automation@test.com in the email field")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And the user enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And the user clicks on the submit button")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()

@pytest.mark.skip(reason="Contact page - the form can be submitted even when the email field is left empty- https://equipo3qa.atlassian.net/browse/KAN-13")
def test_contact_submit_the_form_with_required_email_field_left_empty(page: Page):
    print("Given user visit contact page")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user enters Marta Diaz in the name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And the user enters Test message in the message field")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")
    print("And the user clicks on the submit button")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
