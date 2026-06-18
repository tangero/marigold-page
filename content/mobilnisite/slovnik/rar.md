---
slug: "rar"
url: "/mobilnisite/slovnik/rar/"
type: "slovnik"
title: "RAR – Re-Auth-Request"
date: 2025-01-01
abbr: "RAR"
fullName: "Re-Auth-Request"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rar/"
summary: "Příkaz protokolu Diameter používaný v architektuře Policy and Charging Control (PCC). Je odesílán funkcí Policy and Charging Rules Function (PCRF) za účelem vyžádání si opětovného autorizování probíha"
---

RAR je příkaz protokolu Diameter odesílaný PCRF za účelem vyžádání si opětovného autorizování probíhající servisní relace, typicky za účelem změny jejích QoS politik, účtovacích pravidel nebo servisních parametrů.

## Popis

Re-Auth-Request (RAR) je příkaz Diameter s kódem 258 definovaný v rámci 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) frameworku specifikovaném v TS 29.212 a souvisejících specifikacích. Je klíčovou součástí referenčních bodů Gx a Rx, která umožňuje dynamické řízení politik. Příkaz RAR je iniciován funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a odeslán funkci Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) přes rozhraní Gx nebo Application Function ([AF](/mobilnisite/slovnik/af/)) přes rozhraní Rx, aby spustil opětovné autorizování aktivní [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) relace. To umožňuje PCRF modifikovat parametry relace v reálném čase bez čekání na periodickou aktualizaci nebo spouštěč z přístupové sítě.

Když PCRF rozhodne, že je vyžadována změna politiky – z důvodů jako vyčerpání kvóty účastníka, změna servisní úrovně, přetížení sítě nebo požadavek aplikace – sestaví zprávu RAR. Tato zpráva obsahuje páry atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)), které specifikují požadované akce, jako je instalace, úprava nebo odstranění PCC pravidel. Pro rozhraní Gx může RAR obsahovat nové QoS parametry, účtovací pravidla nebo instrukce stavu brány. Po přijetí RAR musí PCEF (typicky umístěná v [PGW](/mobilnisite/slovnik/pgw/)/GGSN) aplikovat nová pravidla a odpovědět pomocí Re-Auth-Answer ([RAA](/mobilnisite/slovnik/raa/)) na potvrzení změn. Podobně může být na rozhraní Rx RAR použit k notifikaci AF o úpravách relace, což umožňuje adaptaci na aplikační vrstvě.

Procedura RAR je nedílnou součástí mechanismu řízení politik spouštěného událostmi v 3GPP sítích. Funguje ve spojení s dalšími příkazy Diameter jako Credit-Control-Request (CCR) a Answer (CCA). Klíčové AVP v RAR zahrnují Session-Id, Origin-Host, Origin-Realm, Destination-Host, Destination-Realm a specifické PCC rule AVP jako Charging-Rule-Install nebo Charging-Rule-Remove. Protokol zajišťuje spolehlivé doručení prostřednictvím mechanismů failover a transportu základního protokolu Diameter. Tato schopnost dynamického opětovného autorizování je zásadní pro implementaci pokročilých služeb jako sponzorovaná data, QoS na vyžádání a řízení přetížení, což umožňuje síti pružně reagovat na měnící se podmínky při zachování kontinuity relace.

## K čemu slouží

Příkaz RAR byl zaveden, aby řešil potřebu proaktivních, síťově iniciovaných aktualizací politik v rámci PCC architektury. Před jeho standardizací často změny politik závisely na požadavcích iniciovaných klientem nebo statických konfiguracích, které byly nedostatečné pro řízení služeb v reálném čase. RAR umožňuje PCRF, jako centrálnímu bodu pro rozhodování o politikách, vynutit změny politik okamžitě, když jsou spuštěny externími událostmi, jako je změna profilu účastníka, zatížení sítě nebo požadavky aplikace.

Tato schopnost vyřešila významná omezení v časných systémech řízení politik, které byly převážně reaktivní. Například bez RAR by úprava QoS pro video stream během přetížení vyžadovala čekání na žádost UE nebo AF o změnu, což by mohlo degradovat uživatelský zážitek. RAR umožňuje síti převzít iniciativu a zajistit, aby se politiky dynamicky přizpůsobovaly provozním podmínkám. Je obzvláště důležitý pro monetizační strategie jako vrstvené služby a sponzorovaná data, kde musí být účtovací pravidla aktualizována okamžitě na základě účtovacích událostí.

Historicky se zavedení RAR v Release 9 časově shodovalo s dozráním PCC frameworku pro LTE/EPC. Poskytlo chybějící mechanismus pro úpravu relace iniciovanou serverem, který doplnil existující dialogy iniciované klientem CCR/CCA. To umožnilo operátorům implementovat sofistikovanější, reálnocasovou diferenciaci služeb a optimalizaci sítě, což znamenalo posun za jednoduché statické poskytování politik k dynamickému, událostmi řízenému modelu politik, který je základem pro moderní mobilní broadbandové služby.

## Klíčové vlastnosti

- Příkaz Diameter s kódem 258 používaný na rozhraních Gx a Rx
- Umožňuje PCRF-iniciované opětovné autorizování aktivních IP-CAN relací
- Nese AVP pro instalaci, úpravu nebo odstranění PCC pravidel
- Podporuje dynamické aktualizace QoS a účtovacích politik v reálném čase
- Integruje se se spouštěči událostí jako vyčerpání kvóty nebo detekce přetížení
- Vyžaduje povinnou odpověď prostřednictvím Re-Auth-Answer (RAA) pro potvrzení

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [RAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rar/)
