# ScraperAscend

Un scraper para recolectar todos los precios de la competencia para cada producto y poder tomar mejores deciciones al ponerle precio a nuestros productos.
Paginas:
- https://wakomercadonatural.com/

## Uso

1. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```
   
2. Ejecuta el scraper para obtener los precios. Por defecto se analiza solo la primera página y se guarda la información en `productos.xlsx`:


   ```bash
   python scraper.py
   ```

   Usa `--pages` para indicar la cantidad de páginas de la tienda a procesar:

   ```bash
   python scraper.py --pages 3
   ```

   Si el archivo `productos.xlsx` ya existe, se actualiza con los nuevos datos.

