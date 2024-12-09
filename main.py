from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import chromedriver_autoinstaller
import time
import os

print("--------------Installing Chrome Driver----------------")
chromedriver_autoinstaller.install()
print("--------------Chrome Driver Installed----------------")

class MidjourneyAutomation:
    def __init__(self):    
        self.filepath = self.get_filepath()
        print("Prompts File Loaded Successfully")
        options = webdriver.ChromeOptions()
        user_data_dir = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument(f"user-data-dir={user_data_dir}")
        options.add_argument(f"--profile-directory=WhatsappBot")
        self.driver = uc.Chrome(options=options)
    
    def get_filepath(self):
        filepath = input("Enter Prompts File (or drag and drop the file here):")
        return filepath.strip().strip('"')
    
    def load_prompts(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def all_images_generated(self):
        try:
            while True:
                starting = self.driver.find_elements(By.XPATH, "//span[contains(text(),'Starting...')]")
                submitting = self.driver.find_elements(By.XPATH, "//span[contains(text(),'Submitting...')]")
                complete = self.driver.find_elements(By.XPATH, "//span[contains(text(),'% Complete')]")
                queued = self.driver.find_elements(By.XPATH, "//span[contains(text(),'Queued')]")
                if len(submitting) == 0 and len(complete) == 0 and len(queued) == 0 and len(starting) == 0:
                    return True
                print("Images are still generating...")
                time.sleep(10)  # Wait before checking again
        except Exception as e:
            print(f"Error while checking for image generation status: {e}")
            return False

    def process_prompts(self):
        prompts = self.load_prompts(self.filepath)
        self.driver.get("https://www.midjourney.com/imagine")
        input("Please Login First if Already Login Then Press Enter:")
        for i in range(0, len(prompts), 10):
            batch = prompts[i:i+10]
            for prompt in batch:
                try:
                    # Wait for the input bar to be clickable
                    generate_image = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.ID, "desktop_input_bar"))
                    )
                    generate_image.send_keys(prompt)
                    time.sleep(2)  # Simulate human delay
                    generate_image.send_keys(Keys.ENTER)
                    time.sleep(3)  # Wait before sending the next prompt
                except Exception as e:
                    print(f"Error while submitting prompt: {e}")
            print("Wait for 35 Second before Generating Next 10 Prompts")
            time.sleep(35)
            # Wait for all images to be generated
            if not self.all_images_generated():
                print("Error occurred while waiting for images to be generated.")
                break

        print("All prompts processed")
        self.driver.quit()

if __name__ == "__main__":
    automation = MidjourneyAutomation()
    automation.process_prompts()
