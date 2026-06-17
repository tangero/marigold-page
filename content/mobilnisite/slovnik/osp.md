---
slug: "osp"
url: "/mobilnisite/slovnik/osp/"
type: "slovnik"
title: "OSP – Octet Stream Protocol"
date: 2025-01-01
abbr: "OSP"
fullName: "Octet Stream Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/osp/"
summary: "OSP je transportní protokol používaný v sítích 3GPP, především v rámci architektury GPRS Tunneling Protocol (GTP), pro přenos uživatelských dat a signalizace zarovnaných na oktet. Poskytuje spolehlivý"
---

OSP je spolehlivý transportní protokol s navázáním spojení používaný v rámci GTP architektury 3GPP pro přenos uživatelských dat a signalizace zarovnaných na oktet mezi síťovými uzly.

## Popis

Octet Stream Protocol (OSP) je základní transportní protokol definovaný ve specifikacích 3GPP, zejména spojený se sadou protokolů [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) používanou v sítích General Packet Radio Service (GPRS) a Evolved Packet Core (EPC). Funguje jako protokol s navázáním spojení navržený pro přenos datových proudů zarovnaných na oktet, což znamená, že zpracovává data v 8bitových jednotkách (oktetech), což odpovídá běžným standardům digitální komunikace. OSP funguje tak, že mezi dvěma koncovými body, jako je například spojení mezi Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN) v sítích GPRS nebo analogickými uzly v pozdějších architekturách, naváže logické spojení. Zajišťuje spolehlivý přenos dat prostřednictvím mechanismů, jako je číslování sekvencí, potvrzování a opakovaný přenos, které pomáhají zachovat integritu a pořadí dat přes potenciálně nespolehlivé podkladové transportní vrstvy, jako je IP.

Architektonicky je OSP integrován do protokolů řídicí roviny GTP ([GTP-C](/mobilnisite/slovnik/gtp-c/)) a uživatelské roviny GTP ([GTP-U](/mobilnisite/slovnik/gtp-u/)), kde usnadňuje zapouzdření a tunelování paketů uživatelských dat a signalizačních zpráv. V GTP poskytuje OSP základní rámcovou strukturu pro Protocol Data Units (PDU), definuje hlavičky obsahující pole pro typ zprávy, délku a sekvenční čísla. To umožňuje síťovým entitám multiplexovat více datových proudů přes jediný GTP tunel, což podporuje efektivní využití zdrojů. Mezi klíčové komponenty OSP patří jeho formát hlavičky, který typicky obsahuje řídicí informace pro správu relace, a jeho sekce s datovou částí, která nese samotná uživatelská data nebo signalizační informace. Návrh protokolu klade důraz na jednoduchost a efektivitu, což umožňuje komunikaci s nízkou latencí kritickou pro služby v reálném čase a správu mobility.

V širším síťovém kontextu hraje OSP klíčovou roli při umožňování paketově orientovaných služeb v sítích 2G, 3G a 4G tím, že podporuje tunelování založené na GTP. Tvoří základ pro funkce jako směrování paketů, zřizování přenosových drah a předávání spojení při mobilitě, což zajišťuje plynulý tok uživatelských dat mezi rádiovou přístupovou sítí a externími paketovými datovými sítěmi (např. internetem). Zatímco pozdější systémy 5G zavedly nové protokoly, jako je Packet Forwarding Control Protocol (PFCP) a zjednodušené verze GTP, principy OSP ovlivnily vývoj tunelovacích mechanismů, což zdůrazňuje jeho základní význam v architekturách 3GPP. Jeho provoz je pro koncové uživatele transparentní, ale pro síťové operátory je zásadní pro udržování kontinuity a kvality služeb.

## K čemu slouží

OSP byl vytvořen k řešení potřeby standardizovaného, spolehlivého transportního mechanismu v paketových jádrech sítí 3GPP, konkrétně pro [GPRS](/mobilnisite/slovnik/gprs/) a následné evoluce. Před jeho zavedením rané systémy mobilních dat postrádaly jednotný protokol pro tunelování uživatelských dat a signalizace mezi uzly jádra sítě, což vedlo k problémům s interoperabilitou a neefektivním zpracováním dat. OSP poskytl strukturovaný přístup k zapouzdření proudů zarovnaných na oktet, což umožnilo bezproblémovou komunikaci mezi SGSN a GGSN, což bylo nezbytné pro nasazení škálovatelných paketově orientovaných služeb vedle okruhově orientovaného hlasu.

Protokol řešil klíčové problémy, jako je fragmentace dat, opětovné sestavení a obnova po chybě v mobilním prostředí, kde mohly být síťové podmínky proměnlivé. Díky nabídnutí funkcí s navázáním spojení zajišťoval, že datové pakety byly doručeny ve správném pořadí a bez ztrát, což bylo kritické pro aplikace vyžadující spolehlivý transport, jako byl raný přístup k internetu a služby zasílání zpráv. Historicky se vývoj OSP v Release 4 časově shodoval se zráním GPRS a počátečními kroky směrem k plně IP sítím, což položilo základy pro pozdější vylepšení v architekturách [GTP](/mobilnisite/slovnik/gtp/) a EPC. Odstranil omezení dřívějších proprietárních nebo méně robustních tunelovacích metod tím, že poskytl specifikaci, která mohla být široce implementována napříč zařízeními různých výrobců, což podporovalo síťovou interoperabilitu a růst využívání mobilních dat.

## Klíčové vlastnosti

- Přenos dat zarovnaných na oktet pro efektivní zpracování 8bitových jednotek
- Provoz s navázáním spojení se spolehlivými mechanismy doručení
- Integrace s GTP pro tunelování dat uživatelské a řídicí roviny
- Podpora multiplexování více datových proudů přes jednotlivé tunely
- Pole hlavičky pro číslování sekvencí a identifikaci typu zprávy
- Kompatibilita s podkladovými transportními sítěmi založenými na IP

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [OSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/osp/)
