---
slug: "ioc"
url: "/mobilnisite/slovnik/ioc/"
type: "slovnik"
title: "IOC – Information Object Class"
date: 2026-01-01
abbr: "IOC"
fullName: "Information Object Class"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ioc/"
summary: "IOC je koncept správy v 3GPP definující šablonu pro spravované objekty v systémech správy sítě. Specifikuje atributy, notifikace a chování pro reprezentaci síťových prostředků. To umožňuje standardizo"
---

IOC je koncept správy v 3GPP, který definuje šablonu pro spravované objekty. Tato šablona specifikuje jejich atributy, notifikace a chování, aby umožnila standardizovanou správu sítí s více dodavateli.

## Popis

Information Object Class (IOC) je základní konstrukt v rámci architektury správy sítí 3GPP, zejména v modelu FCAPS (Fault, Configuration, Accounting, Performance, and Security). IOC slouží jako šablona nebo schéma, které definuje strukturu a sémantiku spravovaných objektů. Tyto objekty jsou softwarové abstrakce reprezentující fyzické nebo logické síťové prostředky, jako jsou síťové elementy, funkce nebo služby. Každá IOC specifikuje sadu atributů (vlastností), akcí (operací, které lze vyvolat), notifikací (vysílaných událostí) a chování (pravidel řídících objekt). Spravované objekty jsou instancemi IOC naplněnými konkrétními hodnotami a nacházejí se v bázi Management Information Base ([MIB](/mobilnisite/slovnik/mib/)) přístupné přes rozhraní správy, jako je Itf-N nebo OAM rozhraní.

Architektura správy založené na IOC zahrnuje hierarchickou dědičnost tříd, kde lze IOC odvodit z nadřazených tříd, čímž dědí a rozšiřují jejich definice. Tento objektově orientovaný přístup podporuje znovupoužitelnost a konzistenci. Mezi klíčové komponenty patří definice IOC v dokumentech specifikací (např. řady 3GPP TS 28.xxx a 32.xxx), podpůrné protokoly správy (např. SNMP, [CORBA](/mobilnisite/slovnik/corba/) nebo RESTful [API](/mobilnisite/slovnik/api/) v novějších vydáních) a paradigmata agent-správce, kde spravované objekty implementují síťové elementy a přistupují k nim systémy správy. IOC pokrývají široké spektrum entit, od fyzického vybavení, jako jsou základnové stanice, až po logické funkce, jako jsou síťové řezy nebo QoS toky.

V provozu umožňují IOC standardizované operace správy, jako je monitorování výkonnostních čítačů, konfigurace parametrů, příjem alarmů poruch a audit využití. Například IOC pro gNB by definovala atributy pro Cell ID, vysílací výkon a statistiky spojení, akce pro reset nebo aktualizaci softwaru a notifikace pro selhání spoje. Dodržováním definic IOC výrobci zajišťují interoperabilitu, což umožňuje operátorům sítí bezproblémově spravovat nasazení s více dodavateli. IOC jsou klíčové pro Self-Organizing Networks (SON) 3GPP, správu síťových řezů a zajištění služeb 5G, neboť poskytují jednotný informační model pro celý životní cyklus sítě.

## K čemu slouží

IOC byla vyvinuta k řešení výzev spojených se správou složitých telekomunikačních sítí s více dodavateli. Před standardizací používal každý výrobce proprietární informační modely, což ztěžovalo integraci a jednotnou správu a zvyšovalo náklady. Koncept IOC, vycházející ze systémů správy [ITU-T](/mobilnisite/slovnik/itu-t/) TMN a [OSI](/mobilnisite/slovnik/osi/), poskytuje společný jazyk pro popis síťových prostředků, čímž umožňuje interoperabilitu a snižuje provozní náklady.

Mezi hlavní řešené problémy patří fragmentace v reprezentaci dat správy a nedostatek konzistence napříč různými síťovými doménami. IOC usnadňují automatizovanou správu, která je nezbytná pro škálování 5G sítí s obrovským počtem zařízení a dynamických služeb. Podporují funkce FCAPS tím, že zajišťují, aby všechny spravované entity vystavovaly konzistentní sadu atributů a chování. Historicky, jak se sítě vyvíjely od 2G k 5G, se rozsah IOC rozšířil od základní správy síťových elementů tak, aby zahrnoval virtualizované síťové funkce, správu služeb end-to-end a síťové řezy. Tento vývoj byl motivován potřebou agilních, softwarově řízených sítí, kde musí být správa stejně flexibilní a škálovatelná jako samotné služby.

## Klíčové vlastnosti

- Objektově orientovaná šablona pro spravované objekty s dědičností
- Standardizované atributy, akce a notifikace pro síťové prostředky
- Podpora interoperability více dodavatelů v rámci OAM
- Integrace s protokoly správy (např. SNMP, RESTCONF)
- Základ pro SON automatizaci a správu založenou na politikách
- Komplexní pokrytí od fyzických po virtualizované síťové funkce

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)

## Definující specifikace

- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 28.602** (Rel-12) — CN & non-3GPP NRM IRP Information Service
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.611** (Rel-19) — EPC-WLAN Interworking NRM IRP Requirements
- **TS 28.612** (Rel-19) — EPC and non-3GPP interworking NRM IRP IS
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.621** (Rel-19) — Generic Network Resource Model (NRM) IRP Requirements
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- … a dalších 104 specifikací

---

📖 **Anglický originál a plná specifikace:** [IOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ioc/)
