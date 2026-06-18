---
slug: "ihoss"
url: "/mobilnisite/slovnik/ihoss/"
type: "slovnik"
title: "IHOSS – Internet Hosted Octet Stream Service"
date: 2025-01-01
abbr: "IHOSS"
fullName: "Internet Hosted Octet Stream Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ihoss/"
summary: "Služba 3GPP umožňující transparentní, na IP založený proudový přenos dat mezi mobilním uživatelem a internetovým hostitelem. Poskytuje standardizovanou přenosovou službu (bearer service) pro přenos da"
---

IHOSS je služba 3GPP, která poskytuje standardizovaný, transparentní přenosový kanál (bearer) založený na IP pro proudový přenos dat zarovnaných na oktet mezi mobilním uživatelem a internetovým hostitelem přes paketově spínané jádro sítě.

## Popis

Internet Hosted Octet Stream Service (IHOSS) je standardizovaná přenosová služba (bearer service) definovaná v architektuře 3GPP, konkrétně pro paketově spínanou ([PS](/mobilnisite/slovnik/ps/)) doménu. Její hlavní funkcí je poskytnout transparentní, spojově orientovaný mechanismus pro přenos dat mezi mobilním uživatelským zařízením (UE) a internetovým hostitelem. Služba je orientována na 'oktetový proud' (octet stream), což znamená, že data zpracovává jako souvislou, uspořádanou sekvenci oktetů (bytů) a zajišťuje spolehlivé doručení ve správném pořadí, aniž by interpretovala obsah. Architektonicky IHOSS funguje nad kontextem paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)), který je navázán mezi UE a uzlem podpory brány [GPRS](/mobilnisite/slovnik/gprs/) (GGSN) v jádru sítě. Služba využívá podkladový protokol GPRS tunelování ([GTP](/mobilnisite/slovnik/gtp/)) pro přenos paketů uživatelských dat mezi uzlem podpory obsluhy GPRS ([SGSN](/mobilnisite/slovnik/sgsn/)) a GGSN. Z GGSN je datový proud směrován na externí paketovou datovou síť ([PDN](/mobilnisite/slovnik/pdn/)), typicky Internet. Klíčové komponenty zapojené do poskytování IHOSS zahrnují UE, které iniciuje žádost o aktivaci PDP kontextu s uvedením požadovaného názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) a profilu QoS; SGSN, který zajišťuje správu mobility a řízení relace; a GGSN, který funguje jako brána do externí IP sítě a přiděluje UE IP adresu. Role služby je základní: poskytuje základní vrstvu IP konektivity, na které jsou budovány četné aplikace vyšších vrstev (prohlížení webu, e-mail, přenos souborů), a abstrahuje složitost rádiového přístupu a přenosu v jádře sítě od koncové uživatelské aplikace.

## K čemu slouží

IHOSS byl vytvořen za účelem standardizace a poskytnutí spolehlivé, na IP založené služby pro doručování dat v mobilních sítích, jak se vyvíjely z okruhově spínaných systémů orientovaných na hlas na paketově spínané sítě orientované na data. Před jeho definicí byly mobilní datové služby často proprietární nebo omezené na specifické, ne-IP protokoly. Motivací bylo umožnit bezproblémový přístup na internet pro mobilní uživatele, kdy je mobilní síť chápána jako transparentní IP 'trubka' do globálního Internetu. Řešil problém, jak integrovat mobilní terminály do internetové architektury, a poskytoval konzistentní definici služby, která zajišťovala interoperabilitu mezi síťovými prvky různých výrobců a mezi mobilními sítěmi a poskytovateli internetových služeb. Definováním standardizované služby 'oktetového proudu' poskytlo 3GPP jasný model pro účtování, správu QoS a přidělování síťových zdrojů pro obecný IP datový provoz, což bylo klíčové pro komerční úspěch mobilních datových služeb přesahujících jednoduché [SMS](/mobilnisite/slovnik/sms/).

## Klíčové vlastnosti

- Poskytuje transparentní, spojově orientovaný přenos IP dat
- Pro navázání a správu relace využívá PDP kontexty
- Zajišťuje doručení dat uživatele zarovnaných na oktet ve správném pořadí
- Bezešvě spolupracuje s externími paketovými datovými sítěmi (PDN), jako je Internet
- Podporuje konfigurovatelné profily kvality služby (QoS) pro datový přenosový kanál (bearer)
- Spoléhá se na protokol GPRS tunelování (GTP) pro přenos v jádru sítě

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [IHOSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ihoss/)
