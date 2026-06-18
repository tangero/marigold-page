---
slug: "tap"
url: "/mobilnisite/slovnik/tap/"
type: "slovnik"
title: "TAP – Transferred Account Procedure"
date: 2025-01-01
abbr: "TAP"
fullName: "Transferred Account Procedure"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tap/"
summary: "Standardizovaný postup pro výměnu fakturačních a účetních informací mezi operátory mobilních sítí, primárně pro roaming. Definuje formát a proces pro přenos záznamů o uskutečněných hovorech (CDR) za ú"
---

TAP je standardizovaný postup pro výměnu fakturačních a účetních informací mezi operátory mobilních sítí, primárně pro přenos záznamů o uskutečněných hovorech (CDR) za účelem vyúčtování roamingových poplatků a vypořádání mezi operátory.

## Popis

Transferred Account Procedure (TAP) je komplexní soubor specifikací, který standardizuje přenos fakturačních a účetních dat mezi telekomunikačními operátory, zejména v roamingových scénářích. Definuje formát, obsah a procesní pravidla pro vytváření a výměnu souborů Transferred Account Data ([TAD](/mobilnisite/slovnik/tad/)), které obsahují záznamy o uskutečněných hovorech ([CDR](/mobilnisite/slovnik/cdr/)) nebo jiné záznamy o využití služeb. Primárním cílem je umožnit navštívenému síťovému operátorovi (kde roamingový účastník využívá služby) zasílat záznamy o využití domácímu síťovému operátorovi (poskytovateli účastníka) pro účely fakturace a vypořádání. TAP pokrývá celý životní cyklus od generování CDR v navštívené síti přes validaci, formátování, přenos až po zpracování v domácí síti.

Z architektonického hlediska TAP zahrnuje několik klíčových komponent: systém generující TAP (typicky v navštívené síti), který vytváří TAP soubory ze surových CDR; TAP soubor, strukturovaný datový kontejner (původně v binárním formátu, později vyvinutý do [XML](/mobilnisite/slovnik/xml/)), který obsahuje záznamy hlavičky, přenosové dávky a zápatí; a systém zpracovávající TAP (v domácí síti), který soubory přijímá, validuje a vyrovnává. Postup specifikuje podrobná pravidla pro datová pole, jako je typ hovoru, doba trvání, cílová destinace, časová razítka a identifikátory roamingových partnerů. Zahrnuje také mechanismy pro zpracování chyb, žádosti o opětovné odeslání a potvrzení, aby byla zajištěna integrita a úplnost dat. TAP soubory jsou obvykle přenášeny pomocí zabezpečených protokolů, jako je [FTP](/mobilnisite/slovnik/ftp/), nebo modernějšími IP metodami.

Při provozu, když roamingový účastník uskuteční hovor, odešle [SMS](/mobilnisite/slovnik/sms/) nebo využije data, síťové prvky navštívené sítě vygenerují surové CDR. Ty jsou zpracovány systémem generujícím TAP, který je agreguje, aplikuje pravidla formátování a zabalí je do TAP souborů, často denně nebo v dávkách. Soubory jsou následně přeneseny do systému zpracovávajícího TAP domácího operátora. Domácí operátor soubory validuje vůči standardům TAP, kontroluje nesrovnalosti a data použije pro vygenerování faktur roamingovému účastníkovi a pro výpočet poplatků mezi operátory. TAP také podporuje úpravy, opravy a řešení sporů prostřednictvím doplňkových postupů, jako je [RAP](/mobilnisite/slovnik/rap/) (Returned Account Procedure) pro zamítnuté záznamy. Jeho strukturovaný přístup zajišťuje, že operátoři mohou přesně vypořádat účty navzdory rozdílům ve svých interních fakturačních systémech.

## K čemu slouží

TAP byl vytvořen k řešení kritického problému fakturace a vypořádání mezi různými operátory mobilních sítí v roamingových scénářích. Před jeho standardizací operátoři používali bilaterální dohody a proprietární formáty pro výměnu dat o využití, což vedlo k nekonzistentnostem, chybám a zdlouhavým procesům vyrovnání. To mělo za následek úniky příjmů, spory a neefektivitu, zejména s expanzí globálního roamingu v 90. letech 20. století. GSM Asociace ([GSMA](/mobilnisite/slovnik/gsma/)) rozpoznala potřebu jednotného postupu pro usnadnění bezproblémového roamingu a přesného finančního vypořádání, což vedlo k vývoji TAP jako součásti širších standardů GSM.

Historicky byl TAP poprvé představen ve 3GPP Release 4, navazujíc na dřívější koncepty fakturace GSM. Řešil omezení předchozích ad-hoc metod tím, že poskytl společný 'jazyk' pro výměnu účetních dat, což umožnilo automatizaci a snížilo potřebu manuálního zásahu. Postup byl motivován rychlým růstem mezinárodního mobilního roamingu, kde účastníci očekávají využívání služeb v zahraničí bez fakturačních komplikací. TAP zajišťuje, že navštívení operátoři jsou odměněni za poskytování služeb roamingovým účastníkům, zatímco domácí operátoři mohou přesně fakturovat své zákazníky na základě standardizovaných záznamů.

Časem se TAP vyvinul tak, aby podporoval nové služby, jako jsou [GPRS](/mobilnisite/slovnik/gprs/) data, MMS a LTE roaming, přizpůsobuje se technologickému pokroku. Řeší trvající výzvy v oblasti zajištění příjmů, detekce podvodů a regulatorní shody tím, že poskytuje sledovatelný a auditovatelný proces. Vytvoření TAP bylo klíčové pro komerční úspěch globální mobilní komunikace, neboť zavedlo důvěru a efektivitu ve finančních transakcích mezi operátory, což umožnilo rozšířené přijetí roamingových služeb, které uživatelé dnes považují za samozřejmost.

## Klíčové vlastnosti

- Standardizovaný formát pro výměnu fakturačních záznamů (CDR) mezi operátory
- Podpora roamingových scénářů pro hlas, SMS, data a služby s přidanou hodnotou
- Definuje postupy pro generování souborů, přenos, validaci a zpracování chyb
- Zahrnuje mechanismy pro úpravy a řešení sporů (např. RAP)
- Umožňuje automatizované vypořádání mezi operátory a zajištění příjmů
- Vyvijí se tak, aby zahrnoval nové technologie a typy služeb napříč releasy 3GPP

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [GSMA – Global System for Mobile communications Association](/mobilnisite/slovnik/gsma/)

## Definující specifikace

- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol
- **TS 32.849** (Rel-13) — IMS Roaming Charging Study
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [TAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tap/)
