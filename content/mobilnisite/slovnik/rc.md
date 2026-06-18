---
slug: "rc"
url: "/mobilnisite/slovnik/rc/"
type: "slovnik"
title: "RC – Rate Control Procedure Acknowledgement"
date: 2025-01-01
abbr: "RC"
fullName: "Rate Control Procedure Acknowledgement"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rc/"
summary: "Potvrzení procedury řízení přenosové rychlosti (Rate Control Procedure Acknowledgement, RC) je řídicí zpráva signalizační roviny používaná na rozhraní Iu v sítích UMTS k potvrzení přijetí a zpracování"
---

RC je řídicí zpráva signalizační roviny používaná na rozhraní Iu v sítích UMTS k potvrzení přijetí a zpracování příkazu řízení přenosové rychlosti jako součást správy přenosového kanálu rádiového přístupu (Radio Access Bearer).

## Popis

Potvrzení procedury řízení přenosové rychlosti (Rate Control Procedure Acknowledgement, RC) je specifická řídicí zpráva v rámci protokolu [RANAP](/mobilnisite/slovnik/ranap/) (Radio Access Network Application Part), který funguje přes rozhraní Iu spojující řadič rádiové sítě (Radio Network Controller, [RNC](/mobilnisite/slovnik/rnc/)) a jádro sítě (Core Network, CN) v síti UMTS podle 3GPP. Rozhraní Iu je rozděleno na Iu-CS (pro přepojování okruhů) pro hlas a Iu-PS (pro přepojování paketů) pro data; zprávy RC jsou relevantní pro obě domény při správě přenosových rychlostí přenosových kanálů. Potvrzení RC je odesláno jako odpověď na zprávu RANAP 'Rate Control', kterou iniciuje CN za účelem požadavku na změnu maximální povolené přenosové rychlosti pro existující přenosový kanál rádiového přístupu (Radio Access Bearer, [RAB](/mobilnisite/slovnik/rab/)). Toto tvoří část procedury modifikace RAB.

Z provozního hlediska, když se CN rozhodne upravit přenosovou rychlost aktivní uživatelské relace (např. z důvodu změny požadavků služby, přetížení sítě nebo zásad předplatitele), odešle obsluhujícímu RNC zprávu RANAP Rate Control. Tato zpráva obsahuje novou požadovanou maximální přenosovou rychlost pro uplink a/nebo downlink. Po jejím přijetí RNC provede řízení přístupu (admission control) a výpočty rádiových zdrojů, aby určilo, zda lze novou rychlost podpořit. Pokud RNC žádost přijme, překonfiguruje s UE rádiový přenosový kanál a poté odešle zpět do CN zprávu RC potvrzení, čímž potvrdí úspěšnou aplikaci nové rychlosti. Pokud žádost nemůže být vyhověna, RNC místo toho odpoví zprávou Rate Control Failure. Samotné potvrzení RC je prostým potvrzením, ale spouští následné akce v obou entitách k vynucení nových limitů přenosové rychlosti.

Procedura RC je klíčová pro dynamické řízení kvality služeb (QoS) v UMTS. Umožňuje síti přizpůsobit se měnícím se podmínkám v reálném čase a optimalizovat tak využití zdrojů a uživatelský prožitek. Procedura spoléhá na spolehlivý přenos poskytovaný vrstvami [SCCP](/mobilnisite/slovnik/sccp/) (Signalling Connection Control Part) a [MTP](/mobilnisite/slovnik/mtp/) (Message Transfer Part) pod RANAP. Zatímco termín 'RC' konkrétně označuje zprávu potvrzení, celá 'Procedura řízení přenosové rychlosti' zahrnuje žádost, interní zpracování v RNC, rádiovou rekonfiguraci s UE a konečné potvrzení nebo oznámení o selhání, čímž zajišťuje synchronizovaný stav QoS mezi RAN a CN.

## K čemu slouží

Procedura řízení přenosové rychlosti a její potvrzení (RC) byly vytvořeny, aby umožnily dynamické, během relace prováděné úpravy přenosových rychlostí pro uživatelská spojení v sítích UMTS. Předchozí buněčné systémy jako GSM/[GPRS](/mobilnisite/slovnik/gprs/) měly statičtější správu přenosových kanálů, kde se přenosové rychlosti většinou nastavovaly při navázání spojení. UMTS zavedlo bohatší multimediální služby s proměnlivými nároky na šířku pásma, což si vyžádalo mechanismus, aby jádro sítě mohlo během aktivní relace žádat RAN o změny rychlosti. Tím byl vyřešen problém neefektivní fixní alokace zdrojů, což umožnilo přizpůsobit síťové zdroje skutečným potřebám služeb a úrovním přetížení.

Zavedení procedury RC ve vydání 5 (Release 5) bylo úzce spojeno s vývojem rozhraní Iu a protokolu [RANAP](/mobilnisite/slovnik/ranap/), které oddělily funkce RAN a CN. Řešilo potřebu koordinovaného řízení QoS mezi jádrem sítě, které má přehled o službách (zná profily předplatitelů a požadavky služeb), a [RNC](/mobilnisite/slovnik/rnc/), které má přehled o rádiových zdrojích (zná zatížení buňky a rádiové podmínky). Potvrzení RC poskytuje nezbytné potvrzení, aby obě strany udržovaly konzistentní pohled na schopnosti aktivního přenosového kanálu, čímž předchází přerušení služby nebo nesrovnalostem v účtování. Tato dynamická kontrola byla obzvláště důležitá pro rané datové služby 3G a videotelefonii, protože umožňovala plynulé přizpůsobení mezi různými úrovněmi kvality.

## Klíčové vlastnosti

- Řídicí zpráva RANAP na rozhraní Iu (pro Iu-CS i Iu-PS)
- Odesílána RNC do jádra sítě (Core Network) k potvrzení příkazu řízení přenosové rychlosti
- Součást procedury modifikace přenosového kanálu rádiového přístupu (Radio Access Bearer, RAB)
- Zajišťuje spolehlivé vyjednávání maximální přenosové rychlosti pro uživatelskou relaci
- Spouštěna po úspěšné rekonfiguraci rádiového přenosového kanálu s UE
- Využívá spolehlivý signalizační přenos přes SCCP/MTP

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 32.832** (Rel-10) — Alarm Correlation and Root Cause Analysis Study
- **TS 32.856** (Rel-15) — Energy Efficiency Assessment for RAN OAM
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [RC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rc/)
