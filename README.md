# Planer Destinacija

Ovaj projekt je jednostavna Flask aplikacija za upravljanje destinacijama. Omogućuje korisnicima dodavanje, pregledavanje, ažuriranje i brisanje destinacija. Aplikacija je kontejnerizirana pomoću Dockera, što olakšava njezino postavljanje i pokretanje.

## Preduvjeti

- Python 3.9+
- Docker (za kontejnerizaciju)
- Git

## Instalacija

### Kloniranje Repozitorija

1. Klonirajte repozitorij:

    ```sh
    git clone https://github.com/YOUR_USERNAME/Destination-Planner.git
    cd Destination-Planner
    ```

### Postavljanje Virtualnog Okruženja

2. Kreirajte virtualno okruženje i aktivirajte ga:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate   # Na Windowsu
    source venv/bin/activate  # Na macOS/Linuxu
    ```

3. Instalirajte ovisnosti:

    ```sh
    pip install -r requirements.txt
    ```

## Pokretanje Aplikacije Lokalno

Za pokretanje aplikacije lokalno bez Dockera:

1. Provjerite je li virtualno okruženje aktivirano.

2. Pokrenite Flask aplikaciju:

    ```sh
    python run.py
    ```

Aplikacija će biti dostupna na `http://localhost:5000`.

## Pokretanje Aplikacije s Dockerom

Za izgradnju i pokretanje aplikacije koristeći Docker:

1. Izgradite Docker sliku:

    ```sh
    docker build -t my-flask-app .
    ```

2. Pokrenite Docker kontejner:

    ```sh
    docker run -d -p 8000:8000 --name flask-app-container -v --put do file-- :/app/instance my-flask-app
    ```

Aplikacija će biti dostupna na `http://localhost:5000`.

## Korištenje Aplikacije

Aplikacija pruža web sučelje za upravljanje destinacijama. Možete dodavati, uređivati i brisati destinacije kroz obrazac na glavnoj stranici.

### Dodavanje Destinacije

1. Otvorite aplikaciju u svom web pregledniku.
2. Ispunite podatke o destinaciji u obrascu.
3. Kliknite na gumb "Dodaj destinaciju".

### Uređivanje Destinacije

1. Kliknite na gumb "Uredi" pored destinacije koju želite urediti.
2. Unesite nove podatke u prompt.
3. Potvrdite promjene.

### Brisanje Destinacije

1. Kliknite na gumb "Izbriši" pored destinacije koju želite izbrisati.
2. Potvrdite brisanje.
