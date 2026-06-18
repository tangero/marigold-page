---
slug: "info"
url: "/mobilnisite/slovnik/info/"
type: "slovnik"
title: "INFO – Information"
date: 2025-01-01
abbr: "INFO"
fullName: "Information"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/info/"
summary: "INFO je obecný název pole používaný ve specifikacích 3GPP pro označení informačního prvku nebo datového kontejneru. Slouží jako zástupný symbol pro přenos různých typů dat v rámci protokolových zpráv,"
---

INFO je obecný název pole používaný ve specifikacích 3GPP pro označení informačního prvku nebo datového kontejneru pro přenos různých typů dat v rámci protokolových zpráv.

## Popis

Ve specifikacích 3GPP je INFO základní název pole používaný v rámci protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) a informačních prvků ([IE](/mobilnisite/slovnik/ie/)) pro zapouzdření konkrétních datových nákladů. Působí jako kontejner nebo zástupný symbol v rámci struktur zpráv definovaných v technických specifikacích, například pro signalizaci řídicí roviny nebo přenos dat uživatelské roviny. Skutečný obsah a formát pole INFO závisí na kontextu a je definován konkrétním protokolem nebo procedurou, ve které je použito. Například ve specifikaci 37.462, která pokrývá LTE Positioning Protocol A (LPPa), mohou pole INFO přenášet data související s určováním polohy, jako jsou měření nebo asistenční informace mezi Evolved Node B ([eNB](/mobilnisite/slovnik/enb/)) a Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)). Pole je navrženo jako flexibilní, což mu umožňuje přenášet různé datové typy, včetně binárních dat, kódovaných parametrů nebo vnořených struktur, podle požadavků síťové funkce. Jeho použití zajišťuje, že protokolové zprávy mohou být v budoucích vydáních rozšířeny nebo upraveny bez nutnosti přepracování celého formátu zprávy, což podporuje zpětnou kompatibilitu a efektivní vývoj sítě. V praxi je pole INFO analyzováno a interpretováno přijímající entitou na základě typu zprávy a souvisejících protokolových specifikací, což umožňuje přesnou výměnu dat klíčovou pro síťové operace, jako je správa mobility, správa relací nebo poskytování služeb.

## K čemu slouží

Pole INFO existuje za účelem poskytnutí standardizovaného a rozšiřitelného mechanismu pro přenos proměnných nebo složitých dat v rámci protokolových zpráv 3GPP. V telekomunikačních sítích musí protokoly zpracovávat různé typy informací – od identifikátorů uživatelů po parametry služeb – bez rigidních struktur zpráv, které by mohly omezit budoucí vylepšení. Před zavedením takových obecných polí protokoly často používaly pevné formáty, což ztěžovalo zavádění nových datových prvků bez narušení kompatibility. Pole INFO tento problém řeší tím, že funguje jako flexibilní kontejner, umožňující specifikacím definovat konkrétní obsah pro každý případ použití při zachování konzistentního rámce zprávy. Tento návrh podporuje dynamickou povahu mobilních sítí, kde jsou průběžně přidávány nové služby a funkce napříč vydáními. Zjednodušuje návrh protokolu tím, že snižuje potřebu četných specializovaných polí, zefektivňuje implementaci a zajišťuje, že se sítě mohou efektivně vyvíjet od vydání 8 (Release 8) dále.

## Klíčové vlastnosti

- Obecný datový kontejner v rámci protokolových zpráv
- Obsah závislý na kontextu definovaný konkrétními specifikacemi
- Podporuje flexibilitu a rozšiřitelnost signalizace
- Umožňuje zpětnou kompatibilitu napříč vydáními 3GPP
- Používá se pro výměnu dat řídicí i uživatelské roviny
- Umožňuje zapouzdření binárních nebo kódovaných parametrů

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [INFO na 3GPP Explorer](https://3gpp-explorer.com/glossary/info/)
