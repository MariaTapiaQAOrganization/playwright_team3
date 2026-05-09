from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage

def test_checkout_with_empty_card_details(page: Page): #MARÍA

    products_page = ProductsPage(page)
    checkout_page = CheckoutPage(page)
    cart_page = CartPage(page)

    print("Given the user opens the products page")
    products_page.open_products_page()

    print("When the user filters by name palas")
    products_page.search_product("palas")

    print("And the user adds the product to the cart")
    products_page.add_product_to_cart("Juego de palas")

    print("and visits the cart page")
    products_page.go_to_cart()

    print("and clicks on Proceed to Checkout")
    cart_page.click_checkout()
    
    print("when the user enters the valid name Maria Diaz")
    checkout_page.fill_name("Maria Diaz")

    print("and enters the valid email address test@gmail.com")
    checkout_page.fill_email("test@gmail.com")
    
    print("and enters the valid address Calle Aragón, 25 Madrid")
    checkout_page.fill_address("Calle Aragón, 25 Madrid")

    print("and clicks on completar la compra")
    checkout_page.complete_purchase()

    print ("Then the user remains on the checkout page")
    checkout_page.verify_checkout_page()


def test_checkout_invalid_card (page: Page): #MARIA

    products_page = ProductsPage(page)
    checkout_page = CheckoutPage(page)
    cart_page = CartPage(page)

    print("Given the user opens the products page")
    products_page.open_products_page()

    print("When the user filters by name “palas”")
    products_page.search_product("palas")

    print("And the user adds the product to the cart")
    products_page.add_product_to_cart("Juego de palas")

    print("and visits the cart page")
    products_page.go_to_cart()

    print("and clicks on Proceed to Checkout")
    cart_page.click_checkout()
    
    print("when the user enters the valid name Maria Diaz")
    checkout_page.fill_name("Maria Diaz")

    print("and enters the valid email address test@gmail.com")
    checkout_page.fill_email("test@gmail.com")
    
    print("and enters the valid address Calle Aragón, 25 Madrid")
    checkout_page.fill_address("Calle Aragón, 25 Madrid")

    print("and enters the invalid card number 1111 4242 4242 4242")
    checkout_page.fill_card ("1111 4242 4242 4242")

    print("and clicks on completar la compra")
    checkout_page.complete_purchase()

    print ("should see an error message regarding the card") 
    checkout_page.verify_card_error_message()
