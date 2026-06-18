---
slug: "rm"
url: "/mobilnisite/slovnik/rm/"
type: "slovnik"
title: "RM – Resynchronization Marker"
date: 2025-01-01
abbr: "RM"
fullName: "Resynchronization Marker"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rm/"
summary: "Značka vložená do datového proudu, zejména ve vrstvě řízení rádiového spoje (RLC), která označuje bod resynchronizace pro přijímající entitu. Je klíčová pro zotavení z přenosových chyb, protože umožňu"
---

RM je značka vložená do datového proudu na vrstvě RLC, která označuje bod resynchronizace a umožňuje přijímači zotavit se z chyb a správně se zarovnat pro dekódování následujících dat.

## Popis

Značka resynchronizace (RM) je řídicí mechanismus používaný v protokolech vrstvy datového spoje systémů 3GPP, nejvýznamněji ve vrstvě řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) pracující v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)). Jejím hlavním účelem je poskytnout známý, jednoznačný bod v sekvenci vysílaných protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)), od kterého může přijímač po selhání synchronizace znovu zahájit správné zpracování. K selhání synchronizace může dojít v důsledku závažných chybových stavů, jako je ztráta významného počtu PDU, nejednoznačnosti protokolu nebo vypršení časovačů, které způsobí, že vysílač a přijímač mají nekonzistentní představu o tom, která data byla úspěšně doručena.

Provozně, když vysílající RLC entita určí, že je resynchronizace nutná (často vyvolána protokolovou chybou nebo řídicím postupem), zahrne do datového proudu řídicí PDU RM nebo příznak. Tato značka nese specifické informace o čísle sekvence, které definují nový referenční bod. Po přijetí a rozpoznání RM použije přijímající RLC entita informace, které obsahuje, k resetování svých stavových proměnných, jako je očekávané číslo sekvence pro příchozí PDU. Poté typicky zahodí jakékoli nejednoznačně přijaté PDU, které byly zařazeny do fronty před značkou, a začne přijímat a zpracovávat PDU počínaje novým číslem sekvence uvedeným v RM.

RM je klíčovou součástí pro zajištění odolnosti a spolehlivosti služby RLC v potvrzovaném režimu, která garantuje bezchybné doručování dat vyšší vrstvy ve správném pořadí. Bez takového mechanismu by přetrvávající desynchronizace mezi vysílačem a přijímačem mohla vést k trvalému selhání rádiového nosiče a vyžadovat obnovení spojení na vyšší vrstvě. Poskytnutím řízeného mechanismu 'resetu' uvnitř vrstvy umožňuje RM spoji autonomně a rychle se zotavit z přechodných, ale závažných chybových stavů a zachovat tak kontinuitu služby. Jeho implementace je úzce spojena s číslováním sekvencí RLC, správou okna a postupy opakovaného přenosu, čímž tvoří kritickou část sady nástrojů pro zotavení z chyb na spojové vrstvě.

## K čemu slouží

RM byl zaveden, aby řešil zásadní problém spolehlivých protokolů datového spoje: obnovení synchronizace protokolu po katastrofickém selhání. V raných bezdrátových datových službách byla míra chyb vysoká a složité protokoly se stavem, jako je [RLC](/mobilnisite/slovnik/rlc/) v potvrzovaném režimu, mohly přejít do deadlocku nebo nedefinovaných stavů, pokud se prostor čísel sekvence mezi odesílatelem a příjemcem stal nejednoznačným kvůli ztraceným potvrzením nebo řídicím paketům. Před standardizovanou resynchronizací bylo jediným řešením takového stavu zrušení a opětovné zřízení celého rádiového nosiče nebo dokonce [RRC](/mobilnisite/slovnik/rrc/) spojení, což je pomalý, náročný na zdroje a pro uživatele rušivý proces.

Vytvoření RM poskytlo vestavěný, lehký mechanismus obnovy. Problém řeší tím, že umožňuje vysílači jednostranně (nebo prostřednictvím vyjednávání) deklarovat nový počáteční bod pro prostor čísel sekvence, čímž efektivně 'vymaže tabuli' pro segment datového toku. To bylo motivováno potřebou robustnějších a efektivnějších rádiových nosičů pro vznikající paketové služby v systémech 3G a pozdějších, kde bylo prvořadé udržování integrity spojení pro služby jako VoIP, streamování videa a interaktivní hry. RM umožňuje systému udržovat vysokou úroveň spolehlivosti bez nutnosti obnovovat spojení při každé větší chybové události.

Jeho specifikace zajišťuje interoperabilitu mezi implementacemi RLC entit od různých dodavatelů. Standardizací formátu a postupů pro resynchronizaci garantuje, že přijímač od jednoho dodavatele dokáže správně interpretovat RM odeslaný vysílačem od jiného dodavatele, čímž se zachovává spolehlivost služby od konce ke konci v sítích s více dodavateli. To je nezbytné pro zdravý ekosystém mobilních zařízení.

## Klíčové vlastnosti

- Poskytuje definovaný bod resynchronizace v datovém proudu RLC AM
- Nese informace o čísle sekvence pro resetování stavových proměnných přijímače
- Umožňuje zotavení z selhání synchronizace protokolu bez uvolnění spojení na vyšší vrstvě
- Implementován jako součást řídicích PDU RLC nebo specifických polí v datových PDU
- Spouštěn chybovými stavy protokolu nebo specifickými řídicími postupy
- Zajišťuje interoperabilitu pro spolehlivé doručování dat v sítích s více dodavateli

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia

---

📖 **Anglický originál a plná specifikace:** [RM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rm/)
