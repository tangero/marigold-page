---
slug: "mit"
url: "/mobilnisite/slovnik/mit/"
type: "slovnik"
title: "MIT – Management Information Tree"
date: 2025-01-01
abbr: "MIT"
fullName: "Management Information Tree"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mit/"
summary: "Hierarchický, stromově strukturovaný datový model, který organizuje spravované objekty a jejich atributy v systému správy sítě. Slouží jako základní schéma pro reprezentaci konfiguračních, stavových a"
---

MIT je hierarchický, stromově strukturovaný datový model, který organizuje spravované objekty a jejich atributy v systému správy sítě 3GPP.

## Popis

Strom správy informací (Management Information Tree – MIT), známý také jako pojmenovací strom, je konceptuální datová struktura tvořící páteř informačního modelu spravované sítě. V kontextu specifikací 3GPP, zejména pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)), MIT definuje, jak jsou všechny spravovatelné prostředky – jako základnové stanice, uzly jádra sítě, softwarové funkce a logická propojení – reprezentovány a přístupné správnímu systému. Strom se skládá z uzlů, kde každý uzel reprezentuje spravovaný objekt (Managed Object – [MO](/mobilnisite/slovnik/mo/)). MO je abstrakcí fyzického nebo logického prostředku, který lze spravovat. Každý MO má atributy, které uchovávají jeho data (např. provozní stav, hodnoty čítačů), akce, které na něm lze vyvolat, a oznámení, která může generovat.

Hierarchická struktura MIT je klíčová pro škálovatelnost a organizaci. Kořenem stromu je systém správy nejvyšší úrovně. Pod ním se větve vytvářejí na základě vztahů obsahování. Například objekt spravovaného prvku (Managed Element – [ME](/mobilnisite/slovnik/me/)) reprezentující fyzický síťový uzel může obsahovat více objektů zařízení (Equipment) (pro hardwarové jednotky), které zase obsahují objekty fyzických portů (Physical Port). Tento vztah rodič–potomek umožňuje efektivní navigaci a vymezení rozsahu správních operací. Se systémem MIT interagují správní protokoly, jako je Common Management Information Protocol ([CMIP](/mobilnisite/slovnik/cmip/)) ze sady Telekomunikační správní sítě ([TMN](/mobilnisite/slovnik/tmn/)) nebo častěji používaný Simple Network Management Protocol ([SNMP](/mobilnisite/slovnik/snmp/)). Správci (systémy správy sítě) provádějí operace jako GET pro získání hodnoty atributu, [SET](/mobilnisite/slovnik/set/) pro změnu konfigurace nebo CREATE/DELETE pro vytvoření nebo odstranění MO ve stromu.

Z architektonického pohledu je MIT implementován v každém spravovaném síťovém prvku v tzv. bázi správy informací (Management Information Base – [MIB](/mobilnisite/slovnik/mib/)). MIB je skutečná implementačně specifická databáze, která uchovává aktuální hodnoty atributů MO podle schématu definovaného MIT. Specifikace 3GPP, například z řady 32 (Telekomunikační správa), definují standardizovaná schémata MIT pro různé síťové domény (např. správu poruch, správu výkonnosti). Tato standardizace zajišťuje, že síť s více dodavateli může být spravována jednotně. Správce komunikuje s agentním softwarem na síťovém prvku, který překládá požadavky protokolu na čtení nebo zápis do lokální MIB, čímž efektivně prochází a manipuluje s lokální instancí MIT.

## K čemu slouží

Strom správy informací (MIT) existuje proto, aby vnesl řád a standardizaci do komplexního úkolu správy telekomunikačních sítí. Před takovými strukturovanými modely byla rozhraní správy často proprietární, což ztěžovalo a prodražovalo integraci zařízení od různých dodavatelů do jediného systému správy. MIT tento problém řeší tím, že poskytuje společný hierarchický rámec pro reprezentaci čehokoli, co je třeba spravovat, od jedné hardwarové komponenty po celou virtualizovanou síťovou funkci.

Historicky byl tento koncept silně ovlivněn modelem správy systémů OSI a rámcem ITU-T TMN, které byly pro mobilní sítě přijaty a adaptovány 3GPP. Jak sítě rostly z jednoduchých hlasových ústředen na komplexní paketové systémy s mnoha typy uzlů, stal se standardizovaný model správy nezbytným pro provozní efektivitu. MIT řešil omezení ad-hoc rozhraní správy definováním konzistentního objektově orientovaného paradigmatu, kde je každý prostředek modelován se známou sadou atributů a chování. To umožňuje vývoj obecných správních aplikací, které mohou konfigurovat, monitorovat a řešit problémy jakéhokoli síťového prvku, který dodržuje standardizované schéma MIT.

Motivací pro jeho specifikaci v dokumentech jako 3GPP TS 32.622 (Generic Network Resource Model) bylo umožnit automatizované, rozsáhlé síťové operace. Díky předvídatelné stromové struktuře mohou systémy správy programově objevovat topologii sítě, aplikovat hromadné změny konfigurace a korelovat alarmy. To je zásadní pro dosažení klíčových provozních cílů, jako je nasazení typu plug-and-play, vlastní konfigurace a uzavřená automatizace, které jsou obzvláště kritické pro moderní softwarově definované a virtualizované sítě 5G. MIT tedy není jen datovým modelem, ale umožňuje efektivní a nákladově efektivní správu životního cyklu sítě.

## Klíčové vlastnosti

- Hierarchická stromová struktura organizující spravované objekty (MO) podle vztahu obsahování
- Definuje schéma pro třídy spravovaných objektů, jejich atributy, akce a oznámení
- Poskytuje standardizovaný jmenný prostor pro jednoznačnou identifikaci jakéhokoli spravovaného prostředku
- Umožňuje vymezení rozsahu správních operací (např. ovlivnění všech objektů v podstromu)
- Tvoří konceptuální základ pro implementaci báze správy informací (MIB)
- Podporuje správní protokoly (CMIP, SNMP) pro operace vytvoření, čtení, aktualizace a odstranění (CRUD)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM

---

📖 **Anglický originál a plná specifikace:** [MIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mit/)
