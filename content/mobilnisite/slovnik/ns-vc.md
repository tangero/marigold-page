---
slug: "ns-vc"
url: "/mobilnisite/slovnik/ns-vc/"
type: "slovnik"
title: "NS-VC – Network Service Virtual Connection"
date: 2025-01-01
abbr: "NS-VC"
fullName: "Network Service Virtual Connection"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ns-vc/"
summary: "Logické spojení definované na rozhraní Iur-g mezi řadičem základnových stanic (BSC) a synchronizačním serverem BSS (NSS). Přenáší synchronizační informace, jako jsou data o časování a fázovém zarovnán"
---

NS-VC je logické spojení na rozhraní Iur-g mezi řadičem základnových stanic (BSC) a synchronizačním serverem BSS (NSS), které přenáší synchronizační informace, jako jsou časová data, aby zajistilo koordinovaný provoz rádiové přístupové sítě (RAN).

## Popis

Network Service Virtual Connection (NS-VC) je základní logická entita definovaná v rámci rozhraní Iur-g podle 3GPP, které propojuje řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a synchronizační server [BSS](/mobilnisite/slovnik/bss/) ([NSS](/mobilnisite/slovnik/nss/)). Funguje nad podkladovou transportní sítí, typicky využívající Asynchronous Transfer Mode ([ATM](/mobilnisite/slovnik/atm/)) nebo Internet Protocol (IP), jak je specifikováno v 3GPP TS 48.016. NS-VC není fyzický spoj, ale virtuální kanál zřízený pro přenos specifických synchronizačních signalizačních a datových toků. Jeho hlavní funkcí je přenos přesných informací o časování, hodinách a fázovém zarovnání ze synchronizačního serveru do řadiče základnových stanic, což je klíčové pro funkce jako koordinace předávání hovorů a snížení interference v sítích GSM a UMTS.

Architektonicky je NS-VC součástí vrstvy distribuce synchronizace v subsystému základnových stanic (BSS). Je identifikován jedinečným identifikátorem [NS-VCI](/mobilnisite/slovnik/ns-vci/) a je asociován s virtuálním spojením [NS-VL](/mobilnisite/slovnik/ns-vl/), které představuje agregační bod pro více takových spojení. NS-VC podporuje obousměrnou komunikaci, což umožňuje BSC jak přijímat synchronizační reference z NSS, tak potenciálně odesílat zpět stavové informace nebo požadavky. Vytváření, údržba a ukončování NS-VC jsou řízeny prostřednictvím protokolů řídicí roviny, což zajišťuje, že spojení je aktivní pouze tehdy, když je vyžadováno pro účely synchronizace.

V rámci sítě hraje NS-VC klíčovou roli při udržování celosíťové synchronizace, která je nezbytná pro systémy s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)), jako je GSM. Přesná synchronizace minimalizuje intersymbolovou interferenci, umožňuje efektivní předávání hovorů mezi buňkami a podporuje funkce jako synchronní paketový datový provoz. NS-VC zajišťuje, že časové informace jsou doručovány spolehlivě a s požadovanou kvalitou, jak je definováno parametry kvality služby synchronizace. Jeho provoz je transparentní vůči uživatelskému datovému provozu a zaměřuje se výhradně na řízení a distribuci synchronizačních signálů napříč infrastrukturou rádiové přístupové sítě.

## K čemu slouží

NS-VC byl zaveden, aby řešil kritickou potřebu přesné distribuce časování v sítích 2G a 3G, zejména pro systémy GSM a UMTS, které jsou závislé na synchronizovaných základnových stanicích. Před jeho standardizací byly synchronizační metody často proprietární nebo spoléhaly na fyzické linky pro distribuci hodin, které byly nákladné, nepružné a obtížně spravovatelné ve velkých, rozšiřujících se sítích. NS-VC poskytuje standardizovaný, virtualizovaný mechanismus pro přenos synchronizačních informací přes sdílené transportní sítě, čímž odděluje synchronizační logiku od fyzické konektivity.

Jeho vytvoření bylo motivováno vývojem směrem k pružnějším a škálovatelnějším rádiovým přístupovým sítím. Definováním virtuálního spojení přes běžné transportní technologie, jako jsou [ATM](/mobilnisite/slovnik/atm/) nebo IP, mohli operátoři využít stávající síťovou infrastrukturu pro distribuci synchronizace, čímž snížili kapitálové i provozní náklady. NS-VC řeší problém zajištění konzistentního časování napříč geograficky rozptýlenými základnovými stanicemi bez nutnosti vyhrazených synchronizačních sítí, což umožňuje funkce jako bezproblémové předávání hovorů a koordinovaný provoz více bodů, které jsou zásadní pro kvalitu služeb a efektivitu sítě.

Historicky se koncept NS-VC objevil s 3GPP Release 8 jako součást vylepšení rozhraní Iur-g pro lepší správu synchronizace BSS. Řešil omezení dřívějších, méně formalizovaných přístupů k synchronizaci tím, že poskytl jasnou, protokolem definovanou entitu pro přenos synchronizace, což usnadnilo interoperabilitu mezi zařízeními od různých dodavatelů a podpořilo přechod k paketovým transportním spojům.

## Klíčové vlastnosti

- Logické spojení pro přenos synchronizačních dat přes rozhraní Iur-g
- Funguje nad ATM nebo IP transportními sítěmi podle specifikací 3GPP
- Identifikováno jedinečným NS-VCI pro správu a směrování
- Podporuje obousměrnou komunikaci pro distribuci synchronizačních referencí a řízení
- Nezbytné pro udržování časového zarovnání TDMA v sítích GSM/UMTS
- Umožňuje spolehlivé doručování informací o hodinách a fázovém zarovnání

## Související pojmy

- [NS-VCI – Network Service Virtual Connection Identifier](/mobilnisite/slovnik/ns-vci/)
- [NS-VL – Network Service Virtual Link](/mobilnisite/slovnik/ns-vl/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NS-VC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-vc/)
