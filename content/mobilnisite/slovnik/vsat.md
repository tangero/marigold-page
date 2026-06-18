---
slug: "vsat"
url: "/mobilnisite/slovnik/vsat/"
type: "slovnik"
title: "VSAT – Very Small Aperture Terminal"
date: 2026-01-01
abbr: "VSAT"
fullName: "Very Small Aperture Terminal"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/vsat/"
summary: "Kompaktní terminál pro satelitní komunikaci s malou anténou, typicky o průměru do 2,4 metrů. V rámci 3GPP se tento termín vztahuje k integraci takových terminálů jako uživatelského zařízení (UE) nebo"
---

VSAT je kompaktní terminál pro satelitní komunikaci s malou anténou, používaný v 3GPP jako uživatelské zařízení nebo síťové uzly pro Neterestrické sítě (NTN) za účelem umožnění přímé satelitní konektivity.

## Popis

Very Small Aperture Terminal (VSAT) je obousměrná pozemní satelitní stanice charakterizovaná malou parabolickou anténou, obvykle o průměru od 0,75 do 2,4 metrů. V rámci architektury 3GPP, počínaje Release 15, jsou VSATy považovány za typ uživatelského zařízení (UE) nebo za pevné síťové uzly pro integraci Neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)). Specifikace, včetně TS 38.101 (rádiové specifikace UE), 38.304 (procedury UE), 38.306 ([RF](/mobilnisite/slovnik/rf/) požadavky UE), 38.331 (protokol [RRC](/mobilnisite/slovnik/rrc/)) a studijních položek NTN (38.811, 38.821), definují úpravy potřebné pro provoz VSAT jako součásti 3GPP rádiové přístupové sítě.

Architektonicky se VSAT fungující jako UE skládá z venkovní jednotky (ODU) – která zahrnuje parabolickou anténu, blokový převodník (BUC) a konvertor LNB – a vnitřní jednotky (IDU), což je modem/směrovač propojující se s uživatelskými zařízeními. V kontextu 3GPP NTN tento VSAT komunikuje se satelitem, který funguje jako přenosový článek nebo základnová stanice (např. gNB v 5G). Satelit je připojen k pozemní bránové stanici, která je následně propojena s 5G jádrem sítě. Klíčové technické úpravy pro provoz v 3GPP zahrnují vylepšené mechanismy časového předstihu pro kompenzaci velkého přenosového zpoždění (až stovky milisekund na geostacionární dráze), modifikované procedury náhodného přístupu, robustní schémata modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) pro zvládnutí náročného přenosového poměru a specifický management mobility pro buňky pohybující se se satelitní stopou.

Princip fungování spočívá v tom, že VSAT naváže rádiové spojení se satelitem pomocí vyhrazených frekvenčních pásem, jako jsou pásma L, S, C, Ku nebo Ka, jak je studováno v 3GPP. VSAT implementuje 3GPP protokolový zásobník UE, včetně vrstvy řízení rádiových prostředků (RRC). Kvůli dlouhému zpoždění mohou být protokoly jako Hybridní automatický požadavek na opakování ([HARQ](/mobilnisite/slovnik/harq/)) provozovány v režimu s redukovanou zpětnou vazbou nebo deaktivovány. VSAT musí také zvládat velké Dopplerovy posuvy způsobené pohybem satelitu (na negeostacionárních drahách) a potenciálně pracovat v režimu s omezeným výkonem, což vyžaduje účinné zesílení výkonu. Jeho úlohou je poskytovat širokopásmové připojení ve vzdálených, námořních nebo leteckých scénářích, kde jsou pozemní sítě nedostupné nebo nespolehlivé, čímž efektivně rozšiřuje pokrytí služeb 5G po celém světě. Umožňuje služby jako přenosovou síť pro vzdálené základnové stanice, přímou satelitní komunikaci se zařízeními a konektivitu internetu věcí (IoT) v izolovaných oblastech.

## K čemu slouží

Integrace VSAT technologie do standardů 3GPP byla motivována potřebou poskytnout všudypřítomné, globální pokrytí pro 5G a budoucí sítě. Tradiční pozemní sítě mají ekonomická a geografická omezení, což zanechává rozsáhlé oblasti – jako jsou oceány, pouště, polární regiony a odlehlé venkovské komunity – bez pokrytí. Satelitní komunikace prostřednictvím VSATů tyto oblasti dlouhodobě obsluhuje, ale jako samostatné, neintegrované systémy. Účelem standardizace VSAT jako typu 3GPP UE je překlenout tuto propast a vytvořit jednotný, bezproblémový uživatelský zážitek, kde je satelitní přístup nativní součástí mobilní sítě.

Historický kontext představuje vývoj směrem k Neterestrickým sítím ([NTN](/mobilnisite/slovnik/ntn/)) jako klíčové pracovní položce 3GPP od Release 15 dále. Předchozí generace mobilních sítí měly pro integraci se satelity omezenou nebo žádnou standardizaci. Nástup nových satelitních konstelací (nízká oběžná dráha – [LEO](/mobilnisite/slovnik/leo/), střední oběžná dráha – [MEO](/mobilnisite/slovnik/meo/)) nabízejících nižší latenci a vyšší propustnost učinil tuto integraci technicky a komerčně životaschopnou. Standardizace 3GPP řeší specifické problémy integrace satelitních spojení do systému navrženého pro pozemní buňky: extrémní přenosová zpoždění, vysoké Dopplerovy posuvy, pohyblivé buňky a náročné přenosové poměry. Definováním požadavků a úprav pro VSAT ve specifikacích jako 38.306 a 38.331 řeší 3GPP problém interoperability, což umožňuje jediný návrh zařízení pro přístup k pozemním i satelitním sítím pod společnou protokolovou střechou.

Tento vývoj byl hnány případy použití, jako jsou připojené lodě a letadla, odolnost při katastrofách, kdy je pozemní infrastruktura poškozena, a rozsáhlé sítě senzorů IoT v zemědělství nebo monitorování životního prostředí. Umožňuje mobilním operátorům rozšířit své portfolio služeb bez nutnosti budovat infrastrukturu v nerentabilních oblastech. Nakonec začlenění VSAT do 3GPP naplňuje vizi skutečně globální konektivity, podporuje ekonomický rozvoj, bezpečnostní služby a překlenuje digitální propast tím, že zpřístupňuje služby 5G kdekoliv na Zemi.

## Klíčové vlastnosti

- Kompaktní satelitní terminál s anténou typicky do 2,4 metru
- Funguje jako 3GPP uživatelské zařízení (UE) pro Neterestrické sítě (NTN)
- Podporuje frekvenční pásma včetně L, S, C, Ku a Ka pro satelitní spoje
- Implementuje úpravy pro dlouhá přenosová zpoždění a Dopplerův posuv
- Umožňuje globální pokrytí pro vzdálenou, námořní a leteckou konektivitu
- Může fungovat jako pevný bezdrátový přístupový bod nebo mobilní UE

## Definující specifikace

- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks

---

📖 **Anglický originál a plná specifikace:** [VSAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/vsat/)
