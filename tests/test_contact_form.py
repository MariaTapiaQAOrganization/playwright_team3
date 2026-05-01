
from playwright.sync_api import expect


def test_contact_required_message_empty(page):
    page.goto("https://web-qa.dev.adalab.es/")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("button", name="Enviar Mensaje").click()

    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()
    