import sys
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


print("""HOŞGELDİNİZ LÜTFEN YAPTIRMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ

1) Otomatik Arkadaş Kabul(Arkaplanda)

2) Otomatik Arkadaş İsteği Atma(Bakımda)


""")
secim = input("1 Yada 2: ")
arkadas_kabul = 0
arkadas_ekle = 0
if secim == "1":
    arkadas_kabul = 1
elif secim == "2":
    arkadas_ekle = 1
#Geckodriver Dosya yolunu belirtiniz
path = ''
service = Service(path)

firefox_options = webdriver.FirefoxOptions()
#firefox dosya yolunu belirtiniz
firefox_options.binary_location = ""
firefox_options.add_argument('-headless')  # Arka planda çalışır.
browser = webdriver.Firefox(service=service, options=firefox_options)

def login_to_facebook():
    browser.get("https://tr-tr.facebook.com/?_=_")
    time.sleep(2)
    print("Facebook açıldı!")
    pyautogui.hotkey('ctrl', 'm')
    


    try:
        button = browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
        print("Buton bulundu!")
    except Exception as e:
        print("Buton bulunamadı!", e)

    # Giriş bilgilerini bulup giriyoruz
    kullanicigirismail = input("Lütfen Hesabınızın mail adresini giriniz: ")
    kullanicigirissifre = input("Lütfen hesabınızın şifresini giriniz: ")
    kullanici_mail_giris = browser.find_element(By.XPATH, "//input[@id='email']")
    kullanici_sifre_giris = browser.find_element(By.XPATH, "//input[@id='pass']")
    print("Giriş noktası bulundu")
    time.sleep(1)

    kullanici_mail_giris.send_keys(kullanicigirismail)
    kullanici_sifre_giris.send_keys(kullanicigirissifre)

    # Giriş butonuna tıklıyoruz
    login_button = browser.find_element(By.XPATH, "//button[@name='login']")
    login_button.click()
    print("Giriş butonuna tıklandı!")
    time.sleep(2)
    current_url = browser.current_url
    if "https://www.facebook.com/" in current_url:
        print("Facebook'tasınız.")
    else:
        login_to_facebook()

    browser.get("https://www.facebook.com/friends")
    time.sleep(2)

def arkadas_kabul_etme(xpath, index):
    try:
        arkadas_kabul = browser.find_element(By.XPATH, xpath)
        arkadas_kabul.click()
        print(f"Arkadaş kabul edildi {index}")
        time.sleep(0.5)
    except Exception as e:
        print(f"Arkadaş kabul edilemedi {index}:", e)
xpath_listesi = [
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[10]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[11]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]",
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[12]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]"
]

login_to_facebook()

if arkadas_kabul == 1:
    while True:
        for i, xpath in enumerate(xpath_listesi):
            arkadas_kabul_etme(xpath, i + 1)
            if (i + 1) % 11 == 0:
                print("11 arkadaş kabul edildi, sayfa yenileniyor...")
                browser.refresh()
                time.sleep(2)
                break

# Tarayıcıyı kapat
browser.quit()
