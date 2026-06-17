---
slug: "clns"
url: "/mobilnisite/slovnik/clns/"
type: "slovnik"
title: "CLNS – Connectionless Network Service"
date: 2025-01-01
abbr: "CLNS"
fullName: "Connectionless Network Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clns/"
summary: "CLNS je paketově přepínaná síťová služba, která přenáší data bez navázání vyhrazeného spojení typu end-to-end. Umožňuje efektivní přenos dat na vyžádání pro aplikace s přerušovaným provozem, jako byly"
---

CLNS je paketově přepínaná síťová služba, která přenáší data bez navázání vyhrazeného spojení, což umožňuje efektivní přenos na vyžádání pro aplikace jako rané mobilní datové služby v sítích GSM a UMTS.

## Popis

Connectionless Network Service (CLNS) je základní paketově přepínaná datová služba definovaná ve standardech 3GPP, primárně pro sítě GSM a UMTS. Funguje na modelu datagramů, kde je každá datová jednotka (paket) směrována ze zdroje k cíli nezávisle, bez předchozího vytvoření vyhrazené komunikační cesty nebo okruhu. To je v protikladu ke spojově orientovaným službám, které vyžadují fázi navázání pro rezervaci síťových prostředků. CLNS využívá podkladovou síťovou infrastrukturu k doručování paketů na základě adresních informací obsažených v hlavičce každého paketu, což umožňuje flexibilní a efektivní přenos dat.

Architektonicky je CLNS implementována v rámci Core Networku, konkrétně jako součást paketově přepínané (PS) domény. Rozhraní má s Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) a Gateway GPRS Support Node (GGSN) v sítích GPRS a UMTS. Služba na síťové vrstvě negarantuje doručení ve správném pořadí ani spolehlivost; tyto funkce, pokud jsou potřeba, zajišťují protokoly vyšších vrstev, jako je TCP. Z pohledu sítě je CLNS z podstaty bezstavová, pokud jde o jednotlivé toky paketů, což zjednodušuje návrh síťových uzlů a zlepšuje škálovatelnost pro obsluhu mnoha současných datových relací.

Z protokolového hlediska je CLNS v sítích 3GPP úzce spojena s GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) a IP transportem. Uživatelské datové pakety jsou zapouzdřeny v tunelech GTP mezi SGSN a GGSN, aby byla zajištěna mobilita a správa relací napříč core sítí. Služba podporuje různé profily Quality of Service (QoS), což operátorům umožňuje rozlišovat provoz podle parametrů, jako je priorita, zpoždění a spolehlivost. CLNS umožňuje základní mobilní datové služby, včetně přístupu k internetu, emailu a raných messagingových aplikací, tím, že poskytuje základní přenosovou kapacitu pro doručování IP paketů do mobilních zařízení a z nich.

CLNS hraje klíčovou roli v celkové architektuře datových služeb tím, že odděluje transportní mechanismus od aplikací, které jej využívají. Toto oddělení umožňuje více aplikacím a službám vyšších vrstev efektivně využívat stejný bezspojový přenosový kanál. Návrh služby klade důraz na minimální režii pro přerušované přenosy dat, což ji činí vhodnou pro trhaný charakter provozu typický pro mnohé rané mobilní datové aplikace. Její implementace v rámci standardů 3GPP zajistila interoperabilitu mezi síťovými zařízeními různých výrobců a poskytla standardizovaný základ pro vývoj mobilních paketových datových služeb.

## K čemu slouží

CLNS byla vytvořena, aby řešila potřebu efektivního a flexibilního přenosu dat v mobilních sítích, což přesahovalo limity tradičních spojově přepínaných služeb. Spojově přepínaná spojení, používaná primárně pro hlas, jsou neefektivní pro datové aplikace charakteristické přerušovaným, trhaným provozem, protože vyčleňují prostředky na celou dobu trvání relace bez ohledu na skutečnou datovou aktivitu. CLNS zavedla do GSM a UMTS paradigma paketového přepínání, což umožnilo statistické multiplexování uživatelských dat přes sdílené síťové prostředky, což výrazně zlepšilo využití šířky pásma a snížilo náklady pro operátory i uživatele.

Historický kontext CLNS spočívá v iniciativě z počátku 90. let 20. století přidat datové schopnosti do sítí GSM, která vyvrcholila standardizací General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)). Před GPRS byla mobilní data omezena na nízkorychlostní spojově přepínaná datová spojení nebo SMS. CLNS poskytla základní službu síťové vrstvy pro GPRS, což umožnilo mobilním stanicím odesílat a přijímat IP pakety na vyžádání. Toto byl klíčový krok v proměně mobilních telefonů z primárně hlasově orientovaných zařízení na platformy pro datové aplikace, což připravilo cestu pro mobilní přístup k internetu.

CLNS řešila klíčové problémy spojené s efektivitou využití prostředků a flexibilitou služeb. Odstranila potřebu dlouhých časů navazování spojení spojených s spojově přepínanými daty, což umožnilo 'always-on' konektivitu, kdy se zařízení jeví připojené k síti, ale spotřebovává prostředky pouze při aktivním odesílání nebo příjmu dat. Tento model lépe odpovídal interaktivní povaze vznikajících datových aplikací, jako je prohlížení webu a email. Navíc, díky své bezspojové povaze, služba zjednodušila správu sítě pro krátké datové transakce a podporovala širší škálu potenciálních aplikací bez nutnosti úprav základního transportního mechanismu.

## Klíčové vlastnosti

- Doručování paketů založené na datagramech bez předchozího navázání spojení
- Statistické multiplexování uživatelských dat přes sdílené síťové prostředky
- Podpora směrování a přeposílání IP paketů v rámci mobilní core sítě
- Integrace s prvky paketového core GPRS/UMTS (SGSN, GGSN) prostřednictvím GTP tunelování
- Schopnost podporovat diferencované QoS profily pro priorizaci provozu
- Základ pro 'always-on' konektivitu s efektivním využitím prostředků pro přerušovaný provoz

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [CLNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/clns/)
