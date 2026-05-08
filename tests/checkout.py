from playwright.sync_api import Page, expect

def test_checkout_with_empty_card_details(page: Page):
    print("Given the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When the user filters by name “palas”")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("And the user adds the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

    print("and visits the cart page")
    page.get_by_role("link", name="Carrito de compra").click()

    print("and clicks on Proceed to Checkout")
    page.get_by_role("link", name="Proceder al Pago").click()
    
    print("when the user enters the valid name Maria Diaz")
    page.get_by_role("textbox", name="Nombre Completo *").fill("Maria Diaz")

    print("and enters the valid email address test@gmail.com")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print("and enters the valid address Calle Aragón, 25 Madrid")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25 Madrid")

    print("and clicks on completar la compra")
    page.get_by_role("button", name="Completar Compra").click()

    print ("Then the user remains on the checkout page and the page URL must be https://web-qa.dev.adalab.es/checkout")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/checkout")


def test_checkout_invalid_card (page: Page):

    print("Given the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When the user filters by name “palas”")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("And the user adds the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

    print("and visits the cart page")
    page.get_by_role("link", name="Carrito de compra").click()

    print("and clicks on Proceed to Checkout")
    page.get_by_role("link", name="Proceder al Pago").click()
    
    print("when the user enters the valid name Maria Diaz")
    page.get_by_role("textbox", name="Nombre Completo *").fill("Maria Diaz")

    print("and enters the valid email address test@gmail.com")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print("and enters the valid address Calle Aragón, 25 Madrid")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25 Madrid")

    print("and enters the invalid card number 1111 4242 4242 4242")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111424242424242")

    print("and clicks on completar la compra")
    page.get_by_role("button", name="Completar Compra").click()

    print ("should see an error message regarding the card") 
    expect(page.get_by_text("Tarjeta de crédito no válida.")).to_be_visible()
