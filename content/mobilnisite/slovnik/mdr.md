---
slug: "mdr"
url: "/mobilnisite/slovnik/mdr/"
type: "slovnik"
title: "MDR – Missed-Detection Rate"
date: 2026-01-01
abbr: "MDR"
fullName: "Missed-Detection Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mdr/"
summary: "MDR je klíčový výkonnostní ukazatel v bezdrátové komunikaci, který kvantifikuje pravděpodobnost, že přijímač nezachytí signál, který je skutečně přítomen. Je kriticky analyzován v NR specifikacích pro"
---

MDR (míra nezachycených detekcí) je pravděpodobnost, že přijímač nezachytí signál, který je skutečně přítomen; používá se v 3GPP k analýze spolehlivosti řídicích kanálů u funkcí jako sidelink a NTN.

## Popis

Missed-Detection Rate (MDR, míra nezachycených detekcí) je základní statistický výkonnostní ukazatel používaný k vyhodnocení spolehlivosti detekčních algoritmů v přijímačích digitální komunikace. V kontextu specifikací New Radio (NR) od 3GPP konkrétně odkazuje na pravděpodobnost, že přijímající entita (např. UE, gNB nebo IAB-node) neuspěje ve správné identifikaci přítomnosti vysílaného signálu nebo kanálu fyzické vrstvy, když je tento signál ve skutečnosti vysílán. Je to doplněk k pravděpodobnosti detekce (Pd). MDR je kritický parametr pro hodnocení výkonu řídicích kanálů a synchronizačních signálů, kde nezachycená detekce může vést k selhání přístupu do systému, ztrátě plánovacích informací nebo přerušení spojení.

MDR se typicky vyhodnocuje za specifických referenčních podmínek definovaných v konformačních testovacích specifikacích (např. 38.141 pro základnovou stanici). Test zahrnuje konfiguraci vysílače pro odesílání konkrétního signálu (jako je příkaz [PDCCH](/mobilnisite/slovnik/pdcch/), Synchronization Signal Block (SSB) nebo sidelink řídicí kanál) na definované úrovni výkonu. Úkolem přijímače je tento signál detekovat. MDR se vypočítá jako poměr počtu nezachycených detekcí k celkovému počtu pokusů o přenos v rámci velkého počtu pokusů. Vyhodnocení se často provádí při specifickém poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) nebo referenční úrovni citlivosti, aby bylo zajištěno, že přijímač splňuje minimální požadavky na výkon.

U pokročilých funkcí NR se analýza MDR stává složitější. U Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)) ovlivňuje MDR řídicích kanálů propojovacího spoje stabilitu více-skokové sítě. U Non-Terrestrial Networks ([NTN](/mobilnisite/slovnik/ntn/)) mohou dlouhá zpoždění a vysoké Dopplerovy posuny zhoršit detekční výkon, což činí MDR klíčovým problémem pro spoje satelit-země. U sidelink komunikace (např. ve [V2X](/mobilnisite/slovnik/v2x/) nebo pro veřejnou bezpečnost) přímo ovlivňuje MDR Physical Sidelink Control Channel ([PSCCH](/mobilnisite/slovnik/pscch/)) spolehlivost přímé komunikace mezi zařízeními. Proto specifikace 3GPP definují minimální výkonnostní požadavky na MDR, aby byla zaručena základní úroveň interoperability a uživatelského zážitku napříč různými implementacemi a scénáři nasazení.

## K čemu slouží

MDR existuje jako standardizovaný ukazatel, který zajišťuje, že přijímače v celulárních sítích jsou dostatečně citlivé a robustní, aby spolehlivě dekódovaly nezbytné řídicí informace. Před formálním důrazem na ni ve specifikacích byl detekční výkon implikován, ale ne vždy kvantitativně ohraničen způsobem, který by garantoval konzistentní reálný výkon napříč zařízeními různých dodavatelů. Nepřijatelně vysoké míry nezachycených detekcí na řídicích kanálech mohou způsobit tichá selhání – jako když UE nezachytí stránkovací zprávu, neobdrží odpověď na náhodný přístup nebo ztratí příkaz k předání spojení – což vážně degraduje výkon sítě a uživatelský zážitek.

Motivace pro specifikaci požadavků na MDR, zejména od verze Rel-18 pro nové funkce, vychází z rostoucí složitosti a kritičnosti nasazení NR. Technologie jako NR sidelink pro pokročilé [V2X](/mobilnisite/slovnik/v2x/), [IAB](/mobilnisite/slovnik/iab/) pro husté nasazení sítí a NTN pro globální pokrytí zavádějí nová zkreslení kanálu a případy užití, kde je spolehlivost řídicích kanálů prvořadá. Například v životně důležitých aplikacích V2X je nezachycení varovné zprávy o kolizi nepřijatelné. Standardizace požadavků na MDR zajišťuje, že všechna kompatibilní zařízení splňují minimální prahovou hodnotu spolehlivosti, což umožňuje předvídatelné chování systému, usnadňuje plánování sítě a poskytuje měřítko pro testování a certifikaci zařízení dodavatelů.

## Klíčové vlastnosti

- Kvantifikuje pravděpodobnost nezachycení vysílaného signálu.
- Klíčový ukazatel výkonu pro řídicí a synchronizační kanály fyzické vrstvy.
- Hodnocen za standardizovaných referenčních podmínek citlivosti a rušení.
- Kritický pro posouzení spolehlivosti funkcí NR jako sidelink, IAB a NTN.
- Používán v konformačním testování k zajištění minimálního výkonu přijímače.
- Doplňkový k ukazateli False Alarm Rate (FAR) pro úplnou charakterizaci přijímače.

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [MDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdr/)
