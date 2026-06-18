---
slug: "gsn"
url: "/mobilnisite/slovnik/gsn/"
type: "slovnik"
title: "GSN – GPRS Support Node"
date: 2025-01-01
abbr: "GSN"
fullName: "GPRS Support Node"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gsn/"
summary: "Uzel jádrové sítě v sítích 2G/3G/4G GPRS a UMTS, který zpracovává paketový datový provoz. Odkazuje buď na Serving GPRS Support Node (SGSN), nebo Gateway GPRS Support Node (GGSN). Tyto uzly jsou zásadn"
---

GSN je uzel jádrové sítě v sítích 2G/3G/4G GPRS a UMTS, který zpracovává paketový datový provoz, a konkrétně odkazuje buď na Serving GPRS Support Node (SGSN), nebo Gateway GPRS Support Node (GGSN).

## Popis

[GPRS](/mobilnisite/slovnik/gprs/) Support Node (GSN) je obecný termín pro dva hlavní paketově orientované prvky jádrové sítě v architekturách GPRS a UMTS: Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Node (GGSN). SGSN je zodpovědný za doručování datových paketů od a k mobilním stanicím ve své geografické servisní oblasti. Mezi jeho funkce patří směrování a přenos paketů, správa mobility (připojení/odpojení a správa polohy), správa logického spojení a autentizační a účtovací funkce. SGSN komunikuje s rádiovou přístupovou sítí (např. s [BSC](/mobilnisite/slovnik/bsc/) v 2G, [RNC](/mobilnisite/slovnik/rnc/) v 3G) přes rozhraní Gb nebo Iu-ps a s dalšími uzly SGSN a GGSN přes rozhraní Gn/Gp pomocí protokolu GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)).

GGSN funguje jako brána mezi jádrovou sítí GPRS/UMTS a externími paketovými datovými sítěmi ([PDN](/mobilnisite/slovnik/pdn/)), jako je veřejný internet nebo firemní intranet. Obsahuje směrovací informace pro připojené mobilní stanice a je zodpovědný za přidělování IP adres, často prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/). GGSN plní roli směrovače, který přeposílá pakety mezi externí PDN a SGSN obsluhujícím uživatele. Také zajišťuje vynucování politik, filtrování paketů a je primárním bodem pro sběr účtovacích dat (např. pro fakturaci podle objemu dat). Spojení mezi SGSN a GGSN je GTP tunel, který zapouzdřuje IP pakety uživatele, aby zajistil transparentnost mobility.

Společně tvoří SGSN a GGSN páteř paketově orientovaného jádra a umožňují trvalé připojení. SGSN spravuje uživatelskou rovinu (přeposílání dat) a řídicí rovinu (signalizaci pro relaci a mobilitu) směrem k přístupové síti, zatímco GGSN kotví uživatelskou relaci a poskytuje připojení k vnějšímu světu. Tato architektura oddělila paketově orientovanou doménu od domény s přepojováním okruhů pro hlas, což umožnilo efektivní datové služby. V pozdějších sítích 4G EPC a 5G Core jsou funkce SGSN a GGSN rozvinuty a distribuovány do entit jako [MME](/mobilnisite/slovnik/mme/), SGW a PGW.

## K čemu slouží

Architektura GSN byla vytvořena za účelem zavedení možností paketově orientovaných dat do stávajících sítí 2G GSM, které byly původně navrženy pouze pro přepojování okruhů pro hlas a SMS. Před GPRS byly datové služby jako Circuit Switched Data (CSD) neefektivní, protože na celou dobu spojení blokovaly celý přenosový kanál bez ohledu na skutečný přenos dat. Uzly GPRS Support Node byly vyvinuty, aby poskytovaly 'vždy zapojenou' datovou službu založenou na IP, umožňovaly statistické multiplexování více uživatelů na sdílených rádiových zdrojích a efektivní přenos trhaného datového provozu, jako je prohlížení webu a e-mail.

Rozdělení na SGSN a GGSN sloužilo konkrétním účelům. SGSN, který je blíže rádiové síti, efektivně spravuje spojení rádiových zdrojů a mobilitu v místní oblasti. GGSN poskytuje stabilní kotvící bod k externímu IP světu, skrývá mobilitu uživatele před externími sítěmi a zjednodušuje směrování a účtování. Toto rozdělení umožnilo škálovatelné nasazení sítě a nezávislý vývoj funkcí přístupové a jádrové sítě. Rámec GSN položil základy pro mobilní širokopásmový přístup, který se vyvinul přes 3G UMTS až k základům architektury 4G Evolved Packet Core.

## Klíčové vlastnosti

- Směrování a přenos paketů pro mobilní datové relace
- Správa mobility včetně připojení, odpojení a sledování polohy
- Tunelování uživatelských dat pomocí protokolu GPRS Tunneling Protocol (GTP)
- Autentizační, autorizační a účtovací funkce
- Brána (gateway) k externím paketovým datovým sítím (PDN)
- Správa a přidělování IP adres pro mobilní zařízení

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [GSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsn/)
