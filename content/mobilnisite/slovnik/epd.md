---
slug: "epd"
url: "/mobilnisite/slovnik/epd/"
type: "slovnik"
title: "EPD – Extended Protocol Discriminator"
date: 2025-01-01
abbr: "EPD"
fullName: "Extended Protocol Discriminator"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/epd/"
summary: "Pole v 5G NAS (Non-Access Stratum) zprávách sloužící k identifikaci typu protokolu zprávy. Rozšiřuje tradiční Protocol Discriminator pro podporu širší škály protokolů a budoucích vylepšení, čímž zajiš"
---

EPD je rozšířené pole v 5G NAS zprávách, které identifikuje typ protokolu, podporuje více protokolů a budoucí vylepšení při zachování zpětné kompatibility signalizace v jádrové síti.

## Popis

Extended Protocol Discriminator (EPD) je klíčový prvek v zásobníku protokolu 5G Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), definovaný ve specifikacích 3GPP. Jde o pole v hlavičce NAS zprávy, které identifikuje konkrétní protokol použitý pro danou zprávu. Na rozdíl od tradičního Protocol Discriminatoru ([PD](/mobilnisite/slovnik/pd/)) používaného v předchozích generacích, který měl omezený rozsah hodnot, EPD využívá rozšířené schéma kódování, aby pojalo širší sadu protokolů a budoucích rozšíření. To umožňuje 5G sítím podporovat rozmanité služby a vyvíjející se požadavky bez přestavby formátu zprávy.

Z architektonického hlediska je EPD součástí vrstvy protokolu NAS, která zpracovává signalizaci mezi uživatelským zařízením (UE) a jádrovou sítí (např. [AMF](/mobilnisite/slovnik/amf/) – Access and Mobility Management Function). Funguje tak, že je zahrnuto v každé NAS zprávě, typicky na začátku hlavičky zprávy. Hodnota EPD udává, zda se zpráva týká 5G Mobility Management ([5GMM](/mobilnisite/slovnik/5gmm/)), 5G Session Management ([5GSM](/mobilnisite/slovnik/5gsm/)) nebo jiných protokolů, jako jsou [SMS](/mobilnisite/slovnik/sms/) nebo služby polohy. Přijímající entita (UE nebo síť) tuto hodnotu používá ke správnému parsování a zpracování zprávy.

Klíčové komponenty zahrnují samotné pole EPD, které je zakódováno tak, aby umožňovalo zpětnou kompatibilitu s dědičnými hodnotami PD a zároveň zavádělo nové. Například určité bitové vzory v EPD mohou indikovat, že se jedná o rozšířený typ, což spouští odlišná pravidla parsování. Tento návrh zajišťuje, že 5G NAS může v případě potřeby spolupracovat se staršími systémy (jako je 4G EPC), a zároveň podporovat inovativní 5G funkce. Role EPD je zásadní pro rozšiřitelnost a efektivitu 5G signalizace, což umožňuje jádrové síti spravovat široké spektrum služeb od rozšířeného mobilního širokopásmového připojení přes hromadný IoT až po ultra-spolehlivou komunikaci s nízkou latencí.

## K čemu slouží

EPD bylo zavedeno v 5G k překonání omezení Protocol Discriminatoru ([PD](/mobilnisite/slovnik/pd/)) používaného v 4G a starších sítích. Tradiční PD měl pevnou, malou sadu hodnot, což omezovalo počet protokolů, které mohly být jednoznačně identifikovány. Protože 5G si klade za cíl podporovat obrovské spektrum služeb a budoucí technologie, se toto omezení stalo úzkým hrdlem pro flexibilitu signalizace.

Historický kontext zahrnuje vývoj od 2G/3G/4G [NAS](/mobilnisite/slovnik/nas/) protokolů, kde PD stačil pro základní správu mobility a relací, ale selhával u nových případů užití, jako je síťové dělení (network slicing) a edge computing. EPD tento problém řeší tím, že poskytuje rozšířený rozsah identifikátorů, což umožňuje definici nových protokolů bez narušení těch stávajících. Tato zpětná kompatibilita je zásadní pro hladkou migraci ze 4G na 5G.

Motivace pro jeho vytvoření zahrnují potřebu škálovatelné a přizpůsobivé signalizace v servisně orientované architektuře 5G. Tím, že umožňuje více typů protokolů, EPD usnadňuje inovace, jako je samostatná správa pro různá síťová řezy nebo integrace s non-3GPP přístupem. Řeší problém režie a složitosti signalizace a zajišťuje, že 5G sítě mohou efektivně zpracovávat rozmanitý provoz při zachování robustní a jasné diferenciace zpráv.

## Klíčové vlastnosti

- Rozšířený rozsah identifikátorů protokolů nad rámec dědičného PD
- Zpětná kompatibilita s hodnotami 4G Protocol Discriminator
- Podpora 5G-specifických protokolů jako 5GMM a 5GSM
- Flexibilita pro pozdější přidávání protokolů
- Efektivní kódování v hlavičkách NAS zpráv
- Umožňuje diferenciaci služeb pro síťové dělení (network slicing)

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [5GMM – 5G Mobility Management](/mobilnisite/slovnik/5gmm/)
- [5GSM – 5G Session Management](/mobilnisite/slovnik/5gsm/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [EPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/epd/)
