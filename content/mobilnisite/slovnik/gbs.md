---
slug: "gbs"
url: "/mobilnisite/slovnik/gbs/"
type: "slovnik"
title: "GBS – General Bearer Services"
date: 2025-01-01
abbr: "GBS"
fullName: "General Bearer Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gbs/"
summary: "Základní koncept v raných sítích GSM/UMTS definující základní typy datových přenosových spojení (přenosových kanálů), které síť poskytuje uživatelům. Kategorizuje služby na základě základních charakte"
---

GBS je základní koncept v GSM/UMTS, který definuje a kategorizuje základní typy přepojovaných okruhově nebo paketově datových přenosových spojení, které síť poskytuje.

## Popis

General Bearer Services (GBS, obecné přenosové služby) představují klasifikační rámec v rámci servisní architektury 3GPP, primárně definovaný v raných verzích standardů (počínaje GSM Phase 2+). Přenosová služba (bearer service) v telekomunikacích je typ telekomunikační služby, která poskytuje schopnost přenosu signálů mezi rozhraními uživatel-síť. Klasifikace 'General' (obecné) odkazuje na základní, standardizovanou sadu těchto přenosových schopností, které tvoří základ pro konkrétnější teleslužby (jako je telefonie) a doplňkové služby. GBS definuje základní charakteristiky datové cesty, abstrahující od podkladové síťové technologie (např. rádiového přístupu, přepínání v jádru sítě).

Z architektonického hlediska je GBS konceptem ve vrstvě popisu služeb protokolového zásobníku, nad spojovou a fyzickou vrstvou. Používá se při sestavování hovoru a vyjednávání služeb. Mezi klíčové parametry definující obecnou přenosovou službu patří režim přenosu informací (přepojovaný okruhově nebo paketově), rychlost přenosu informací (např. plná rychlost, poloviční rychlost, specifické datové rychlosti), schopnost přenosu informací (řeč, neomezený digitální, omezený digitální, 3,1 kHz audio), režim spojení (spojově orientovaný nebo nespojový) a přístupová struktura (např. vyhrazená nebo sdílená). Například přenosová služba přepojovaná okruhově, neomezená digitální, s rychlostí 64 kbps, je klasický GBS používaný pro faxová nebo modemová data. Síť tyto parametry používá k vytvoření přenosového kanálu s odpovídající kvalitou a alokací prostředků prostřednictvím jádra sítě (CN) a rádiové přístupové sítě (RAN).

Jak to funguje: terminál ([MS](/mobilnisite/slovnik/ms/)/UE) a síť na začátku relace vyjednávají požadovanou přenosovou službu. Termínál v signalizačních zprávách (např. ve zprávě SETUP nebo ACTIVATE PDP CONTEXT REQUEST) indikuje své požadované parametry GBS. Síť následně zkontroluje profily účastníka, síťové možnosti a dostupnost prostředků, aby požadavek přijala, upravila nebo odmítla. Jakmile je služba zřízena, poskytuje přenosová služba transparentní potrubí pro uživatelská data podle dohodnutých charakteristik. Jejím úkolem bylo poskytnout jednotný model služeb, který mohl být podporován napříč různými generacemi síťové infrastruktury, což umožnilo zpětnou kompatibilitu a jasné definice služeb pro testování interoperability a poskytování služeb sítí.

## K čemu slouží

GBS byl vytvořen, aby poskytl standardizovaný a jednoznačný způsob popisu základních přenosových schopností sítě GSM a UMTS. V počátcích digitální buněčné sítě bylo třeba podporovat nejen hlas, ale také datové služby jako fax a data přepojovaná okruhově. Bez společné taxonomie byl popis toho, jaký druh spojení uživatel potřebuje, nejednoznačný. GBS tento problém vyřešil definováním jasné sady atributů (režim, rychlost, schopnost), které mohly být signalizovány mezi mobilní stanicí a sítí k vytvoření spojení se správnými technickými vlastnostmi.

Historický kontext je evoluce z analogových (1G) na digitální (2G GSM) systémy. Analogové systémy byly v podstatě pouze hlasové. GSM zavedlo digitální kanály, které mohly přenášet hlas nebo data, což si vyžádalo způsob, jak specifikovat, jak má být kanál použit. Omezení předchozích ad-hoc přístupů byla nedostatečná interoperabilita a složité poskytování služeb. GBS poskytl základní stavební kameny, na kterých byly vybudovány všechny ostatní služby (teleslužby). Vyřešil problém přenositelnosti služeb a interoperability více dodavatelů tím, že zajistil, že 'neomezený digitální přenosový kanál 64 kbps' znamenal totéž pro všechny síťové prvky a terminály bez ohledu na výrobce. Tento konceptuální model byl klíčový pro počáteční nasazení a úspěch mobilních datových služeb.

## Klíčové vlastnosti

- Definuje základní přenosové charakteristiky: režim přenosu informací (okruhově/paketově)
- Specifikuje rychlosti přenosu informací a přístupové struktury
- Kategorizuje schopnost přenosu informací (řeč, audio, digitální)
- Používá se pro vyjednávání služeb a signalizaci při zřizování přenosového kanálu
- Poskytuje podkladový přenos pro teleslužby a doplňkové služby
- Základ pro definice parametrů QoS v pozdějších paketově přepojovaných systémech

## Definující specifikace

- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1

---

📖 **Anglický originál a plná specifikace:** [GBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gbs/)
