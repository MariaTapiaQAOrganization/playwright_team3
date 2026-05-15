from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.confirmation_page import ConfirmationPage


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



def test_complete_purchase_valid_data(page: Page):    #GRIMANESA
    print("Given the user opens the products page")
    
    products_page = ProductsPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page = ConfirmationPage(page)
    cart_page = CartPage(page)

    products_page.open_products_page()

    print("When the user filters by name “palas”")
    products_page.search_product("palas")

    print("And the user adds the product to the cart")
    products_page.add_product_to_cart("Juego de Palas")

    print("And the user clicks on Finalizar Compra")
    cart_page.click_finish_purchase()

    print("Then the user should see the order summary")
    checkout_page.verify_order_summary_product("juego de palas")

    checkout_page.verify_order_summary_prices(
        "15.99 €",
        "3.36 €",
        "5.00 €",
        "24.35 €"
    )

    print("And the user clicks on proceed to payment")
    cart_page.click_checkout()

    print("When the user fills the checkout form")
    checkout_page.fill_name("Maria Diaz")
    checkout_page.fill_email("test@gmail.com")
    checkout_page.fill_address("Calle Aragón, 25, Madrid")
    checkout_page.fill_card("4242424242424242")
    
    print("And the user completes the purchase")
    checkout_page.complete_purchase()

    print("Then the user should see the success message")
    confirmation_page.verify_purchase_completed()