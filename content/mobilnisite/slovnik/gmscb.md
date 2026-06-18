---
slug: "gmscb"
url: "/mobilnisite/slovnik/gmscb/"
type: "slovnik"
title: "GMSCB – Gateway MSC of the B subscriber"
date: 2025-01-01
abbr: "GMSCB"
fullName: "Gateway MSC of the B subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmscb/"
summary: "Gateway MSC (GMSC), který zpracovává sestavení hovoru pro koncového (B) účastníka v mobilní síti. Je zodpovědný za dotazování na HLR, aby získal směrovací informace pro volaného účastníka, a je klíčov"
---

GMSCB je Gateway MSC, který zpracovává sestavení hovoru pro koncového účastníka B tím, že se dotazuje na HLR, aby získal směrovací informace potřebné k dokončení mobilních příchozích hovorů.

## Popis

Gateway [MSC](/mobilnisite/slovnik/msc/) účastníka B (GMSCB) je funkční role Mobile Switching Center (MSC) v okruhově přepínané jádrové síti systémů 2G (GSM) a 3G (UMTS). Jeho primární funkcí je sloužit jako vstupní bod do domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)) pro příchozí hovory určené mobilnímu účastníkovi (strana B). Když je uskutečněn hovor na mobilní číslo, je hovor nejprve směrován na [GMSC](/mobilnisite/slovnik/gmsc/). GMSCB je konkrétně ten GMSC, který obsluhuje domovskou síť volaného účastníka. Provádí klíčový proces dotazování na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Po přijetí hovoru odešle GMSCB zprávu Send Routing Information ([SRI](/mobilnisite/slovnik/sri/)) na HLR účastníka. HLR, které uchovává aktuální polohu účastníka (adresu Visitor Location Register nebo [VLR](/mobilnisite/slovnik/vlr/)), odpoví Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)). GMSCB poté použije toto MSRN k směrování hovoru na MSC, které aktuálně obsluhuje účastníka (Visited MSC nebo [VMSC](/mobilnisite/slovnik/vmsc/)), kde je navázáno konečné spojení s mobilním zařízením.

Z architektonického hlediska není GMSCB nutně samostatný fyzický uzel; jde o logickou funkci, která může být integrována do standardního MSC. Jeho činnost je definována v kontextu procedur řízení hovorů a správy mobility. GMSCB komunikuje s HLR pomocí protokolu Mobile Application Part (MAP) přes signalizační síť SS7. Také zajišťuje vzájemné propojení mezi různými typy sítí, jako je Public Switched Telephone Network (PSTN) nebo jiné mobilní sítě, a mobilní jádrovou sítí, řídí převod signalizace a směrování hovorů.

Jeho role je zásadní pro dokončení mobilních příchozích (MT) hovorů. Bez funkce dotazování GMSCB by síť neměla efektivní způsob, jak lokalizovat roamujícího účastníka. Odděluje volané Mobile Station International Subscriber Directory Number (MSISDN) od fyzického směrovacího čísla (MSRN), což umožňuje mobilitu účastníka a přenositelnost čísel. GMSCB se také podílí na zpracování doplňkových služeb pro koncovou větev hovoru, jako je bezpodmínečné přesměrování hovoru (CFU), kde HLR může poskytnout alternativní směrovací instrukce.

## K čemu slouží

GMSCB byl vytvořen k řešení základního problému lokalizace a směrování hovorů k mobilnímu účastníkovi, jehož fyzická poloha se může dynamicky měnit. Ve fixní telefonii je telefonní číslo vázáno na konkrétní fyzickou linku. V mobilních sítích je MSISDN účastníka logický identifikátor, nikoli identifikátor vázaný na polohu. GMSCB prostřednictvím svého dotazování na centralizované HLR poskytuje potřebný překlad z tohoto logického identifikátoru (MSISDN) na dočasnou, směrovatelnou adresu (MSRN), která ukazuje na aktuálně obsluhující MSC účastníka.

Tato architektura řeší omezení statického směrování a umožňuje skutečnou mobilitu uživatele. Umožňuje správné doručení hovorů bez ohledu na to, zda je účastník ve své domovské síti, nebo roamuje v navštívené síti. Oddělení funkce GMSC pro volajícího (A) a volaného (B) účastníka poskytuje jasnost v procedurách řízení hovorů a účtování. GMSCB je základním kamenem návrhu jádrové sítě GSM/UMTS, vytváří jasný kotvící bod v domovské síti pro zabezpečení, zprostředkování účtování a řízení služeb pro příchozí provoz.

## Klíčové vlastnosti

- Slouží jako vstupní bod pro mobilní příchozí (MT) hovory do HPLMN účastníka
- Dotazuje se na Home Location Register (HLR) pomocí MAP signalizace, aby získal směrovací informace
- Přijímá od HLR Mobile Station Roaming Number (MSRN) pro směrování hovoru
- Směruje příchozí hovor na Visited MSC (VMSC), které obsluhuje účastníka
- Zajišťuje vzájemné propojení mezi externími sítěmi (PSTN, jiné PLMN) a mobilní jádrovou sítí
- Podílí se na provádění doplňkových služeb pro koncovou větev hovoru

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [GMSCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmscb/)
