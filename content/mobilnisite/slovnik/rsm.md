---
slug: "rsm"
url: "/mobilnisite/slovnik/rsm/"
type: "slovnik"
title: "RSM – Reference Site Method"
date: 2025-01-01
abbr: "RSM"
fullName: "Reference Site Method"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rsm/"
summary: "Standardizovaná metodologie definovaná v 3GPP pro provádění testů rádiového výkonu uživatelského zařízení (UE) v řízeném laboratorním prostředí. Specifikuje použití referenčního simulátoru základnové"
---

RSM je standardizovaná 3GPP laboratorní metoda pro testování rádiového výkonu uživatelského zařízení (UE) za použití referenčního simulátoru základnové stanice a modelovaného prostředi šíření signálu, která zajišťuje konzistentní a opakovatelná měření.

## Popis

Metoda referenčního místa (Reference Site Method – RSM) je metodologie testování shody definovaná v technických specifikacích 3GPP, především v TS 38.113 pro NR (New Radio). Poskytuje rámec pro testování výkonu rádiového vysílání a příjmu uživatelského zařízení (UE) za standardizovaných, reprodukovatelných podmínek. Základní myšlenkou je nahradit proměnlivé reálné rádiové prostředí řízeným laboratorním uspořádáním zahrnujícím „referenční místo“ – simulovanou základnovou stanici (gNB) a definovaný model šíření rádiového signálu.

Z architektonického hlediska se testovací sestava RSM skládá z klíčových komponent: simulátoru základnové stanice ([BSS](/mobilnisite/slovnik/bss/)), který emuluje síťovou stranu (gNB) podle protokolů 3GPP, simulátoru rádiového kanálu, který modeluje podmínky šíření mezi BSS a UE, a testovaného UE. Simulátor rádiového kanálu implementuje specifické referenční prostředí šíření, které často zahrnuje útlum na dráze, vícecestné úniky (např. pomocí definovaného kanálového modelu jako [ETU](/mobilnisite/slovnik/etu/) nebo [EPA](/mobilnisite/slovnik/epa/)) a případně efekty mobility. Tím vzniká konzistentní „referenční místo“, které mohou všechny testovací laboratoře replikovat, což zajišťuje srovnatelnost měření výkonu UE bez ohledu na fyzickou polohu testovacího pracoviště.

Jak to funguje: Test provádí předdefinované testovací případy specifikované v 3GPP. BSS naváže spojení s UE a nakonfiguruje specifické rádiové podmínky (např. šířku pásma, modulaci, kanálový model). Poté vysílá referenční signály nebo datové pakety. Výkon UE je měřen proti kritériím, jako je maximální výstupní výkon, přesnost řízení výkonu, citlivost přijímače, demodulační výkon při únicích a propustnost. Měření se provádějí pomocí kalibrované aparatury připojené k anténním portům UE nebo přes řízené spojení s vyzařováním. Výsledky jsou porovnány s minimálními požadavky na výkon definovanými ve specifikaci.

Její role v síťovém ekosystému je zásadní pro zajištění kvality a interoperability UE. Poskytnutím standardizované testovací metody umožňuje RSM regulačním orgánům, certifikačním laboratořím a výrobcům jednotně posoudit, zda UE splňuje standardy 3GPP pro rádiový výkon. To zaručuje, že zařízení nasazená v reálných sítích budou spolehlivě fungovat za typických podmínek modelovaných referenčním prostředím. Je to klíčový nástroj pro typové schvalování, označení [CE](/mobilnisite/slovnik/ce/) a akceptační testy síťových operátorů, který zajišťuje, že široká škála produktů UE poskytuje konzistentní uživatelský zážitek a nepoškozuje výkon sítě.

## K čemu slouží

Metoda referenčního místa (RSM) existuje, aby vyřešila zásadní problém nekonzistentního a neopakovatelného testování rádiového výkonu UE. Před standardizovanými metodami, jako je RSM, mohli výrobci a testovací organizace používat proprietární sestavy s různými kanálovými modely, emulátory základnových stanic a měřicími technikami. To ztěžovalo objektivní srovnání výkonu UE, certifikaci zařízení pro globální trhy a zajištění jejich spolehlivého fungování v reálných sítích. Proměnlivost výsledků testů bránila interoperabilitě a kontrole kvality.

K jejímu vytvoření vedla potřeba společného technického základu pro testování shody, jak se mobilní technologie stávaly složitějšími. Se zavedením 3G, 4G a zejména 5G NR se rádiové požadavky zpřísnily (např. pro beamforming, široká pásma, nízkou latenci). Standardizovaná testovací metoda byla nezbytná k ověření, že UE tyto požadavky splňují. RSM poskytuje toto společné „referenční místo“, virtuální ekvivalent typického buňkového místa, který umožňuje všem stranám testovat proti stejnému etalonu.

RSM řeší omezení testování v reálném provozním prostředí, které je časově náročné, drahé a podléhá nekontrolovatelným proměnným prostředí (počasí, rušení, měnící se provoz). Přesunutím klíčových testů výkonu do laboratoře s řízeným referenčním prostředím umožňuje efektivní testování ve velkém objemu během vývoje a certifikace UE. Zajišťuje, že metriky výkonu, jako je výstupní výkon, citlivost přijímače a demodulace při únicích, jsou hodnoceny přesně a konzistentně, což vede k uvádění kvalitnějších zařízení na trh a spolehlivějšímu síťovému zážitku pro koncové uživatele.

## Klíčové vlastnosti

- Definuje standardizované laboratorní testovací prostředí využívající simulátor základnové stanice
- Specifikuje referenční modely rádiového kanálu pro šíření signálu (např. profily úniků)
- Poskytuje reprodukovatelné podmínky pro měření výkonu vysílače a přijímače UE
- Podporuje testování shody pro minimální rádiové požadavky definované v 3GPP
- Umožňuje konzistentní výsledky v různých testovacích laboratořích po celém světě
- Aplikovatelná na více technologií (NR, LTE) v rámci 3GPP

## Definující specifikace

- **TS 38.113** (Rel-19) — NR Base Station EMC Specification

---

📖 **Anglický originál a plná specifikace:** [RSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsm/)
