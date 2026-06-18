---
slug: "hes"
url: "/mobilnisite/slovnik/hes/"
type: "slovnik"
title: "HES – Hosted Enterprise Services"
date: 2025-01-01
abbr: "HES"
fullName: "Hosted Enterprise Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hes/"
summary: "HES je rámec 3GPP umožňující mobilním síťovým operátorům hostovat a poskytovat služby zaměřené na podniky prostřednictvím své infrastruktury. Umožňuje podnikům nabízet přizpůsobené hlasové služby, slu"
---

HES je rámec 3GPP umožňující mobilním operátorům hostovat a poskytovat přizpůsobené komunikační služby pro podniky, jako je hlas a zasílání zpráv, zaměstnancům využívajícím infrastrukturu sítě operátora.

## Popis

Hosted Enterprise Services (HES) je standardizovaný servisní rámec v rámci 3GPP, který umožňuje mobilnímu síťovému operátorovi ([MNO](/mobilnisite/slovnik/mno/)) hostovat telekomunikační služby pro podnik na infrastruktuře sítě tohoto operátora. Podnik v tomto modelu vystupuje jako poskytovatel služeb pro své vlastní zaměstnance nebo členy a využívá základní síťové funkce MNO bez nutnosti nasazovat vlastní fyzickou síť. Z architektonického hlediska zavádí HES koncept Hosted Enterprise Services Identity (HESID) a Hosted Enterprise Services User Identity (HESUID) pro jedinečnou identifikaci podniku a jeho uživatelů v rámci domény operátora. Síť MNO, konkrétně Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) v 5G, ukládá profily předplatitelů, které asociují uživatele s parametry jejich podnikových služeb. Když uživatel iniciuje službu, obslužná funkce Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) dotazuje data předplatitele, identifikuje příslušnost k HES a aplikuje specifickou servisní logiku a politiky definované pro daný podnik. To může zahrnovat specializované směrování hlasových hovorů (např. na firemní ústřednu - [PBX](/mobilnisite/slovnik/pbx/)), podnikově specifické krátké kódy pro zasílání zpráv, funkce uzavřené skupiny uživatelů a přizpůsobené politiky přístupu k datům. Rámec se opírá o standardní rozhraní 3GPP, jako je rozhraní Sh mezi aplikačním serverem ([AS](/mobilnisite/slovnik/as/)) hostujícím logiku podnikových služeb a HSS, a rozhraní Ut pro samoobslužnou správu služeb uživatelem. HES umožňuje operátorovi nabízet podniku oddělený, virtualizovaný výřez svých síťových schopností, podporující funkce jako centralizované firemní telefonní plány, zkrácené číslování a integraci s podnikovými IP-PBX systémy přes IP Multimedia Subsystem (IMS).

## K čemu slouží

HES byl vytvořen, aby řešil rostoucí poptávku podniků po větší kontrole a přizpůsobení komunikačních služeb pro svou pracovní sílu, a zároveň se vyhnul kapitálovým a provozním výdajům spojeným s nasazením a správou soukromého jádra mobilní sítě. Před HES podniky často spoléhaly na základní mobilní hlasové a datové tarify nebo nasazovaly izolovaná řešení Fixed-Mobile Convergence ([FMC](/mobilnisite/slovnik/fmc/)), která byla složitá a nestandardizovaná. To vedlo k roztříštěným uživatelským zkušenostem a omezené integraci s veřejnou mobilní sítí. Standardizovaný rámec HES od 3GPP, zavedený ve vydání 12, poskytuje jasný, operátorem hostovaný model, který tyto problémy řeší. Umožňuje MNO zpeněžit své síťové investice nabídkou přidaných, značkových podnikových služeb, čímž zvyšuje průměrný výnos na uživatele (ARPU) a loajalitu zákazníků. Pro podniky řeší problém poskytování konzistentní, funkčně bohaté a bezpečné komunikační zkušenosti mobilním zaměstnancům, která se bezproblémově integruje s jejich stávajícími telefonními a IT systémy. Historický kontext zahrnuje vývoj služeb Centrex ve fixních sítích a jejich rozšíření do mobilní oblasti, přičemž HES představuje plnou, standardizovanou mobilní podobu. Řeší omezení dřívějších proprietárních hostovaných řešení tím, že zajišťuje interoperabilitu mezi sítěmi různých operátorů a uživatelskými zařízeními, a podporuje tak konkurenční trh podnikových komunikačních služeb.

## Klíčové vlastnosti

- Operátorem hostovaná servisní platforma umožňující podnikům vystupovat jako poskytovatelé mobilních služeb
- Jedinečné identifikátory (HESID/HESUID) pro rozlišení podniku a uživatele v síti operátora
- Integrace s IMS pro umožnění IP-based podnikových hlasových, video a messaging služeb
- Podpora podnikově specifické servisní logiky a řízení politik prostřednictvím standardních rozhraní 3GPP
- Umožňuje funkce jako uzavřené skupiny uživatelů, zkrácené vytáčení a integrace s podnikovými PBX
- Umožňuje samoobslužnou provizi a správu podnikových služeb uživatelem prostřednictvím rozhraní Ut

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [PBX – Private Branch eXchange](/mobilnisite/slovnik/pbx/)

## Definující specifikace

- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [HES na 3GPP Explorer](https://3gpp-explorer.com/glossary/hes/)
