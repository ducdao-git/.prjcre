from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def enter_in_field(bot, field, text):
    bot = bot.find_element_by_id(field)
    bot.clear()
    bot.send_keys(text)


def git_login(bot, username, password):
    enter_in_field(bot, "login_field", username)
    enter_in_field(bot, "password", password)
    bot.find_element_by_name("commit").click()


def git_create_repo(bot, repo_name, repo_des):
    bot.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()

    enter_in_field(bot, "repository_name", repo_name)
    enter_in_field(bot, "repository_description", repo_des)
    bot.find_element_by_id("repository_visibility_private").click()

    wait = WebDriverWait(bot, 10)
    wait.until(expected_conditions.element_to_be_clickable((
        By.XPATH, '//*[@id="new_repository"]/div[3]/button'))).click()
