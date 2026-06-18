---
slug: "uddi"
url: "/mobilnisite/slovnik/uddi/"
type: "slovnik"
title: "UDDI – Universal Description, Discovery and Integration"
date: 2025-01-01
abbr: "UDDI"
fullName: "Universal Description, Discovery and Integration"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uddi/"
summary: "Standard pro registr popisu, publikování a vyhledávání webových služeb, umožňující automatizovanou službu objevování a integrace. V 3GPP je používán v rámci funkce pro vystavení služeb (SCEF) a archit"
---

UDDI je standard pro registr popisu, publikování a vyhledávání webových služeb, používaný v rámci SCEF a NEF 3GPP pro správu síťových API a usnadnění ekosystémů pro vývojáře třetích stran.

## Popis

Universal Description, Discovery and Integration (UDDI) je nezávislá, na [XML](/mobilnisite/slovnik/xml/) založená specifikace registru pro výpis a vyhledávání webových služeb. V rámci architektury 3GPP, zejména od vydání Release 15, je přijata jako mechanismus pro službu objevování v rámci rámce vystavení síťových schopností. Primární architektonické komponenty jsou Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) v 5G Core a Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) v 4G Core. Tyto funkce fungují jako brány, které bezpečně vystavují síťové schopnosti a události autorizovaným aplikačním funkcím ([AF](/mobilnisite/slovnik/af/)) třetích stran. UDDI poskytuje standardizovaný způsob, jak tyto AF mohou zjistit, jaké služby nebo [API](/mobilnisite/slovnik/api/) jsou k dispozici.

Technicky obsahuje registr UDDI informace modelované v konkrétní datové struktuře. Ta zahrnuje 'businessEntity' (informace o poskytovateli služby, což může být síťový operátor), 'businessService' (logické seskupení souvisejících webových služeb), 'bindingTemplate' (technické detaily, jak službu vyvolat, včetně koncového bodu síťového API) a 'tModel' (technické modely, specifikace nebo klasifikace, jako jsou specifikace API definované 3GPP, např. rozhraní typu 'Nnef_'). Když NEF nebo SCEF publikuje novou síťovou schopnost jako službu, vytvoří v registru UDDI záznamy s těmito strukturovanými detaily.

Proces objevování funguje prostřednictvím UDDI Inquiry API. Vývojář aplikace nebo AF může dotazovat registr UDDI pomocí vyhledávacích kritérií (např. najít všechny služby určité kategorie nebo od konkrétního poskytovatele). Registr vrátí informace o vazbě, včetně [URL](/mobilnisite/slovnik/url/) koncového bodu a požadovaných odkazů na tModel. AF pak může tyto informace použít k navázání spojení se skutečným koncovým bodem služby (NEF) a začít vyvolávat síťová API, například žádat o kvalitu služby pro konkrétního uživatele nebo se přihlásit k odběru oznámení o událostech polohy. Tím se oddělí popis služby od její implementace, což umožňuje dynamickou a automatizovanou integraci.

Role UDDI je klíčová pro umožnění vývojářsky přívětivého ekosystému. Překračuje statickou dokumentaci API směrem k adresáři strojově objevitelnému. To je zvláště důležité v prostředích s více dodavateli a více operátory, protože umožňuje interoperabilitu a snižuje režii integrace. Registr může být hostován operátorem, třetí stranou nebo federovaným způsobem. Bezpečnost je prvořadá, přístup k registru UDDI je typicky chráněn mechanismy autentizace a autorizace, aby bylo zajištěno, že pouze autorizované entity mohou publikovat nebo objevovat citlivá síťová API.

## K čemu slouží

UDDI bylo vytvořeno k řešení základního problému objevování služeb v distribuovaném světě založeném na webových službách. Před existencí takových registrů vyžadovalo nalezení a integrace s webovou službou manuální procesy, komunikaci mimo pásmo a pevně zakódované [URL](/mobilnisite/slovnik/url/) koncových bodů, což bylo křehké a neškálovatelné. Původní motivací pro UDDI (mimo 3GPP) bylo vytvořit globální 'žluté stránky' pro webové služby, které by usnadnily elektronický obchod mezi podniky ([B2B](/mobilnisite/slovnik/b2b/)).

3GPP přijalo a specifikovalo UDDI k řešení konkrétní výzvy vystavení síťových API a rozvoje ekosystému. S nástupem programovatelnosti sítí a otevřených API (jak je například vidět v iniciativách jako GSMA Open Gateway) potřebovali operátoři standardizovaný způsob, jak mohou poskytovatelé aplikací třetích stran objevovat dostupné síťové schopnosti. Omezení pouhého publikování specifikací API na webové stránce je absence automatizace. UDDI poskytuje strojově čitelné, dotazovatelné rozhraní, které umožňuje automatickou konfiguraci klienta a dynamické navázání vazby, což je nezbytné pro škálovatelné cloud-nativní architektury a postupy DevOps.

Jeho integrace do 3GPP, počínaje Release 15, byla motivována potřebou plně realizovat službami řízenou architekturu (SBA) 5G. V SBA nabízejí síťové funkce služby navzájem. Rozšíření tohoto principu na externí aplikace vyžaduje robustní mechanismus objevování. UDDI tento problém řeší tím, že poskytuje dobře známý standard pro vytváření katalogu vystavených síťových služeb (jako je poloha zařízení, stav sítě, řízení QoS), čímž snižuje vstupní bariéru pro vývojáře a podporuje inovace ve vertikálních aplikacích pro IoT, podnikové a spotřebitelské služby.

## Klíčové vlastnosti

- Registr založený na XML pro publikování a vyhledávání webových služeb.
- Definované datové struktury: businessEntity, businessService, bindingTemplate a tModel.
- Poskytuje sady API pro dotazování (Inquiry) a publikování (Publishing) pro programovou interakci.
- Umožňuje dynamické navázání vazby mezi spotřebiteli služeb a jejich poskytovateli.
- Podporuje kategorizaci a taxonomii služeb prostřednictvím tModels.
- Usnadňuje vytváření federovaných registrů napříč administrativními doménami.

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [UDDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uddi/)
