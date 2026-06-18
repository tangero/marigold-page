---
slug: "pmip"
url: "/mobilnisite/slovnik/pmip/"
type: "slovnik"
title: "PMIP – Proxy Mobile Internet Protocol version 6"
date: 2025-01-01
abbr: "PMIP"
fullName: "Proxy Mobile Internet Protocol version 6"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pmip/"
summary: "Proxy Mobile IPv6 (PMIPv6) je síťový protokol správy mobility standardizovaný IETF a přijatý organizací 3GPP. Umožňuje IP mobilitu pro mobilní uzel bez nutnosti jeho účasti na signalizaci mobility. Sí"
---

PMIP je síťový protokol mobility, v němž síť zařídí veškerou signalizaci mobility za mobilní uzel, což umožňuje IP mobilitu bez nutnosti přímé účasti zařízení.

## Popis

Proxy Mobile IPv6 (PMIPv6) je síťový protokol správy mobility, který poskytuje podporu IP mobility pro mobilní uzel bez nutnosti, aby se tento uzel účastnil jakékoli signalizace související s IP mobilitou. Protokol je definován [IETF](/mobilnisite/slovnik/ietf/) v dokumentu [RFC](/mobilnisite/slovnik/rfc/) 5213 a navazujících dokumentech a byl přijat a profilován organizací 3GPP pro použití v rámci Evolved Packet Core (EPC) a později 5G Core (5GC). V doméně PMIPv6 jsou síťové entity zodpovědné za správu mobility mobilního uzlu. Dvěma klíčovými funkčními entitami jsou Mobile Access Gateway ([MAG](/mobilnisite/slovnik/mag/)) a Local Mobility Anchor ([LMA](/mobilnisite/slovnik/lma/)). MAG je funkce typicky umístěná společně s přístupovým směrovačem (např. Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) v EPC nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC). Detekuje připojení mobilního uzlu k síti, iniciuje za něj signalizaci mobility s LMA a vytváří obousměrný tunel. LMA je topologický kotvní bod pro prefix(y) domovské sítě mobilního uzlu. Spravuje položku vázací cache, která asociuje identitu mobilního uzlu (např. jeho Network Access Identifier) s care-of adresou MAG, která jej aktuálně obsluhuje. Veškerý provoz určený pro mobilní uzel je směrován přes LMA, která jej tuneluje příslušnému MAG. MAG následně detunneluje pakety a doručí je mobilnímu uzlu. Opačným směrem je provoz z mobilního uzlu tunelován MAG k LMA. Toto tunelové přeposílání zajišťuje kontinuitu relace při pohybu mobilního uzlu mezi MAG, neboť LMA zůstává konstantním kotvním bodem. Protokol používá mezi MAG a LMA zprávy Proxy Binding Update ([PBU](/mobilnisite/slovnik/pbu/)) a Proxy Binding Acknowledgment ([PBA](/mobilnisite/slovnik/pba/)) pro vytvoření, aktualizaci a zrušení vázacího stavu. PMIPv6 podporuje přenos i adresování pro IPv4 i IPv6, včetně mechanismů jako je dual-stack provoz a mobilita IPv4 domovské adresy. V architekturách 3GPP je PMIPv6 specifikován jako jeden z protokolů řídicí roviny pro rozhraní S5/S8 mezi SGW a Packet Data Network Gateway (PGW) v EPC, což poskytuje alternativu k GPRS Tunneling Protocol (GTP).

## K čemu slouží

PMIPv6 byl vyvinut k řešení omezení hostitelských protokolů mobility, jako je Mobile IPv6 (MIPv6), které vyžadují mobilní zásobník a aktivní účast samotného mobilního uzlu. Tento požadavek představoval výzvu pro jednoduchá zařízení s omezenou kapacitou baterií a komplikoval kontrolu síťovým operátorem. Primárním účelem PMIPv6 je poskytnout bezproblémovou IP mobilitu jako síťovou službu, pro koncové zařízení transparentně. Přesunutím funkcionality správy mobility do síťové infrastruktury PMIPv6 zjednodušuje návrh zařízení, šetří životnost baterie zařízení a dává operátorům větší kontrolu nad mobilitními politikami a správou prostředků. Jeho přijetí v 3GPP, počínaje Release 8 pro EPC, bylo motivováno potřebou standardizovaného, IP-based protokolu mobility, který by mohl spolupracovat s nepřístupovými sítěmi 3GPP (jako je Wi-Fi) a podporovat síťové řízení provozu a vymáhání politik. Poskytl alternativu k GTP, což podpořilo konkurenci a umožnilo nasazení v sítích, kde GTP nebylo žádoucí. PMIPv6 vyřešil problém udržení probíhajících datových relací při pohybu zařízení mezi různými body připojení, což je zásadní pro permanentní připojení v mobilních broadbandových službách.

## Klíčové vlastnosti

- Síťová správa mobility, nevyžadující klientský software na mobilním uzlu
- Používá zprávy Proxy Binding Update/Acknowledgment mezi MAG a LMA
- Vytváří obousměrný IP-in-IP tunel mezi MAG a LMA pro přenos dat
- Podporuje adresování i přenos pro IPv4 i IPv6 (dual-stack provoz)
- Umožňuje mezitechnologové předávání spojení (např. mezi 3GPP a důvěryhodným nepřístupem 3GPP)
- Poskytuje mobilnímu uzlu stabilní prefix domovské sítě, což zajišťuje kontinuitu relace

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [MAG – Mobility Access Gateway](/mobilnisite/slovnik/mag/)
- [LMA – Local Mobility Anchor](/mobilnisite/slovnik/lma/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [PMIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmip/)
