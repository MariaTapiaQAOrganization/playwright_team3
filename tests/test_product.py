from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


def test_visit(page: Page):   #KARELIA scrum-37

    products_page = ProductsPage(page)

    print("When the user opens the products pag")
    products_page.open_products_page()

    print("Then the user sees the product category 'Plants'")
    products_page.verify_product_category("Plantas")

    print("And the user sees the product name 'Ficus Lyrata'")
    products_page.verify_product_name("Ficus Lyrata")

    print("And the user sees the product price '35.00 €'")
    products_page.verify_product_price("35.00 €")





    

