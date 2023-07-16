# Fizjoterapia

## Opis
Projekt Fizjoterapii to zaawansowana aplikacja webowa stworzona w celu ułatwienia zarządzania i organizacji gabinetu fizjoterapeutycznego. Aplikacja umożliwia zarówno pacjentom, jak i fizjoterapeutom skuteczne planowanie wizyt, śledzenie postępów terapii oraz współpracę w celu osiągnięcia jak najlepszych wyników.

## Funkcje

Rejestracja pacjentów: Pacjenci mogą założyć swoje konta w aplikacji, podając niezbędne dane osobowe oraz historię medyczną, które ułatwią fizjoterapeutom dostosowanie odpowiednich planów terapeutycznych.

Terminy wizyt: Pacjenci mają możliwość wyświetlenia dostępnych terminów wizyt i samodzielnej rezerwacji terminu, co pozwala na elastyczne planowanie terapii.

Kalendarz fizjoterapeuty: Fizjoterapeuci mają dostęp do spersonalizowanego kalendarza, który pozwala na zarządzanie ich harmonogramem wizyt, unikając kolizji terminów.

Dokumentacja: Istnieje możliwość przechowywania dokumentacji medycznej pacjentów w bezpieczny i poufny sposób.

## Technologie

Projekt został wykonany przy użyciu następujących technologii:

- HTML
- CSS
- JavaScript
- Django

## Wymagania

Przed rozpoczęciem pracy z projektem upewnij się, że na Twoim komputerze zainstalowane są:

- Python 3.8 lub nowszy
- pip
- virtualenv

## Instalacja i uruchomienie projektu

1. Sklonuj repozytorium na swój komputer:

git clone git@github.com:OnizukaGit/Physiotherapy_site.git

2. Utwórz wirtualne środowisko i aktywuj je:


cd Physiotherapy_site

virtualenv venv

source venv/bin/activate

3. Zainstaluj wymagane biblioteki:

pip install -r requirements.txt

4. Przeprowadź migracje bazodanowe:

python manage.py migrate

5. Utwórz konto administratora:

python manage.py createsuperuser

6. Uruchom serwer:

python manage.py runserver

7. Otwórz przeglądarkę internetową i przejdź do adresu http://localhost:8000/ aby uruchomić stronę.

Autorzy
OnizukaGit


Jeśli masz jakieś uwagi lub sugestie dotyczące projektu, zachęcam do kontaktu z autorem.

Dziękuję za zainteresowanie się moim projektem!


# Uwaga
Projekt powstał w celu edukacyjnym. Aby korzystać w pełni legalnie z kodu frontendowego, należy zakupić licenjce u autora kodu. 
