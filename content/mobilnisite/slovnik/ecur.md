---
slug: "ecur"
url: "/mobilnisite/slovnik/ecur/"
type: "slovnik"
title: "ECUR – Event Charging with Unit Reservation"
date: 2025-01-01
abbr: "ECUR"
fullName: "Event Charging with Unit Reservation"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecur/"
summary: "Event Charging with Unit Reservation (ECUR) je mechanismus účtování v sítích 3GPP, který kombinuje účtování založené na událostech s předběžnou rezervací peněžních nebo servisních jednotek. Umožňuje k"
---

ECUR je 3GPP mechanismus účtování, který kombinuje účtování založené na událostech s předběžnou rezervací jednotek, aby umožnil kontrolu zůstatku v reálném čase a přidělování kvót pro služby, čímž zajišťuje přesné fakturace a zabraňuje překročení limitu.

## Popis

Event Charging with Unit Reservation (ECUR) je klíčovou součástí Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) dle 3GPP, definovanou v doméně účtování a fakturace. Funguje tak, že zpracovává účtovací události, u kterých využití služby vyžaduje předchozí rezervaci jednotek (např. peněžního kreditu, objemu dat, času) před doručením služby. Proces zahrnuje interakci OCS se síťovými prvky, jako je Policy and Charging Rules Function (PCRF) nebo aplikační servery, za účelem autorizace a sledování spotřeby prostředků v reálném čase.

Z architektonického hlediska ECUR funguje prostřednictvím řady standardizovaných rozhraní, především referenčního bodu Sy mezi OCS a PCRF a referenčního bodu Ro pro komunikaci založenou na protokolu Diameter se síťovými prvky. Při zahájení požadavku na službu odešle síťový prvek do OCS požadavek Credit Control Request ([CCR](/mobilnisite/slovnik/ccr/)) specifikující požadované jednotky. OCS následně provede kontrolu zůstatku, rezervuje příslušné jednotky z účtu uživatele a odpoví odpovědí Credit Control Answer ([CCA](/mobilnisite/slovnik/cca/)) s přidělenou kvótou. Během poskytování služby jsou periodicky odesílány hlášení o spotřebě a OCS odečítá z rezervovaných jednotek, případně vydává nové rezervace podle potřeby, dokud relace neskončí nebo se jednotky nevyčerpají.

Mezi klíčové komponenty patří funkce správy zůstatku na účtu (Account Balance Management Function – [ABMF](/mobilnisite/slovnik/abmf/)) v OCS pro sledování zůstatků, Rating Function (RF) pro stanovení ceny a Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)) v síťových prvcích, která detekuje zpoplatnitelné události. ECUR podporuje různé typy služeb, jako je přístup k datům, hlasové hovory, SMS a multimediální služby, což umožňuje flexibilní tarifní modely, například předplacené nebo hybridní plány. Jeho fungování zajišťuje těsné propojení účtování s řízením služeb, čímž brání úniku výnosů a umožňuje okamžité ukončení služby při nedostatku prostředků. Tento mechanismus je zásadní pro scénáře účtování v reálném čase v sítích LTE a 5G, kde vysokorychlostní využití dat vyžaduje okamžité aktualizace fakturace.

## K čemu slouží

ECUR byl vyvinut k řešení omezení offline účtování a jednoduchého účtování založeného na událostech v systémech před 3GPP, které nedokázaly v reálném čase zabránit využití služeb nad rámec kreditního limitu uživatele. S tím, jak se mobilní služby rozvíjely a zahrnovaly datově náročné aplikace a předplacené modely se rozšířily, vznikla potřeba mechanismu, který by dokázal jednotky předem rezervovat, a zajistil tak operátorům kontrolu finančního rizika při poskytování plynulého uživatelského zážitku. ECUR umožňuje operátorům nabízet komplexní, využitím citlivé tarify a předcházet podvodům přímou integrací účtování s autorizací služby.

Jeho zavedení v Release 8 časově souviselo s nasazením LTE a vylepšené architektury [OCS](/mobilnisite/slovnik/ocs/), což podpořilo přechod k plně IP sítím a bohatší nabídce služeb. Kombinací účtování událostí s rezervací řeší problém přesného a okamžitého účtování služeb na vyžádání, což je nezbytné pro spokojenost zákazníků a provozní efektivitu na konkurenčních telekomunikačních trzích. Historický kontext zahrnuje dřívější mechanismy, jako je Advice of Charge (AoC), které byly méně dynamické a nebyly integrovány s řízením politik.

## Klíčové vlastnosti

- Rezervace jednotek v reálném čase před poskytnutím služby
- Integrace s Online Charging System (OCS) prostřednictvím protokolu Diameter
- Podpora více typů jednotek (peněžní, objemové, časové)
- Dynamická správa kvót s aktualizacemi během relace
- Interakce s Policy and Charging Rules Function (PCRF) pro vynucování politik
- Zpracování různých servisních událostí, jako jsou datové relace, hovory a zasílání zpráv

## Definující specifikace

- **TS 28.204** (Rel-18) — Charging management
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.274** (Rel-19) — SMS Charging Management Specification
- **TS 32.277** (Rel-19) — Charging Management for Proximity Services (ProSe)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [ECUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecur/)
