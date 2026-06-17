---
slug: "ats"
url: "/mobilnisite/slovnik/ats/"
type: "slovnik"
title: "ATS – Air Traffic Service"
date: 2025-01-01
abbr: "ATS"
fullName: "Air Traffic Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ats/"
summary: "ATS je služba 3GPP, která umožňuje mobilním sítím podporovat komunikaci pro řízení letového provozu. Poskytuje spolehlivé a zabezpečené připojení pro letadla, pozemní stanice a řídící letového provozu"
---

ATS je služba 3GPP, která umožňuje mobilním sítím poskytovat spolehlivé a zabezpečené připojení pro komunikaci řízení letového provozu mezi letadly, pozemními stanicemi a dispečery.

## Popis

Služba řízení letového provozu (Air Traffic Service – ATS) v 3GPP označuje standardizaci schopností mobilních sítí pro podporu komunikace v rámci řízení letového provozu (Air Traffic Management – [ATM](/mobilnisite/slovnik/atm/)). To zahrnuje výměnu kritických informací mezi letadly (letecké koncové zařízení, AUE), pozemními jednotkami řízení letového provozu ([ATC](/mobilnisite/slovnik/atc/)) a dalšími leteckými subjekty. Služba je navržena tak, aby splňovala přísné požadavky letecké bezpečnosti a pravidelnosti provozu, včetně vysoké spolehlivosti, nízké latence, zabezpečení a dostupnosti, v rozsáhlé geografické oblasti zahrnující vzdušný prostor a pozemní stanice.

Architektura pro ATS využívá stávající komponenty systému 5G, ale zavádí specifická vylepšení a nové funkční prvky pro splnění leteckých potřeb. Mezi klíčové architektonické aspekty patří podpora leteckých koncových zařízení (AUE), což jsou zařízení instalovaná na letadlech připojující se k síti 5G. Síť musí podporovat mobilitu při vysokých rychlostech a ve velkých výškách, což vyžaduje vylepšení správy mobility a řízení rádiových prostředků. Pozemní síťové funkce, jako je funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), jsou rozšířeny o letecké specifické politiky a požadavky na služby. Dále architektura zvažuje propojení se stávajícími leteckými komunikačními sítěmi, jako jsou sítě založené na ATN/[IPS](/mobilnisite/slovnik/ips/) nebo jiných legacy systémech, prostřednictvím definovaných funkcí pro vystavení sítě a propojovacích jednotek.

ATS funguje tak, že vytváří vyhrazené komunikační služby mezi AUE a pozemními jednotkami ATC nebo centry provozního řízení leteckých společností ([AOC](/mobilnisite/slovnik/aoc/)). Tyto služby mohou zahrnovat hlasovou komunikaci (datové spojení řídící–pilot, CPDLC) a datové služby pro sledování (např. automatická závislá sledovací služba – vysílání, ADS-B) nebo letové informace. Síť 5G poskytuje základní konektivitu s toky kvality služeb (QoS) přizpůsobenými leteckým profilům, což zajišťuje prioritní zpracování zpráv souvisejících s bezpečností. Zabezpečení je prvořadé, s mechanismy pro vzájemné ověřování mezi AUE a sítí, ochranu integrity a důvěrnost, často v souladu s leteckými specifickými bezpečnostními rámci.

Role ATS v síti spočívá v přeměně 5G na životaschopný doplněk nebo případného nástupce tradičních leteckých systémů s vyhrazeným spektrem (jako je VHF datalink nebo satelitní spoje). Umožňuje efektivnější využití spektra, vyšší datové rychlosti a integraci s inovacemi širšího mobilního ekosystému. Pro síťové operátory otevírá nový vertikální trh vyžadující specifické schopnosti síťového řezání, edge computingu a správy služeb k poskytování certifikovaných a spolehlivých služeb leteckému průmyslu.

## K čemu slouží

ATS byla vytvořena, aby řešila rostoucí potřebu modernizovaných, škálovatelných a nákladově efektivních komunikačních řešení pro řízení letového provozu. Tradiční letecké komunikační systémy, jako je VHF hlas a datové spoje, čelí zahlcení spektra, omezené datové kapacitě a vysokým provozním nákladům. Navíc očekávaný růst leteckého provozu, včetně dronů a pokročilých vozidel pro mobilitu ve vzdušném prostoru ([AAM](/mobilnisite/slovnik/aam/)), vyžaduje flexibilnější a datově bohatší komunikační infrastrukturu. Mobilní sítě založené na 3GPP nabízejí globálně nasazenou, kontinuálně se vyvíjející technologickou základnu, která může poskytovat vysokou šířku pásma, nízkou latenci a robustní zabezpečení, což z nich činí přesvědčivého kandidáta pro podporu stávající i budoucí komunikace [ATM](/mobilnisite/slovnik/atm/).

Motivace pro standardizaci ATS v rámci 3GPP, počínaje vydáním 17, vychází ze spolupráce mezi telekomunikačním a leteckým průmyslem. Orgány jako Mezinárodní organizace pro civilní letectví (ICAO) a letecké úřady zkoumaly využití komerčních mobilních sítí pro bezpečnou a pravidelnou letovou komunikaci. Standardizace 3GPP zajišťuje interoperabilitu, globální roaming pro letadla a úspory z rozsahu díky využití masivního nasazení sítí 5G. Cílem je definovat technické prvky, které umožní mobilním síťovým operátorům nabízet služby splňující přísné regulační a výkonnostní požadavky letectví, a tím usnadnit konvergenci pozemní mobilní a letecké komunikace.

Předchozí přístupy spoléhaly na izolované specializované systémy pro letectví, což vedlo k fragmentaci a pomalejším inovačním cyklům. Integrací požadavků ATM do rámce 5G řeší ATS omezení v efektivitě spektra, schopnostech datových služeb a zahušťování sítě. Umožňuje nové operační koncepty, jako je bezproblémová konektivita od země po cestovní výšky, podpora hustých operací městské mobility ve vzdušném prostoru a integrace s digitalizačními snahami řízení letového provozu, jako je systémové celoplošné informační řízení (SWIM).

## Klíčové vlastnosti

- Podpora leteckých koncových zařízení (AUE) s mobilitou ve velkých výškách a při vysokých rychlostech
- Letecké specifické profily kvality služeb (QoS) pro bezpečnostně kritickou komunikaci
- Rozšířené bezpečnostní mechanismy splňující letecké certifikační požadavky
- Spolupráce se staršími leteckými sítěmi (např. ATN/IPS)
- Síťové řezy pro vyhrazené instance služby řízení letového provozu
- Podpora datového spojení řídící–pilot (CPDLC) a služeb dat pro sledování

## Definující specifikace

- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [ATS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ats/)
