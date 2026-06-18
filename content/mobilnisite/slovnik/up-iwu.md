---
slug: "up-iwu"
url: "/mobilnisite/slovnik/up-iwu/"
type: "slovnik"
title: "UP-IWU – User Plane Interworking Unit"
date: 2025-01-01
abbr: "UP-IWU"
fullName: "User Plane Interworking Unit"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/up-iwu/"
summary: "UP-IWU je funkční entita, která usnadňuje interoperabilitu mezi různými generacemi mobilních jader sítí, konkrétně mezi 5G Core (5GC) a Evolved Packet Core (EPC). Překládá protokoly uživatelské roviny"
---

UP-IWU je funkční entita, která zprostředkovává interoperabilitu uživatelské roviny mezi 5G Core a 4G Evolved Packet Core překladem protokolů a přeposíláním dat pro plynulé soužití sítí.

## Popis

User Plane Interworking Unit (UP-IWU) je síťová funkce působící na úrovni uživatelské roviny, která umožňuje bezproblémovou kontinuitu datových relací a interoperabilitu mezi 5G Core Network (5GC) a 4G Evolved Packet Core (EPC). Funguje jako překladač protokolů a přeposílač dat, nacházející se v přenosové cestě uživatelské roviny mezi Radio Access Network (RAN) a jádrem sítě. V typickém scénáři interoperability, například když se UE připojuje přes 5G New Radio (NR), ale relace je ukotvena v 4G Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)), UP-IWU zajišťuje, že [GTP-U](/mobilnisite/slovnik/gtp-u/) tunely z RAN mohou být správně ukončeny a namapovány na příslušná rozhraní jádra sítě a verze GTP-U.

Z architektonického hlediska je UP-IWU často kolidována nebo integrována do bránové funkce, jako je User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC nebo Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) v EPC. Jejím hlavním úkolem je přizpůsobení mezi protokolem GTP-U používaným na rozhraní N3 (mezi 5G RAN a UPF) a protokolem GTP-U používaným na rozhraní S5/S8 (mezi SGW a PGW v EPC), nebo podobných kombinací. Zpracovává enkapsulaci a dekapsulaci paketů uživatelských dat, spravuje identifikátory koncových bodů tunelů ([TEID](/mobilnisite/slovnik/teid/)) a může provádět potřebné mapování parametrů QoS mezi různými modely QoS v 5G (QoS Flow) a 4G (EPS Bearer). UP-IWU zajišťuje správné směrování paketů mezi různými doménami jádra sítě bez ztráty konektivity.

Mezi klíčové komponenty její funkčnosti patří logika interoperability pro pole hlaviček GTP-U, schopnosti ukládání do vyrovnávací paměti během procedur předávání spojení a podpora operací s duálním zásobníkem. Její role je klíčová v architekturách nasazení 5G v nestandalone ([NSA](/mobilnisite/slovnik/nsa/)) režimu, jako je [EN-DC](/mobilnisite/slovnik/en-dc/), kde je 5G NR využíváno jako sekundární skupina buněk pro zvýšení datového výkonu, zatímco řídicí rovina zůstává ukotvena v LTE a EPC. UP-IWU umožňuje agregaci a rozdělování provozu uživatelské roviny mezi oběma RAN a jedním ukotvovacím bodem v jádru. Je to klíčový prvek pro zajištění kontinuity služeb během vývoje sítě, který operátorům umožňuje zavádět pokrytí 5G rádiovým přístupem bez okamžité modernizace celého jádra sítě, čímž usnadňuje nákladově efektivní a postupnou migrační cestu.

## K čemu slouží

UP-IWU byla vyvinuta k řešení praktických výzev mezisystémové mobility a souběžného provozu mezi 4G a 5G sítěmi během přechodného období. Po dokončení standardů 5G bylo zřejmé, že rozsáhlé nasazení plnohodnotného 5GC bude trvat a operátoři potřebovali způsob, jak okamžitě využít nové 5G rádiové prvky s použitím svých stávajících investic do EPC. To vedlo k nestandalone ([NSA](/mobilnisite/slovnik/nsa/)) režimu provozu, ale vytvořilo to technický problém: jak připojit uzel 5G RAN (gNB) používající nové zásobníky protokolů k 4G jádru sítě (EPC) navrženému pro LTE RAN. UP-IWU poskytuje potřebnou adaptační vrstvu k překlenutí této mezery.

Její vytvoření bylo motivováno potřebou standardizovaného, efektivního řešení interoperability, které se vyhne proprietárním branám a zajistí interoperabilitu mezi různými dodavateli. Před její specifikací často vyžadovala interoperabilita mezi různými generacemi sítí složité, nestandardní brány nebo nutila veškerý provoz procházet jediným typem jádra, což omezovalo flexibilitu nasazení. UP-IWU řeší konkrétní rozdíly v protokolech, jako jsou rozdíly ve verzích GTP-U, rozšiřujících hlavičkách a kontextech PDU session versus EPS bearer. Řeší problém kontinuity přenosové cesty uživatelské roviny, když se UE pohybuje mezi oblastmi pokrytí 4G a 5G nebo pracuje v režimu duální konektivity.

Zavedená v Rel-9 pro dřívější scénáře interoperability a výrazně vylepšená pro interoperabilitu 4G-5G v pozdějších vydáních, UP-IWU umožňuje klíčové strategie operátorů, jako je 'ukotvení v EPC' pro raná nasazení 5G. Umožňuje opětovné využití stávajících služeb paketového jádra, řízení politik a účtovacích systémů při zavádění nových rádiových schopností. To zkracuje dobu uvedení 5G služeb na trh a snižuje kapitálové výdaje. UP-IWU je v konečném důsledku přechodnou, ale nezbytnou síťovou funkcí, která podporuje dlouhodobé soužití a plynulou vývojovou cestu od EPC k 5GC a zajišťuje, že účastníci zažívají bezproblémové služby bez ohledu na generaci podkladového jádra sítě.

## Klíčové vlastnosti

- Interoperabilita protokolů mezi rozhraními 5GC N3 GTP-U a EPC S5/S8 GTP-U
- Podpora správy přenosové cesty uživatelské roviny ve scénářích interoperability 4G-5G a EN-DC
- Mapování mezi 5G QoS Flows a 4G EPS Bearers pro zpracování provozu
- Ukončuje a znovu vytváří GTP-U tunely mezi různými doménami jádra sítě
- Umožňuje přeposílání dat během předávání spojení mezi různými RAT a kontinuitu relací
- Často integrována v rámci síťových funkcí UPF nebo SGW

## Související pojmy

- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [UP-IWU na 3GPP Explorer](https://3gpp-explorer.com/glossary/up-iwu/)
