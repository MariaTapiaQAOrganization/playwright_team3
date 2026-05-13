from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage



def test_visit(page: Page):   #KARELIA scrum-37

    products_page = ProductsPage(page)

    print("When the user opens the products page")
    products_page.open_products_page()

    print("Then the user sees the product category “Plants”")
    products_page.verify_product_category()

    print("And the user sees the product name “Ficus Lyrata”")
    products_page.verify_product_name()

    print("And the user sees the product price “35.00 €”")
    products_page.verify_product_price()


def test_filter_by_value_no_result(page: Page):     #KARELIA scrum-45
    
    products_page = ProductsPage(page)
    
    print("When the user visits the products page")
    products_page.visit_product()

    print("And filters by name with no results “manzana”")
    products_page.fill_name_manzana()

    print("Then they should see the message “No se encontraron productos”")
    products_page.message_no_results()



    

