---
slug: "shr"
url: "/mobilnisite/slovnik/shr/"
type: "slovnik"
title: "SHR – Successful Handover Report"
date: 2026-01-01
abbr: "SHR"
fullName: "Successful Handover Report"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/shr/"
summary: "Successful Handover Report (SHR) je mechanismus pro sběr dat a vytváření hlášení zavedený v 5G. Poskytuje podrobné informace o dokončeném postupu předání spojení (handover) z cílového základnového uzl"
---

SHR je datová zpráva v sítích 5G, kterou cílový základnový uzel zasílá zdrojovému uzlu a která poskytuje podrobné informace o dokončeném předání spojení pro optimalizaci sítě a řešení problémů.

## Popis

Successful Handover Report (SHR) je klíčovým prvkem pro pokročilé řízení mobility a funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) v 5G NR a vyvinutých sítích LTE. Jedná se o strukturovanou zprávu, kterou vygeneruje cílový uzel (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) po úspěšném dokončení předání spojení a odešle ji zpět uzlu zdrojovému. Na rozdíl od základních signálů o dokončení handoveru obsahuje SHR bohatou sadu kontextových dat o rádiových podmínkách a konfiguraci v okamžiku provedení předání. Tato zpráva je definována v rámci protokolů Xn Application Protocol (XnAP) a [NG](/mobilnisite/slovnik/ng/) Application Protocol ([NGAP](/mobilnisite/slovnik/ngap/)) pro komunikaci mezi gNB a mezi systémy, jak je uvedeno v technických specifikacích jako TS 38.423 a TS 38.413.

Obsah hlášení je komplexní. Typicky zahrnuje Cell Radio Network Temporary Identifier ([C-RNTI](/mobilnisite/slovnik/c-rnti/)) přidělený uživatelskému zařízení (UE) v cílové buňce, podrobné výsledky měření hlášené UE těsně před předáním spojení (např. Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)), Reference Signal Received Quality ([RSRQ](/mobilnisite/slovnik/rsrq/))) a konkrétní konfiguraci rádiových přenosových kanálů, které byly úspěšně zřízeny. Dále může obsahovat časová razítka a identifikátory konkrétního příkazu k předání spojení. Tato detailní data umožňují zdrojovému uzlu vytvářet historický záznam výsledků předání spojení korelovaný s rádiovými podmínkami, které vedly k rozhodnutí o handoveru.

Z architektonického hlediska proudí SHR přes rozhraní Xn mezi gNB nebo přes rozhraní NG mezi eNB a 5GC. Jeho generování a využití jsou nedílnou součástí algoritmů pro optimalizaci robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)). Analýzou sekvencí SHR (a jejich protějšku, Handover Failure Report) může síť detekovat problémy, jako jsou příliš časná, příliš pozdní nebo předání spojení do nesprávné buňky. Zdrojový uzel pak může automatizovaně nebo poloautomatizovaně upravit své řídicí parametry handoveru, jako jsou hysterezní okraje, doba do spuštění (time-to-trigger) nebo individuální posuny buňky (cell individual offsets). Tato optimalizace v uzavřené smyčce je klíčová pro udržení plynulé mobility v hustých, heterogenních nasazeních 5G s komplexními scénáři rušení.

## K čemu slouží

SHR byl zaveden, aby řešil omezení dřívějších systémů řízení mobility, které se často spoléhaly na zjednodušené indikátory úspěchu/neúspěchu nebo vyžadovaly rozsáhlý drive-testing a manuální analýzu pro optimalizaci parametrů handoveru. V 4G LTE začaly funkce SON automatizovat optimalizaci, ale výměna dat byla často méně podrobná. Nástup 5G s využitím vyšších frekvencí (mmWave), ultra-hustých sítí a náročných případů užití, jako je ultra-spolehlivá nízkolatenční komunikace (URLLC), vytvořil naléhavou potřebu inteligentnějšího a daty řízeného řízení mobility.

Hlavním problémem, který SHR řeší, je nedostatek přehledu zdrojového uzlu o *výsledku* jeho rozhodnutí o předání spojení. Před zavedením SHR zdrojový ulez nařídil handover a mohl obdržet potvrzení o dokončení, ale nikoli podrobný kontext *proč* byl úspěšný právě za těch konkrétních rádiových podmínek. To činilo řešení suboptimálních handoverů a ladění algoritmů neefektivní. SHR poskytuje tuto zásadní zpětnou vazbu, což umožňuje zdrojovému uzlu učit se z každé události předání spojení. Jeho vytvoření bylo motivováno snahou posílit schopnosti SON, snížit provozní náklady (OPEX) minimalizací manuální optimalizace a zásadně zlepšit robustnost mobility – což je kritický faktor pro uživatelský komfort a výkon sítě v pokročilých systémech 5G.

## Klíčové vlastnosti

- Zpětná hlášení po provedení handoveru od cílového uzlu ke zdrojovému
- Obsahuje podrobná měřicí data z UE z doby těsně před provedením handoveru
- Zahrnuje potvrzení o úspěšném zřízení rádiových přenosových kanálů a jejich konfiguraci
- Přenášeno přes rozhraní Xn (mezi gNB) nebo NG (mezi různými RAT)
- Primární zdroj dat pro algoritmy optimalizace robustnosti mobility (MRO)
- Umožňuje uzavřenou smyčku a daty řízené nastavování řídicích parametrů handoveru

## Související pojmy

- [MRO – Mobility Robustness Optimisation](/mobilnisite/slovnik/mro/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [SHR na 3GPP Explorer](https://3gpp-explorer.com/glossary/shr/)
