---
slug: "cbsp"
url: "/mobilnisite/slovnik/cbsp/"
type: "slovnik"
title: "CBSP – Cell Broadcast Service Protocol"
date: 2025-01-01
abbr: "CBSP"
fullName: "Cell Broadcast Service Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbsp/"
summary: "CBSP je protokol používaný v sítích 3GPP pro doručování zpráv Cell Broadcast, jako jsou výstrahy systému veřejného varování, na všechna zařízení v určité geografické oblasti. Funguje mezi centrem Cell"
---

CBSP je protokol 3GPP používaný mezi centrem Cell Broadcast Center a jádrovou sítí pro efektivní a spolehlivý přenos vysílacích zpráv, jako jsou výstrahy systému veřejného varování, na všechna zařízení v určité geografické oblasti.

## Popis

Cell Broadcast Service Protocol (CBSP) je klíčový protokol aplikační vrstvy definovaný v 3GPP TS 48.049. Umožňuje doručování zpráv Cell Broadcast ([CB](/mobilnisite/slovnik/cb/)) z centra Cell Broadcast Center ([CBC](/mobilnisite/slovnik/cbc/)) do uzlů jádrové sítě odpovědných za vysílání těchto zpráv přes rádiovou přístupovou síť. Hlavní funkcí protokolu je přenos požadavků typu write-replace warning, které obsahují obsah vysílací zprávy, informace o cílové geografické oblasti (definované seznamem buněk nebo oblastí sledování) a parametry plánování, jako je doba opakování a priorita. CBC používá CBSP k instruování jádrové sítě, aby zahájila, upravila nebo zastavila konkrétní vysílání v určených buňkách.

Z architektonického hlediska CBSP funguje nad spolehlivou transportní vrstvou, typicky využívá [SCTP](/mobilnisite/slovnik/sctp/) (Stream Control Transmission Protocol) pro své spojově orientované a spolehlivé přenosové charakteristiky, které jsou klíčové pro zajištění doručení kritických varovných zpráv. Protokol definuje konkrétní zprávy a procedury. Mezi klíčové zprávy patří Write-Replace Warning Request (z CBC do jádrové sítě), Write-Replace Warning Response (potvrzení z jádrové sítě) a Stop Warning Request/Response pro ukončení vysílání. Uzel jádrové sítě (např. Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G) přijme zprávu CBSP, zpracuje informace o cílové oblasti a přepošle instrukci k vysílání příslušným základnovým stanicím ([eNB](/mobilnisite/slovnik/enb/)/gNB) přes další rozhraní (jako S1-AP nebo [NGAP](/mobilnisite/slovnik/ngap/)).

Role CBSP je klíčová v architektuře služby Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)). Slouží jako standardizované, zabezpečené a řízené rozhraní, které odděluje servisní logiku a původ zpráv (zpracovávané CBC) od distribučního mechanismu vysílání sítě. Protokol zahrnuje mechanismy pro zpracování chyb, hlášení selhání a řízení zátěže, což zajišťuje, že systém dokáže elegantně zvládat zahlcení sítě nebo výpadky uzlů. Jeho návrh upřednostňuje spolehlivost a včasnost, protože je často používán pro život zachraňující výstrahy systému veřejného varování (PWS), kde musí být doručení zprávy zaručeno a okamžité v cílové oblasti, bez ohledu na aktuální zatížení sítě nebo počet připojených uživatelských zařízení.

## K čemu slouží

CBSP byl vytvořen za účelem standardizace a zlepšení mechanismu doručování zpráv Cell Broadcast v sítích 3GPP. Před jeho standardizací byly metody pro odesílání vysílacích výstrah často proprietární nebo méně efektivní. Protokol řeší problém, jak spolehlivě a rychle instruovat mobilní síť, aby vysílala konkrétní zprávu na všechna zařízení v definované skupině buněk, což je klíčové pro aplikace veřejné bezpečnosti, jako jsou výstrahy před zemětřesením, tsunami nebo AMBER výstrahy. Poskytuje jasné, interoperabilní rozhraní mezi původcem varovné zprávy (CBC) a síťovými elementy, které vysílání provádějí.

Historický kontext CBSP je zakořeněn v potřebě regulovaných celostátních systémů veřejného varování. Tradiční metody, jako je varování pomocí SMS, trpí během mimořádných událostí zahlcením sítě, protože jsou doručovány bod-bod. Služba Cell Broadcast je naopak službou bod-oblast, která těmito problémy zahlcení netrpí. CBSP byl zaveden, aby se tato vysílací schopnost stala standardizovanou, síťově integrovanou službou. Odstraňuje omezení předchozích nestandardizovaných implementací tím, že zajišťuje, že varovné zprávy mohou být vloženy do sítě s přesným geografickým cílením, plánováním a zaručenými mechanismy doručení, čímž se celý systém varování stává robustnějším, škálovatelnějším a spolehlivějším pro operátory a regulační orgány.

## Klíčové vlastnosti

- Standardizované rozhraní mezi CBC a jádrovou sítí (MME/AMF)
- Podporuje procedury Write-Replace Warning pro zahájení/aktualizaci vysílání
- Umožňuje geografické cílení pomocí seznamů buněk nebo oblastí sledování
- Zahrnuje parametry plánování zpráv (priorita, interval opakování)
- Poskytuje spolehlivý transport přes SCTP s ošetřením chyb a hlášením selhání
- Umožňuje jak nouzové služby systému veřejného varování (PWS), tak komerční služby Cell Broadcast

## Související pojmy

- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TS 48.049** (Rel-19) — Cell Broadcast Service Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CBSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbsp/)
