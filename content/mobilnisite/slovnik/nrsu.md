---
slug: "nrsu"
url: "/mobilnisite/slovnik/nrsu/"
type: "slovnik"
title: "NRSU – Network Request Support UE"
date: 2025-01-01
abbr: "NRSU"
fullName: "Network Request Support UE"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nrsu/"
summary: "NRSU je schopnost UE indikující podporu procedury Network Requested Bearer Control, která umožňuje síti iniciovat zřízení nebo modifikaci PDP (Packet Data Protocol) kontextů či PDU (Packet Data Unit)"
---

NRSU je schopnost UE (User Equipment) indikující podporu procedury Network Requested Bearer Control, která umožňuje síti iniciovat zřízení nebo modifikaci PDP kontextů či PDU relací.

## Popis

Network Request Support UE (NRSU) je příznak schopnosti uvnitř uživatelského zařízení (UE), který signalizuje síti, zda zařízení podporuje procedury, při nichž může síť iniciovat aktivaci nebo modifikaci přenosového kanálu datové relace. V kontextu paketově orientovaných jader 3GPP – konkrétně [GPRS](/mobilnisite/slovnik/gprs/) jádra pro 2G/3G a Evolved Packet Core (EPC) pro 4G – je datová relace reprezentována [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) kontextem nebo přenosovým kanálem Evolved Packet System (EPS). Schopnost NRSU řídí použití procedury Network Requested Bearer Control, což je síťově iniciovaná obdoba standardní aktivace/modifikace PDP kontextu iniciované UE.

Z architektonického hlediska je schopnost NRSU vyměňována během signalizačních procedur jádra sítě. V systémech GPRS/UMTS je přenášena v rámci informačního prvku „network capability“ UE během procedur Připojení (Attach) nebo Aktualizace směrovací oblasti (Routing Area Update) směrem k [SGSN](/mobilnisite/slovnik/sgsn/). V EPS je podobná informace o schopnostech komunikována k [MME](/mobilnisite/slovnik/mme/). Když síťový uzel (jako Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Application Function ([AF](/mobilnisite/slovnik/af/)), například IMS server) určí potřebu zřídit nebo upravit přenosový kanál se specifickými parametry QoS pro službu, zkontroluje, zda UE indikovalo podporu NRSU. Pokud je podpora přítomna, může SGSN nebo MME iniciovat proceduru zřízení/modifikace přenosového kanálu směrem k UE pomocí specifických zpráv správy relací a vyžádat si od UE lokální aktivaci nebo modifikaci odpovídajícího kontextu.

Procedura funguje prostřednictvím definovaného signalizačního dialogu. Například po obdržení podnětu od PCRF (např. pro IMS hlasové volání) odešle MME k UE příkaz Bearer Resource Command. UE, která si je vědoma své vlastní schopnosti NRSU, tento požadavek zpracuje, odpovídajícím způsobem nakonfiguruje svou vnitřní správu relací a rádiové vrstvy a odpoví, čímž proceduru dokončí. Tento mechanismus umožňuje síti proaktivně nastavovat vyhrazené přenosové kanály se zaručenou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) pro služby v reálném čase ještě před začátkem toku médií, což zajišťuje nízkou latenci a splnění požadavků na QoS. Schopnost NRSU je tedy základním prvkem umožňujícím QoS řízené sítí a umožňuje jádru sítě optimalizovat využití prostředků a poskytování služeb na základě požadavků aplikace, namísto spoléhání se výhradně na žádosti o prostředky od aplikací v UE.

## K čemu slouží

Schopnost NRSU byla zavedena, aby vyřešila zásadní problém v časných paketově orientovaných sítích: neschopnost sítě efektivně zřizovat přenosové kanály se zárukou QoS pro služby, které se chystala doručit. V počátečních verzích [GPRS](/mobilnisite/slovnik/gprs/) mohlo pouze UE iniciovat aktivaci PDP kontextu. To bylo dostačující pro služby typu „best-effort“, jako je prohlížení internetu, ale způsobovalo významná zpoždění při sestavování a potenciální problémy s kvalitou u služeb v reálném čase, jako je Voice over IP (VoIP). Síť, která byla prostřednictvím IMS informována o příchozím volání, neměla přímý způsob, jak připravit vhodný přenosový kanál; musela čekat na žádost aplikace v UE, což vedlo ke zpožděním při sestavování hovoru a zhoršenému uživatelskému zážitku.

Vytvoření NRSU a související procedury Network Requested PDP Context Activation ve 3GPP Release 7 bylo přímo motivováno nasazením služeb založených na IMS, konkrétně Voice over LTE (VoLTE) a později Video over LTE (ViLTE). Vyřešilo to omezení čistě uživatelsky orientované správy relací tím, že umožnilo síťově iniciované řízení QoS. To operátorům umožňuje zajistit, že kritické služby obdrží potřebné síťové prostředky okamžitě a spolehlivě. Z historického kontextu šlo o významný krok směrem k přeměně mobilních sítí na skutečně služebně orientované platformy, posun od modelu jednoduché datové trubice k inteligentní síti schopné spravovat kvalitu služeb od konce ke konci.

Tato schopnost je klíčová pro model „vždy připojeného“ IP spojení v LTE a 5G, kde se očekává okamžitá dostupnost služeb. Řeší problém latence při sestavování služeb a zajišťuje, že QoS dohodnutá signalizační vrstvou IMS může být rychle namapována na podkladovou vrstvu přenosových kanálů. Bez podpory NRSU by sítě musely přejít k méně efektivním metodám nebo by trpěly špatným výkonem služeb v reálném čase, což by bránilo adopci čistě IP komunikačních služeb přes mobilní sítě.

## Klíčové vlastnosti

- Příznak schopnosti UE indikující podporu síťově iniciovaných procedur pro přenosové kanály.
- Umožňuje síťově iniciovanou aktivaci a modifikaci PDP kontextu v jádrech sítí 2G/3G/4G.
- Základní prvek pro síťově iniciované zřizování vyhrazených přenosových kanálů pro IMS a další služby citlivé na QoS.
- Vyměňována během procedur připojení a registrace v jádru sítě.
- Umožňuje PCRF a AF (např. IMS) spustit zřízení přenosového kanálu na základě služební politiky.
- Snižuje dobu sestavení služby a zajišťuje, že záruky QoS jsou splněny již od začátku toku služby.

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [NRSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrsu/)
