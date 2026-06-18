---
slug: "nam"
url: "/mobilnisite/slovnik/nam/"
type: "slovnik"
title: "NAM – Network Access Mode"
date: 2025-01-01
abbr: "NAM"
fullName: "Network Access Mode"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nam/"
summary: "Konfigurační parametr uživatelského zařízení (UE), který určuje, které rádiové přístupové technologie (RAT) může použít pro přístup k síti. Řídí, zda může zařízení pracovat v jedno-režimovém (např. po"
---

NAM je konfigurační parametr uživatelského zařízení (UE), který určuje, které rádiové přístupové technologie může zařízení použít pro přístup k síti, a řídí tak jedno- nebo dvou/více-režimový provoz.

## Popis

Network Access Mode (NAM) je základní konfigurační parametr uložený v uživatelském zařízení (UE), jako je mobilní telefon nebo zařízení IoT. Definuje sadu rádiových přístupových technologií, které je UE oprávněno použít pro připojení k síti. Nastavení NAM v UE je typicky zajišťováno operátorem, často prostřednictvím [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module), a může být někdy vybráno uživatelem v nastavení zařízení. Působí jako filtr během procesů výběru sítě a výběru/převýběru buňky, čímž zajišťuje, že se zařízení pokouší připojit pouze k sítím a buňkám, které pracují s technologiemi uvedenými v jeho aktivním NAM.

Technicky je parametr NAM součástí kontextu správy mobility UE. Když je UE zapnuto nebo ztratí pokrytí, provede výběr [PLMN](/mobilnisite/slovnik/plmn/) (Public Land Mobile Network) a následně výběr buňky. Během těchto procedur UE konzultuje svůj NAM, aby určilo, které [RAT](/mobilnisite/slovnik/rat/) má vyhledávat a vyhodnocovat. Například UE s NAM nastaveným na 'pouze [UTRAN](/mobilnisite/slovnik/utran/)' bude ignorovat buňky GSM a bude hledat pouze buňky UMTS. NAM interaguje s dalšími parametry, jako je seznam schopností 'Supported RATs', ale zatímco schopnosti definují, co hardware dokáže, NAM definuje, co je mu povoleno dělat podle politiky operátora nebo preference uživatele.

Jeho role zasahuje i do signalizace v jádře sítě. Když UE provádí aktualizaci polohy nebo směrovací oblasti, může síti indikovat svůj aktuální přístupový režim. To umožňuje síti lépe porozumět kontextu připojení UE. Ve složitějších scénářích, jako je Circuit-Switched Fallback ([CSFB](/mobilnisite/slovnik/csfb/)) nebo předávání hovoru, může NAM ovlivnit výběr cílové RAT. Ačkoli se jedná převážně o koncept z Release 8 a starších pro základní dvou- a více-režimový provoz 2G/3G, tento princip se vyvinul ve složitější konfigurace přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) a ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) pro 4G a 5G, kde je více RAT spravováno pod jednotným jádrem sítě. NAM je klíčovým prvkem pro zajištění efektivního využití rádiových zdrojů, správu zatížení sítě napříč různými generacemi a poskytování řízeného uživatelského zážitku.

## K čemu slouží

Network Access Mode byl zaveden, aby řešil rostoucí složitost více-RAT zařízení a sítí. Jak se buněčná technologie vyvíjela z 2G (GSM) na 3G (UMTS), operátoři nasazovali nové sítě, zatímco často udržovali starší. To vytvořilo potřebu dvou-režimových zařízení, která by mohla přistupovat k oběma. Nekontrolovaný přístup však mohl vést k problémům: zařízení by se mohlo zbytečně připojit k zastaralé 2G síti, když je k dispozici síť 3G s vyšší kapacitou, nebo by mohlo neustále přepínat mezi technologiemi, čímž by plýtvalo baterií a signalizačními zdroji.

NAM poskytuje centralizovaný a spravovatelný způsob, jak operátor (nebo uživatel) může diktovat politiku [RAT](/mobilnisite/slovnik/rat/) zařízení. Řeší problém inteligentního výběru sítě tím, že předem definuje povolenou sadu technologií. To umožňuje operátorům například řídit provoz nastavením výchozího NAM, který upřednostňuje 3G pro datové služby, ale umožňuje návrat k 2G pro hlas. Také umožňuje vytváření služebních tarifů vázaných na konkrétní technologie (např. datový tarif pouze na 3G). Pro uživatele může poskytnout jednoduchý způsob, jak zakázat určité rádiové moduly pro úsporu baterie. V zásadě NAM stanovil princip výběru RAT řízeného politikou, koncept, který se stal ještě kritičtějším v éře 4G/5G s integrací LTE, NR a nepřístupových přístupů 3GPP, jako je Wi-Fi.

## Klíčové vlastnosti

- Definuje povolené rádiové přístupové technologie (RAT) pro UE
- Zajišťován operátorem, často prostřednictvím aplikace USIM
- Řídí chování během výběru PLMN a výběru/převýběru buňky
- Může ovlivnit rozhodnutí o cílové RAT pro předání hovoru (handover) a CSFB
- Může být prezentován jako uživatelsky volitelné nastavení na zařízení
- Interaguje s informacemi o schopnostech UE pro řízení přístupu

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [RAT – Radio Access Technology](/mobilnisite/slovnik/rat/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TR 36.779** (Rel-17) — Upper 700MHz A Block E-UTRA Band

---

📖 **Anglický originál a plná specifikace:** [NAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nam/)
