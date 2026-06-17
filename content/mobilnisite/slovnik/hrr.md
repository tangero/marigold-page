---
slug: "hrr"
url: "/mobilnisite/slovnik/hrr/"
type: "slovnik"
title: "HRR – Handover Resource Reservation"
date: 2025-01-01
abbr: "HRR"
fullName: "Handover Resource Reservation"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hrr/"
summary: "HRR je mechanismus mobility řízený sítí, při kterém jsou rádiové prostředky proaktivně rezervovány v cílové buňce před provedením předání. Tato předrezervace si klade za cíl zaručit dostupnost prostře"
---

HRR je mechanismus předávání řízený sítí, při kterém jsou rádiové prostředky proaktivně rezervovány v cílové buňce před provedením předání, aby byla zajištěna jejich dostupnost a minimalizovalo se přerušení služby.

## Popis

Handover Resource Reservation (HRR, rezervace prostředků pro předání) je proaktivní procedura správy prostředků používaná v celulárních sítích k přípravě na blížící se předání. Základní princip spočívá v tom, že zdrojový síťový uzel (např. základnová stanice nebo RNC) komunikuje s potenciálním cílovým uzlem, aby požádal o rezervaci konkrétních rádiových prostředků – jako jsou časové sloty, kódy nebo přenosové kanály – pro konkrétní uživatelské zařízení (UE) před vydáním skutečného povelu k předání. Tento proces je typicky spuštěn na základě měřicích hlášení od UE, která indikují zhoršující se kvalitu signálu z obsluhující buňky a zlepšující se kvalitu ze sousední buňky.

Procedura funguje v rámci signalizačních protokolů řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a rádiové síťové vrstvy. Po rozhodnutí, že je předání nutné, odešle zdrojový uzel cílovému uzlu žádost o rezervaci prostředků (např. zprávu HANDOVER REQUEST). Tato žádost obsahuje kontext UE a požadavky na QoS. Cílový uzel následně provede řízení přístupu; pokud jsou prostředky dostupné, přidělí je a zarezervuje a odešle potvrzení zpět zdrojovému uzlu. Zdrojový uzel poté přikáže UE, aby se předala do cílové buňky, která může okamžitě zahájit komunikaci pomocí předem přidělených prostředků, čímž se vyhne kolizím nebo zpožděním při nastavování.

Role HRR je klíčová pro řízení mobility v přetížených sítích nebo pro služby s přísnými požadavky na QoS, jako je Voice over LTE (VoLTE) nebo video v reálném čase. Tím, že zajišťuje připravenost prostředků, minimalizuje dobu, po kterou je UE v přechodném, nesynchronizovaném stavu mezi buňkami, a snižuje tak ztrátu paketů a latenci při předání. Tento mechanismus je základní součástí předávání řízených sítí v GSM, UMTS a LTE, ačkoli konkrétní detaily implementace a zasílané zprávy se liší mezi různými technologiemi rádiového přístupu (RAT).

## K čemu slouží

HRR byl vyvinut, aby řešil inherentní nepředvídatelnost a potenciální zdroje selhání při mobilních předáních, zejména v raných celulárních systémech. Bez rezervace by se pokus o předání mohl nezdařit, pokud by cílové buňka náhle dosáhla přetížení mezi měřicím hlášením a provedením předání, což by vedlo k přerušeným hovorům a špatné uživatelské zkušenosti. Primární problém, který HRR řeší, je zaručení dostupnosti prostředků v okamžiku provedení předání.

Jeho vznik byl motivován potřebou spolehlivé, síťově řízené mobility pro podporu služeb hlasu s přepojováním okruhů, kde jsou i krátká přerušení nepřijatelná. Rezervací prostředků předem přebírá síť kontrolu nad procesem mobility, optimalizuje využití prostředků napříč buňkami a zabraňuje scénářům, kdy se UE úspěšně přistupuje k nové buňce, ale je okamžitě blokována z důvodu nedostatku kapacity. Tento proaktivní přístup se stal standardem pro řízenou mobilitu a vytvořil základ pro pokročilejší techniky, jako jsou bezproblémová předání v LTE a 5G.

## Klíčové vlastnosti

- Proaktivní rezervace rádiových prostředků v cílové buňce před provedením předání
- Snižuje pravděpodobnost selhání předání a míru přerušení hovorů
- Minimalizuje dobu přerušení služby a ztrátu paketů při pohybu
- Procedura řízená sítí založená na měřicích hlášeních od UE
- Integruje se s řízením přístupu v cílové buňce
- Základní prvek spolehlivého předávání v GSM, UMTS a LTE

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges

---

📖 **Anglický originál a plná specifikace:** [HRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrr/)
