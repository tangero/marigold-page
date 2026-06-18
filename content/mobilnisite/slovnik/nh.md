---
slug: "nh"
url: "/mobilnisite/slovnik/nh/"
type: "slovnik"
title: "NH – Next Hop key"
date: 2025-01-01
abbr: "NH"
fullName: "Next Hop key"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nh/"
summary: "Bezpečnostní klíč používaný v 3GPP sítích pro zajištění dopředné bezpečnosti během předávání spojení. Je odvozen z aktuálního klíče K_ASME nebo kotvového klíče a slouží k vytvoření následných klíčů př"
---

NH je klíč pro dopřednou bezpečnost odvozený z kotvového klíče za účelem generování nových klíčů přístupové vrstvy pro cílovou základnovou stanici při předávání spojení, čímž chrání budoucí relace v sítích LTE a 5G.

## Popis

Klíč Next Hop (NH) je klíčovou součástí hierarchie klíčů 3GPP, konkrétně navrženou pro zajištění dopředné bezpečnosti přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) během předávání spojení uvnitř jednoho [RAT](/mobilnisite/slovnik/rat/) i mezi různými RAT. Funguje v rámci horizontálního rámce odvozování klíčů definovaného v TS 33.401. Klíč NH se nepoužívá přímo pro šifrování nebo ochranu integrity uživatelských či signalizačních dat. Místo toho slouží jako nadřazený klíč, ze kterého je během procedury předávání spojení odvozen klíč KeNB* (v LTE) nebo KgNB* (v 5G NR) cílové stanice eNodeB/gNodeB. Při odvozování se používá čítač řetězení NH ([NCC](/mobilnisite/slovnik/ncc/)), který je synchronizován mezi UE a sítí, a fyzické ID buňky ([PCI](/mobilnisite/slovnik/pci/)) cílové buňky. Tento proces zajišťuje, že nový základní klíč AS je kryptograficky čerstvý a nelze jej přímo spojit s předchozími klíči.

Generování nového klíče NH je spuštěno specifickými událostmi správy bezpečnostního kontextu, nejvýznamněji předáním spojení uvnitř buňky, kdy je klíč KeNB/KgNB aktualizován pomocí vertikální metody odvozování klíčů (s využitím [NAS](/mobilnisite/slovnik/nas/) uplink COUNT). Když k tomuto vertikálnímu odvození dojde, síť také vypočítá nový parametr NH a inkrementuje NCC. Tento nový klíč NH je pak uložen jak UE, tak [MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/) pro budoucí použití. Během dalšího předávání spojení, které může využít horizontální odvození (např. předávání přes [X2](/mobilnisite/slovnik/x2/) v LTE), poskytne zdrojová stanice eNodeB cílové stanici eNodeB parametr NH a hodnotu NCC. Cílová stanice eNodeB a UE pak mohou nezávisle odvodit stejný nový klíč KeNB* za použití tohoto klíče NH, NCC a PCI cílové buňky, aniž by bylo potřeba zapojovat jádro sítě (MME/AMF) do generování klíče.

Tato architektura odděluje správu klíčů pro předávání od jádra sítě pro následné kroky, což významně snižuje latenci předávání a signalizační zátěž. Mechanismus řetězení NH zajišťuje dopřednou bezpečnost: i když útočník získá aktuální klíč KeNB/KgNB, nemůže vypočítat budoucí klíče NH ani klíče KeNB/KgNB použité poté, co došlo k vertikálnímu odvození klíče, protože klíč NH je odvozen z kotvového klíče (K_ASME) pomocí jednosměrné funkce. NCC funguje jako pořadové číslo, které zajišťuje, že se UE a síť shodnou na tom, který klíč NH v řetězci použít, čímž se předchází útokům typu replay a problémům se synchronizací. Paradigma NH je tedy klíčové pro umožnění bezpečné, rychlé a škálovatelné mobility v 3GPP sítích.

## K čemu slouží

Klíč NH byl zaveden, aby vyřešil kritické bezpečnostní a výkonnostní výzvy při předávání spojení v celulárních sítích, zejména s příchodem LTE a jeho plošší architektury. Před LTE byla bezpečnost předávání v UMTS více závislá na zapojení jádra sítě. Mezi cíle návrhu LTE patřilo snížení latence předávání a signalizace řídicí roviny, aby bylo možné podporovat plynulou mobilitu pro vysokorychlostní uživatele a služby v reálném čase. Byl potřeba bezpečnostní mechanismus, který by umožnil zdrojové základnové stanici bezpečně připravit cílovou základnovou stanici, aniž by se musela vždy dotazovat jádra sítě na nové klíče, protože by to přidalo zpoždění.

Hlavní problém, který klíč NH řeší, je zajištění dopředné bezpečnosti pro klíče přístupové vrstvy během sekvence předání spojení. Bez takového mechanismu, pokud by byl klíč používaný na jedné základnové stanici prozrazen, mohl by útočník odvodit všechny budoucí relakční klíče, čímž by prolomil bezpečnost celé mobilní cesty uživatele. Koncept řetězení NH vytváří pro každý nový krok předání spojení po aktualizaci klíče ověřené jádrem sítě kryptograficky nezávislý klíč, čímž omezuje dopad prozrazení klíče. Řeší také výkonnostní problém tím, že umožňuje 'horizontální' odvozování klíčů, kdy si zdrojová a cílová základnová stanice mohou lokálně spravovat přechody klíčů pomocí předem sdílených parametrů NH, přičemž pouze periodicky vyžadují 'vertikální' obnovení klíče z kotvového klíče jádra sítě. Tento vyvážený přístup optimalizuje jak bezpečnost, tak efektivitu sítě.

## Klíčové vlastnosti

- Umožňuje dopřednou bezpečnost pro klíče přístupové vrstvy (AS) během předávání spojení
- Podporuje horizontální odvozování klíčů (mezi základnovými stanicemi) nezávislé na jádru sítě
- Využívá čítač řetězení NH (NCC) pro synchronizaci mezi UE a sítí
- Odvozen z kotvového bezpečnostního klíče (K_ASME nebo ekvivalentního) během vertikálních aktualizací klíčů
- Používá se k vygenerování klíče KeNB (LTE) nebo KgNB (5G NR) pro cílovou buňku
- Snižuje latenci předávání spojení a signalizační zátěž jádra sítě

## Související pojmy

- [NCC – Network (PLMN) Colour Code](/mobilnisite/slovnik/ncc/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [NH na 3GPP Explorer](https://3gpp-explorer.com/glossary/nh/)
