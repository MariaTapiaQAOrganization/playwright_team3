from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("When the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("Then the user sees the product category “Plants”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("Plantas")

    print("And the user sees the product name “Ficus Lyrata”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("Ficus Lyrata")

    print("And the user sees the product price “35.00 €”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("35.00 €")


def test_complete_purchase_valid_data(page: Page):    
    print("Given the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When the user filters by name “palas”")
    page.get_by_placeholder("Buscar productos...").fill("palas")

    print("And the user adds the product to the cart")
    page.get_by_label("Añadir Juego de Palas al carrito").click()

    print("And the user clicks on Finalizar Compra")
    page.get_by_role("link", name="Finalizar Compra").first.click()

    print("Then the user should see the order summary")
    expect(page.get_by_text("juego de palas")).to_be_visible()

    summary = page.get_by_label("Resumen del Pedido")

    expect(summary.get_by_text("15.99 €")).to_be_visible()
    expect(summary.get_by_text("3.36 €")).to_be_visible()
    expect(summary.get_by_text("5.00 €")).to_be_visible()
    expect(summary.get_by_text("24.35 €")).to_be_visible()

    print("And the user clicks on proceed to payment")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("When the user fills the checkout form")
    page.get_by_placeholder("María González").fill("Maria Diaz")
    page.get_by_placeholder("maria@example.com").fill("test@gmail.com")
    page.get_by_placeholder("Rúa da Raíña, 25, Lugo, 27001").fill("Calle Aragón, 25, Madrid")
    page.get_by_placeholder("4242 4242 4242 4242").fill("4242424242424242")
    
    print("And the user completes the purchase")
    page.get_by_role("button", name="Completar Compra").click()

    print("Then the user should see the success message")
    expect(page.get_by_text("Compra Realizada con Éxito")).to_be_visible()