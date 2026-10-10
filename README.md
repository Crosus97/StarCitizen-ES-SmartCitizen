# Star Citizen en español + mejoras de Smart Citizen

Traducción al español de Star Citizen con las **mejoras de Smart Citizen** integradas: estadísticas de naves, componentes, armas y misiles en sus descripciones, recompensas de misiones (XP, blueprints), datos de fabricación y más.

- **Versión del juego:** Alpha 4.10 (LIVE)
- **Archivo:** `live/global.ini`

## Instalación con SC Launch Configurator (recomendado)

1. Abre SC Launch Configurator y entra en **Star Citizen URLs de Actualización de Traducción**.
2. En **Select Language** elige **Spanish (Spain)**.
3. En **Translation URL** pega:
   ```
   https://raw.githubusercontent.com/Crosus97/StarCitizen-ES-SmartCitizen/refs/heads/main/live/global.ini
   ```
4. Pulsa **Validate** y luego **Aplicar**. Deja **Blueprint URL** vacío.

El launcher descargará la versión más reciente cada vez que se actualice este repo.

## Instalación manual

1. Descarga [`live/global.ini`](live/global.ini).
2. Cópialo en:
   ```
   C:\...\StarCitizen\LIVE\data\Localization\spanish_(spain)\global.ini
   ```
3. En `C:\...\StarCitizen\LIVE\user.cfg` añade (o ajusta) la línea:
   ```
   g_language = spanish_(spain)
   ```

## Créditos

- **Traducción:** [Thord82/Star_citizen_ES](https://github.com/Thord82/Star_citizen_ES) (rama `propuestas_thord`). Todo el mérito de la traducción es suyo; los errores de traducción se reportan en su repositorio.
- **Mejoras:** generadas con Smart Citizen (v2.3.1) de Osiris DevWorks a partir del `Data.p4k` del juego.
- Las claves que aún no están traducidas aparecen en inglés.

Proyecto no oficial, sin relación con Cloud Imperium Games.
