# Star Citizen en español + mejoras de Smart Citizen

Traducción al español de Star Citizen con las **mejoras de Smart Citizen** integradas: estadísticas de naves, componentes, armas y misiles en sus descripciones, recompensas de misiones (XP, planos), datos de fabricación y más.

- **Versión del juego:** Alpha 4.10 (LIVE)
- **Archivo:** [`live/global.ini`](live/global.ini)

> ⚙️ **Sistema semiautomático, no gestionado.**
> Este repositorio no tiene a nadie revisándolo ni manteniéndolo de forma activa. El archivo se regenera con Smart Citizen tras cada parche o actualización de la traducción, y el resto del proceso es automático. Si algo se rompe, se corregirá, pero sin plazos ni garantías. Los errores de traducción se reportan en [el repositorio de Thord82](https://github.com/Thord82/Star_citizen_ES/issues), no aquí.

## Instalación con SC Launch Configurator (recomendado)

1. Abre SC Launch Configurator y entra en **Star Citizen URLs de Actualización de Traducción**.
2. En **Select Language** elige **Spanish (Spain)**.
3. En **Translation URL** pega:
   ```
   https://raw.githubusercontent.com/Crosus97/StarCitizen-ES-SmartCitizen/refs/heads/main/live/global.ini
   ```
4. Pulsa **Validate** y luego **Aplicar**. Deja **Blueprint URL** vacío: los planos ya vienen incluidos en las misiones.

La URL no cambia nunca: el launcher descarga la versión más reciente cada vez que se actualiza este repo.

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

> No uses a la vez SC Launch Configurator y Smart Citizen en el mismo PC: los dos escriben el mismo `global.ini` y el último que se ejecuta pisa al otro.

## Cómo se actualiza

1. Se genera `global.ini` con Smart Citizen a partir de la traducción de Thord82 y del `Data.p4k` del juego (este paso es manual: necesita el juego instalado).
2. Al subirlo, una GitHub Action ([`branding.yml`](.github/workflows/branding.yml)) cambia automáticamente la línea de versión de la pantalla de inicio.

## Créditos

- **Traducción:** [Thord82/Star_citizen_ES](https://github.com/Thord82/Star_citizen_ES) (rama `propuestas_thord`). Todo el mérito de la traducción es suyo.
- **Mejoras:** generadas con Smart Citizen (v2.4.0) de Osiris DevWorks.
- **Recopilación y automatización:** Crosus97.
- Los textos que aún no están traducidos aparecen en inglés.

¿Usas SCMDB? → Traducción al español en [SCMDB_LANG](https://github.com/Crosus97/SCMDB_LANG)

Proyecto no oficial, sin relación con Cloud Imperium Games.
