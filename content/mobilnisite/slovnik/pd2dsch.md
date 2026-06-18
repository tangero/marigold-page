---
slug: "pd2dsch"
url: "/mobilnisite/slovnik/pd2dsch/"
type: "slovnik"
title: "PD2DSCH – Physical D2D Synchronization Channel"
date: 2018-01-01
abbr: "PD2DSCH"
fullName: "Physical D2D Synchronization Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pd2dsch/"
summary: "Fyzický kanál v komunikaci zařízení-zařízení (D2D) založené na LTE, určený speciálně pro přímé objevování a komunikaci ProSe. Přenáší synchronizační signály a bloky systémových informací (SIB), které"
---

PD2DSCH je fyzický kanál v D2D komunikaci založené na LTE, který přenáší synchronizační signály a systémové informace, aby umožnil synchronizaci a objevování zařízení mimo pokrytí sítě.

## Popis

Physical [D2D](/mobilnisite/slovnik/d2d/) Synchronization Channel (PD2DSCH) je klíčový fyzický kanál podobný downlinku, definovaný pro operace postranního spoje (sidelink, [SL](/mobilnisite/slovnik/sl/)) v LTE, zejména v rámci služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) pro veřejnou bezpečnost a komerční D2D komunikaci. Funguje na rozhraní PC5. Na rozdíl od buněčných kanálů vysílaných eNodeB je PD2DSCH vysílán uživatelským zařízením (UE) fungujícím jako zdroj synchronizace, což může být UE v pokrytí, mimo pokrytí nebo UE přenoska. Jeho hlavní funkcí je vysílat základní synchronizační a minimální systémové informace ostatním blízkým UE, aby usnadnil objevování zařízení a navázání komunikace, zejména když jsou zařízení mimo pokrytí sítě.

Z architektonického hlediska je PD2DSCH úzce spjat se synchronizačními signály D2D ([PD2DSS](/mobilnisite/slovnik/pd2dss/) a [SD2DSS](/mobilnisite/slovnik/sd2dss/)). Vysílající UE odešle primární a sekundární synchronizační signály (PD2DSS/SD2DSS) ve specifických podrámcích. PD2DSCH je poté vysílán ve stejném nebo úzce souvisejícím podrámci a nese Physical Sidelink Broadcast Channel ([PSBCH](/mobilnisite/slovnik/psbch/)). Datová část PSBCH obsahuje Sidelink Master Information Block (SL-MIB), který zahrnuje klíčové parametry, jako jsou časové informace (Direct Frame Number, [DFN](/mobilnisite/slovnik/dfn/)), indikátor stavu pokrytí, typ zdroje synchronizace (např. [eNB](/mobilnisite/slovnik/enb/), UE, GNSS) a informace o šířce pásma. Přijímající UE nejprve detekují PD2DSS/SD2DSS, aby dosáhly časové a frekvenční synchronizace, a poté dekódují přidružený PD2DSCH, aby získaly SL-MIB a pochopily kontext zdroje synchronizace.

Fungování zahrnuje specifickou alokaci zdrojů v rámci fondu zdrojů postranního spoje. Zdroje pro vysílání PD2DSCH jsou předdefinovány v rámci bloků synchronizačních signálů. Vysílající UE zakóduje SL-MIB, použije kanálové kódování (např. tail-biting konvoluční kódování) a namapuje jej na zdrojové elementy alokované pro PD2DSCH. Tento kanál umožňuje hierarchickou synchronizační strukturu, kde se UE může stát synchronizační referencí pro jiná UE, čímž vytváří vícevrstvé synchronizační řetězce klíčové pro rozšíření dosahu komunikace ve scénářích veřejné bezpečnosti. Jeho správná funkce je zásadní pro vytvoření společného časového referenčního bodu ve skupině zařízení, což je předpoklad pro efektivní plánování zdrojů a řízení interference v autonomní D2D komunikaci bez sítě.

## K čemu slouží

PD2DSCH byl vytvořen, aby řešil kritickou výzvu navázání a udržení synchronizace v D2D komunikaci založené na LTE, zejména pro scénáře mimo pokrytí a s částečným pokrytím, které jsou vyžadovány pro veřejnou bezpečnost. Před zavedením D2D funkcí byla LTE UE zcela závislá na eNodeB pro synchronizaci a systémové informace. To bylo hlavním omezením pro přímou komunikaci při výpadcích sítě nebo v odlehlých oblastech. PD2DSCH spolu s D2DSS umožňuje UE vytvářet vlastní synchronizační shluky.

Motivace vycházela z požadavků veřejné bezpečnosti, kde musí záchranáři komunikovat přímo bez síťové infrastruktury. PD2DSCH řeší problém, jak šířit základní časové a konfigurační informace ze zdrojového UE pro synchronizaci na objevující se UE. Poskytuje 'maják', který nese minimální systémové informace potřebné pro ostatní zařízení, aby pochopila kontext synchronizace (např. je tento zdroj synchronizace zarovnán s eNB nebo jiným UE?) a správně nakonfigurovala své přijímače. To umožňuje vytváření ad-hoc sítí, rozšiřuje síťové pokrytí prostřednictvím přenosu z UE na síť a podporuje komerční aplikace ProSe tím, že umožňuje zařízením efektivně se vzájemně objevovat, čímž tvoří základní řídicí kanál pro fyzickou vrstvu postranního spoje.

## Klíčové vlastnosti

- Přenáší Sidelink Master Information Block (SL-MIB) na Physical Sidelink Broadcast Channel (PSBCH)
- Vysíláno uživatelským zařízením (UE) fungujícím jako zdroj synchronizace (v pokrytí, mimo pokrytí nebo přenoska)
- Vysílá klíčové parametry: Direct Frame Number, indikátor stavu pokrytí, typ zdroje synchronizace a šířka pásma
- Funguje ve spojení se synchronizačními signály D2D (PD2DSS/SD2DSS) v definovaných fondech zdrojů
- Umožňuje vícevrstvou synchronizaci pro rozšíření dosahu D2D komunikace
- Zásadní pro scénáře přímého objevování a komunikace ProSe mimo pokrytí a s částečným pokrytím

## Související pojmy

- [D2D – Device-to-Device](/mobilnisite/slovnik/d2d/)
- [PD2DSS – Primary D2D Synchronization Signal](/mobilnisite/slovnik/pd2dss/)
- [SD2DSS – Secondary D2D Synchronization Signal](/mobilnisite/slovnik/sd2dss/)
- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.843** (Rel-12) — D2D Proximity Services Feasibility Study
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services

---

📖 **Anglický originál a plná specifikace:** [PD2DSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pd2dsch/)
