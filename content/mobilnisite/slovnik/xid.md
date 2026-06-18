---
slug: "xid"
url: "/mobilnisite/slovnik/xid/"
type: "slovnik"
title: "XID – Exchange Identification frame"
date: 2025-01-01
abbr: "XID"
fullName: "Exchange Identification frame"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/xid/"
summary: "Rámec Exchange Identification (XID) je řídicí rámec používaný v protokolech vrstvy datového spoje, jako jsou ty založené na HDLC, k vyjednání a výměně konfiguračních parametrů mezi dvěma propojenými e"
---

XID je řídicí rámec používaný v legacy okruhově přepínaných datových službách 3GPP k vyjednání a výměně parametrů konfigurace spoje mezi dvěma entitami před přenosem dat.

## Popis

Rámec Exchange Identification (XID) je základní řídicí rámec používaný v protokolech vrstvy datového spoje odvozených od High-Level Data Link Control ([HDLC](/mobilnisite/slovnik/hdlc/)). Ve specifikacích 3GPP, zejména TS 24.022 (Radio Link Protocol) a TS 37.462 (F1 application protocol), slouží rámec XID jako mechanismus, který umožňuje dvěma partnerským entitám vyměnit si a vyjednat provozní parametry datového spojení před zahájením přenosu uživatelských dat. Struktura rámce typicky obsahuje pole pro identifikaci typu rámce jako XID a informační pole obsahující jeden nebo více parametrů k vyjednání.

Provozně je výměna XID součástí fáze navázání nebo inicializace spoje. Když je datové spojení nastavováno – například mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí pro okruhově přepínaná data, nebo mezi centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)) a distribuovanou jednotkou ([DU](/mobilnisite/slovnik/du/)) v 5G RAN přes rozhraní F1 – jedna strana odešle XID příkazový rámec. Tento rámec navrhuje hodnoty konfigurovatelných parametrů, jako je velikost okna (počet rámců, které lze odeslat bez potvrzení), maximální délka rámce, časovače pro opakovaný přenos a verze používaného protokolu. Přijímající entita odpoví XID odpovědním rámcem, který buď navržené parametry přijme, nebo navrhne alternativy, což vede k vyjednávání, dokud se obě strany nedohodnou na kompatibilní sadě.

Jeho úloha v síti spočívá v zajištění spolehlivého a efektivního provozu datového spoje sladěním možností a očekávání dvou komunikujících partnerů. Dynamickým vyjednáváním parametrů lze spoj optimalizovat pro konkrétní podmínky a požadavky relace, což je flexibilnější než použití statických, předem nastavených hodnot. V kontextu TS 24.022 je toto klíčové pro Radio Link Protocol ([RLP](/mobilnisite/slovnik/rlp/)) používaný v legacy okruhově přepínaných datových službách GSM a UMTS, který poskytuje opravovaný datový proud přes rozhraní rádiového přenosu. V modernějším kontextu TS 37.462 mohou být XID rámce součástí inicializace F1 application protocol ([F1AP](/mobilnisite/slovnik/f1ap/)), což zajišťuje, že se CU a DU dohodnou na základních parametrech přenosu dat pro rozhraní řídicí roviny F1 v disagregované 5G základnové stanici.

## K čemu slouží

Rámec XID existuje, aby vyřešil problém statických, nepružných konfigurací datového spoje. V raných datových komunikacích byly parametry spoje často pevně nastaveny, což znamenalo, že jakákoliv nekompatibilita mezi dvěma připojenými zařízeními způsobila selhání nebo suboptimální provoz spoje. Mechanismus XID zavádí možnost dynamického vyjednávání, které umožňuje partnerům automaticky zjistit vzájemné možnosti a dohodnout se na vzájemně podporovaných parametrech, čímž maximalizuje kompatibilitu a výkon.

Historická motivace vychází z rodiny protokolů [HDLC](/mobilnisite/slovnik/hdlc/), která byla široce přijata v telekomunikacích a síťování. 3GPP začlenilo tyto dobře zavedené postupy datového spoje do svých specifikací pro okruhově přepínané datové služby, aby zajistilo robustnost. Pro služby jako fax a vytáčený přenos dat přes GSM byl Radio Link Protocol (používající XID) nezbytný k vytvoření spolehlivého bytového proudu přes inherentně náchylné k chybám rozhraní rádiového přenosu. Řešil tak omezení plynoucí z absence vyjednávání, které mohlo vést k přetečení vyrovnávací paměti, nadměrným opakovaným přenosům nebo nekompatibilitě verzí protokolů.

Ve vývoji směrem k 5G, zatímco mnoho protokolů uživatelské roviny pokročilo, koncept XID přetrvává na některých rozhraních řídicí roviny, jako je [F1AP](/mobilnisite/slovnik/f1ap/). Jeho účel zde zůstává podobný: umožnit autonomní vyjednávání a konfiguraci mezi síťovými funkcemi (CU a DU), které mohou pocházet od různých dodavatelů nebo z různých verzí softwaru. To podporuje cíl 3GPP v oblasti interoperability a flexibilního nasazení sítě, zajišťuje, že spoj řídicí roviny může být navázán s optimálními parametry bez manuálního zásahu, což je klíčové pro automatizované a škálovatelné síťové operace.

## Klíčové vlastnosti

- Řídicí rámec pro vyjednávání parametrů v protokolech založených na HDLC
- Používá se během fáze navázání nebo rekonfigurace spoje
- Nese vyjednatelné parametry, jako je velikost okna a délka rámce
- Podporuje výměnu příkaz/odpověď pro dosažení dohody
- Umožňuje interoperabilitu mezi implementacemi různých dodavatelů
- Specifikován v několika specifikacích 3GPP pro různá rozhraní (např. RLP, F1AP)

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [XID na 3GPP Explorer](https://3gpp-explorer.com/glossary/xid/)
