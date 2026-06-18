---
slug: "iplmn"
url: "/mobilnisite/slovnik/iplmn/"
type: "slovnik"
title: "IPLMN – Interrogating Public Land Mobile Network"
date: 2025-01-01
abbr: "IPLMN"
fullName: "Interrogating Public Land Mobile Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iplmn/"
summary: "PLMN, která obsahuje bránu MSC pro službu krátkých zpráv (GMSC) nebo dotazovací funkci řízení komunikační relace (I-CSCF). Je to síť, která přijímá příchozí hovor nebo zprávu z jiné sítě a dotazuje se"
---

IPLMN je veřejná pozemní mobilní síť, která přijímá příchozí hovor nebo zprávu a dotazuje se HLR/HSS, aby lokalizovala účastníka a směrovala komunikaci dál.

## Popis

Dotazující se [PLMN](/mobilnisite/slovnik/plmn/) (IPLMN) je základním konceptem v architektuře roamingu a propojení dle 3GPP. Označuje veřejnou pozemní mobilní síť, která provádí počáteční dotaz pro příchozí transakci směrovanou k mobilnímu účastníkovi, jako je hlasový hovor nebo [SMS](/mobilnisite/slovnik/sms/) zpráva, určenou pro účastníka, který se pohybuje mimo svou domovskou síť. Klíčovým síťovým prvkem nacházejícím se v IPLMN je brána [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) pro služby s přepojováním okruhů ve 2G/3G nebo dotazovací funkce řízení komunikační relace ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) pro služby založené na IMS v 4G/5G. Když hovor nebo SMS dorazí z externí sítě (např. z jiné PLMN nebo z [PSTN](/mobilnisite/slovnik/pstn/)), nejprve přistane na GMSC v IPLMN. Tato GMSC zpočátku nezná aktuální polohu účastníka. Jejím hlavním úkolem je dotázat se domovského registračního centra ([HLR](/mobilnisite/slovnik/hlr/)) nebo domovského serveru účastníků ([HSS](/mobilnisite/slovnik/hss/)), které se nachází v domovské PLMN (HPLMN) účastníka. GMSC odešle požadavek na směrovací informace (např. Send Routing Information nebo SRI) do HLR. HLR, které zná aktuální navštívenou PLMN (VPLMN) účastníka a jeho roamingové číslo (MSRN), odpoví s potřebným směrovacím číslem. GMSC v IPLMN poté použije toto MSRN k směrování hovoru do MSC ve VPLMN, kde se účastník aktuálně nachází. V případě IMS se I-CSCF v IPLMN dotazuje HSS, aby zjistil obsluhující S-CSCF nebo aktuální Proxy-CSCF pro daného uživatele. IPLMN funguje jako vstupní bod a inteligentní směrovací uzel pro příchozí roamingový provoz, oddělující databázi účastníků domovské sítě od fyzické cesty směrování hovoru.

## K čemu slouží

Koncept IPLMN existuje, aby umožnil efektivní dokončování hovorů k mobilním účastníkům a roaming v globálním ekosystému více operátorů. Řeší základní problém směrování hovoru nebo zprávy k mobilnímu účastníkovi, jehož přesná poloha (obsluhující MSC nebo oblast) je zdrojové síti neznámá. Před standardizovanými postupy dotazování GMSC/HLR by bylo směrování mobilních hovorů velmi neefektivní nebo nemožné. Architektura IPLMN poskytuje jasné oddělení odpovědností: HPLMN spravuje data a autentizaci účastníků, zatímco IPLMN zajišťuje fyzické propojení a počáteční směrovací logiku. Toto oddělení je klíčové pro zabezpečení, účtování (zúčtování mezi operátory) a škálovatelnost sítě. Historicky byla tato architektura definována od GSM (Release 99) dále a vyvíjela se napříč všemi generacemi. Řeší omezení pevných sítí, kde je umístění koncového bodu statické a známé; pro mobilní uživatele je nezbytný dynamický vyhledávací mechanismus (přes HLR/HSS). Model IPLMN umožňuje jakékoli síti s roamingovou smlouvou fungovat jako vstupní bod, což usnadňuje globální konektivitu.

## Klíčové vlastnosti

- Obsahuje bránu MSC (GMSC) pro hovory/SMS s přepojováním okruhů nebo I-CSCF pro relace IMS.
- Přijímá příchozí komunikaci směrovanou k mobilnímu účastníkovi z externích sítí.
- Dotazuje se HLR nebo HSS v domovské PLMN účastníka, aby získala směrovací informace.
- Nevyžaduje předchozí znalost aktuální polohy účastníka.
- Klíčový síťový prvek pro implementaci smluv o příchozím roamingu a zúčtování.
- Tvoří jednu ze tří primárních rolí PLMN v roamingu (HPLMN, VPLMN, IPLMN).

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [IPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/iplmn/)
