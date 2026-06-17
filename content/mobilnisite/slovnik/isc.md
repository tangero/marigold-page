---
slug: "isc"
url: "/mobilnisite/slovnik/isc/"
type: "slovnik"
title: "ISC – IP multimedia subsystem Service Control interface"
date: 2025-01-01
abbr: "ISC"
fullName: "IP multimedia subsystem Service Control interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isc/"
summary: "Rozhraní ISC je standardizovaný referenční bod mezi funkcí řízení hovorové relace (CSCF) a aplikačním serverem (AS) v jádru IMS. Je založeno na protokolu SIP (Session Initiation Protocol) a používá se"
---

ISC je rozhraní založené na SIP mezi funkcí řízení hovorové relace (Call Session Control Function) a aplikačním serverem v jádru IMS, používané k delegování řízení relace pro řízení služeb.

## Popis

Rozhraní ISC (IP multimedia subsystem Service Control) je klíčový referenční bod v architektuře 3GPP IMS (IP Multimedia Subsystem) založený na SIP. Je definováno jako rozhraní mezi obslužným S-CSCF (Serving-CSCF) nebo dotazovacím [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating-CSCF) a aplikačním serverem ([AS](/mobilnisite/slovnik/as/)). Hlavní úlohou ISC je umožnit řízení a provádění služeb pro relace založené na IMS. Když S-CSCF, který funguje jako centrální uzel řízení relace, zpracovává požadavek SIP (jako INVITE nebo REGISTER), vyhodnotí počáteční filtrační kritéria (iFC) uložená v profilu služeb uživatele na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server). Pokud iFC spustí službu, S-CSCF přepošle SIP požadavek na určený AS prostřednictvím rozhraní ISC.

Z architektonického hlediska umožňuje rozhraní ISC jasné oddělení řízení relace (které zajišťuje [CSCF](/mobilnisite/slovnik/cscf/)) a servisní logiky (hostované na AS). To odpovídá principu nezávislosti služeb na podkladovém transportu. AS může být telekomunikační aplikační server (TAS) poskytující tradiční telefonní služby, server přítomnosti, server pro zasílání zpráv nebo vlastní platforma služeb. Komunikace přes ISC využívá standardní metody a dialogy SIP, často rozšířené o specifické hlavičky nebo těla SIP definované 3GPP (např. P-Asserted-Identity, P-Charging-Vector) pro předání identity uživatele, informací o účtování a kontextu služby.

Jak to funguje, zahrnuje podrobný tok signalizace SIP. Po přijetí SIP požadavku pro uživatele provede S-CSCF porovnání s profilem služeb. Porovná požadavek s prioritním seznamem iFC. Každé iFC obsahuje spouštěč servisního bodu (SPT), který definuje podmínky (např. konkrétní metodu SIP, požadovaný URI, přítomnost určitých hlaviček) a adresu AS, která má být vyvolána, pokud je podmínka splněna. Když dojde k shodě, S-CSCF proxy přepošle SIP požadavek na tento AS. AS následně provede svou servisní logiku, což může zahrnovat úpravu zprávy SIP, interakci s jinými síťovými elementy, přehrávání hlášení nebo zahájení nových relací. AS pak může vrátit řízení zpět S-CSCF (fungujícímu jako SIP Back-to-Back User Agent neboli [B2BUA](/mobilnisite/slovnik/b2bua/)) pro další zpracování nebo směrování.

Jeho role je zásadní pro model poskytování služeb IMS. Rozhraní ISC je mechanismus, který činí IMS 'service-aware' (schopné rozpoznávat služby). Umožňuje vytvoření živého ekosystému aplikačních serverů od různých dodavatelů, které všechny spolupracují se standardizovaným jádrem. Podporuje poskytování služeb třetími stranami a umožňuje komplexní řetězení služeb, kdy může být relace sekvenčně zpracována více AS (např. pro screening hovoru, následný překlad čísla a poté hlasovou schránku). ISC zajišťuje, že servisní logika může řízeným a bezpečným způsobem ovlivňovat směrování relací, politiky a média, čímž tvoří páteř pro poskytování pokročilých komunikačních služeb přes IP.

## K čemu slouží

Rozhraní ISC bylo vytvořeno k řešení zásadního problému při přechodu od tradiční telefonie s přepojováním okruhů k architektuře multimediálních služeb plně založených na IP. V sítích před IMS byla servisní logika často pevně integrována s přepojovacím hardwarem (jako v [IN](/mobilnisite/slovnik/in/)/AIN), což ztěžovalo a prodražovalo vývoj, nasazení a úpravy služeb. Cílem IMS bylo oddělit služby od podkladového síťového transportu a umožnit rychlou inovaci služeb. Rozhraní ISC je klíčovým prvkem tohoto oddělení, neboť poskytuje standardizovaný 'háček' pro řízení služeb mezi vrstvou řízení relace a aplikační vrstvou.

Historicky byl jeho vývoj v 3GPP Release 5 (součást původní specifikace IMS) motivován potřebou flexibilního mechanismu pro vyvolávání služeb, který je přátelský k internetu (založený na SIP). Řešil omezení předchozích protokolů inteligentních sítí (IN), jako je [CAMEL](/mobilnisite/slovnik/camel/), které byly navrženy pro hovory s přepojováním okruhů a postrádaly flexibilitu pro bohaté multimediální relace. Rozhraní ISC, založené na SIP, umožnilo hladkou integraci webových služeb a telekomunikací a podporovalo vše od základních hlasových hovorů přes přítomnost, instant messaging až po videokonference v rámci jednotného rámce.

Problémy, které řeší, jsou mnohé: zabraňuje vázanosti na konkrétního dodavatele standardizací interakce mezi síťovým jádrem a aplikacemi; umožňuje přenositelnost služeb a mobilitu uživatele, protože služby jsou vyvolávány na základě profilu uživatele, nikoli jeho polohy; a usnadňuje konvergenci služeb tím, že umožňuje přístup ke stejné servisní logice (na [AS](/mobilnisite/slovnik/as/)) z různých přístupových sítí (např. LTE, WLAN, pevný broadband). Vytvoření ISC bylo klíčovým krokem k posunu telekomunikačních sítí směrem k otevřené, aplikací řízené architektuře, která podporuje konkurenci a inovace ve vrstvě služeb.

## Klíčové vlastnosti

- Standardizované rozhraní založené na SIP mezi S-CSCF/I-CSCF a aplikačními servery
- Umožňuje vyvolání služby na základě počátečních filtračních kritérií (iFC) z uživatelského profilu
- Podporuje řetězení služeb a sekvenční vyvolávání AS
- Přenáší klíčové hlavičky SIP pro identitu, účtování a kontext služby
- Usnadňuje vývoj a integraci služeb třetích stran
- Klíčový prvek architektury poskytování služeb IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISC na 3GPP Explorer](https://3gpp-explorer.com/glossary/isc/)
