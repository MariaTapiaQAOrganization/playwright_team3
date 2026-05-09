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








