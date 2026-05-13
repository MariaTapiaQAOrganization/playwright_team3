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

    cart_page = CartPage(page)

    print("When the user visits the products page")
    cart_page.visit_product()

    print("And filters by name “Sansevieria”")
    print("And adds the product to the cart")
    cart_page.fill_name_plant_and_add()

    print("And clears the filter")
    cart_page.clear_filter()

    print("And filters by name “maceta de barro”")
    print("And adds the product to the cart")
    cart_page.fill_name_pot_and_add()

    print("And visits the shopping cart")
    cart_page.click_on_cart()
  
    print("Then they should see the name “Sansevieria”")
    print("And its category “Plants”")
    print("And its price “22.00 €”")
    cart_page.verify_details_plant()

    print("And they should see the product “Maceta de Barro Grande”")
    print("And its category “Pots”")
    print("And its price “10.50 €”")
    cart_page.verify_details_pot()

    print("And they should see the order summary with the following details:")
    print("Subtotal, the sum of both items “32.50”")
    print("VAT 21% “6.83”")
    print("And they should see the delivery cost “5.00”")
    print("And they should see the total “44.33”")
    cart_page.verify_summary_details()

    print("When they click on empty cart")
    print("Then they should see the message “Tu carrito está vacío”")
    cart_page.empty_cart()



