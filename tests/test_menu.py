from playwright.sync_api import Page, expect
from pages.about_us_page import AboutUsPage
from pages.components.menu import Menu
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


#KARELIA scrum-36

def test_visit_menu_links(page:Page):  
    
    home_page = HomePage(page)
    menu = Menu(page)
    about_us_page = AboutUsPage(page)
    products_page = ProductsPage(page)
    contact_page = ContactPage(page)

#HOMEPAGE
    print("Given the user opens the page Inicio | Vida Verde") 
    home_page.open_home_page()

    print("Then they should see the title “Vida Verde”")  
    home_page.verify_home_page_title()

#ABOUT US
    print("When they click on “About us”")
    menu.visit_menu_about_us()

    print("Then they should see the title “About us”")
    about_us_page.verify_about_us_page_title()

    print("And they should see the URL Quiénes Somos | Vida Verde")
    about_us_page.verify_about_us_page_url()

#PRODUCTS
    print("When they click on “Products”")
    menu.visit_menu_products()

    print("Then they should see the title “Product Catalogue”")
    products_page.verify_products_title()

    print("And they should see the URL Nuestros Productos | Vida Verde")
    products_page.verify_products_url()


#CONTACT

    print("When they click on “Contact”")
    menu.visit_menu_contact()

    print("Then they should see the title “Contact us”")
    contact_page.verify_contact_title()
    
    print("And they should see the URL Contáctanos | Vida Verde")
    contact_page.verify_contact_url()


    
