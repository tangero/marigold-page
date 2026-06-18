---
slug: "cs-gw"
url: "/mobilnisite/slovnik/cs-gw/"
type: "slovnik"
title: "CS-GW – Circuit Switched Gateway"
date: 2025-01-01
abbr: "CS-GW"
fullName: "Circuit Switched Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cs-gw/"
summary: "Circuit Switched Gateway je síťový prvek, který zajišťuje spolupráci mezi okruhově komutovanou doménou 3GPP a externími okruhově komutovanými sítěmi. Umožňuje pokračující fungování hlasových a staršíc"
---

CS-GW je síťový prvek, který zajišťuje spolupráci mezi okruhově komutovanou doménou 3GPP a externími okruhově komutovanými sítěmi za účelem zachování kontinuity služeb během přechodu na paketově komutované architektury.

## Popis

Circuit Switched Gateway (CS-GW) je klíčový síťový prvek v architekturách 3GPP, který slouží jako rozhraní mezi okruhově komutovanou doménou jádra mobilní sítě a externími okruhově komutovanými sítěmi, především veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)) a sítí [ISDN](/mobilnisite/slovnik/isdn/). Z architektonického hlediska CS-GW funguje jako signalizační a mediální brána, která překládá mezi různými protokoly a transportními technologiemi. Působí v rámci domény jádra sítě (CN) a rozhraní se strany mobilní sítě s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a na straně externí sítě s ústřednami PSTN/ISDN.

CS-GW plní několik klíčových funkcí, včetně převodu protokolů mezi mobilními signalizačními protokoly (jako jsou BICC nebo [ISUP](/mobilnisite/slovnik/isup/)) a signalizačními protokoly PSTN/ISDN, převodu mediálních proudů mezi okruhově komutovanými [TDM](/mobilnisite/slovnik/tdm/) (Time Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)) hlasovými kanály a paketovým přenosem hlasu a řízení přenosu pro navazování, udržování a uvolňování hlasových spojení. Brána zpracovává jak signalizaci řídicí roviny, tak provoz uživatelské roviny, čímž zajišťuje správnou spolupráci mezi různými síťovými doménami. Podporuje různé kodeky a v případě potřeby i funkce překódování, aby vyhověla různým formátům kódování hlasu mezi sítěmi.

Z hlediska síťové integrace se CS-GW typicky připojuje k MSC prostřednictvím standardních rozhraní, jako je A-interface nebo Iu-CS interface, v závislosti na konkrétní síťové architektuře a vydání 3GPP. Na straně PSTN se připojuje prostřednictvím standardních telefonních rozhraní, jako jsou E1/T1 trunky nebo přes spoje signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)). Brána spravuje směrování hovorů, sběr informací pro účtování a podporu doplňkových služeb při zachování kvality služeb očekávané od tradičních telefonních sítí. Její implementace umožňuje mobilním operátorům využívat stávající infrastrukturu PSTN při zavádění novějších paketových mobilních sítí.

CS-GW hraje klíčovou roli ve vývoji sítí tím, že umožňuje postupný přechod z okruhově komutovaných na paketově komutované architektury. Umožňuje operátorům udržovat hlasové služby pro starší mobilní zařízení a zároveň zavádět novější paketové služby. Brána také podporuje různé regulatorní požadavky, jako je zákonné odposlouchávání a služby tísňového volání, tím, že poskytuje potřebná rozhraní a schopnosti očekávané v tradičních telefonních sítích. Její návrh zajišťuje, že uživatelé zaznamenávají bezproblémové hlasové služby bez ohledu na to, zda jejich hovory končí v paketově nebo okruhově komutovaných doménách.

## K čemu slouží

CS-GW byl vytvořen, aby řešil základní výzvu spolupráce mezi vznikajícími mobilními sítěmi 3GPP a rozsáhlou stávající globální infrastrukturou [PSTN](/mobilnisite/slovnik/pstn/). Když byly sítě 3GPP poprvé standardizovány, většina hlasového provozu na světě byla přenášena přes okruhově komutované sítě a úplná náhrada této infrastruktury nebyla praktická ani ekonomicky proveditelná. CS-GW poskytl potřebný most, který umožnil mobilním operátorům zavádět nové sítě a zároveň udržovat připojení ke globální telefonní síti.

Historicky telekomunikační průmysl procházel významným přechodným obdobím, kdy nové paketové technologie koexistovaly se staršími okruhově komutovanými systémy. CS-GW vyřešil problém nekompatibility protokolů a přenosu mezi těmito různými typy sítí. Bez takové brány by mobilní sítě byly izolovanými ostrovy neschopnými připojit se ke zavedené telefonní síti, což by vážně omezilo jejich užitečnost a přijetí. Brána umožnila operátorům využít jejich stávající investice do infrastruktury PSTN a zároveň postupně migrovat k efektivnějším paketově komutovaným architekturám.

Vytvoření CS-GW bylo motivováno potřebou zpětné kompatibility a kontinuity služeb. Rané mobilní sítě potřebovaly podporovat hlasové služby se stejnou spolehlivostí a kvalitou jako tradiční telefonie a zároveň zavádět nové datové služby. Brána řešila omezení předchozích přístupů, které buď vyžadovaly úplnou náhradu sítě, nebo poskytovaly nedostatečné schopnosti spolupráce. Standardizací CS-GW ve specifikacích 3GPP průmysl zajistil interoperabilitu mezi zařízeními od různých dodavatelů a konzistentní kvalitu služeb přes síťové hranice, což usnadnilo globální nasazení sítí 3GPP.

## Klíčové vlastnosti

- Převod protokolů mezi signalizací mobilní sítě a signalizací PSTN/ISDN
- Převod mediálních proudů mezi TDM okruhy a paketovým transportem
- Podpora více hlasových kodeků a schopností překódování
- Řízení přenosu pro navazování a správu hlasových spojení
- Sběr účtovacích dat a jejich korelace mezi síťovými doménami
- Rozhraní pro zákonný odposlech pro splnění regulatorních požadavků

## Související pojmy

- [MSS – Mobile Satellite Services](/mobilnisite/slovnik/mss/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CS-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs-gw/)
