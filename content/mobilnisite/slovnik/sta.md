---
slug: "sta"
url: "/mobilnisite/slovnik/sta/"
type: "slovnik"
title: "STA – Session-Termination-Answer"
date: 2025-01-01
abbr: "STA"
fullName: "Session-Termination-Answer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sta/"
summary: "Zpráva protokolu Diameter používaná v sítích 3GPP k potvrzení ukončení relace. Odesílá se jako odpověď na Session-Termination-Request (STR) a potvrzuje, že prostředky relace byly uvolněny a záznamy o"
---

STA je zpráva protokolu Diameter odeslaná jako odpověď na Session-Termination-Request (STR) za účelem potvrzení ukončení relace, potvrzení uvolnění prostředků a dokončení záznamů o účtování v sítích 3GPP.

## Popis

Session-Termination-Answer (STA) je zpráva protokolu Diameter definovaná v rámci standardů 3GPP, konkrétně používaná pro správu relací a účtovací operace. Je součástí základního protokolu Diameter ([RFC](/mobilnisite/slovnik/rfc/) 6733) v adaptaci 3GPP pro telekomunikační sítě, například v architektuře Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). STA generuje Diameter server, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)), jako odpověď na Session-Termination-Request ([STR](/mobilnisite/slovnik/str/)) odeslaný klientem, jako je Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo Application Function ([AF](/mobilnisite/slovnik/af/)). Tato výměna zpráv typicky nastává při ukončení uživatelské relace z důvodů, jako je odhlášení, odpojení od sítě nebo ukončení služby.

Z architektonického hlediska STA funguje přes rozhraní Diameter, jako je Gx (mezi PCEF a PCRF), Gy (mezi PCEF a OCS) nebo Rx (mezi AF a PCRF). Zpráva obsahuje atributy [AVP](/mobilnisite/slovnik/avp/) (Attribute-Value Pairs), které přenášejí identifikátory relací, výsledkové kódy a informace o účtování. Po přijetí STR server požadavek zpracuje uvolněním přidělených politik, aktualizací účtovacích relací a vygenerováním finálních účtovacích záznamů. STA následně potvrzuje toto dokončení výsledkovým kódem indikujícím úspěch nebo selhání (např. DIAMETER_SUCCESS nebo chyba). Tím je zajištěna synchronizace stavu relace na obou koncích, což zabraňuje únikům prostředků nebo nesrovnalostem v účtování.

V praxi je STA klíčová pro účtování v reálném čase a vynucování politik v sítích LTE a 5G. Například když UE ukončí datovou relaci, PCEF odešle STR k PCRF přes rozhraní Gx; PCRF odpoví STA, což spustí odstranění pravidel QoS a uzavření záznamů o účtovacích datech. Zpráva může obsahovat AVP, jako je CC-Request-Type nastavený na TERMINATION_REQUEST a Session-Id pro jednoznačnou identifikaci relace. Klíčové komponenty zahrnují uzly Diameter, databáze relací a účtovací systémy, přičemž STA zajišťuje čisté ukončení relace a přesné finanční vyúčtování.

Role STA sahá až k interoperabilitě s dalšími protokoly, jako je RADIUS ve starších systémech, ačkoli Diameter je upřednostňován pro své rozšířené schopnosti. Podporuje různé typy relací, včetně IP-CAN (IP Connectivity Access Network) relací a relací vyhrazených nosičů, což ji činí univerzální napříč síťovými službami. Poskytnutím standardizovaného mechanismu potvrzení zvyšuje STA spolehlivost správy životního cyklu relace, což je nezbytné pro škálovatelné a automatizované operace v moderních telekomunikačních sítích.

## K čemu slouží

STA byla zavedena, aby vyřešila potřebu spolehlivého ukončení relace a dokončení účtování v paketově přepínaných sítích, zejména s vývojem 3GPP směrem k all-IP architekturám ve verzi Release 11. Před její standardizací se správa relací často spoléhala na méně robustní mechanismy, jako jsou časové limity nebo proprietární signalizace, což mohlo vést k plýtvání prostředky a chybám v účtování. Například v raných systémech GPRS nebylo ukončení relace vždy explicitně potvrzováno, což způsobovalo nekonzistence mezi síťovými prvky a účtovacími systémy. STA tento problém řeší tím, že poskytuje potvrzenou odpověď na požadavky o ukončení založenou na protokolu Diameter.

Historicky přechod na služby řízené LTE a IMS zvýšil složitost správy relací, přičemž dynamické vynucování politik a účtování v reálném čase se stalo prvořadým. STA vznikla jako součást přijetí protokolu Diameter v 3GPP, který nahradil starší protokoly, jako je RADIUS, pro lepší škálovatelnost a bezpečnost. Odstraňuje omezení předchozích přístupů tím, že zajišťuje explicitní potvrzení ukončení relace, což umožňuje okamžité uvolnění prostředků a přesné generování záznamů o účtovacích datech (CDR). To je motivováno požadavky operátorů na efektivní využití síťových prostředků a přesné účtování, zejména s růstem datově náročných aplikací.

Kromě toho STA podporuje regulatorní a komerční potřeby, jako je dodržování předpisů pro účtování a podpora služeb předplacených i s fakturou. Tím, že umožňuje synchronizované uzavření relace napříč více síťovými funkcemi, předchází problémům, jako je nadměrné nebo nedostatečné účtování, které byly v dřívějších systémech běžné. Její vznik byl hnán snahou odvětví o automatizované, politikami řízené sítě, kde je správa životního cyklu relace klíčová pro QoS, zabezpečení a monetizaci v nasazeních 4G a 5G.

## Klíčové vlastnosti

- Potvrzovací zpráva založená na protokolu Diameter pro ukončení relace
- Odesílána jako odpověď na Session-Termination-Request (STR)
- Obsahuje AVP pro identifikátory relací a výsledkové kódy
- Integruje se s architekturou PCC přes rozhraní jako Gx a Gy
- Zajišťuje uvolnění politik a dokončení záznamů o účtování
- Podporuje různé typy relací (např. IP-CAN, vyhrazené nosiče)

## Související pojmy

- [STR – Session-Termination-Request](/mobilnisite/slovnik/str/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [STA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sta/)
