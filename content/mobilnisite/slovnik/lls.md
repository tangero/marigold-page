---
slug: "lls"
url: "/mobilnisite/slovnik/lls/"
type: "slovnik"
title: "LLS – Link Level Simulations"
date: 2025-01-01
abbr: "LLS"
fullName: "Link Level Simulations"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lls/"
summary: "Link Level Simulations (LLS) jsou podrobné výpočetní modely používané v 3GPP k vyhodnocení výkonu technologií fyzické vrstvy v mobilních sítích. Simulují přenos signálu přes rádiové spoje a zohledňují"
---

LLS je podrobný výpočetní model používaný v 3GPP k simulaci přenosu rádiového signálu, který zohledňuje efekty jako útlum, a slouží k vyhodnocení metrik výkonnosti fyzické vrstvy, jako je propustnost a chybovost.

## Popis

Link Level Simulations (LLS) jsou metodologie definovaná ve specifikacích 3GPP pro modelování a analýzu chování fyzické vrstvy technologií rádiového přístupu, jako jsou LTE, NR (5G) a další. Tyto simulace se zaměřují na bodový spoj mezi vysílačem (např. základnovou stanicí nebo UE) a přijímačem a zahrnují podrobné modely stupňů zpracování signálu. Mezi klíčové komponenty patří schémata modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), kanálové kódování (např. Turbo nebo [LDPC](/mobilnisite/slovnik/ldpc/) kódy), techniky více antén ([MIMO](/mobilnisite/slovnik/mimo/)) a modely rádiového kanálu, které emulují efekty šíření jako útlum na dráze, vícecestný útlum, Dopplerův posuv a interferenci. LLS typicky pracuje na úrovni symbolu nebo bitu, což inženýrům umožňuje měřit metriky výkonu jako Block Error Rate ([BLER](/mobilnisite/slovnik/bler/)), propustnost, spektrální účinnost a latenci za různých podmínek.

Z architektonického hlediska jsou rámce LLS specifikovány v dokumentech jako 3GPP TS 38.830 a 38.843, které poskytují pokyny pro simulační předpoklady, modely kanálů a hodnotící kritéria. Proces zahrnuje generování vysílaných signálů, aplikaci degradací kanálu a zpracování na přijímači pomocí algoritmů pro demodulaci, ekvalizaci a dekódování. Simulace často používají standardizované referenční kanály, jako je Additive White Gaussian Noise ([AWGN](/mobilnisite/slovnik/awgn/)) kanál, nebo složitější scénáře jako 3GPP definovaný Typical Urban (TU) kanál. LLS lze provádět pro různá nasazení sítě, včetně městského makro, venkovského a vnitřního prostředí, aby se zajistila robustnost napříč případy použití. Nástroje pro LLS sahají od proprietárního softwaru po open-source platformy, což umožňuje interoperabilitu a validaci mezi výrobci zařízení a výzkumníky.

V praxi LLS funguje tak, že iteruje přes více simulačních běhů s náhodnými parametry, aby získala statistické výsledky. Například v 5G NR může LLS vyhodnocovat výkon nových možností vlnových forem, jako je cyclic prefix [OFDM](/mobilnisite/slovnik/ofdm/) ([CP-OFDM](/mobilnisite/slovnik/cp-ofdm/)) nebo DFT-s-OFDM, v pásmech vysokých frekvencí. Pomáhá při ladění parametrů fyzické vrstvy, jako je volba řádu modulace nebo kódovacího poměru, k dosažení cílových chybovostí. LLS také podporuje vývoj pokročilých funkcí, jako je formování svazku a massive MIMO, simulací odezev anténních polí a zpětné vazby informací o stavu kanálu. Poskytnutím kontrolovaného prostředí umožňuje LLS srovnávací analýzu mezi různými technologickými návrhy během zasedání standardizace 3GPP, což zajišťuje, že vybrané techniky splňují požadavky na výkon, než jsou zahrnuty do specifikací.

## K čemu slouží

Link Level Simulations (LLS) existují, aby umožnily důkladné, standardizované vyhodnocení technologií fyzické vrstvy v mobilní komunikaci a řešily potřebu validace výkonu před hardwarovou implementací. Jak se bezdrátové systémy vyvíjely od 2G přes 5G až k současnému 6G, rostla složitost rozhraní vzduchu s funkcemi jako [MIMO](/mobilnisite/slovnik/mimo/) vyššího řádu, pokročilé kanálové kódování a milimetrové vlny. LLS poskytuje společný rámec pro hodnocení těchto inovací reprodukovatelným způsobem a řeší problémy jako nekonzistentní testovací metodologie mezi výrobci a operátory. Byla motivována historickými výzvami spoléhání se pouze na laboratorní testy nebo zkoušky v terénu, které jsou nákladné, časově náročné a nemusí pokrýt všechny scénáře.

Vznik LLS v 3GPP, zvláště zdůrazňovaný od Release 14 dále, byl hnán poptávkou po rozhodování založeném na datech ve standardizaci. Řeší omezení předchozích ad-hoc simulačních přístupů definováním jednotných modelů kanálů, hodnotících metrik a simulačních předpokladů. LLS pomáhá optimalizovat návrh systému pro klíčové ukazatele výkonu (KPI), jako je datový tok a spolehlivost, a zajišťuje, že nové technologie jako NR splňují přísné požadavky enhanced mobile broadband (eMBB) a ultra-reliable low-latency communications (URLLC). Tím, že usnadňuje srovnávání výkonu v raných fázích, LLS urychluje inovace, snižuje vývojová rizika a zajišťuje interoperabilitu napříč odvětvím.

## Klíčové vlastnosti

- Modeluje přenos a příjem na fyzické vrstvě s podrobným zpracováním signálu
- Zahrnuje standardizované modely kanálů (např. AWGN, vícecestný útlum) pro realistické podmínky
- Vyhodnocuje metriky výkonu jako BLER, propustnost a spektrální účinnost
- Podporuje více technologií včetně LTE, NR a pokročilých anténních systémů
- Poskytuje pokyny pro simulační předpoklady a referenční scénáře ve specifikacích 3GPP
- Umožňuje srovnávací analýzu schémat modulace, kódování a MIMO

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 38.830** (Rel-17) — NR Coverage Enhancements Study
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [LLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lls/)
