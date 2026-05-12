from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

#TEST MARÍA
def test_cart_remove_items_from_the_cart_and_view_summary(page:Page):  
    
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    print("When the user visits the product page")
    products_page.open_products_page()

    print("and filters by name ficus")
    products_page.search_product("ficus")

    print("and adds the product to the cart")
    products_page.add_product_to_cart("Ficus Lyrata")

    print("and clears the filter")
    products_page.clear_filter()

    print("and filters by name tijeras")
    products_page.search_product("tijeras")

    print("and adds the product to the cart")
    products_page.add_product_to_cart("Tijeras de Podar")

    print("when the user visits the cart page")
    products_page.go_to_cart()

    print("when the user removes the product ficus")
    cart_page.remove_product("Ficus Lyrata")

    print("then the user not see the ficus product")
    cart_page.verify_item_not_visible("Ficus Lyrata")

    print("then the user should see the update summary")
    cart_page.verify_item_visible("Tijeras de Podar")
    cart_page.verify_summary("18.50 €", "3.88 €", "5.00 €", "27.38 €")



def test_add_view_summary_and_empty(page: Page):     #KARELIA scrum-46

    print("When the user visits the products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("And filters by name “Sansevieria”")
    page.get_by_role("searchbox", name="Nombre").fill("sansevieria")

    print("And adds the product to the cart")
    page.get_by_role("button", name="Añadir Sansevieria al carrito").click()

    print("And clears the filter")
    page.get_by_role("button", name="Quitar filtros y ver todos").click()

    print("And filters by name “maceta de barro”")
    page.get_by_role("searchbox", name="Nombre").fill("maceta de barro")

    print("And adds the product to the cart")
    page.get_by_role("button", name="Añadir Maceta de Barro Grande").click()

    print("And visits the shopping cart")
    page.get_by_role("link", name="Carrito de compra").click()
  
    print("Then they should see the name “Sansevieria”")
    expect(page.get_by_role("heading", name="Sansevieria")).to_be_visible()

    print("And its category “Plants”")
    expect(page.get_by_text("Plantas")).to_be_visible()

    print("And its price “22.00 €”")
    expect(page.get_by_text("22.00 €")).to_be_visible()

    print("And they should see the product “Maceta de Barro Grande”")
    expect(page.get_by_role("heading", name="Maceta de Barro Grande")).to_be_visible()

    print("And its category “Pots”")
    expect(page.get_by_text("Macetas")).to_be_visible()

    print("And its price “10.50 €”")
    expect(page.get_by_text("10.50 €")).to_be_visible()

    print("And they should see the order summary with the following details:")
    page.get_by_role("heading", name="Resumen del Pedido")

    print("Subtotal, the sum of both items “32.50”")
    expect(page.get_by_text("32.50 €")).to_be_visible()

    print("VAT 21% “6.83”")
    expect(page.get_by_text("6.83 €")).to_be_visible()

    print("And they should see the delivery cost “5.00”")
    expect(page.get_by_text("5.00 €")).to_be_visible()
    
    print("And they should see the total “44.33”")
    expect(page.get_by_text("44.33 €")).to_be_visible()

    print("When they click on empty cart")
    page.get_by_role("button", name="Vaciar Carrito").click()

    print("Then they should see the message “Tu carrito está vacío”")
    expect(page.get_by_text("Tu carrito está vacío")).to_be_visible()
