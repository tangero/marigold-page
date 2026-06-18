---
slug: "s-tsid"
url: "/mobilnisite/slovnik/s-tsid/"
type: "slovnik"
title: "S-TSID – Service-based Transport Session Instance Description"
date: 2025-01-01
abbr: "S-TSID"
fullName: "Service-based Transport Session Instance Description"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-tsid/"
summary: "S-TSID je popis metadat používaný ve službě Multimedia Broadcast Multicast Service (MBMS) k definici přenosových charakteristik komponenty služby. Umožňuje efektivní doručování vysílacího a skupinovéh"
---

S-TSID (popis instance přenosové relace založené na službě) je popis metadat používaný v MBMS k definici přenosových charakteristik komponenty služby pro efektivní doručování vysílacího a skupinového obsahu.

## Popis

Service-based Transport Session Instance Description (S-TSID) je klíčová komponenta v architektuře služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) podle 3GPP, konkrétně definovaná pro evolved MBMS (eMBMS). Funguje jako strukturovaný deskriptor metadat, který poskytuje podrobný plán přenosové relace pro konkrétní komponentu služby, například video nebo audio stream, v rámci vysílací/skupinové služby. S-TSID je typicky doručován jako součást oznámení služby nebo v rámci protokolu [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) používaného pro doručování souborů vysíláním. Popisuje mapování mezi komponentami služby a jim odpovídajícími přenosovými relacemi, které jsou identifikovány pomocí Transport Session Identifiers ([TSI](/mobilnisite/slovnik/tsi/)). Pro každou přenosovou relaci S-TSID specifikuje parametry jako zdrojovou IP adresu, cílovou IP adresu, cílový port a přidružené schéma Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)), což přijímačům umožňuje správně identifikovat, připojit se a dekódovat datové toky skupinového vysílání.

Architektonicky S-TSID funguje v aplikační vrstvě rámce MBMS. Je generován centrem Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita zodpovědná za poskytování a doručování služeb MBMS. BM-SC vkládá informace S-TSID do User Service Description ([USD](/mobilnisite/slovnik/usd/)) nebo File Delivery Table ([FDT](/mobilnisite/slovnik/fdt/)) v rámci relace FLUTE. Když chce uživatelské zařízení (UE) přijímat službu MBMS, nejprve získá oznámení služby, které obsahuje nebo odkazuje na S-TSID. UE následně analyzuje S-TSID, aby se dozvědělo potřebné parametry síťové vrstvy pro konfiguraci své IP vrstvy a aplikační vrstvy k přijímání konkrétních skupinových streamů. Tím odděluje logiku služby od detailů přenosu, což umožňuje flexibilní definice služeb.

Role S-TSID je klíčová pro umožnění pokročilých funkcí MBMS, jako je kontinuita služby a dynamická adaptace. Například u vylepšených televizních (TV) služeb může jeden program sestávat z více komponent (např. hlavní video, alternativní úhly, více zvukových stop, titulky). S-TSID popisuje přenosovou instanci každé komponenty, což umožňuje UE selektivně se přihlásit pouze k požadovaným komponentám a šetřit tak baterii a rádiové prostředky. Dále podporuje popis opravných toků pro FEC, detailně popisujících, jak lze ztracené pakety obnovit. Poskytnutím standardizovaného, strojově čitelného popisu instancí přenosových relací S-TSID zajišťuje interoperabilitu mezi různými implementacemi BM-SC a přijímači UE, čímž tvoří páteř spolehlivého a efektivního doručování vysílacích služeb v sítích LTE a 5G.

## K čemu slouží

S-TSID byl zaveden, aby řešil rostoucí složitost multimediálních vysílacích služeb, zejména s vývojem eMBMS pro doručování bohatých médií, jako je mobilní TV a komunikace pro veřejnou bezpečnost. Před jeho standardizací bylo řízení více souběžných přenosových toků pro jednu službu méně strukturované, což mohlo vést k problémům s interoperabilitou a neefektivnímu využití prostředků na UE. Potřeba formalizovaného mechanismu popisu se stala zřejmou, jak se služby vyvíjely od jednoduchého jednoho audio/video streamu k zahrnutí více komponent, alternativních reprezentací a pokročilých funkcí, jako je Forward Error Correction na aplikační vrstvě.

Hlavní problém, který S-TSID řeší, je efektivní a jednoznačné signalizování způsobu, jakým jsou komponenty služby doručovány přes IP skupinové vysílání v rámci přenašeče MBMS. Poskytuje jasnou smlouvu mezi poskytovatelem služby (BM-SC) a přijímačem (UE), detailně popisující, které IP toky nesou které části obsahu. To je zásadní ve vysílacím prostředí, kde UE nemůže žádat o opakovaný přenos; musí být schopno správně identifikovat a sestavit všechny části služby z vysílacího přenosu. Standardizací tohoto popisu v dokumentu 3GPP TS 26.917 zajišťuje, že jakékoli kompatibilní UE může dekódovat služby z jakékoli kompatibilní sítě, čímž podporuje konkurenční ekosystém pro poskytovatele vysílacích služeb a výrobce zařízení.

Jeho vytvoření bylo motivováno snahou průmyslu o konvergované doručování médií, kde jsou kombinovány vysílací a širokopásmové (jednosměrné) cesty. S-TSID poskytuje nezbytný metadatový základ pro takové hybridní modely doručování, umožňující funkce jako bezproblémové přepínání mezi vysíláním a jednosměrným přenosem pro komponentu služby. Abstrahuje přenosové detaily, což umožňuje aplikacím vyšší vrstvy se soustředit na prezentaci obsahu, zatímco middleware se stará o složitost připojování ke správným skupinovým skupinám a aplikaci specifikovaného FEC. Tato abstrakce je klíčovým prvkem pro škálovatelné doručování lineárního a obsah na vyžádání masivním publikům, což je základním požadavkem moderních vysílacích služeb v 4G a 5G.

## Klíčové vlastnosti

- Definuje mapování mezi komponentami služby MBMS a jejich přenosovými relacemi (TSI)
- Specifikuje parametry síťové vrstvy včetně zdrojových/cílových IP adres a portů
- Podporuje popis přidružených schémat Forward Error Correction (FEC) pro spolehlivost
- Umožňuje selektivní příjem komponent služby zařízením UE pro efektivitu využití prostředků
- Doručován prostřednictvím oznámení služby nebo v rámci protokolu FLUTE/ALC pro doručování souborů
- Usnadňuje dynamickou adaptaci služby a hybridní modely doručování kombinující vysílání a širokopásmový přenos

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [S-TSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-tsid/)
