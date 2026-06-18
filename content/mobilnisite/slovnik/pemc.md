---
slug: "pemc"
url: "/mobilnisite/slovnik/pemc/"
type: "slovnik"
title: "PEMC – PIN Elements with Management Capability"
date: 2026-01-01
abbr: "PEMC"
fullName: "PIN Elements with Management Capability"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pemc/"
summary: "Rámec pro správu prvků osobního identifikačního čísla (PIN) v rámci univerzální integrované obvodové karty (UICC) nebo vestavěné SIM karty (eSIM). Umožňuje dálkovou správu PINů, klíčů pro odblokování"
---

PEMC je rámec pro správu prvků PIN a jejich atributů na UICC nebo eSIM umožňující dálkovou správu zabezpečení.

## Popis

[PIN](/mobilnisite/slovnik/pin/) Elements with Management Capability (PEMC) je rámec pro správu standardizovaný v 3GPP Release 18, primárně v kontextu rozšířené správy [SIM](/mobilnisite/slovnik/sim/)/UICC. Definuje strukturovaný datový model a postupy dálkové správy pro bezpečnostní prvky související s PINem uložené na UICC. 'Prvek PIN' (PIN Element) označuje PIN, jeho přidružený klíč pro odblokování PINu ([PUK](/mobilnisite/slovnik/puk/)) a všechny související atributy, jako je hodnota PINu, čítač pokusů, stav povoleno/zakázáno a pravidla použití (např. které operace vyžadují ověření PINem). 'Schopnost správy' (Management Capability) znamená, že tyto prvky lze vytvářet, upravovat, povolovat, zakazovat nebo mazat prostřednictvím protokolů dálkové správy, jako jsou ty definované architekturou Remote SIM Provisioning (RSP) pro eSIM. Rámec je specifikován v několika 3GPP specifikacích: systémová architektura (23.501, 23.542), servisní požadavky pro PEMC (23.700), protokoly Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) pro přenos zpráv správy PINu mezi UE a sítí (24.501, 24.583), podrobnosti managementového protokolu (26.806) a bezpečnostní postupy (33.127). Architektonicky zahrnuje PEMC UE, UICC/eSIM a síťové funkce jako Subscription Manager - Data Preparation (SM-DP+) nebo jiné správní servery. Příkazy správy jsou bezpečně přeneseny na UICC, které následně aplikuje změny na určený prvek PIN. To umožňuje například podnikovému [IT](/mobilnisite/slovnik/it/) oddělení vzdáleně resetovat PIN zařízení nebo mobilnímu operátorovi inicializovat PINy během zřizování eSIM bez fyzického přístupu k zařízení.

## K čemu slouží

PEMC byl vyvinut k překonání omezení statické, pevně zakódované správy [PIN](/mobilnisite/slovnik/pin/)ů v tradičních [SIM](/mobilnisite/slovnik/sim/) kartách. V zastaralých systémech byly PINy a PUKy předprogramovány výrobcem SIM karty a mohly být změněny pouze lokálně uživatelem přes menu zařízení, pokud to vůbec bylo povoleno. To představovalo významné provozní výzvy pro rozsáhlá nasazení IoT, flotily podnikových zařízení a standardní zřizování eSIM pro spotřebitele. Pokud uživatel zapomněl PIN nebo vyčerpal pokusy, často bylo vyžadováno fyzické zasahování. PEMC řeší tyto problémy tím, že umožňuje dálkovou, 'over-the-air' správu bezpečnostních prvků PIN. To je klíčové pro ekosystém eSIM, kde jsou profily stahovány vzdáleně; PEMC umožňuje, aby byly přidružené PINy konfigurovány dynamicky jako součást procesu zřizování profilu. Řeší logistické obtíže v IoT tím, že umožňuje správcům flotil vzdáleně resetovat PINy na tisících senzorů. Pro spotřebitele umožňuje samoobslužné obnovení PINu prostřednictvím portálů operátora. Motivace vychází z posunu průmyslu k plně vzdálené správě životního cyklu zařízení a předplatného, který vyžaduje stejnou flexibilitu pro bezpečnostní prvky (PINy) jako pro jiná data předplatného. Zlepšuje jak bezpečnostní postavení prostřednictvím centralizované kontroly politik, tak uživatelský zážitek zjednodušením obnovy PINu.

## Klíčové vlastnosti

- Vzdálené vytváření, úprava a mazání hodnot PIN a PUK
- Správa atributů PINu (čítač pokusů, povolený stav, pravidla použití)
- Integrace s architekturou eSIM Remote SIM Provisioning (RSP)
- Bezpečný přenos příkazů správy PINu prostřednictvím standardizovaných protokolů
- Podpora více prvků PIN (např. PIN1, PIN2) na jedné UICC
- Umožňuje hromadnou a automatizovanou správu PINů pro flotily IoT zařízení

## Související pojmy

- [PIN – Personal Identification Number](/mobilnisite/slovnik/pin/)
- [PUK – PIN Unblocking Key](/mobilnisite/slovnik/puk/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.542** (Rel-20) — Application layer support for Personal IoT Network
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.583** (Rel-19) — Application Layer Support for Personal IoT Network
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [PEMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pemc/)
