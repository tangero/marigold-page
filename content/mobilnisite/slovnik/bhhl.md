---
slug: "bhhl"
url: "/mobilnisite/slovnik/bhhl/"
type: "slovnik"
title: "BHHL – Beside Head and Hand Left Side"
date: 2025-01-01
abbr: "BHHL"
fullName: "Beside Head and Hand Left Side"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/bhhl/"
summary: "BHHL je standardizované antropomorfní testovací zařízení (fantom) používané pro testování Specifické míry absorpce (SAR) a výkonu Over-The-Air (OTA) bezdrátových zařízení, zejména uživatelských zaříze"
---

BHHL je standardizovaný fantom hlavy a ruky používaný pro testování SAR a OTA bezdrátových zařízení, který reprezentuje levostrannou polohu pro měření RF expozice a výkonu antény.

## Popis

BHHL je přesně definovaný fyzický a výpočetní model neboli 'fantom', který simuluje elektromagnetickou interakci mezi bezdrátovým zařízením a lidským uživatelem. Je součástí sady standardizovaných fantomů specifikovaných 3GPP pro testování shody. Model BHHL konkrétně reprezentuje scénář, kdy uživatel drží mobilní zařízení (jako smartphone) u hlavy svou levou rukou. Fantom se skládá z detailních geometrických modelů lidské hlavy (včetně prvků jako ucho a tvář) a zjednodušeného modelu ruky, vše naplněné tekutinou ekvivalentní tkání, která napodobuje dielektrické vlastnosti (permitivitu a vodivost) lidských tkání v konkrétních frekvenčních pásmech. To umožňuje vysoce kontrolovaná laboratorní měření, která korelují s reálnou expozicí uživatele.

V testovacích postupech je testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) umístěno v přesné, opakovatelné orientaci vůči fantomu BHHL uvnitř anechoické komory nebo podobného kontrolovaného prostředí. Pro testování [SAR](/mobilnisite/slovnik/sar/) robotický systém sond prohledává povrch nebo vnitřek fantomu, aby změřil intenzitu elektrického pole, která se následně použije k výpočtu míry absorpce [RF](/mobilnisite/slovnik/rf/) energie (SAR) ve wattech na kilogram. Tím se zajišťuje, že zařízení splňuje mezinárodní bezpečnostní limity pro lidskou expozici elektromagnetickým polím. Pro testování výkonu [OTA](/mobilnisite/slovnik/ota/), jako je Celkový vyzářený výkon ([TRP](/mobilnisite/slovnik/trp/)) a Celková izotropní citlivost (TIS), přítomnost fantomu BHHL významně ovlivňuje vyzařovací diagram a účinnost antény zařízení. Měření se provádějí se zařízením v této 'zatížené' podmínce, aby se vyhodnotil jeho reálný rádiový výkon, protože lidské tělo absorbuje a rozptyluje RF energii, což degraduje výkon antény ve srovnání s podmínkami ve volném prostoru.

Technické specifikace pro fantom BHHL, včetně jeho přesných rozměrů, tvaru a dielektrických vlastností tkáňově simulující tekutiny, jsou detailně popsány ve specifikacích 3GPP, jako je TS 38.161 (pro NR) a série 38.8xx. Tyto specifikace zajišťují globální harmonizaci testovacích metodologií, což umožňuje konzistentní a srovnatelné výsledky napříč různými testovacími laboratořemi a výrobci zařízení. Použití BHHL a jeho protějškových modelů (jako [BHHR](/mobilnisite/slovnik/bhhr/) pro pravou stranu) je klíčové pro certifikaci, že zařízení splňují jak regulační bezpečnostní požadavky, tak minimální výkonnostní standardy před uvedením na trh, což zajišťuje bezpečnost uživatelů a spolehlivé síťové připojení.

## K čemu slouží

Fantom BHHL byl zaveden, aby řešil kritickou potřebu standardizovaného, realistického a opakovatelného testování mobilních zařízení z hlediska bezpečnosti [RF](/mobilnisite/slovnik/rf/) expozice a vyzařovaného výkonu. Před takovou standardizací se testovací metodologie mohly lišit, což vedlo k nekonzistentním výsledkům [SAR](/mobilnisite/slovnik/sar/) a OTA mezi různými laboratořemi a regiony. To komplikovalo globální certifikaci zařízení a mohlo potenciálně umožnit uvedení zařízení s podoptimálním reálným výkonem nebo s hraniční shodou na trh. Lidské tělo je významným faktorem v RF charakteristikách zařízení; výkon antény telefonu je drasticky odlišný, když je držen v ruce a přiložen k hlavě, ve srovnání s volným prostorem. Testování v izolaci tedy neodráží skutečný uživatelský zážitek.

Vytvoření BHHL a příbuzných fantomů v rámci 3GPP Rel-17 bylo motivováno vývojem mobilních technologií, zejména nasazením 5G New Radio (NR) v nových frekvenčních pásmech (včetně FR1 a FR2/milimetrových vln). Tyto nové technologie vyžadovaly aktualizované testovací metodologie, které by zohlednily různé charakteristiky šíření a chování beamformingu. Standardizace fantomu jako BHHL zajišťuje, že všichni zúčastnění – výrobci, testovací domy a regulátoři – mají společný referenční bod pro hodnocení zařízení. Řeší problém variability testovacích výsledků a poskytuje vědecky robustní model, který reprezentuje běžný, konzervativní scénář použití (levostranná poloha při hovoru), což je zásadní pro zajištění ochrany spotřebitele v oblasti RF expozice a pro záruku, že metriky výkonu sítě, jako je propustnost dat a spolehlivost hovorů, jsou hodnoceny za realistických podmínek.

## Klíčové vlastnosti

- Standardizovaný geometrický model lidské hlavy a levé ruky pro konzistentní pozicování zařízení
- Definované dielektrické vlastnosti ekvivalentní tkání pro přesnou simulaci RF absorpce a rozptylu
- Umožňuje testování shody Specifické míry absorpce (SAR) pro regulační bezpečnostní certifikaci
- Umožňuje testování výkonu Over-The-Air (OTA) (např. TRP, TIS) za realistických uživatelských podmínek
- Klíčový pro hodnocení degradace výkonu antény způsobené blízkostí uživatele (ztráta tělem)
- Podporuje testování napříč více frekvenčními pásmy, včetně těch používaných pro 5G NR

## Související pojmy

- [SAR – Security Assurance Requirements](/mobilnisite/slovnik/sar/)
- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [BHHL na 3GPP Explorer](https://3gpp-explorer.com/glossary/bhhl/)
