from selenium.webdriver.common.by import By
import time
from user_session import get_user_session, user_sessions
import random
import requests
import os


def get_driver(user_id):
    session = get_user_session(user_id)

    return session.driver, session

def generate_content_from_random_page(user_id, message):
    driver, session = get_driver(user_id)
    result_messages = []
    try:
        modefied_message_for_url = '+'.join(message.strip().split()).lower()

        driver.get("https://www.pornhub.com/")

        search_div = driver.find_element(By.XPATH, '//*[@id="searchBarContainer"]')

        input_field = search_div.find_element(By.TAG_NAME, "input")

        input_field.send_keys(message)

        btn_search_element = driver.find_element(By.XPATH, '//*[@id="btnSearch"]')

        btn_search_element.click()

        time.sleep(1)

        error_element_div = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[3]')

        if "Error Page Not Found" in error_element_div.text:
            return [-1]

        div_all_results_number = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[4]/div/div/div[1]/div[2]')

        results_number = int(div_all_results_number.text.split()[-1])

        if results_number < 300:
            return []

        page_number = int(((results_number - 33) / 33))

        page_number = 455 if page_number > 455 else page_number

        random_page = random.randint(1, page_number)

        url = f"https://www.pornhub.com/video/search?search={modefied_message_for_url}&page=" \
              f"{random_page}"

        driver.get(url)

        time.sleep(1)

        temp_div_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[4]/div/div/div[1]')

        temp_div_element.click()

        # video_search_results = driver.find_element(By.ID, 'videoSearchResult') # здесь в некоторых случаях выдает ошибку
        video_search_results = driver.find_element(By.XPATH,
                                                   '//ul[@id="videoSearchResult"]')  # здесь в некоторых случаях выдает ошибку


        results = video_search_results.find_elements(By.TAG_NAME, 'li')

        if results:

            results.pop(0)

            random.shuffle(results)

            new_random_results = random.sample(results, 10)

            for result in new_random_results:

                div_element_1 = result.find_element(By.CSS_SELECTOR, '.wrap.flexibleHeight')

                div_element_2 = div_element_1.find_element(By.CSS_SELECTOR, '.thumbnail-info-wrapper.clearfix')

                span_video_name_text = div_element_2.find_element(By.CLASS_NAME, 'title').text

                div_photo_element = result.find_element(By.CLASS_NAME, 'phimage')
                a_element = div_photo_element.find_element(By.TAG_NAME, 'a')
                video_link = f"{a_element.get_attribute('href')}"
                img_element = a_element.find_element(By.TAG_NAME, 'img')
                image_url = img_element.get_attribute("src")

                result_message = f"📸 ПРЕВЬЮ:\n{image_url}\n📇 НАЗВАНИЕ:\n{span_video_name_text}\n🔗 ССЫЛКА НА ВИДЕО:\n{video_link}"

                result_messages.append(result_message)

    except Exception as error:
        print(error)
    finally:
        session.close()
        del user_sessions[user_id]
        return result_messages


# messages = generate_content_from_random_page(777, "Анал")
# print(messages)
