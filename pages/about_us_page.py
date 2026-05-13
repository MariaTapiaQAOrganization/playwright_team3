from playwright.sync_api import Page, expect

class AboutUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/about"
        self.title = "Quiénes Somos"
    
    def verify_about_us_page_title(self):
        expect(self.page.get_by_role("heading", name=self.title)).to_be_visible()

    def verify_about_us_page_url(self):
        expect(self.page).to_have_url(self.url)