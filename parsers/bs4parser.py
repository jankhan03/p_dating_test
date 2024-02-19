import requests as req
from bs4 import BeautifulSoup
import random

def get_pornhub_results(message):
    try:
        modefied_message_for_url = '+'.join(message.strip().split()).lower()

        result = req.get(f"https://www.pornhub.com/video/search?search={modefied_message_for_url}")

        soup = BeautifulSoup(result.content, "html.parser")

        section_title_div_element = soup.find("div", class_="sectionTitle")
        results_counter_div = section_title_div_element.find("div", class_="showingCounter")
        if len(results_counter_div.text) == 1:
            print("No results")
            return []

        results_number = int(results_counter_div.text.split()[-1])
        page_number = int(((results_number - 33) / 33))
        page_number = 100 if page_number > 100 else page_number
        random_page = random.randint(1, page_number)

        result = req.get(f"https://www.pornhub.com/video/search?search={modefied_message_for_url}&page={random_page}")
        soup = BeautifulSoup(result.content, "html.parser")
        video_search_results_ul_element = soup.find("ul", class_="videos search-video-thumbs freeView")
        all_li_elements = video_search_results_ul_element.find_all("li")
        random_li_elements = random.sample(all_li_elements, 10) if len(all_li_elements) >= 10 else all_li_elements
        final_messages = []
        for li_element in random_li_elements:
            description_div_element = li_element.find("div", class_="phimage")
            a_element = description_div_element.find("a")
            video_link = "https://www.pornhub.com" + a_element["href"]
            img_element = a_element.find("img")
            img_link = img_element["src"]
            video_lengh = a_element.find("var", class_="duration").text
            title_element_div = li_element.find("div", class_="thumbnail-info-wrapper clearfix")
            title_text = title_element_div.find("span", class_="title").text.strip()
            message = f"⏳ Длина видео: {video_lengh} минут\n📸 ПРЕВЬЮ:\n{img_link}\n📇 НАЗВАНИЕ:\n{title_text}\n🔗 ССЫЛКА НА ВИДЕО:\n{video_link}"
            final_messages.append(message)

        return final_messages
    except Exception as error:
        print(error)
        return []

# messages = get_pornhub_results("Aletta Ocean")
#
# print(messages)