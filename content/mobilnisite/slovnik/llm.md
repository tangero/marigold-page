---
slug: "llm"
url: "/mobilnisite/slovnik/llm/"
type: "slovnik"
title: "LLM – Logical Link Management"
date: 2025-01-01
abbr: "LLM"
fullName: "Logical Link Management"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/llm/"
summary: "Logical Link Management (LLM) je protokolová vrstva definovaná ve specifikacích 3GPP pro správu logických spojů v mobilních sítích, konkrétně v GPRS páteřní síti. Zajišťuje vytváření, udržování a uvol"
---

LLM je protokolová vrstva 3GPP pro správu vytváření, udržování a uvolňování logických spojů mezi síťovými entitami v GPRS páteřní síti za účelem zajištění spolehlivého přenosu dat.

## Popis

Logical Link Management (LLM) funguje jako podvrstva v rámci [GPRS](/mobilnisite/slovnik/gprs/) protokolového zásobníku, konkrétně mezi vrstvou Network Service ([NS](/mobilnisite/slovnik/ns/)) a vrstvou Radio Link Control/Medium Access Control ([RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)). Její primární funkcí je správa Logical Link Control ([LLC](/mobilnisite/slovnik/llc/)) spojení mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)). Protokol LLM je zodpovědný za vytváření, udržování, dohled a uvolňování těchto logických spojů, které jsou nezbytné pro přenos uživatelských dat a signalizačních zpráv. Řídí procedury jako aktivace, deaktivace a reset spojení, zajišťuje správnou synchronizaci a údržbu logických spojení i během událostí mobility, jako je převýběr buňky.

Architektonicky LLM úzce spolupracuje s protokoly GPRS Mobility Management ([GMM](/mobilnisite/slovnik/gmm/)) a Session Management (SM). Když se mobilní zařízení připojí k síti, LLM usnadňuje nastavení kontextu logického spoje, který zahrnuje parametry jako Temporary Logical Link Identity (TLLI) a profily kvality služby (QoS). Tento kontext je uložen jak v MS, tak v SGSN, což umožňuje konzistentní správu stavu. LLM také řídí mechanismy řízení toku a obnovy po chybě na úrovni logického spoje, ačkoli detailní opravu chyb typicky zajišťuje podkladová vrstva RLC. Protokol využívá specifické zprávy a procedury definované v 3GPP TS 44.064, včetně LLC rámců pro řízení a přenos dat.

Během provozu LLM zajišťuje, že více logických spojů může být multiplexováno přes jeden fyzický rádiový zdroj, čímž optimalizuje využití spektra. Podporuje různé provozní režimy, jako jsou režimy s potvrzením a bez potvrzení, v závislosti na požadavcích na spolehlivost přenášených dat. Například signalizační zprávy často používají režim s potvrzením pro zaručení doručení, zatímco některá uživatelská data mohou používat režim bez potvrzení pro nižší latenci. LLM také zajišťuje dohled nad spojením pomocí časovačů a čítačů, detekuje poruchy spojení a provádí jejich obnovu. Jeho integrace se sítí GPRS umožňuje plynulé předávání spojení a kontinuitu relací, což z něj činí základní komponentu pro paketové datové služby v sítích 2G a 3G.

## K čemu slouží

Logical Link Management (LLM) byl zaveden, aby řešil potřebu efektivní a spolehlivé správy logických spojení v paketově orientovaných mobilních sítích, konkrétně v systémech GPRS a později EGPRS. Před GPRS sítě s přepojováním okruhů, jako je GSM, řešily spojení prostřednictvím vyhrazených fyzických kanálů, což bylo pro přerušovaný datový provoz neefektivní. LLM umožňuje dynamickou alokaci a správu logických spojů přes sdílené rádiové zdroje, což dovoluje více uživatelům sdílet stejný fyzický kanál a zlepšuje spektrální účinnost. To bylo zásadní pro podporu raných mobilních datových služeb, jako je e-mail a prohlížení webu, které vyžadovaly flexibilní správu spojení bez nutnosti vyhrazených okruhů.

Vytvoření LLM bylo motivováno omezeními stávajících přístupů ke správě spojení v sítích s přepojováním okruhů, kterým chyběla pružnost pro paketová data. Poskytnutím protokolové vrstvy věnované řízení logických spojů LLM usnadňuje správu mobility, obnovu po chybě a diferenciaci QoS. Řeší problémy jako zpoždění při vytváření spojení, soupeření o zdroje a synchronizaci stavu během předávání spojení. Historicky vývoj LLM ve vydání 8 a jeho přetrvávání v pozdějších vydáních odráží jeho základní roli ve vývoji architektur paketového jádra, a to i při přechodu sítí na 3G a dále, kde byly podobné funkce adaptovány v různých protokolech.

## Klíčové vlastnosti

- Spravuje vytváření, udržování a uvolňování logických spojů mezi MS a SGSN
- Podporuje multiplexování více logických spojů přes jediné fyzické zdroje
- Poskytuje provozní režimy s potvrzením a bez potvrzení pro přenos dat
- Zajišťuje dohled nad spojením pomocí časovačů a mechanismů obnovy po chybě
- Integruje se s GMM a SM pro správu mobility a relací
- Používá TLLI pro identifikaci logického spoje a správu kontextu

## Související pojmy

- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [TLLI – Temporary Logical Link Identifier](/mobilnisite/slovnik/tlli/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LLM na 3GPP Explorer](https://3gpp-explorer.com/glossary/llm/)
