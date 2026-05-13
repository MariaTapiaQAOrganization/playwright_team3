from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"
        self.title = "Vida Verde"

    def open_home_page(self):
        self.page.goto(self.url)

    def verify_home_page_title(self):
        expect(self.page.get_by_role("heading", name=self.title)).to_be_visible()