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