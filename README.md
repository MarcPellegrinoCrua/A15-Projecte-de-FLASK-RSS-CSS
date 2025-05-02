# README.md

## 📚 Projecte RSS Reader amb Flask + Bootstrap

Aquesta aplicació et permet llegir notícies dels diaris *La Vanguardia* i *El Punt Avui* des de fitxers XML locals o directament des del web (mode remot). Està feta amb **Flask**, **Feedparser** i **Bootstrap**.

```bash

## 🔧 Instal·lació i execució

1. **Crea un entorn virtual:**
   
   - A Linux/Mac:

     python3 -m venv .venv
     source .venv/bin/activate

   - A Windows:

     python -m venv .venv
     .venv\Scripts\activate


2. **Instal·la les dependències:**

   pip install flask feedparser


3. **Executa el servidor:**
   flask run --debug

4. **Obre el navegador:**

   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## 🌐 Modes de lectura RSS

- **Mode local** (llegeix fitxers XML des de la carpeta `rss/`):

  http://127.0.0.1:5000/lavanguardia/economia Mode per defecte


- **Mode remot** (llegeix l'RSS directament des d'internet):

  http://127.0.0.1:5000/lavanguardia/economia?mode=remot Botó per accedir al mode remot incorporat al HTML


## 📰 Seccions disponibles

### La Vanguardia
- Portada (home)
- Política (politica)
- Esports (deportes)
- Economia (economia)
- Cultura (cultura)

### El Punt Avui
- Economia (economia)
- Política (politica)
- Esports (esports)
- Territori (territori)
- Cultura (cultura)
