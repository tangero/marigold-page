---
slug: "ft"
url: "/mobilnisite/slovnik/ft/"
type: "slovnik"
title: "FT – Fast BSS Transition"
date: 2025-01-01
abbr: "FT"
fullName: "Fast BSS Transition"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ft/"
summary: "Soubor protokolů a procedur definovaných 3GPP, který umožňuje uživatelskému zařízení (UE) rychlý a bezpečný přechod mezi různými podsystémy základnových stanic (BSS) nebo přístupovými body s minimální"
---

FT je soubor 3GPP protokolů a procedur umožňujících rychlý a bezpečný přechod mezi podsystémy základnových stanic (Base Station Subsystems) s cílem minimalizovat přerušení služby a podpořit plynulou mobilitu.

## Popis

Rychlý přechod [BSS](/mobilnisite/slovnik/bss/) (FT) je funkce správy mobility standardizovaná 3GPP za účelem optimalizace předávání spojení, zejména ve scénářích zahrnujících nepřístupové sítě ne-3GPP, jako je Wi-Fi (jak je definováno v kontextu mobility S2a přes důvěryhodné [WLAN](/mobilnisite/slovnik/wlan/)). Hlavním cílem je snížit latenci a ztrátu paketů spojenou s přesunem uživatelského zařízení (UE) z jednoho přístupového bodu ([AP](/mobilnisite/slovnik/ap/)) nebo základnové stanice na jiný. Procedury FT fungují tak, že předem navážou bezpečnostní a kontextové informace v cílovém AP *před* tím, než se UE fyzicky odpojí od obsluhujícího AP. Jedná se o proaktivní mechanismus předání, na rozdíl od tradičního reaktivního přístupu break-before-make.

Architektonicky FT spoléhá na klíčové síťové entity definované ve specifikacích pro propojení 3GPP-WLAN, jako je brána přístupu k důvěryhodné WLAN ([TWAG](/mobilnisite/slovnik/twag/)) a server [AAA](/mobilnisite/slovnik/aaa/). Procedura typicky zahrnuje výměnu několika klíčových zpráv mezi UE, aktuálním AP (Current BSS), cílovým AP (Target BSS) a centrálním autentizačním serverem. Základní součástí je použití hierarchie klíčů odvozených z počáteční autentizace. UE a síť mohou vygenerovat párový hlavní klíč ([PMK](/mobilnisite/slovnik/pmk/)) nebo PMK pro rychlý přechod BSS (FT-PMK), který lze použít k rychlému navázání zabezpečeného spojení s cílovým AP bez nutnosti plné opakované [EAP](/mobilnisite/slovnik/eap/) autentizace, která je časově náročná.

Proces FT může fungovat v různých režimech: Over-the-Air (kde UE komunikuje přímo s cílovým AP), Over-the-DS (Distribution System, kde jsou zprávy přeposílány přes aktuální AP) a Rychlý přechod s rezervací prostředků (kde jsou QoS prostředky předem rezervovány). Proces je zahájen UE odesláním žádosti o přeřazení (reassociation request) obsahující FT autentizační materiál cílovému AP. Cílový AP, který potřebný bezpečnostní kontext předem získal nebo odvodil, může uživatelské zařízení ověřit a navázat spojení na linkové vrstvě téměř okamžitě. Celý tento proces handshake je navržen tak, aby byl dokončen během desítek milisekund, což jej činí vhodným pro hlasové a další aplikace citlivé na latenci. Rozsáhlý seznam specifikací (např. 24.502 pro politiky, 32.xxx pro správu) ukazuje na integraci FT do širších rámců správy sítě, účtování a řízení politik.

## K čemu slouží

Rychlý přechod [BSS](/mobilnisite/slovnik/bss/) (FT) byl vytvořen, aby řešil kritický problém přerušení služby během předávání spojení, zejména pro aplikace v reálném čase. V tradičních Wi-Fi sítích vyžadoval přesun mezi přístupovými body úplný proces deautentizace/reautentizace a přeřazení, což mohlo způsobit přerušení v řádu stovek milisekund – katastrofální pro VoIP hovory nebo živé streamování videa. FT to řeší oddělením časově náročného autentizačního procesu od samotné události fyzického přechodu.

Historická motivace vychází z rostoucí integrace Wi-Fi jako důvěryhodné přístupové sítě v rámci ekosystému 3GPP (např. v ANDSF, Hotspot 2.0 a později v 5G Access Traffic Steering, Switching and Splitting (ATSSS)). Když operátoři začali spoléhat na Wi-Fi pro odlehčení datového provozu (data offloading) a plynulé pokrytí, potřeba mobility na úrovni operátorských sítí se stala prvořadou. FT řeší omezení původních procedur předání IEEE 802.11, které nebyly navrženy s ohledem na rychlou, bezpečnou a operátorem řízenou mobilitu. Standardizací FT v rámci 3GPP se zajišťuje, že předání spojení mezi Wi-Fi přístupovými body může splňovat přísné požadavky mobilních operátorů na latenci a zabezpečení, a umožňuje tak skutečně plynulou mobilitu napříč heterogenními sítěmi.

## Klíčové vlastnosti

- Předběžná autentizace a předběžné navázání bezpečnostního kontextu v cílovém AP
- Více provozních režimů: Over-the-Air a Over-the-DS
- Využívá PMK pro rychlý přechod BSS (FT-PMK) pro rychlé odvozování klíčů
- Minimalizuje latenci předání spojení a ztrátu paketů pro služby v reálném čase
- Integrováno s infrastrukturou 3GPP AAA pro centralizovanou správu politik a zabezpečení
- Podporuje rezervaci prostředků a přenos kontextu QoS

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 32.332** (Rel-19) — Notification Log IRP Information Service
- **TS 32.336** (Rel-19) — Notification Log IRP Solution Set Definitions
- **TS 32.337** (Rel-9) — Notification Log IRP SOAP Solution Set
- **TS 32.341** (Rel-19) — File Transfer IRP Requirements
- **TS 32.343** (Rel-9) — File Transfer IRP CORBA Solution Set
- **TS 32.345** (Rel-9) — XML Definitions for File Transfer IRP
- **TS 32.346** (Rel-19) — File Transfer IRP Solution Set Definitions
- **TS 32.371** (Rel-19) — Security Management Concept & Requirements
- **TS 32.387** (Rel-9) — Partial Suspension of Itf-N IRP SOAP Solution Set
- **TS 32.411** (Rel-19) — PM IRP Requirements
- **TS 32.572** (Rel-19) — HNB/HeNB Type 2 Interface Concepts & Requirements

---

📖 **Anglický originál a plná specifikace:** [FT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ft/)
