---
slug: "sut"
url: "/mobilnisite/slovnik/sut/"
type: "slovnik"
title: "SUT – System Under Test"
date: 2025-01-01
abbr: "SUT"
fullName: "System Under Test"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sut/"
summary: "System Under Test (SUT, testovaný systém) označuje konkrétní síťový prvek, zařízení nebo systém, který je hodnocen během testů shody, výkonu nebo interoperability. Jde o základní koncept v testovacích"
---

SUT (System Under Test, testovaný systém) je konkrétní síťový prvek, zařízení nebo systém, který je hodnocen během testů shody, výkonu nebo interoperability v rámci 3GPP specifikací.

## Popis

System Under Test (SUT, testovaný systém) je klíčový koncept v ekosystému testování a validace 3GPP, definovaný v řadě technických specifikací (TS). Představuje entitu – ať už hardwarovou, softwarovou nebo jejich kombinaci – která je předmětem dané testovací kampaně. V kontextu 3GPP je SUT typicky User Equipment (UE), základnová stanice (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) nebo funkce jádra sítě. Specifikace, jako je TS 37.579 pro testování vzájemného fungování NR a [E-UTRA](/mobilnisite/slovnik/e-utra/) nebo TS 51.010 pro GSM/[EDGE](/mobilnisite/slovnik/edge/), podrobně popisují testovací prostředí, postupy a kritéria úspěšnosti/neúspěšnosti aplikované na SUT. Architektura testovacího systému zahrnuje SUT, testovací zařízení (jako jsou simulátory sítě nebo analyzátory protokolů) a řídicí systém testů, který řídí provádění testovacích případů.

Testování SUT zahrnuje provedení sady předdefinovaných testovacích případů navržených k ověření konkrétních požadavků. Ty mohou zahrnovat testy shody v rádiové části (např. výkon vysílače, citlivost přijímače), testy signalizace protokolů (např. navázání [RRC](/mobilnisite/slovnik/rrc/) spojení, [NAS](/mobilnisite/slovnik/nas/) procedury) a výkonnostní testy (např. propustnost, latence). Testovací zařízení stimuluje SUT standardizovanou signalizací a provozem a zároveň monitoruje jeho odezvy ve srovnání s očekávaným chováním definovaným ve specifikacích 3GPP. Rozhraní SUT jsou připojena k testovacímu zařízení, čímž vzniká kontrolované a opakovatelné laboratorní prostředí, které izoluje výkon systému od proměnných živé sítě.

Role SUT je klíčová pro zajištění interoperability a shody. Předtím, než může být jakékoli síťové zařízení nebo koncové zařízení certifikováno pro použití v síti založené na 3GPP (jako je 5G, LTE nebo GSM), musí jako SUT projít důkladným testováním. Tento proces validuje, že implementace správně interpretuje a reaguje na síťové příkazy, dodržuje rádiové předpisy a poskytuje očekávanou kvalitu služeb. Organizace jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB se při certifikaci spoléhají na tyto standardizované definice testů SUT. Koncept SUT v konečném důsledku zajišťuje, že různé produkty od různých výrobců mohou v globální mobilní síti bezproblémově spolupracovat a udržovat tak kvalitu služeb a uživatelský zážitek.

## K čemu slouží

Koncept System Under Test (SUT, testovaný systém) existuje proto, aby poskytl standardizovaný, objektivní rámec pro ověření, že telekomunikační zařízení splňuje specifikace 3GPP. Bez takového rámce by každý výrobce mohl standardy interpretovat odlišně, což by vedlo k závažným problémům s interoperabilitou ve více-dodavatelských sítích. Jeho účelem je řešit základní problém zajištění, aby se UE od výrobce A mohlo úspěšně připojit, komunikovat a předat spojení k základnové stanici od výrobce B, a naopak, kdekoliv na světě.

Historicky, jak se mobilní sítě vyvíjely z proprietárních systémů na globální standardy, se potřeba formalizovaného testování shody stala klíčovou. Rané celulární systémy často měly omezenou interoperabilitu. Vytvoření podrobných testovacích specifikací (jako je řada 3x.xxx pro rádiové aspekty a 5x.xxx pro GSM) formalizovalo SUT jako centrální entitu podléhající hodnocení. Tím se odstranila omezení ad-hoc testování a výrobci specifických interpretací a poskytl se společný jazyk a metodologie pro testovací laboratoře a certifikační orgány.

Motivace přesahuje pouhou interoperabilitu a zahrnuje také regulační shodu (např. splnění norem pro rádiové emise), výkonnostní srovnávání a zajištění síťové bezpečnosti a stability. Tím, že 3GPP přesně definuje SUT a jeho testovací prostředí, umožňuje vývoj robustního ekosystému certifikovaných zařízení a síťové infrastruktury, což je zásadní pro komerční úspěch a technický vývoj každé generace (3G, 4G, 5G). Jde o základní prvek zajištění kvality v telekomunikačním průmyslu.

## Klíčové vlastnosti

- Centrální entita v testování shody a interoperability
- Definována v řadě testovacích specifikací 3GPP (např. TS 37.579, TS 51.010)
- Může jít o UE, základnovou stanici nebo funkci jádra sítě
- Funguje v kontrolovaném testovacím prostředí se simulovanými síťovými prvky
- Podléhá testovacím případům pro rádiovou část, protokoly a výkon
- Klíčová pro certifikaci zařízení a infrastruktury orgány jako je GCF

## Definující specifikace

- **TS 26.139** (Rel-19) — RTP/RTCP Conformance Testing Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [SUT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sut/)
