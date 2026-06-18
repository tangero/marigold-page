---
slug: "quic"
url: "/mobilnisite/slovnik/quic/"
type: "slovnik"
title: "QUIC – Quick UDP Internet Connections"
date: 2026-01-01
abbr: "QUIC"
fullName: "Quick UDP Internet Connections"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/quic/"
summary: "QUIC je síťový protokol transportní vrstvy standardizovaný IETF a přijatý 3GPP. Funguje nad UDP, poskytuje sníženou latenci spojení a transportu, vylepšené zabezpečení s povinným TLS 1.3 a multiplexov"
---

QUIC je standardizovaný transportní protokol pracující nad UDP, navržený ke snížení latence spojení a zlepšení zabezpečení a multiplexního doručování dat pro zvýšený výkon aplikací v mobilních sítích.

## Popis

Quick [UDP](/mobilnisite/slovnik/udp/) Internet Connections (QUIC) je moderní protokol transportní vrstvy, původně vyvinutý společností Google a později standardizovaný [IETF](/mobilnisite/slovnik/ietf/). V architektuře 3GPP je jeho přijetí specifikováno pro umožnění efektivní přepravy dat mezi uživatelským zařízením (UE), 5G jádrem sítě (5GC) a aplikačními servery. Na rozdíl od tradičního zásobníku TCP/[TLS](/mobilnisite/slovnik/tls/) integruje QUIC kryptografické handshake a transportní mechanismy do jediné protokolové vrstvy a funguje nad UDP. Tento návrh se vyhýbá problému blokování hlavy fronty, který je přítomen v TCP, tím, že umožňuje více nezávislých toků v rámci jednoho spojení. Každý tok může být doručován nezávisle, takže ztráta paketu na jednom toku nezastaví doručování dat na ostatních.

Činnost protokolu začíná handshake, který kombinuje navázání spojení a výměnu kryptografických klíčů, což významně snižuje počáteční latenci spojení ve srovnání s sekvenčním TCP handshake a TLS vyjednáváním. QUIC spojení jsou identifikována ID spojení, což je činí odolnými vůči změnám v podkladové síťové adrese, což je zvláště výhodné pro mobilní zařízení procházející předáváním. Všechny QUIC pakety jsou autentizovány a šifrovány, včetně většiny hlavičkových informací, což ve výchozím nastavení poskytuje silné zabezpečení a soukromí a zmírňuje osifikaci a zásahy middleboxů.

V systému 3GPP je QUIC využíván pro specifická rozhraní založená na službách a optimalizace uživatelské roviny. Specifikace podrobně popisují jeho použití pro protokoly jako [HTTP](/mobilnisite/slovnik/http/)/3, což umožňuje efektivnější webový provoz. 5G jádro může využít QUIC pro komunikaci mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) přes rozhraní založená na službách, kde jeho nízkolatentní navazování spojení a vylepšené řízení zahlcení mohou zvýšit odezivost síťové signalizace. Pro uživatelskou rovinu může QUIC přenášet aplikační data a nabízet výhody pro služby citlivé na latenci, jako je hraní her v reálném čase, videokonference a streamování s nízkou latencí, minimalizací dob odezvy a zlepšením výkonu na ztrátových nebo proměnných sítích.

## K čemu slouží

QUIC byl vytvořen, aby řešil základní výkonnostní a bezpečnostní omezení tradičního zásobníku protokolů TCP/[TLS](/mobilnisite/slovnik/tls/), který tvoří základ velké části internetu. Primární motivací bylo snížení latence, která je klíčová pro moderní interaktivní webové aplikace, mobilní služby a komunikaci v reálném čase. Sekvenční povaha navázání TCP spojení a TLS bezpečnostního vyjednávání zavádí před odesláním aplikačních dat více zpoždění způsobených cestou tam a zpět. Pro mobilní uživatele v celulárních sítích, kde mohou být doby odezvy vysoké a proměnlivé, je tato latence znásobena a zhoršuje uživatelský zážitek.

Navíc inherentní blokování hlavy fronty v TCP, kdy jediný ztracený paket zastaví tok dat celého spojení, není vhodné pro multiplexovaný provoz [HTTP](/mobilnisite/slovnik/http/)/2. QUIC to řeší implementací multiplexování na transportní vrstvě s nezávislými toky. Jeho použití [UDP](/mobilnisite/slovnik/udp/) také umožňuje rychlejší inovace v algoritmech řízení zahlcení bez nutnosti aktualizací jádra, protože je implementován v uživatelském prostoru. Z hlediska zabezpečení a soukromí povinné šifrování téměř všech polí paketu v QUIC zabraňuje pasivnímu sledování a manipulaci middleboxy a řeší tak rostoucí obavy z osifikace a sledování na internetu.

Integrace QUIC v 3GPP, počínaje Release 18, je hnána potřebou optimalizovat výkon systému 5G pro širokou škálu služeb, včetně vylepšeného mobilního širokopásmového připojení (eMBB) a ultra-spolehlivých komunikací s nízkou latencí (URLLC). Přijetím moderního, efektivního transportního protokolu mohou sítě 3GPP lépe podporovat náročné požadavky budoucích aplikací, snížit doby načítání, zlepšit kvalitu videostreamování a poskytnout robustnější základ pro vyvíjející se ekosystém internetových protokolů v mobilní doméně.

## Klíčové vlastnosti

- Snížená latence navázání spojení díky kombinovanému kryptografickému a transportnímu handshake
- Eliminace blokování hlavy fronty prostřednictvím multiplexovaných nezávislých toků
- Odolnost vůči migraci spojení pomocí ID spojení nezávislých na síťových adresách
- Povinné šifrování a autentizace pro téměř všechny hlavičky a datové části paketů
- Vylepšená flexibilita řízení zahlcení implementovaná v uživatelském prostoru
- Nativní podpora pro obnovení dat s 0-RTT a 1-RTT pro následná spojení

## Související pojmy

- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [QUIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/quic/)
