---
slug: "eprom"
url: "/mobilnisite/slovnik/eprom/"
type: "slovnik"
title: "EPROM – Erasable Programmable Read Only Memory"
date: 2025-01-01
abbr: "EPROM"
fullName: "Erasable Programmable Read Only Memory"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eprom/"
summary: "EPROM je typ nevolatilního paměťového čipu používaného v raných mobilních zařízeních a síťové infrastruktuře k uložení firmwaru, konfiguračních dat nebo spouštěcího kódu. Lze jej vymazat ultrafialovým"
---

EPROM je typ nevolatilního paměťového čipu používaného v raných mobilních zařízeních a síťové infrastruktuře k uložení firmwaru nebo konfiguračních dat, který lze vymazat ultrafialovým světlem a přeprogramovat pro úpravy v provozu.

## Popis

Erasable Programmable Read Only Memory (EPROM) je nevolatilní paměťová technologie, která si udržuje data bez napájení a lze ji programovat elektricky, ale pro vymazání vyžaduje expozici ultrafialovému (UV) světlu přes průhledné křemenné okénko na pouzdře čipu. V kontextu specifikací 3GPP, zejména v raných vydáních, je EPROM zmiňováno jako úložné médium v uživatelském zařízení (UE), základnových stanicích nebo jiných síťových prvcích. Běžně se používalo k uchovávání trvalého nebo polotrvalého softwaru, jako je firmware zařízení, zavaděč, kód základnového procesoru nebo parametry síťové konfigurace. Proces programování zahrnuje aplikaci vyššího než normálního napětí na vstupní piny, aby se změnil náboj na tranzistorech s plovoucím hradlem v paměťových buňkách, čímž se zapisují data.

V telekomunikačním zařízení by EPROM bylo součástí hardwarového subsystému odpovědného za počáteční start zařízení a základní provoz. Po zapnutí napájení by procesor načetl své počáteční instrukce (spouštěcí kód) z EPROM. Tento kód by pak inicializoval systém, provedl autotesty a případně načetl rozsáhlejší operační systém nebo aplikační software z jiné paměti, jako je Flash nebo DRAM. U síťové infrastruktury mohly EPROM ukládat jedinečné identifikátory zařízení, kalibrované rádiové parametry nebo rané verze provozního softwaru. Potřeba UV okénka činila EPROM vhodnými pro vývoj a scénáře, kde software mohl potřebovat změnu omezený početkrát během životního cyklu produktu, nikoli však snadno přímo v provozu.

Zmínka o EPROM ve specifikacích 3GPP, jako je 21.905 (slovníček), odráží technologickou krajinu své doby (počátek 2000. let, Release 5). Specifikace musely brát v úvahu fyzikální charakteristiky takových komponent, zejména pokud jde o testování, spolehlivost a způsoby aktualizace softwaru. Zatímco technologie EPROM jako taková není definována 3GPP, její zahrnutí ji uznává jako možný implementační detail pro ukládání standardizovaného softwaru nebo dat definovaných specifikacemi. V následujících vydáních se odkazy na konkrétní paměťové technologie, jako je EPROM, staly méně častými, protože specifikace abstrahovaly úložné médium a místo toho se zaměřovaly na logická data a procedury.

## K čemu slouží

Technologie EPROM byla začleněna do úvah o zařízeních a infrastruktuře 3GPP, aby řešila potřebu spolehlivého, nevolatilního a aktualizovatelného úložiště firmwaru v éře před rozšířením flexibilnější Flash paměti. Při vývoji systémů 3G (UMTS) vyžadovala síťová zařízení a mobilní terminály trvalé paměťové řešení pro uložení komplexního softwaru, který implementoval protokolové zásobníky 3GPP, rádiové algoritmy a funkce správy zařízení. Paměť [ROM](/mobilnisite/slovnik/rom/) (jen pro čtení) byla příliš nepružná a paměť [RAM](/mobilnisite/slovnik/ram/) byla volatilní. EPROM poskytovala střední cestu: mohla být naprogramována během výroby a, což bylo klíčové, vymazána a přeprogramována, pokud byly nalezeny chyby nebo se standardy vyvíjely, což bylo nezbytné během vývojových a raných nasazovacích fází nových technologií.

Jejím účelem v kontextu specifikace bylo poskytnout známý, hmatatelný referenční bod pro umístění standardizovaného kódu nebo dat. Pro testování shody a schvalování typu bylo důležité zajistit, aby provozní software UE – potenciálně uložený v EPROM – správně implementoval standardy 3GPP. Možnost vymazání a přeprogramování také napomáhala údržbě a upgradu nasazených základnových stanic, ačkoli proces UV vymazání byl pro vzdálené aktualizace nepraktický. Omezení EPROM – konkrétně potřeba fyzického UV vymazání a omezený počet cyklů vymazání/zápisu – motivovala průmysl k přechodu na [EEPROM](/mobilnisite/slovnik/eeprom/) (Electrically Erasable PROM) a později na paměti NAND/NOR Flash, které podporují elektrické vymazání v systému a jsou základem pro moderní aktualizace firmwaru přes vzdušné rozhraní (FOTA).

## Klíčové vlastnosti

- Nevolatilní uchování dat bez napájení.
- Elektricky programovatelná pro ukládání dat.
- Vyžaduje expozici ultrafialovému světlu pro vymazání celého čipu.
- Obsahuje průhledné křemenné okénko na pouzdře čipu pro UV expozici.
- Používá se pro ukládání firmwaru, spouštěcího kódu nebo pevných konfiguračních dat.
- Poskytuje větší flexibilitu než masková ROM, ale menší než plně elektrická Flash paměť.

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [EPROM na 3GPP Explorer](https://3gpp-explorer.com/glossary/eprom/)
