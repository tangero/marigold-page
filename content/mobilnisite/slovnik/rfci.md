---
slug: "rfci"
url: "/mobilnisite/slovnik/rfci/"
type: "slovnik"
title: "RFCI – RFC Indicator"
date: 2025-01-01
abbr: "RFCI"
fullName: "RFC Indicator"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rfci/"
summary: "RFC Indicator (RFCI) je parametr používaný k identifikaci konkrétní konfigurace rádiového přístupového přenosového kanálu (RAB) nebo rádiového přenosového kanálu (RB) v sítích 3GPP. Signalizuje sadu k"
---

RFCI je parametr identifikující konkrétní konfiguraci rádiového přenosového kanálu (Radio Bearer), signalizující transportní formáty a charakteristiky mezi sítí a zařízením za účelem zajištění konzistentního zpracování dat během nastavování přenosového kanálu.

## Popis

[RFC](/mobilnisite/slovnik/rfc/) Indicator (RFCI) je klíčový parametr v rádiové přístupové síti (RAN) 3GPP, konkrétně v kontextu rozhraní Iu a Iub pro UMTS a vyvinutý [UTRAN](/mobilnisite/slovnik/utran/). Funguje jako index nebo štítek, který jednoznačně identifikuje předem definovanou sadu kombinací transportních formátů pro rádiový přístupový přenosový kanál ([RAB](/mobilnisite/slovnik/rab/)) nebo rádiový přenosový kanál ([RB](/mobilnisite/slovnik/rb/)). RFCI je komunikován mezi řadičem rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) a uživatelským zařízením (UE) během procedur přiřazení nebo rekonfigurace RAB. V podstatě odkazuje na konkrétní řádek v tabulce sady kombinací transportních formátů ([TFCS](/mobilnisite/slovnik/tfcs/)), která definuje přípustné kombinace transportních formátů pro vyhrazené transportní kanály ([DCH](/mobilnisite/slovnik/dch/)) asociované s daným přenosovým kanálem. Tato tabulka zahrnuje parametry jako velikost transportního bloku, přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)) a schéma kódování kanálu.

Architektonicky je RFCI součástí definic služby rádiového přístupového přenosového kanálu (RABs) a služby rádiového přenosového kanálu (RBs), kterými spravuje protokol řízení rádiových zdrojů (RRC). Když RNC zřizuje přenosový kanál pro uživatelskou relaci, vybere vhodný RFCI na základě požadovaného profilu QoS (např. datový tok, tolerance zpoždění). Tato hodnota RFCI je následně odeslána do UE v rámci signalizačních zpráv RRC, jako jsou RADIO BEARER SETUP nebo RADIO BEARER RECONFIGURATION. UE používá přijatý RFCI k nalezení odpovídající sady kombinací transportních formátů ve své konfiguraci, čímž sladí své zpracování na fyzické a MAC vrstvě s očekáváními sítě.

Úlohou parametru je oddělit podrobné a rozsáhlé informace o transportních formátech od častých signalizačních zpráv. Namísto opakovaného přenosu celé tabulky TFCS je vyměňován pouze kompaktní index RFCI, což výrazně snižuje signalizační režii. Tato efektivita je klíčová pro události mobility, jako jsou předávání hovoru nebo změny služeb, kde musí být přenosové kanály rychle rekonfigurovány. RFCI zajišťuje, že oba konce rádiového spoje mají synchronizované porozumění o tom, jak jsou datové bloky formátovány, velikostně nastaveny a načasovány pro přenos, což je základní pro spolehlivý přenos dat a optimalizaci rádiových zdrojů. Jeho definice pokrývá více specifikací 3GPP, včetně těch, které detailně popisují RANAP (25.413), uživatelskou rovinu rozhraní Iu (25.415) a specifikace kodeků (26.102, 26.202, 26.454), kde souvisí s konfigurací transportu pro hlasová a multimediální data.

## K čemu slouží

RFCI bylo zavedeno, aby vyřešilo problém signalizační efektivity a jednoznačné konfigurace přenosového kanálu v sítích 3G UMTS. Před jeho standardizací by předávání kompletní sady transportních formátů pro přenosový kanál během jeho nastavování nebo rekonfigurace vyžadovalo přenos rozsáhlých a komplexních sad parametrů přes rozhraní vzduchu a mezi síťovými uzly. To by spotřebovávalo cenné rádiové zdroje a prodlužovalo časy navazování hovoru, což by negativně ovlivnilo uživatelský zážitek a kapacitu sítě.

Jeho vytvoření bylo motivováno potřebou škálovatelného a flexibilního mechanismu pro podporu široké škály služeb s různými požadavky na QoS, od hlasových hovorů po paketově přepínaná data. Použitím indikátoru může síť předem definovat a spravovat knihovny kombinací transportních formátů vhodných pro různé typy služeb. RFCI umožňuje jádru sítě a RNC požadovat přenosový kanál se specifickými charakteristikami a RNC rychle nařídit UE, aby použilo odpovídající předem dohodnutou konfiguraci. Tato vrstva abstrakce je klíčová pro dynamické řízení zdrojů a umožňuje funkce jako změny rychlosti adaptivního vícerychlostního (AMR) kodeku nebo přepínání mezi konverzačními a streamovacími typy přenosových kanálů bez vyčerpávajícího opětovného signalizování.

## Klíčové vlastnosti

- Jednoznačně identifikuje sadu kombinací transportních formátů (TFCS) pro RAB/RB
- Snižuje signalizační režii tím, že funguje jako kompaktní index namísto přenosu plných sad parametrů
- Umožňuje synchronizovanou konfiguraci mezi RNC a UE pro spolehlivý přenos dat
- Podporuje dynamickou rekonfiguraci přenosového kanálu během procedur předávání hovoru a změny služby
- Integrální součást zpráv protokolu RRC pro správu rádiových přenosových kanálů
- Definován ve spojení se specifikacemi kodeků, aby zajistil správný transport médií

## Definující specifikace

- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks

---

📖 **Anglický originál a plná specifikace:** [RFCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfci/)
