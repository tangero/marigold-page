---
slug: "ngaf"
url: "/mobilnisite/slovnik/ngaf/"
type: "slovnik"
title: "NGAF – Non-GPRS Alert Flag"
date: 2025-01-01
abbr: "NGAF"
fullName: "Non-GPRS Alert Flag"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ngaf/"
summary: "Non-GPRS Alert Flag (NGAF) je informační prvek používaný v jádrové síti GSM/UMTS s přepojováním okruhů k indikaci, že účastník má aktivní relaci v paketové doméně (GPRS). Umožňuje koordinaci mezi domé"
---

NGAF je informační prvek v jádrové síti GSM/UMTS s přepojováním okruhů, který signalizuje, že účastník má aktivní relaci GPRS, což umožňuje koordinaci mezi doménami s přepojováním okruhů a paketů.

## Popis

Non-GPRS Alert Flag (NGAF) je zastaralý signalizační parametr definovaný ve specifikacích jádrové sítě 3GPP, konkrétně pro sítě GSM a UMTS. Jde o informační prvek používaný v protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), především ve zprávách jako Send Routing Info (SRI) a Provide Subscriber Info (PSI), které si vyměňují síťové entity jako Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Visitor Location Register (VLR) a Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)). Jeho hlavní funkcí je předávat stav připojení účastníka k paketové doméně (PS) z HLR entitám okruhové domény ([CS](/mobilnisite/slovnik/cs/)).

NGAF funguje tak, že je nastaven v profilu účastníka v HLR. Když entita okruhové domény (např. GMSC pokoušející se směrovat hlasový hovor) dotazuje HLR na směrovací informace, HLR do své odpovědi zahrne NGAF, pokud je účastník aktuálně připojen k síti [GPRS](/mobilnisite/slovnik/gprs/) (paketové doméně). Tento příznak slouží jako jednoduchý binární indikátor (výstraha nebo žádná výstraha), který informuje CS síť o tom, že účastník má aktivní PS kontext. Tyto informace pak může síťová logika využít k ovlivnění procedur zpracování hovoru, zejména pro implementaci služeb, které vyžadují povědomí o duálním stavu účastníka.

Z architektonického hlediska je NGAF součástí sady protokolů MAP, která funguje nad signalizační sítí SS7. Je klíčovým prvkem koordinačního mechanismu mezi jádrovou sítí CS (MSC/VLR) a jádrovou sítí PS (SGSN/GGSN). Jeho role byla klíčová v raných sítích 2G/3G pro podporu základního povědomí o současném provozu hlasu a dat, což umožňovalo funkce jako síťově iniciované procedury odpojení nebo optimalizovaná rozhodnutí o směrování na základě stavu připojení účastníka, ačkoli poskytoval pouze jednoduchou výstrahu, nikoli podrobné informace o relaci.

## K čemu slouží

NGAF byl vytvořen v raných fázích zavádění [GPRS](/mobilnisite/slovnik/gprs/) (3GPP Release 4), aby řešil základní problém koordinace mezi nově zaváděnou paketovou doménou (GPRS) a stávající okruhovou doménou. Před GPRS jádrová síť zpracovávala pouze hlas a SMS prostřednictvím [CS](/mobilnisite/slovnik/cs/) domény. Zavedení datových služeb vytvořilo scénář, kdy mohl být účastník současně připojen k oběma doménám, ale entity CS sítě o tom neměly žádný vnitřní způsob, jak to zjistit. Tento nedostatek povědomí mohl vést k neoptimálnímu chování sítě, jako jsou zbytečné pokusy o paging v obou doménách.

Řešil problém základního povědomí mezi doménami. Příznak umožňoval HLR jako centrální databázi účastníků informovat CS entity (jako MSC) o stavu připojení účastníka k GPRS. To umožnilo rané implementace funkcí jako 'GSM Suspend' během hovoru v okruhové doméně, kde mohla být paketová relace dočasně pozastavena, a optimalizované strategie pagingu. Jeho vytvoření bylo motivováno potřebou jednoduchého, zpětně kompatibilního signalizačního mechanismu pro usnadnění koexistence a základní interakce služeb CS a PS bez nutnosti kompletní přestavby stávajících protokolů MAP.

## Klíčové vlastnosti

- Binární indikátor stavu připojení účastníka k GPRS
- Přenášen v rámci signalizačních zpráv MAP (např. SRI, PSI)
- Nastavován HLR na základě stavu registrace účastníka v PS doméně
- Používán entitami CS sítě pro rozhodování při zpracování hovorů
- Umožňuje základní koordinaci mezi doménami s přepojováním okruhů a paketů
- Součást zastaralé signalizace jádrové sítě GSM/UMTS

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [NGAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngaf/)
