---
slug: "vbr"
url: "/mobilnisite/slovnik/vbr/"
type: "slovnik"
title: "VBR – Variable Bit Rate"
date: 2025-01-01
abbr: "VBR"
fullName: "Variable Bit Rate"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vbr/"
summary: "Variable Bit Rate (VBR, proměnná přenosová rychlost) je třída služby, ve které přenosová rychlost dat není konstantní, ale v čase se mění na základě okamžitých požadavků zdroje provozu, například při"
---

VBR je třída služby, ve které se přenosová rychlost dat v čase mění na základě okamžitých požadavků zdroje provozu, čímž optimalizuje využití šířky pásma pro multimédia.

## Popis

Variable Bit Rate (VBR, proměnná přenosová rychlost) je charakteristika provozu a parametr QoS, při kterém se přenosová rychlost datového toku dynamicky mění v reakci na složitost a informační obsah zdrojového materiálu. V systémech 3GPP je VBR zvláště relevantní pro kódované mediální proudy, jako je videokonferenční přenos (H.264/[AVC](/mobilnisite/slovnik/avc/), H.265/[HEVC](/mobilnisite/slovnik/hevc/)) nebo audio ([AMR-WB](/mobilnisite/slovnik/amr-wb/)), kde kodér vydává více bitů během scén s vysokým pohybem nebo složitých scén a méně bitů během statických nebo jednoduchých období. Tato proměnlivost je řízena v rámci rádiové přístupové sítě (RAN) a jádra sítě prostřednictvím mechanismů QoS, které přidělují prostředky flexibilně, místo aby rezervovaly pevnou špičkovou rychlost. Například v UMTS (TS 25.222) a LTE může plánovač RAN zacházet s tokem VBR jako s přenašečem bez garantované přenosové rychlosti (non-GBR), kde jsou prostředky sdíleny a přidělovány na základě dostupnosti a priority, což umožňuje zisky statistického multiplexování. Architektura Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) v jádru sítě může definovat provoz VBR pomocí parametrů QoS, jako je Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)) a Maximum Bit Rate ([MBR](/mobilnisite/slovnik/mbr/)), kde pro služby VBR může být GBR nastaveno na nulu nebo nízký průměr a MBR definuje horní limit. Během přenosu jsou datové pakety ze zdroje VBR ukládány do vyrovnávací paměti a plánovány přes rozhraní vzduchem pomocí algoritmů, které berou v úvahu stav kanálu, identifikátor třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) a prioritu přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)). Tento přístup maximalizuje spektrální účinnost tím, že šířku pásma využívá pouze v případě potřeby, na rozdíl od konstantní přenosové rychlosti (CBR), která plýtvá kapacitou během období nízké aktivity. VBR je tedy nedílnou součástí doručování vysoce kvalitních multimédií přes bezdrátové spoje s omezenou šířkou pásma.

## K čemu slouží

Technologie Variable Bit Rate byla vyvinuta za účelem překonání neefektivit přenosu s konstantní přenosovou rychlostí (CBR) pro komprimovaný multimediální obsah. V raných systémech digitálního videa a audia bylo CBR jednodušší na správu, ale vedlo buď k trvalému nadměrnému poskytování šířky pásma (plýtvání kapacitou), nebo k nedostatečnému poskytování způsobujícímu degradaci kvality během složitých scén. VBR se objevila s pokročilými kompresními algoritmy (např. MPEG, H.26x), které inherentně vytvářejí proměnný výstup, což umožňuje, aby se přenosová rychlost přizpůsobila entropii zdroje. V mobilních sítích, kde je rádiové spektrum vzácným a drahým zdrojem, je efektivní využití šířky pásma prvořadé. VBR umožňuje operátorům obsloužit více uživatelů s danou kapacitou prostřednictvím statistického multiplexování proměnných toků, čímž zlepšuje celkovou účinnost sítě. Také zlepšuje uživatelský zážitek tím, že udržuje vyšší percepční kvalitu – přiděluje více bitů složitým snímkům a méně jednoduchým – v rámci rozpočtu průměrné přenosové rychlosti. Zařazení VBR do specifikací 3GPP již od raných vydání (R99) řešilo potřebu diferenciace QoS pro služby reálného času, jako je streamování videa a VoIP, a podpořilo růst mobilních multimédií. Vyřešila problém, jak doručovat vysoce kvalitní, na šířku pásma náročné aplikace přes bezdrátové spoje bez nutnosti nadměrných, statických rezervací prostředků.

## Klíčové vlastnosti

- Dynamické přizpůsobení přenosové rychlosti na základě složitosti zdrojového obsahu a rozhodnutí kodéru
- Efektivní využití šířky pásma prostřednictvím statistického multiplexování více toků VBR
- Podpora v rámci rámců QoS jako přenašečů non-GBR pro provoz reálného času a streamování
- Integrace s kodekovými standardy (např. H.264, EVS), které inherentně vytvářejí výstupy VBR
- Tvarování a regulace provozu pomocí parametrů jako Maximum Bit Rate (MBR) a QoS Class Identifier (QCI)
- Vylepšená percepční kvalita videa/audia přidělováním bitů tam, kde jsou nejvíce potřeba

## Související pojmy

- [CBR – Channel Busy Ratio](/mobilnisite/slovnik/cbr/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [VBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbr/)
