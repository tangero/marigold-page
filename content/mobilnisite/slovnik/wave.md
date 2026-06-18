---
slug: "wave"
url: "/mobilnisite/slovnik/wave/"
type: "slovnik"
title: "WAVE – Wireless Access in Vehicular Environments"
date: 2025-01-01
abbr: "WAVE"
fullName: "Wireless Access in Vehicular Environments"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wave/"
summary: "WAVE je 3GPP rámec pro umožnění přímé komunikace vozidlo-se-vším (V2X) přes rozhraní PC5, nezávisle na pokrytí mobilní sítí. Podporuje služby bezpečnosti s nízkou latencí a dopravní efektivity pro při"
---

WAVE je 3GPP rámec pro umožnění přímé komunikace vozidlo-se-vším (vehicle-to-everything) přes rozhraní PC5 za účelem podpory služeb bezpečnosti s nízkou latencí a dopravní efektivity pro připojená vozidla.

## Popis

Wireless Access in Vehicular Environments (WAVE) je standardizovaný 3GPP servisní rámec navržený k usnadnění přímé komunikace zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)), konkrétně pro vozidlové scénáře, s využitím referenčního bodu PC5. Funguje v rámci širšího ekosystému [V2X](/mobilnisite/slovnik/v2x/) (Vehicle-to-Everything), umožňující vozidlům (uživatelským zařízením, UE), vozidlům roadside units a zranitelným účastníkům provozu, jako jsou chodci, si vyměňovat data přímo, aniž by bylo nutné směrovat provoz přes infrastrukturu mobilní sítě (rozhraní Uu). Tento přímý režim komunikace, často označovaný jako sidelink komunikace, je zásadní pro bezpečnostní aplikace kritické na latenci, kde je i minimální síťové zpoždění nepřijatelné.

Architektura WAVE využívá rozhraní PC5 založené na LTE, definované pro služby pro komunikaci na krátkou vzdálenost ([ProSe](/mobilnisite/slovnik/prose/)), a rozšiřuje a optimalizuje jej pro vysokorychlostní vozidlová prostředí. Mezi klíčové komponenty patří V2X řídicí funkce, která spravuje autorizaci a provisioning pro V2X služby, a UE, které implementuje V2X aplikační vrstvu a protokoly přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) pro PC5. Komunikace probíhá na vyhrazeném spektru pro inteligentní dopravní systémy ([ITS](/mobilnisite/slovnik/its/)), jako je pásmo 5,9 GHz, s využitím specifických mechanismů přidělování zdrojů. Ty zahrnují jak režim plánovaný sítí (mode 3), kde [eNB](/mobilnisite/slovnik/enb/) přiděluje zdroje, tak autonomní režim výběru zdrojů (mode 4), kde vozidla detekují kanál a vybírají si zdroje sama, což je klíčové pro provoz mimo pokrytí sítě.

WAVE podporuje různé typy V2X zpráv, včetně zpráv pro kooperativní povědomí (CAMs) a decentralizovaných zpráv o upozornění na okolní prostředí (DENMs), které přenášejí základní bezpečnostní informace, jako je poloha, rychlost a varování před nebezpečím. Protokolový zásobník zahrnuje úpravy na fyzické vrstvě pro robustní přenos ve scénářích s vysokým Dopplerovým jevem a na síťové vrstvě pro komunikaci založenou na IP nebo nezávislou na IP. Jeho úlohou je poskytnout standardizovaný, interoperabilní základ pro přímou komunikaci [V2V](/mobilnisite/slovnik/v2v/) (vozidlo-vozidlo), V2I (vozidlo-infrastruktura) a V2P (vozidlo-chodec), čímž tvoří kritickou součást celkové architektury 5G systému pro automobilové služby, doplňující V2X založené na mobilní síti (přes Uu) pro širší pokrytí a infotainment.

## K čemu slouží

WAVE byl vytvořen, aby řešil přísné požadavky na spolehlivost a latenci aplikací aktivní bezpečnosti silničního provozu a dopravní efektivity, které tradiční mobilní sítě původně nebyly navrženy splňovat. Před standardizací 3GPP byla vozidlová komunikace založena na [IEEE](/mobilnisite/slovnik/ieee/) 802.11p/DSRC (Dedicated Short-Range Communications) a zásobníku IEEE 1609 WAVE, které nabízely přímou komunikaci, ale postrádaly integraci s všudypřítomným mobilním ekosystémem. Motivací pro WAVE od 3GPP bylo využít globálního rozsahu, bezpečnostního rámce a vývojové cesty mobilní technologie (LTE a později NR) k vytvoření jednotného řešení V2X.

Omezení čistě na bázi IEEE 802.11p zahrnovala výzvy v dosažení globální harmonizace, omezené síťově asistované funkce pro vylepšené přidělování zdrojů a zabezpečení a žádnou inherentní integraci se službami mobilního širokopásmového připojení. Práce 3GPP, začínající ve verzi 14, si kladla za cíl poskytnout alternativní a vylepšenou V2X rádiovou technologii využívající LTE a později 5G NR pro podporu jak bezpečnostních, tak pokročilých případů užití, jako je sdílení senzorů pro autonomní řízení. Standardizací WAVE umožnilo 3GPP bezproblémovou kombinaci přímé PC5 komunikace pro bezpečnostní aplikace kritické na latenci a mobilní Uu komunikace pro celoplošnou konektivitu, vše v rámci společného rámce správy předplatného a zabezpečení. Tím byla řešena potřeba architektury připravené na budoucnost a škálovatelné, která by se mohla vyvíjet spolu s generacemi mobilních sítí.

## Klíčové vlastnosti

- Přímá sidelink komunikace přes PC5 pro V2V, V2I a V2P
- Provoz ve vyhrazeném ITS spektru (např. 5,9 GHz)
- Podpora jak síťově plánovaného (mode 3), tak autonomního (mode 4) přidělování zdrojů
- Optimalizovaná fyzická vrstva pro vysokorychlostní vozidlové kanály s vysokým Dopplerovým jevem
- Podpora přenosu dat založeného na IP i nezávislého na IP (např. V2X zprávy)
- Integrace s 3GPP zabezpečením a správou předplatného

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [WAVE na 3GPP Explorer](https://3gpp-explorer.com/glossary/wave/)
