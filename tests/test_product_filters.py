from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


def test_filter_product_by_name_category_and_price(page: Page):  #GRIMANESA
    products_page = ProductsPage(page)
    
    print("Given the user opens the products page")
    products_page.open_products_page()

    print("When the user filters by name Regadera")
    products_page.search_product("Regadera")

    print("And the user selects Herramientas category")
    products_page.filter_by_category("Herramientas")

    print("And the user filters by minimum price")
    products_page.filter_by_min_price("20")

    print("And the user filters by maximum price")
    products_page.filter_by_max_price("25")
    
    print("Then the user should see Regadera Metálica")
    products_page.verify_products_result("Regadera Metálica")