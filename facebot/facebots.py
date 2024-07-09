import sys
import time
import locale
import warnings
import colorama
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Dillerin seçeneklerini güncelleyelim
menu_options = {
    'de': f"""
[{Fore.GREEN}Willkommen {Fore.YELLOW}bitte {Fore.RESET}wählen Sie die gewünschte Prozedur aus.]
    1 - Automatische Freundschaftsanfragen annehmen.

    2 - {Fore.RED}Automatische Freundschaftsanfragen senden -> (In Wartung){Fore.RESET}
""",
    'tr': f"""
[{Fore.GREEN}Hoş geldiniz {Fore.YELLOW}lütfen {Fore.RESET}yapmak istediğiniz işlemi seçiniz.]
    1 - Otomatik arkadaş isteğini kabul et.

    2 - {Fore.RED}Otomatik arkadaş isteği gönder --> (Bakımda){Fore.RESET}
""",
    'en': f"""
[{Fore.GREEN}Welcome {Fore.YELLOW}please {Fore.RESET}select the procedure you want to perform.]
    1 - Accept automatic friend requests.

    2 - {Fore.RED}Send automatic friend requests --> (In maintenance){Fore.RESET}
"""
}

login_options = {
    'de': {1: 'Facebook geöffnet!', 2: 'Bitte geben Sie die E-Mail-Adresse Ihres Kontos ein: ',
           3: 'Bitte geben Sie Ihr Kontopasswort ein:'},
    'tr': {1: 'Facebook açıldı!', 2: 'Lütfen hesabınızın e-posta adresini girin: ',
           3: 'Lütfen hesabınızın şifresini girin:'},
    'en': {1: 'Facebook is opened!', 2: 'Please enter your account\'s email address: ',
           3: 'Please enter your account password: '}
}

exit_options = {
    'de': "Beenden",
    'tr': "Çıkılıyor!",
    'en': "Exiting"
}

class Facebook:
    ACCEPT = 1
    SEND = 2

class FacebookAutomation:
    def __init__(self):
        # Initialize colorama
        colorama.init()

        # Define the preferences
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.binary_location = r'127.0.2\firefox.exe'
        self.driver = webdriver.Firefox(service=Service("geckodriver.exe"), options=options)
        #Service(GeckoDriverManager().install())

        # Get the language code from the locale
        self.language_code = locale.getdefaultlocale()[0].split('_')[0]  # Use default locale

    def FacebookLogin(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        print(login_options.get(self.language_code, login_options['en'])[1])

        try:
            mail = input(login_options.get(self.language_code, login_options['en'])[2])
            pasw = input(login_options.get(self.language_code, login_options['en'])[3])

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
            email = driver.find_element(By.ID, 'email')

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'pass')))
            password = driver.find_element(By.ID, 'pass')

            email.send_keys(mail)
            password.send_keys(pasw)

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'login')))
            login_button = driver.find_element(By.NAME, 'login')
            login_button.click()

        except Exception as e:
            print(f"Error during login: {e}")

    def FacebookAccept(self):
        driver = self.driver
        i = 0
        while True:
            try:
                i+=1
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div/a/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]')))
                confirm = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[4]/div/div/a/div[1]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[1]')
                confirm.click()
                driver.refresh()
                time.sleep(0.4)
                print(f"{i} request accepted")
            except Exception as e:
                print("All friends accepted or an error occurred.")
                print("Alle Freunde akzeptiert oder ein Fehler ist aufgetreten.")
                print("Tüm arkadaşlar kabul edildi veya bir hata oluştu.")

    def FacebookSend(self):
        print(f"{Fore.RED}{exit_options.get(self.language_code, exit_options['en'])}{Fore.RESET}")
        self.driver.quit()
        sys.exit()

    def menu(self):
        self.FacebookLogin()
        self.driver.get("https://www.facebook.com/friends/requests")

        print(menu_options.get(self.language_code, menu_options['en']))

        try:
            user_input = int(input(">"))
            if user_input == Facebook.ACCEPT:
                self.FacebookAccept()
            elif user_input == Facebook.SEND:
                self.FacebookSend()
            else:
                print(f"{Fore.RED}Invalid option selected.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

FaceAuto = FacebookAutomation()
FaceAuto.menu()

# bu kod Mücahit(Blass) Tarafından Yazılmıştır.
# Bu kod Muhammed(Karabei) tarafından düzenlenmiştir.
