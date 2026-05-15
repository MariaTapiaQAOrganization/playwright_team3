from playwright.sync_api import Page, expect

class Menu:

#ORIGINAL karelia
#    def __init__(self, page: Page):
#        self.page = page
#        self.menu_about_us = "Quiénes Somos"
#        self.menu_products = "Productos"
#        self.menu_contact = "Contacto"
#    
#    def visit_menu_about_us(self):
#        self.page.get_by_role("link", name=self.menu_about_us).click()
#
#    def visit_menu_products(self):
#        self.page.get_by_role("link", name=self.menu_products).click()
#
#    def visit_menu_contact(self):
#        self.page.get_by_role("link", name=self.menu_contact).click()



    def __init__(self, page: Page):
        self.page = page
        self.menu_about_us = "Quiénes Somos"
        self.menu_products = "Productos"
        self.menu_contact = "Contacto"
        self.menu_mobile = "Abrir menú principal"
    
    def isMobile(self):
        size = self.page.viewport_size['width']
        if size < 1024:
            return True;
        else:
            return False;

    def visit_menu_about_us(self):
        if(self.isMobile()):
            #Mobile
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_about_us).click()
        else:
            self.page.get_by_role("link", name=self.menu_about_us).click()

    def visit_menu_products(self):
        if(self.isMobile()):
            #Mobile
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_products).click()
        else:
         self.page.get_by_role("link", name=self.menu_products).click()

    def visit_menu_contact(self):
        if(self.isMobile()):
            #Mobile
            self.page.get_by_role("button", name=self.menu_mobile).click()
            self.page.get_by_role("menuitem", name=self.menu_contact).click()
        else:
            self.page.get_by_role("link", name= self.menu_contact).click()