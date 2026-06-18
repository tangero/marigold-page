---
slug: "tcer"
url: "/mobilnisite/slovnik/tcer/"
type: "slovnik"
title: "TCER – Total Character Error Rate"
date: 2025-01-01
abbr: "TCER"
fullName: "Total Character Error Rate"
category: "Services"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/tcer/"
summary: "Metrika výkonu používaná k hodnocení přesnosti textových služeb, jako je SMS, měřící poměr nesprávně přijatých znaků k celkovému počtu odeslaných znaků. Je klíčová pro posouzení spolehlivosti služeb z"
---

TCER je poměr nesprávně přijatých znaků k celkovému počtu odeslaných znaků, používaný jako metrika výkonu pro hodnocení přesnosti a spolehlivosti textových služeb, jako je SMS, v mobilních sítích.

## Popis

Total Character Error Rate (TCER, celková chybovost znaků) je standardizované měření výkonu definované 3GPP pro kvantifikaci přesnosti přenosu informací založeného na znacích v telekomunikačních službách, nejčastěji aplikované na službu krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Vypočítává se jako poměr počtu nesprávně přijatých znaků (včetně substitucí, vložení a vypuštění) k celkovému počtu odeslaných znaků, vyjádřený jako hodnota nebo procento. TCER poskytuje komplexní hodnocení kvality služby od konce ke konci tím, že zohledňuje všechny možné chyby znaků, které mohou nastat během kódování, přenosu, dekódování a prezentace napříč sítí a uživatelským zařízením (UE).

Z technického hlediska se TCER měří za specifických testovacích podmínek definovaných ve specifikacích 3GPP, jako je TS 26.231. Proces zahrnuje odeslání známé referenční textové zprávy ze zdroje do cíle za řízených síťových podmínek (např. při různých úrovních signálu a rušení). Přijatá zpráva je porovnána znak po znaku s originálem a chyby jsou zaznamenány. Hodnota TCER je poté vypočtena, často spolu s dalšími metrikami, jako je Character Transfer Rate ([CTR](/mobilnisite/slovnik/ctr/)) nebo Message Error Rate ([MER](/mobilnisite/slovnik/mer/)), aby poskytla ucelený pohled na výkon zasílání zpráv. Toto měření typicky provádějí síťoví operátoři, dodavatelé zařízení nebo regulační orgány pomocí specializovaných testovacích zařízení nebo softwaru, který simuluje uživatelský provoz a analyzuje výsledky.

Role TCER v síti je nedílnou součástí zajišťování kvality a řízení úrovně služeb. Pomáhá identifikovat problémy v signalizačních a transportních vrstvách, které ovlivňují textové služby, jako jsou problémy v [SMSC](/mobilnisite/slovnik/smsc/) (Short Message Service Center), vzájemná spolupráce mezi různými síťovými technologiemi (např. GSM a LTE) nebo nesoulad v kódování (např. GSM 7bitová výchozí abeceda vs. [UCS2](/mobilnisite/slovnik/ucs2/)). Monitorováním TCER mohou operátoři určit zdroje zhoršení výkonu, optimalizovat síťové parametry a zajistit soulad s regulačními požadavky na spolehlivost služeb. V kontextu se rozvíjejících služeb, jako jsou Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)) nebo zasílání zpráv přes IP, mohou být principy TCER rozšířeny na hodnocení komponent multimediálních zpráv, ačkoli hlavní zaměření zůstává na přesnosti znaků u tradiční SMS.

## K čemu slouží

TCER byl zaveden, aby poskytl standardizovanou, objektivní metriku pro hodnocení výkonu služeb textových zpráv, které se staly všudypřítomnými s rozmachem [SMS](/mobilnisite/slovnik/sms/) v sítích 2G/3G. Před jeho definicí operátoři postrádali konzistentní způsob měření přesnosti zasílání zpráv a spoléhali se na subjektivní stížnosti uživatelů nebo základní míry úspěšnosti/neúspěšnosti, které nezachycovaly dílčí chyby (např. jeden špatný znak v dlouhé zprávě). TCER tento problém řeší tím, že nabízí podrobnou míru, která odráží reálnou uživatelskou zkušenost, kde i drobné chyby mohou ovlivnit vnímání služby, zejména v kritických aplikacích, jako jsou ověřovací kódy nebo finanční upozornění.

Historicky, jak využití SMS rostlo pro osobní komunikaci i komunikaci mezi stroji (M2M), stalo se zajištění spolehlivého doručování klíčovým. Vytvoření TCER bylo motivováno potřebou srovnávat a zlepšovat síťový výkon napříč různými dodavateli a technologiemi, což usnadňuje testování interoperability a porovnávání kvality. Řešilo to omezení dřívějších metrik, které zvažovaly pouze úspěšnost doručení zprávy bez posouzení věrnosti obsahu, což je zásadní pro služby, kde je integrita dat prvořadá, jako je telemetrie nebo nouzová upozornění.

S vývojem směrem k 5G a IoT zůstává TCER relevantní pro hodnocení spolehlivosti textových služeb v různých scénářích, včetně úzkopásmového IoT (NB-IoT), kde se SMS používá pro správu zařízení a přenos malých objemů dat. Pomáhá operátorům zajistit, aby služby zasílání zpráv splňovaly požadavky na nízkou chybovost aplikací IoT, kde nepřesnosti mohou vést k provozním selháním. Tím, že poskytuje jasný výkonnostní cíl, TCER podporuje neustálé zlepšování v návrhu a údržbě sítě, čímž přispívá k celkovému cíli poskytování vysoce kvalitních komunikačních služeb ve stále více propojeném světě.

## Klíčové vlastnosti

- Standardizované měření přesnosti znaků pro textové služby, jako je SMS
- Výpočet založený na poměru nesprávných znaků k celkovému počtu odeslaných znaků
- Komplexní zahrnutí chyb včetně substitucí, vložení a vypuštění
- Definované testovací metodiky ve specifikacích 3GPP pro reprodukovatelné výsledky
- Aplikace napříč různými síťovými technologiemi (GSM, UMTS, LTE, 5G)
- Podpora zajišťování kvality a testování interoperability v prostředí více dodavatelů

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)

## Definující specifikace

- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing

---

📖 **Anglický originál a plná specifikace:** [TCER na 3GPP Explorer](https://3gpp-explorer.com/glossary/tcer/)
