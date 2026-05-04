
import pytest
from playwright.sync_api import expect


def test_contact_required_message_empty(page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()

@pytest.mark.skip(reason="Bug: contact form accepts invalid email - KAN-35")
def test_contact_invalid_email(page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("testgmail.com")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("¡Mensaje enviado con éxito!")).not_to_be_visible()