---
slug: "iab-du"
url: "/mobilnisite/slovnik/iab-du/"
type: "slovnik"
title: "IAB-DU – IAB Distributed Unit"
date: 2025-01-01
abbr: "IAB-DU"
fullName: "IAB Distributed Unit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iab-du/"
summary: "IAB-DU je komponenta gNB Distributed Unit (distribuovaná jednotka gNB) v uzlu integrovaného přístupu a přenosové trasy (IAB). Poskytuje rozhraní přístupové radiové sítě uživatelským zařízením (UE) neb"
---

IAB-DU je komponenta gNB Distributed Unit (distribuovaná jednotka gNB) v uzlu IAB, která poskytuje rozhraní radiového přístupu uživatelským zařízením nebo podřízeným IAB uzlům pod kontrolou centrální jednotky (CU) donoru.

## Popis

[IAB](/mobilnisite/slovnik/iab/) Distributed Unit (IAB-DU) je jednou ze dvou klíčových funkčních komponent uzlu integrovaného přístupu a přenosové trasy (IAB), druhou je [IAB-MT](/mobilnisite/slovnik/iab-mt/) (Mobile Termination). IAB-DU je zodpovědná za funkčnost přístupové radiové sítě směrem ke svým 'podřízeným' uzlům. Z pohledu uživatelského zařízení (UE) nebo komponenty IAB-MT podřízeného IAB uzlu se IAB-DU jeví a funguje shodně jako standardní distribuovaná jednotka gNB (gNB-DU) v síti 5G. Ukončuje vrstvy radiového rozhraní až po vrstvu řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)), zpracovává fyzickou vrstvu ([PHY](/mobilnisite/slovnik/phy/)), plánování řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a správu rádiových prostředků pro svou obsluhovanou buňku/buňky.

Z architektonického hlediska je IAB-DU řízena centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)) umístěnou v donorovém IAB uzlu. Tento řídicí vztah je navázán přes rozhraní F1, konkrétně [F1-C](/mobilnisite/slovnik/f1-c/) (řídicí rovina) a [F1-U](/mobilnisite/slovnik/f1-u/) (uživatelská rovina). Na rozdíl od tradičního fronthaulového spoje však toto F1 připojení není vedeno přímým optickým nebo mikrovlnným spojem. Místo toho je tunelováno přes bezdrátovou přenosovou trasu (backhaul) vytvořenou komponentou IAB-MT téhož IAB uzlu a případně dalšími nadřazenými IAB uzly. Zprávy F1-AP a data uživatelské roviny jsou zapouzdřeny a směrovány přes backhaulové kanály RLC s využitím backhaulového adaptačního protokolu (BAP) pro přeposílání mezi jednotlivými skoky.

Činnost IAB-DU je úzce koordinována s IAB-MT, aby se zabránilo vlastnímu rušení a optimalizovala se celková kapacita uzlu. Donorová CU poskytuje konfiguraci prostředků, která určuje, kdy může IAB-DU vysílat/přijímat ke svým podřízeným uzlům (přístupové spoje) a kdy musí IAB-MT vysílat/přijímat ke svému nadřazenému uzlu (backhaulový spoj). Tato konfigurace definuje vzor 'měkkých' buněk, kde je buňka IAB-DU dostupná pouze během specifických časových prostředků, pokud je použito časového multiplexu (TDM). IAB-DU vykonává všechny standardní funkce gNB-DU, jako je vysílání systémových informací, obsluha kanálu náhodného přístupu (RACH), plánování datových přenosů v uplinku a downlinku a procesy HARQ, avšak v rámci omezení daných prostředky přidělenými donorovou CU.

## K čemu slouží

IAB-DU existuje za účelem poskytování základní funkce bodu radiového přístupu v bezdrátovém IAB uzlu, což umožňuje vytvoření více-skokové, samostatně přenosovou trasu využívající sítě bez nutnosti samostatné, vyhrazené přístupové radiové jednotky. Jejím účelem je oddělit funkci radiového přístupu od potřeby přímého, kabelového připojení k jádru sítě. Integrací standardně kompatibilní gNB-DU do IAB uzlu může síť představovat normální 5G radiové rozhraní koncovým uživatelským zařízením, což zajišťuje plnou kompatibilitu s UE a využívá všech stávajících funkcí NR pro přístup.

Tento návrh řeší problém, jak zajistit, aby se přenosový uzel jevil zařízením, která obsluhuje, jako nativní součást 5G RAN. Předchozí přenosová řešení někdy vyžadovala specializované chování UE nebo vytvářela netransparentní spoje. IAB-DU díky shodě se specifikací gNB-DU definovanou 3GPP zajišťuje transparentnost a interoperabilitu. Motivace vychází z potřeby nákladově efektivního zahušťování sítě; IAB-DU umožňuje operátorovi umístit uzel, který okamžitě začne obsluhovat provoz, přičemž využívá svou bezdrátovou přenosovou trasu (přes spolulokalizovanou IAB-MT) k dosažení jádra sítě.

Navíc oddělení funkce DU od CU (v donoru) umožňuje centralizovanou koordinaci a efektivní sdružování prostředků v celé topologii IAB. Donorová CU může dynamicky upravovat prostředky mezi IAB-DU (pro přístup) a IAB-MT (pro přenosovou trasu) více uzlů na základě poptávky po provozu, čímž optimalizuje kapacitu celé bezdrátové sítě typu mesh. IAB-DU je tedy klíčovým prvkem umožňujícím flexibilní, rychlé a nákladově efektivní nasazení 5G small cells, které se předpokládá pro městské prostředí a průmyslové kampusy IoT.

## Klíčové vlastnosti

- Funguje jako standardní distribuovaná jednotka gNB (gNB-DU) dle 3GPP pro radiový přístup
- Ukončuje vrstvy NR radiového rozhraní (PHY, MAC, RLC) směrem k UE a podřízeným IAB uzlům
- Řízena centrální jednotkou (CU) IAB donoru přes rozhraní F1 tunelované přes bezdrátovou přenosovou trasu
- Plánuje rádiové prostředky pro svou buňku na základě konfigurace od donorové CU
- Funguje s časovými/frekvenčními prostředky dynamicky rozdělenými mezi přístupové a přenosové spoje
- Vysílá systémové informace a spravuje procedury rádiového připojení pro připojená UE

## Související pojmy

- [IAB-MT – Integrated Access and Backhaul Mobile Termination](/mobilnisite/slovnik/iab-mt/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.420** (Rel-19) — Introduction to Xn interface specifications
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background

---

📖 **Anglický originál a plná specifikace:** [IAB-DU na 3GPP Explorer](https://3gpp-explorer.com/glossary/iab-du/)
