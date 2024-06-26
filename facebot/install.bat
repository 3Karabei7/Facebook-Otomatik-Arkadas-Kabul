@echo off
echo PIP ile pyautogui ve selenium kütüphanelerini yüklüyor...

pip install pyautogui selenium

echo PyAutoGUI ve Selenium yüklendi.

echo PyInstaller ile facebots.py dosyasını derliyor...

pyinstaller --onefile facebots.py

echo facebots.py dosyası başarıyla derlendi.

pause
