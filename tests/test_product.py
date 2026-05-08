from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


def test_visit(page: Page):
    print("When the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("Then the user sees the product category “Plants”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("Plantas")

    print("And the user sees the product name “Ficus Lyrata”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("Ficus Lyrata")

    print("And the user sees the product price “35.00 €”")
    expect(page.get_by_label("Catálogo de productos").get_by_role("list")).to_contain_text("35.00 €")


def test_complete_purchase_valid_data(page: Page):    #GRIMANESA
    print("Given the user opens the products page")
    products_page = ProductsPage(page)
    products_page.open_products_page()

    print("When the user filters by name “palas”")
    products_page.search_product("palas")

    print("And the user adds the product to the cart")
    products_page.add_product_to_cart("Juego de Palas")

    print("And the user clicks on Finalizar Compra")
    products_page.click_checkout()

    print("Then the user should see the order summary")
    expect(page.get_by_text("juego de palas")).to_be_visible()

    summary = page.get_by_label("Resumen del Pedido")

    expect(summary.get_by_text("15.99 €")).to_be_visible()
    expect(summary.get_by_text("3.36 €")).to_be_visible()
    expect(summary.get_by_text("5.00 €")).to_be_visible()
    expect(summary.get_by_text("24.35 €")).to_be_visible()

    print("And the user clicks on proceed to payment")
    products_page.click_proceed_to_payment()

    print("When the user fills the checkout form")
    products_page.fill_checkout_form(
    "Maria Diaz",
    "test@gmail.com",
    "Calle Aragón, 25, Madrid",
    "4242424242424242"
    )
    
    print("And the user completes the purchase")
    products_page.complete_purchase()

    print("Then the user should see the success message")
    products_page.verify_success_message("Compra Realizada con Éxito")