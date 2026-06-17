---
slug: "esg"
url: "/mobilnisite/slovnik/esg/"
type: "slovnik"
title: "ESG – Electronic Service Guide"
date: 2025-01-01
abbr: "ESG"
fullName: "Electronic Service Guide"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esg/"
summary: "Elektronický průvodce službami (ESG) je strukturovaná datová služba, která uživatelům poskytuje informace o dostupných vysílacích a multicastových službách, jako je mobilní TV. Umožňuje objevování slu"
---

ESG je elektronický průvodce službami (Electronic Service Guide), který uživatelům poskytuje informace o dostupných vysílacích a multicastových službách, umožňuje objevování služeb a funguje jako elektronický programový průvodce pro mobilní sítě.

## Popis

Elektronický průvodce službami (ESG) je základní komponentou architektur služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a jejího vylepšeného nástupce evolved MBMS (eMBMS) dle 3GPP. Jedná se o strukturovanou datovou službu, typicky distribuovanou přes vysílací nebo multicastové kanály, která uživatelům poskytuje komplexní metadata o dostupných vysílacích a multicastových službách. ESG není jediný monolitický soubor, ale kolekce XML fragmentů nebo jiných strukturovaných datových objektů, z nichž každý popisuje jiný aspekt nabídky služeb. Tyto fragmenty zahrnují informace pro objevování služeb (jako názvy služeb, poskytovatele a popisy), informace k zakoupení služby (včetně údajů o předplatném a cenách) a informace pro objevování obsahu (jako programové schéma, žánry a přidružené mediální popisy). Datový model ESG je definován jako rozšiřitelný a může podporovat různé obchodní modely, včetně volně přístupných služeb, služeb založených na předplatném a služeb typu pay-per-view.

Z architektonického hlediska je ESG generován vysílacím poskytovatelem služeb (Broadcast Service Provider) nebo poskytovatelem obsahu (Content Provider) a je doručován do uživatelského zařízení přes přenosovou službu MBMS. Doručení řídí [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre), což je hlavní síťová entita zodpovědná za poskytování a doručování služeb MBMS. Data ESG jsou typicky doručována přes vyhrazenou přenosovou službu MBMS, odděleně od skutečných přenosových služeb pro mediální obsah, což umožňuje zařízením objevit a vybrat služby před připojením k odpovídajícím mediálním streamům. Na straně zařízení specializovaná ESG klientská aplikace parsuje a interpretuje data ESG a poskytuje uživatelsky přívětivé rozhraní pro výběr služeb, často integrované s mediálním přehrávačem zařízení nebo specializovanou vysílací aplikací.

Role ESG je klíčová pro použitelnost a komerční životaschopnost vysílacích služeb. Umožňuje automatické objevování služeb, díky čemuž uživatelé vidí, co je k dispozici, bez nutnosti ruční konfigurace. Podporuje získání služby tím, že poskytuje potřebné informace (jako IP multicastové adresy, čísla portů a identifikátory služeb) pro připojení zařízení ke správné přenosové službě MBMS. Dále usnadňuje navigaci ve službách a výběr obsahu, podobně jako elektronický programový průvodce ([EPG](/mobilnisite/slovnik/epg/)) v tradičních TV systémech. ESG může také nést metadata pro systémy ochrany obsahu (jako informace [DRM](/mobilnisite/slovnik/drm/)) a může být dynamicky aktualizován, aby odrážel změny v nabídce služeb nebo programu, čímž zajišťuje, že uživatelé mají přístup k aktuálním informacím.

## K čemu slouží

ESG byl vytvořen, aby vyřešil základní problém objevování služeb a uživatelské navigace v mobilních vysílacích a multicastových sítích. Před jeho standardizací vyžadovalo poskytování vysílacích služeb, jako je mobilní TV, proprietární a často těžkopádné metody, aby uživatelé mohli obsah najít a získat k němu přístup. Nedostatek jednotného průvodce bránil přijetí uživateli a komplikoval poskytování služeb pro operátory. ESG poskytuje standardizovaný, síťově efektivní mechanismus pro doručení bohatých metadat o dostupných službách přímo do zařízení.

Jeho vytvoření bylo motivováno potřebou učinit služby [MBMS](/mobilnisite/slovnik/mbms/) a později eMBMS uživatelsky přívětivými a komerčně provozovatelnými. Bez ESG by uživatelé potřebovali znát specifické technické podrobnosti (jako multicastové adresy) pro přístup ke službě, což je nepraktické. ESG tuto složitost abstrahuje a prezentuje informace způsobem přátelským pro spotřebitele. Také umožňuje pokročilé obchodní modely tím, že nese informace o nákupu a právech, což umožňuje integrované předplatné služeb a možnosti typu pay-per-view v rámci vysílacího rámce. Tím, že je distribuován přes samotný vysílací kanál, zajišťuje efektivní, škálovatelné šíření těchto průvodních informací všem potenciálním uživatelům současně, na rozdíl od průvodců založených na unicastu, které by se pro hromadné vysílací služby neškálovaly.

## Klíčové vlastnosti

- Strukturovaný datový model založený na XML pro popis služeb a obsahu
- Distribuce přes efektivní vysílací nebo multicastové přenosové služby MBMS/eMBMS
- Podpora objevování služeb, jejich získávání a navigace
- Umožňuje různé obchodní modely (volně přístupné, předplatné, pay-per-view)
- Nese metadata pro ochranu obsahu a správu digitálních práv (DRM)
- Umožňuje dynamické aktualizace pro odraz změn v programových schématech a nabídce služeb

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [ESG na 3GPP Explorer](https://3gpp-explorer.com/glossary/esg/)
