# Crypto Data Pipeline

## Yleiskatsaus

Tämä projekti on PEP 8 -standardien mukaisesti toteutettu Crypto Data Pipeline, joka hakee kryptovaluuttahintoja CoinGecko API:sta, tallentaa ne CSV-muodossa ja lataa ne Google BigQueryyn analysointia varten. Projektiin kuuluu myös visualisointi BigQueryn ja Looker Studion avulla.

## Käytetyt teknologiat ja kirjastot

Projektissa käytetyt teknologiat ja kirjastot:

- **Python** – pääasiallinen ohjelmointikieli
- **Google Cloud BigQuery** – tietovarasto datan tallentamiseen ja analysointiin
- **CoinGecko API** – kryptovaluuttahintojen hakemiseen
- **pandas** – datan käsittelyyn ja muotoiluun
- **requests** – API-kutsujen tekemiseen
- **google-cloud-bigquery** – BigQuery-yhteyksiin
- **python-dotenv** – ympäristömuuttujien hallintaan
- **logging** – tapahtumien ja virheiden lokittamiseen
- **ChatGPT** – projektin suunnitteluun ja toteutukseen

## Asennus ja käyttö

### 1. Asenna riippuvuudet

```bash
pip install requests pandas google-cloud-bigquery python-dotenv pyarrow
```

### 2. Aseta ympäristömuuttuja Google Cloud -avaimelle

```bash
export GOOGLE_APPLICATION_CREDENTIALS="C:/Users/Matias/Desktop/crypto_data_pipeline/credentials/crypto-data-pipeline.json"
```

### 3. Hae data CoinGecko API:sta

```bash
python 1_scripts/fetch_data.py
```

### 4. Testaa BigQuery-yhteys

```bash
python 1_scripts/test_connection.py
```

### 5. Lataa data BigQueryyn

```bash
python 1_scripts/load_data.py
```

### 6. Visualisoi BigQueryssä

1. Avaa BigQuery Console
2. Suorita SQL-kysely:
   ```sql
   SELECT * FROM `crypto-data-pipeline-449309.crypto_dataset.crypto_prices`;
   ```
3. Klikkaa "Explore Data" → "Explore with Charts" ja valitse pylväsdiagrammi.

### 7. Looker Studio -visualisointi

Lopuksi dataa voidaan visualisoida Looker Studiossa, esimerkiksi pylväsdiagrammin avulla, joka näyttää kryptovaluuttojen hinnat viimeisimmästä datasta.

## Lisenssi

Tämä projekti on lisensoitu **MIT-lisenssillä**, mikä tarkoittaa, että kuka tahansa saa käyttää, kopioida, muokata ja levittää tätä ohjelmistoa **edellyttäen, että alkuperäinen tekijä mainitaan**.
