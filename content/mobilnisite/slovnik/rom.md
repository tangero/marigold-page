---
slug: "rom"
url: "/mobilnisite/slovnik/rom/"
type: "slovnik"
title: "ROM – Receive Only Mode"
date: 2025-01-01
abbr: "ROM"
fullName: "Receive Only Mode"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rom/"
summary: "Provozní režim uživatelského zařízení (UE), ve kterém je konfigurováno pouze pro příjem signálů a dat v downlinku, bez možnosti vysílání v uplinku. Tím se šetří výdrž baterie UE a zjednodušuje se kons"
---

ROM je provozní režim uživatelského zařízení (UE), ve kterém je konfigurováno pouze pro příjem signálů a dat v downlinku, bez možnosti vysílání v uplinku.

## Popis

Režim pouze pro příjem (ROM) je schopnost a provozní stav uživatelského zařízení (UE) definovaný ve specifikacích 3GPP, ve kterém zařízení funguje čistě jako přijímač v downlinku. V tomto režimu je vysílací řetězec UE vypnutý nebo může být zcela nepřítomný. UE se může synchronizovat se sítí, přijímat systémové informace a dekódovat downlinkové kanály, ale neprovádí žádné uplinkové procedury, jako jsou procedury náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)), žádosti o naplánování (scheduling requests) nebo vysílání uplinkových řídicích či datových kanálů.

Z architektonického hlediska ROM ovlivňuje procedury napříč protokolovou zásobníkem. Na fyzické vrstvě (specifikace jako 36.300, 36.976) UE nevyžaduje výkonové zesilovače ani složitý obvod pro uplinkovou modulaci. Potřebuje pouze implementovat přijímací funkce pro synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/)), vysílací kanály ([PBCH](/mobilnisite/slovnik/pbch/)) a sdílené downlinkové kanály ([PDSCH](/mobilnisite/slovnik/pdsch/)). Na vyšších vrstvách nebude mít UE v ROM platný stav uplinkové synchronizace a nebude mu přidělen [C-RNTI](/mobilnisite/slovnik/c-rnti/) pro uplinkové plánování. Může používat skupinové identifikátory, jako je [TMGI](/mobilnisite/slovnik/tmgi/) (Temporary Mobile Group Identity), pro příjem [MBMS](/mobilnisite/slovnik/mbms/).

Jak to funguje: síť vysílá služby, které jsou dostupné bez nutnosti obousměrného RRC spojení. Například v MBMS/eMBMS může UE přilnout k buňce, získat MCCH (MBMS Control Channel) pro zjištění dostupných vysílacích služeb a následně přijímat MTCH (MBMS Traffic Channel) pro spotřebu obsahu. UE nezřizuje stav RRC_CONNECTED. ROM je často spojován se specifickými třídami zařízení, jako jsou nízkonákladová MTC (Machine-Type Communication) zařízení nebo specializované přijímače pro vysílání, specifikované v dokumentech jako 26.073 pro charakteristiky terminálů s kodekem AMR a 34.131 pro testování shody.

Jeho role v síti spočívá v umožnění efektivních služeb typu jeden-všem a ve facilitaci návrhu zařízení s ultra nízkým příkonem a nízkou složitostí. Odlehčuje zátěž uplinkové signalizace pro obrovské množství zařízení, což je klíčové pro nasazení IoT a vysílací scénáře. Síť musí podporovat konfigurace, kde jsou určité buňky nebo nosné určeny pro UE s podporou ROM, a zajistit, aby všechny potřebné systémové informace a služby byly doručovány prostřednictvím vysílacích mechanismů.

## K čemu slouží

ROM byl vytvořen pro podporu tříd zařízení a služeb, kde je uplinková komunikace buď nepotřebná, nežádoucí, nebo příliš nákladná. Tradiční mobilní zařízení jsou ze své podstaty obousměrná, vyžadují složité a energeticky náročné vysílací obvody a zapojují se do nepřetržité signalizace pro správu mobility a relací. To je neefektivní pro aplikace jako aktualizace firmwaru přes vzdušné rozhraní (FOTA), příjem televizního/rozhlasového vysílání nebo jednoduché senzory, které pouze příležitostně hlásí data jinými prostředky.

Problém, který řeší, je dvojí: snižuje náklady/složitost zařízení a dramaticky prodlužuje výdrž baterie. Odstraněním uplinkového řetězce se sníží cena zařízení z hlediska použitých součástek, což umožňuje skutečně nízkonákladové IoT moduly. Výdrž baterie se může prodloužit na roky, protože je odstraněn největší spotřebič energie při typickém vysílání – výkonový zesilovač. Jeho zavedení v Release 8 se časově shodovalo se standardizací LTE a obnoveným zaměřením na vysílání (MBMS) a komunikaci mezi stroji (MTC).

Historicky ROM řeší omezení dřívějších mobilních systémů, které vyžadovaly obousměrnou schopnost u všech zařízení, dokonce i pro čistý příjem vysílání. Umožnil nové obchodní modely pro specializované přijímače (např. zábava v automobilu, přenosná TV) a připravil cestu pro koncepty masivního IoT, jako je NB-IoT a eMTC, které později začlenily omezený uplink, ale převzaly filozofii návrhu extrémní optimalizace přijímače. Odráží posun od univerzálního návrhu UE k profilům zařízení optimalizovaným pro konkrétní služby.

## Klíčové vlastnosti

- Vysílací obvody UE jsou vypnuty nebo nepřítomny, čímž se eliminuje spotřeba energie za uplink
- Funguje bez navázání stavu RRC_CONNECTED, typicky ve stavu RRC_IDLE nebo specifickém idle režimu pro vysílání
- Podporuje příjem vysílacích/multicastových služeb, jako je MBMS/eMBMS, bez uplinkové interakce
- Snižuje složitost a cenu zařízení vynecháním RF komponent pro uplink
- Umožňuje ultra dlouhou výdrž baterie pro pasivní sběr dat nebo zařízení pro příjem médií
- Definován pro různé třídy zařízení ve specifikacích pro shodu terminálů a kodeků

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)

## Definující specifikace

- **TS 26.073** (Rel-19) — AMR Speech Codec ANSI-C Implementation
- **TS 26.104** (Rel-19) — AMR Floating-Point Codec Implementation
- **TS 26.173** (Rel-19) — AMR-WB Codec ANSI-C Implementation
- **TS 26.204** (Rel-19) — AMR-WB Floating-Point Codec Specification
- **TS 26.243** (Rel-19) — DSR Extended Advanced Front-end C Code
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.273** (Rel-19) — Fixed-point AMR-WB+ codec ANSI-C code
- **TS 26.304** (Rel-19) — Floating-point Extended AMR-WB+ Codec ANSI-C Code
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [ROM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rom/)
