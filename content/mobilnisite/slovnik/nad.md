---
slug: "nad"
url: "/mobilnisite/slovnik/nad/"
type: "slovnik"
title: "NAD – Node Address byte"
date: 2025-01-01
abbr: "NAD"
fullName: "Node Address byte"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nad/"
summary: "Jednobajtové pole používané v některých datových jednotkách protokolu 3GPP k identifikaci síťového uzlu nebo koncového bodu v rámci komunikační relace. Usnadňuje multiplexování a směrování zpráv mezi"
---

NAD je jednobajtové pole používané v protokolech 3GPP k identifikaci síťového uzlu nebo koncového bodu, které usnadňuje multiplexování a směrování zpráv mezi partnerskými entitami v zastaralých řídicích protokolech.

## Popis

Bajt adresy uzlu (NAD) je pole protokolu definované v raných specifikacích 3GPP, zejména v kontextu řízení rádiového spoje (RLC) a dalších protokolů vrstvy 2/3 pro UMTS a vývoj GSM. Slouží jako lokální identifikátor, typicky o délce jednoho oktetu, který se používá k rozlišení mezi různými logickými spojeními nebo body přístupu ke službám mezi dvěma komunikujícími síťovými entitami. Z architektonického hlediska je NAD součástí hlavičky datové jednotky protokolu (PDU), což umožňuje, aby jeden fyzický nebo transportní kanál přenášel více logických kanálů nebo datových toků určených pro různé procesy nebo aplikace vyšší vrstvy ve stejném uzlu.

Provozně NAD funguje tak, že je přiřazen během navazování spojení nebo nastavení relace. Například v některých konfiguracích RLC pro vyhrazené kanály může bajt NAD identifikovat konkrétní entitu RLC nebo typ přenášené datové jednotky služby (SDU), což umožňuje přijímači správně demultiplexovat příchozí data na příslušný protokol vyšší vrstvy (např. řízení hovoru, správu mobility nebo data uživatelské roviny). Rozsah hodnot 0–255 poskytuje dostatečnou kapacitu multiplexování pro většinu koncových bodů uvnitř uzlu. NAD se často používá ve spojení s dalšími identifikátory, jako je identifikátor spojení datové vazby ([DLCI](/mobilnisite/slovnik/dlci/)) nebo identifikátor bodu přístupu ke službě (SAPI), k vytvoření úplného adresovacího schématu pro protokoly vrstvy 2.

Jeho role je zvláště důležitá v zastaralých doménách s přepojováním okruhů a signalizaci řídicí roviny raného přepojování paketů, kde bylo kritické efektivní využití omezené šířky pásma a strukturované směrování zpráv. Zahrnutím NAD do PDU protokol zajišťuje, že zprávy jsou doručeny správnému internímu obslužnému programu, aniž by vyžadovaly samostatná fyzická spojení pro každý logický kanál, čímž šetří prostředky a zjednodušuje síťovou architekturu. S vývojem směrem k plně IP sítím a efektivnějším protokolům v LTE a NR však bylo explicitní použití vyhrazeného bajtu NAD z velké části nahrazeno sofistikovanějšími mechanismy multiplexování ve vrstvách [MAC](/mobilnisite/slovnik/mac/) a PDCP.

## K čemu slouží

Bajt adresy uzlu byl vytvořen pro řešení potřeby efektivního multiplexování více logických kanálů přes jedno fyzické nebo transportní spojení v raných digitálních celulárních systémech, jako jsou GSM a UMTS. Před jeho standardizací mohla proprietární nebo méně flexibilní adresovací schémata vést k problémům s interoperabilitou a neefektivnímu využití prostředků při obsluze simultánních služeb (např. hlasu, signalizace a paketových dat) na stejném rádiovém spoji.

Řeší problém směrování datových jednotek protokolu ke správné interní zpracovávající entitě uvnitř síťového uzlu (např. základnové stanice nebo mobilní stanice) bez nutnosti samostatných fyzických prostředků pro každý logický proud. To bylo zvláště důležité v éře sítí dominovaných přepojováním okruhů, kde bylo třeba spolehlivě oddělit a spravovat signalizační a uživatelská data na spojích s omezenou kapacitou. NAD poskytl jednoduchý, standardizovaný způsob, jak tohoto demultiplexování dosáhnout, a zajistil, že řídicí zprávy pro sestavení hovoru, předávání hovoru a doplňkové služby mohou koexistovat s uživatelskými hlasovými rámci na stejném spojení.

Historicky jeho zavedení ve verzi 4 (Release 4) souviselo s vylepšením GSM a počátečním nasazením UMTS, podporujícím rostoucí složitost služeb a přechod k více paketově orientované komunikaci. Ačkoli jeho význam v pozdějších systémech 4G a 5G poklesl kvůli přijetí IP protokolů a integrovanějších návrhů vrstvy 2, NAD zůstává relevantním konceptem pro pochopení fungování zastaralých systémů a zpětné kompatibility v sítích s více RAT.

## Klíčové vlastnosti

- Jednooktetové pole pro lokální adresování v uzlu
- Umožňuje multiplexování více logických kanálů přes jeden transport
- Používá se v hlavičkách protokolů RLC a dalších vrstev 2/3
- Podporuje demultiplexování ke správným entitám vyšší vrstvy
- Usnadňuje efektivní využití prostředků v zastaralých systémech
- Součást raných protokolů 3GPP pro přepojování okruhů a paketové řízení

## Související pojmy

- [DLCI – Data Link Connection Identifier](/mobilnisite/slovnik/dlci/)
- [Multiplexing](/mobilnisite/slovnik/multiplexing/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/nad/)
