---
slug: "pqi"
url: "/mobilnisite/slovnik/pqi/"
type: "slovnik"
title: "PQI – PC5 QoS Identifier"
date: 2026-01-01
abbr: "PQI"
fullName: "PC5 QoS Identifier"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pqi/"
summary: "Identifikátor kvality služeb pro PC5 (PQI) je standardizovaný index odkazující na předdefinovanou sadu charakteristik QoS (jako priorita, zpoždění, spolehlivost) pro komunikaci přes rozhraní postranní"
---

PQI je standardizovaný index odkazující na předdefinovanou sadu charakteristik kvality služeb (QoS) pro komunikaci přes rozhraní postranního spoje PC5, který zajišťuje interoperabilní správu QoS pro přímé datové toky mezi zařízeními.

## Popis

Identifikátor kvality služeb pro PC5 (PQI) je skalární hodnota, která slouží jako odkaz na standardizovaný profil QoS definovaný ve specifikacích 3GPP pro komunikaci přes referenční bod PC5. Rozhraní PC5 umožňuje přímou komunikaci mezi uživatelskými zařízeními (UE), známou jako komunikace postranním spojem, která je klíčová pro komunikaci vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)), veřejnou bezpečnost a komerční služby [D2D](/mobilnisite/slovnik/d2d/). Každá hodnota PQI odpovídá konkrétní kombinaci parametrů QoS, včetně typu prostředků (např. garantovaný přenosový výkon nebo Non-GBR), úrovně priority, rozpočtu zpoždění paketů, míry chybovosti paketů a volitelně výchozího maximálního objemu datového vzplanutí a průměrovacího okna.

Během provozu, když aplikace na UE zahájí komunikační relaci přes PC5, vyžádá si určitou úroveň QoS. Tento požadavek je často převeden na hodnotu PQI. PQI se používá během procedur navázání nebo změny jednosměrného spoje PC5, jak je definováno ve specifikacích jako TS 23.287. Iniciující UE signalizuje požadovaný PQI partnerskému UE. Obě UE pak tento identifikátor použijí k lokálnímu odvození kompletní sady charakteristik QoS ze standardizované tabulky. Toto odvození informuje klíčové funkce, jako je klasifikace paketů, označování, plánování a řízení přístupu na rádiových nosičích postranního spoje.

Architektura využívá PQI k abstrakci komplexních sad parametrů QoS do jednoduchého celého čísla, což zjednodušuje signalizaci a zajišťuje konzistenci. Profil QoS, na který PQI odkazuje, určuje, jak má být s datovým tokem zacházeno napříč vrstvami protokolu, zejména na přístupové vrstvě ([AS](/mobilnisite/slovnik/as/)). Například PQI spojený s typem prostředků s vysokou prioritou a nízkým zpožděním ovlivní, jak vrstva [MAC](/mobilnisite/slovnik/mac/) plánuje přenosy a vybírá prostředky v zásobníku prostředků postranního spoje, případně použitím spolehlivějších modulačních a kódovacích schémat nebo častějších přenosových příležitostí.

PQI je základním kamenem rámce QoS pro postranní spoj NR a vyvinutý postranní spoj LTE (při použití v kontextu 5G). Funguje v součinnosti s identifikátorem toku QoS pro PC5 ([PQFI](/mobilnisite/slovnik/pqfi/)). Zatímco PQI definuje „co“ – šablonu charakteristik QoS – PQFI identifikuje „který“ – konkrétní instanci datového toku, na kterou se tyto charakteristiky aplikují. Toto oddělení umožňuje více tokům (každý s jedinečným PQFI) sdílet stejný PQI, pokud mají stejné požadavky na QoS, nebo mít různé PQI, pokud se jejich požadavky liší. Řídící entity, jako je funkce [ProSe](/mobilnisite/slovnik/prose/) nebo funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) jádra 5G sítě, mohou zřizovat nebo autorizovat použití konkrétních hodnot PQI pro různé služby nebo aplikace, což umožňuje síťově řízenou QoS i pro přímou komunikaci mezi UE.

## K čemu slouží

PQI byl vytvořen za účelem standardizace a zjednodušení správy QoS pro přímou komunikaci založenou na PC5, což se stalo nezbytným se zavedením pokročilých služeb [V2X](/mobilnisite/slovnik/v2x/) ve verzi 14 3GPP a jeho významným vylepšením v kontextu 5G od verze 16. Dřívější mechanismy D2D postrádaly komplexní, standardizovaný identifikátor QoS, což ztěžovalo zajištění předvídatelné a interoperabilní kvality služeb napříč zařízeními různých výrobců, zejména pro životně důležité aplikace jako autonomní řízení.

Řeší problém komplexní a neefektivní signalizace kompletních sad parametrů QoS pro každou komunikační relaci. Bez PQI by si UE musela pokaždé vyjednávat a signalizovat četné jednotlivé parametry (rozpočet zpoždění, míru chybovosti atd.), což by zvyšovalo signalizační režii a latenci navazování. PQI tuto informaci kondenzuje do jediného, známého indexu, což drasticky zjednodušuje navazování a změnu relace. Tato efektivita je klíčová pro dynamická prostředí V2X, kde mohou být komunikační relace krátké a navazovány rychle.

Motivace vychází z potřeby rozšířit robustní rámec QoS 5G, který používá 5QI pro rozhraní Uu, také na rozhraní postranního spoje. Tím je zajištěn jednotný přístup ke kvalitě služeb napříč všemi typy přístupu. PQI umožňuje síti uplatňovat řízení politik nad komunikací postranním spojem autorizací toho, které hodnoty PQI může UE použít pro konkrétní služby. Odstraňuje tak omezení dřívější priority na paket ProSe (PPPP), což byl jednodušší indikátor priority, tím, že poskytuje kompletní sadu charakteristik QoS nezbytných pro podporu různorodých a přísných požadavků vertikál využívajících 5G, jako je automobilový průmysl a průmyslový IoT.

## Klíčové vlastnosti

- Odkazuje na standardizovanou sadu parametrů QoS definovanou ve specifikacích 3GPP
- Zjednodušuje signalizaci QoS použitím jedné skalární hodnoty místo více parametrů
- Umožňuje konzistentní zacházení s QoS a interoperabilitu napříč různými implementacemi UE
- Podporuje jak typy prostředků s garantovaným přenosovým výkonem (GBR), tak Non-GBR pro postranní spoj
- Integruje se se síťovým řízením politik pro autorizované použití QoS
- Funguje v součinnosti s PQFI pro detailní správu QoS na úrovni toků na PC5

## Související pojmy

- [PQFI – PC5 QoS Flow Identifier](/mobilnisite/slovnik/pqfi/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [PQI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pqi/)
