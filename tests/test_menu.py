from playwright.sync_api import Page, expect

def test_visit_menu_links(page:Page):
    
    print("Given the user opens the page Inicio | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/")
    print("Then they should see the title “Vida Verde”")
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()

    print("When they click on “About us”")
    page.get_by_role("link", name="Quiénes Somos").click()
    print("Then they should see the title “About us”")
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    print("And they should see the URL Quiénes Somos | Vida Verde")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/about")
    
    print("When they click on “Products”")
    page.get_by_role("link", name="Productos").click()
    print("Then they should see the title “Product Catalogue”")
    expect(page.locator("h1")).to_contain_text("Catálogo de Productos")
    print("And they should see the URL Nuestros Productos | Vida Verde")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")

    print("When they click on “Contact”")
    page.get_by_role("link", name="Contacto").click()
    print("Then they should see the title “Contact us”")
    expect(page.locator("h1")).to_contain_text("Contáctanos")
    print("And they should see the URL Contáctanos | Vida Verde")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/contact")

    
