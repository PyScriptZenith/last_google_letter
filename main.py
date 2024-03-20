import os
import time

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKJjkP8k_tP-eoXoFKxnWqZ11i3K4-0KqF_jy4W_H-lH_56DZgHlPYXWCZ2Ssj_wuxG8_v8D&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1578032931%3A1710937177178617&theme=glif&ddm=0")

    email_input = page.get_by_label("Email or phone")
    email_input.fill(MY_EMAIL)

    next_button = page.get_by_role("button", name="Next")
    next_button.click()

    password_input = page.get_by_label("Enter your password")
    password_input.fill(MY_PASSWORD)

    password_next_button = page.get_by_role("button", name="Next")
    password_next_button.click()

    last_email = page.wait_for_selector('div[role="main"] table[role="grid"] tr[role="row"]:first-child')
    last_email.click()

    time.sleep(10)
    browser.close()