---
slug: "ngcn"
url: "/mobilnisite/slovnik/ngcn/"
type: "slovnik"
title: "NGCN – Next Generation Corporate Network / Next Generation Core Network"
date: 2025-01-01
abbr: "NGCN"
fullName: "Next Generation Corporate Network / Next Generation Core Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ngcn/"
summary: "NGCN původně označovalo Next Generation Corporate Network, koncept pro podnikovou konektivitu. Od Release 15 byl tento termín v dokumentaci 3GPP přejat pro označení Next Generation Core Network, čímž"
---

NGCN je 3GPP termín pro Next Generation Core Network, což je standardizovaná architektura 5G Core (5GC) definovaná od Release 15.

## Popis

Termín NGCN má v dokumentaci 3GPP dvojí význam, rozdělený časovou osou Release 15. Ve specifikacích pocházejících z období před Release 15 (např. Rel-11 až Rel-14) NGCN znamená 'Next Generation Corporate Network' (příští generace podnikové sítě). Tento koncept zkoumal architektury pro poskytování vylepšených, vyhrazených síťových služeb podnikovým zákazníkům, potenciálně využívající principy Evolved Packet Core, ale se zaměřením na podnikové potřeby, jako je integrace [VPN](/mobilnisite/slovnik/vpn/), konvergence pevných a mobilních sítí v rámci podnikového areálu a vylepšená bezpečnost. Technické studie se zaměřovaly na to, jak může mobilní operátor nabízet bezproblémový, spravovaný síťový řez nebo virtuální síť pro podniky, integrovaný s existující podnikovou [IT](/mobilnisite/slovnik/it/) infrastrukturou. Od Release 15 byla zkratka NGCN v určitých technických specifikacích (TS) znovu použita ve významu 'Next Generation Core Network' (příští generace jádrové sítě), čímž se stala synonymem pro nově standardizovanou 5G Core Network (5GC). V tomto kontextu odkazuje na celou cloud-nativní, službami řízenou architekturu jádra definovanou pro 5G. To zahrnuje všechny její součástní síťové funkce ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/) atd.), rozhraní mezi nimi založená na službách a základní procedury pro registraci, autentizaci, správu relací, řízení politik a mobilitu. NGCN (jako 5GC) funguje na principu oddělení softwarových funkcí od hardwaru, což umožňuje jejich nasazení na cloudové infrastruktuře. Používá jednotnou datovou vrstvu (poskytovanou [UDR](/mobilnisite/slovnik/udr/)) a centralizovaný rámec pro řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) ke správě chování sítě. Jeho činnost je založena na [PDU](/mobilnisite/slovnik/pdu/) Session, kterou vytváří a spravuje za účelem poskytnutí konektivity s konkrétními charakteristikami QoS k datové síti. Toto dvojí použití ilustruje vývoj zaměření 3GPP od vylepšování podnikových služeb na existující infrastruktuře k návrhu zcela nové, univerzální jádrové sítě schopné obsloužit všechny tržní segmenty, včetně podniků, prostřednictvím mechanismů, jako je síťové krájení.

## K čemu slouží

Účelem NGCN (Corporate Network) před Release 15 bylo reagovat na rostoucí poptávku podniků po integrovanějších, bezpečnějších a výkonnějších řešeních mobilní konektivity, která by mohla nahradit nebo bezproblémově splynout s tradičními podnikovými sítěmi LAN/WAN. Cílem bylo vyřešit problém nespojitého přístupu pro mobilní zaměstnance a zařízení IoT v rámci podniku. Koncept zkoumal, jak mohou mobilní operátoři nabízet 'síť jako službu' šitou na míru podnikům, což přesahuje jednoduchý přístup k internetu založený na APN. Přehodnocení termínu po Release 15 ve významu Core Network (jádrová síť) bylo motivováno potřebou stručného označení pro novou architekturu 5G jádra během její specifikace. Zatímco '5GC' se stal běžným termínem, 'NGCN' se objevuje v názvech a oblastech působnosti různých technických specifikací, které tvoří základ systému. Tento lexikální posun značí vyvrcholení dřívějších studií v plně realizovanou, standardizovanou architekturu. Nové NGCN (5GC) bylo vytvořeno, aby odstranilo základní omezení 4G EPC, a poskytlo tak agilitu, škálovatelnost a přizpůsobení konkrétním službám potřebné pro éru 5G, což v konečném důsledku umožnilo realizaci podnikových konceptů, které byly kdysi studovány pod starým názvem NGCN, prostřednictvím standardizovaného síťového krájení a funkcí edge computingu.

## Klíčové vlastnosti

- Před Rel-15: Zaměření na integraci podnikových VPN a konvergenci pevných a mobilních sítí
- Před Rel-15: Zkoumání vyhrazených logických sítí pro podnikové zákazníky
- Po Rel-15: Plná implementace architektury 5G založené na službách (SBA)
- Po Rel-15: Nativní podpora síťového krájení, umožňující virtuální podnikové sítě
- Po Rel-15: Oddělení řídicí a uživatelské roviny (CUPS) pro distribuované nasazení
- Po Rel-15: Jednotný rámec pro řízení politik a cloud-nativní, softwarově definovaný návrh

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 22.809** (Rel-11) — Interworking between 3GPP networks and Enterprise voice
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TR 24.969** (Rel-19) — NGCN to NGN Interconnection Implementation Guide

---

📖 **Anglický originál a plná specifikace:** [NGCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngcn/)
