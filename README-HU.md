# SuperMupla
- még nem is igazán egy játék, július 20-án kezdtem el
- egy egyszerű Pythonban írott 2D platformer játék (lesz), ami Pythonban konfigurálható és bővíthető (saját ellenségek, blockok, pályák) (legalábbis remélhetőleg)
- egy jobb újraírása a [SuperMuki](https://github.com/Krist0FF-T/supermuki) játékomnak, amit 2022 februárban írtam
- inspired by
- inspiráció
    - [SuperTux](https://github.com/SuperTux/supertux), Super Mario Bros, és egyéb 2D platformerek amik "Super"-rel kezdődnek
    - Fireboy & Watergirl (Lokális Co-Op)

# Telepítés (még csak Linuxon)
1. telepíts python-t (és git-et) ha még nincs
2. töltsd le a kódot
    a) git-tel:
        ```bash
        git clone https://github.com/Krist0FF-T/supermupla
        ```
    b) GitHub-ról (git nélkül)
        1. https://github.com/Krist0FF-T/supermupla
        2. nyomd meg a kék "Code" gombot
        3. alul "Download ZIP" gomb

3. futtasd a setup script-et
```bash
source setup.sh
```
4. activate the created virtual environment:
```bash
source venv/bin/activate
```
5. futtasd a játékot
```bash
python supermupla.py
```

# Érdekességek

A név eredete:
- egy saját script-tel generáltam, ami úgy generál új szavakat, hogy megnézi, hogy a bemeneti szavakban milyen karakterek után milyen karakterek jönnek. Ezek jelen esetben a "super", "platformer" and "multiplayer" szavak voltak
- utána adtam neki értelmet
- Super: mert sok 2d platformer "Super"-rel kezdődik
- Mu: **mu**lti- (-player)
- Pla: -**pla**yer, vagy **pla**tformer




