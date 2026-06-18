---
slug: "int-rnti"
url: "/mobilnisite/slovnik/int-rnti/"
type: "slovnik"
title: "INT-RNTI – Interruption RNTI"
date: 2025-01-01
abbr: "INT-RNTI"
fullName: "Interruption RNTI"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/int-rnti/"
summary: "INT-RNTI je dočasný identifikátor rádiové sítě používaný v 5G NR pro signalizaci přerušení uplinkových přenosů. Identifikuje UE, která potřebují pozastavit uplinkové přenosy pro měření nebo omezení in"
---

INT-RNTI je dočasný identifikátor rádiové sítě (Radio Network Temporary Identifier) používaný v 5G NR pro signalizaci přerušení uplinkových přenosů, který identifikuje UE, jež potřebují pozastavit přenosy pro měření nebo omezení interference.

## Popis

Interruption [RNTI](/mobilnisite/slovnik/rnti/) (INT-RNTI) je specifický typ dočasného identifikátoru rádiové sítě (Radio Network Temporary Identifier) přidělený stanicí gNB UE v 5G New Radio (NR). Slouží ke správě a signalizaci přerušení uplinkových přenosů, což jsou období, kdy musí UE dočasně zastavit své uplinkové přenosy. INT-RNTI je obsažen ve formátech řídicí informace pro downlink (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)), což umožňuje gNB efektivně přikázat více UE, aby přerušily uplinkové přenosy současně nebo koordinovaným způsobem. Tento identifikátor je klíčový pro scénáře vyžadující období ticha, jako je provádění měření správy rádiových zdrojů (Radio Resource Management, [RRM](/mobilnisite/slovnik/rrm/)), snímání pro sdílení spektra nebo omezení mezifázové interference v systémech s duplexem s časovým dělením (Time Division Duplex, [TDD](/mobilnisite/slovnik/tdd/)).

Operačně, když gNB potřebuje vytvořit okno přerušení, odešle DCI zakódované (scrambled) s INT-RNTI. UE monitorují [PDCCH](/mobilnisite/slovnik/pdcch/) pro tento RNTI a po jeho detekci interpretují DCI, aby určily načasování a délku požadovaného přerušení. DCI může specifikovat parametry jako počáteční symbol, délku a postiženou část šířky pásma (bandwidth part). Během přerušení UE zastaví uplinkové přenosy na indikovaných zdrojích, což umožní síti nebo jiným UE provádět měření bez interference. Mechanismus INT-RNTI podporuje dynamické a flexibilní plánování přerušení, které se přizpůsobuje podmínkám sítě v reálném čase.

Klíčové komponenty zahrnují proceduru přidělování RNTI, návrh formátu DCI (např. DCI formát 2_0 s indikací formátu slotu nebo jiné formáty vylepšené pro signalizaci přerušení) a specifikace chování UE. INT-RNTI hraje zásadní roli ve zlepšování využití spektra, umožňuje efektivní mechanismy koexistence ve sdílených a nelicencovaných pásmech ([NR-U](/mobilnisite/slovnik/nr-u/)) a zlepšuje výkon mobility díky přesným měřením sousedních buněk. Je nedílnou součástí pokročilých funkcí 5G, jako je dynamické sdílení spektra a ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), kde je zásadní přesné řízení časování.

## K čemu slouží

INT-RNTI byl zaveden v 5G NR, aby řešil potřebu řízených přerušení uplinkových přenosů v dynamických spektrálních prostředích. V dřívějších verzích byly mechanismy přerušení méně standardizované nebo spoléhaly na semistatické konfigurace, kterým chyběla flexibilita. S příchodem 5G a provozem ve sdíleném spektru (např. 3,5 GHz [CBRS](/mobilnisite/slovnik/cbrs/), nelicencovaná pásma 5 GHz/6 GHz) vznikla potřeba agilních a sítí koordinovaných období ticha pro usnadnění snímání, vyhýbání se interferencím a spravedlivé koexistence s jinými systémy, jako je Wi-Fi, nebo s původními uživateli pásma.

Primární problém, který řeší, je efektivní správa uplinkových přenosů, aby nebránily kritickým síťovým funkcím. Například v sítích TDD mohou uplinkové přenosy z jedné buňky interferovat s příjmem downlinku v buňkách sousedních. INT-RNTI umožňuje gNB rychle utlumit konkrétní UE, čímž omezuje mezifázovou interferenci. Dále podporuje vylepšená RRM měření pro mobilitu, protože nepřerušované uplinkové signály mohou maskovat referenční signály sousedních buněk. Poskytnutím standardizované signalizační metody založené na RNTI zajišťuje 3GPP spolehlivé a nízkolatentní řízení přerušení, což je nezbytné pro dosažení výkonnostních cílů 5G v různých scénářích nasazení.

## Klíčové vlastnosti

- Dynamická signalizace příkazů k přerušení uplinku prostřednictvím DCI
- Podpora skupinově společných přerušení cílících na více UE
- Konfigurovatelná délka přerušení a přidělování zdrojů
- Vylepšení pro koexistenci NR-U a sdílení spektra
- Integrace se správou mezifázové interference v TDD
- Řízení s nízkou latencí pro URLLC a měřicí mezery

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [INT-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/int-rnti/)
