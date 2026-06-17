---
slug: "cds"
url: "/mobilnisite/slovnik/cds/"
type: "slovnik"
title: "CDS – Content Distribution Service"
date: 2025-01-01
abbr: "CDS"
fullName: "Content Distribution Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cds/"
summary: "Rámec služeb 3GPP pro efektivní distribuci obsahu v mobilních sítích. Umožňuje optimalizované doručování multimediálního obsahu, jako je video, audio a aplikace, k uživatelům využitím ukládání do mezi"
---

CDS je rámec služeb 3GPP pro efektivní distribuci obsahu v mobilních sítích, který využívá ukládání do mezipaměti a mechanismy zohledňující stav sítě k distribuci multimediálního obsahu a snížení zahlcení.

## Popis

Content Distribution Service (CDS, služba distribuce obsahu) je komplexní rámec v rámci specifikací 3GPP navržený pro usnadnění efektivní a inteligentní distribuce digitálního obsahu v mobilních sítích. Služba řeší základní výzvy spojené s doručováním náročného multimediálního obsahu, jako je streamování videa, aktualizace softwaru a velké soubory, potenciálně milionům mobilních účastníků. Její architektura je postavena na konceptu přiblížení obsahu uživateli prostřednictvím strategického umístění v topologii sítě, čímž se minimalizuje latence, snižuje zatížení přenosové sítě jádra (backhaul) a optimalizuje celkové využití rádiových zdrojů.

Technické fungování CDS zahrnuje několik klíčových komponent pracujících souběžně. Ústředním prvkem je Content Distribution Manager ([CDM](/mobilnisite/slovnik/cdm/)), který řídí distribuční strategii, spravuje metadata obsahu a komunikuje s dalšími síťovými entitami, jako jsou Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) a Serving GPRS Support Node (SGSN) v dřívějších vydáních. Obsah je ukládán a poskytován z distribuovaných uzlů mezipaměti, často nasazených na okraji sítě, například v rámci rádiové přístupové sítě (RAN) nebo v agregacích. Tyto mezipaměti inteligentně ukládají populární obsah na základě vzorců využití. Když uživatel požádá o obsah, síť může přesměrovat požadavek na blízkou mezipaměť, pokud je obsah dostupný; tento proces je často usnadněn transparentními nebo proxy-based přesměrovacími mechanismy definovanými v rámci tohoto služebního rámce.

CDS dále zahrnuje schopnosti adaptace obsahu. S ohledem na různorodost uživatelských zařízení (s různými velikostmi obrazovky, podporou kodeků a výpočetním výkonem) a síťových podmínek (dostupná šířka pásma, síla signálu) může služba obsah dynamicky převádět (transkódovat) nebo měnit jeho datový tok (transratovat). Například stream videa ve vysokém rozlišení může být upraven na nižší rozlišení pro zařízení v přetížené okrajové části buňky. Tuto adaptaci typicky řídí specializované Media Adaptation Functions. Služba také definuje rozhraní a protokoly pro provisioning obsahu, synchronizaci mezipaměti a reporting, čímž zajišťuje, že původci obsahu mohou obsah vkládat do distribuční sítě a získávat analytické údaje o jeho spotřebě.

V širším síťovém ekosystému hraje CDS klíčovou roli při umožnění škálovatelných služeb mobilního širokopásmového přístupu. Proměňuje síť z jednoduchého přenosového kanálu na platformu pro distribuci obsahu s povědomím o jeho charakteru. Vyloučením opakujícího se provozu z jádra sítě a zkrácením přenosové vzdálenosti dat přímo přispívá k nižší latenci, což je zásadní pro interaktivní služby a živé streamování. Tento rámec také vytváří základ pro pozdější technologie, jako je Mobile Edge Computing ([MEC](/mobilnisite/slovnik/mec/)) a spolupráce s content delivery network ([CDN](/mobilnisite/slovnik/cdn/)), a stanovuje rané principy inteligence na okraji sítě a síťové optimalizace obsahu, které jsou ústřední pro moderní poskytování služeb v 5G.

## K čemu slouží

CDS byl vytvořen pro řešení blížící se „datové tsunami“, která byla předpovídána s nástupem mobilního internetu a multimediálních služeb na konci 90. let a začátkem roku 2000. Před jeho standardizací byly mobilní sítě navrženy primárně pro hlas a nízkorychlostní data. Doručování oblíbeného videa nebo softwarových souborů znamenalo načítání každého bajtu ze vzdáleného původního serveru pro každého jednotlivého uživatele, což kladlo obrovskou a neudržitelnou zátěž na přenosovou část jádra sítě a mezinárodní spoje. Tento přístup vedl k vysoké latenci, špatnému uživatelskému zážitku během špičky a neefektivnímu využití drahého rádiového spektra. Služba byla motivována potřebou učinit distribuci obsahu ekonomicky životaschopnou a technicky škálovatelnou s růstem adopce mobilních dat.

Historickým kontextem byl přechod od dominance okruhově přepínaných sítí 2G (GSM) k paketově přepínaným sítím 2,5G/3G ([GPRS](/mobilnisite/slovnik/gprs/), UMTS) schopným vyšších přenosových rychlostí. To umožnilo nové služby, ale také odhalilo limity centralizovaného modelu přístupu k internetu. CDS poskytlo standardizovaný rámec pro síťové operátory, aby mohli nasazovat ukládání do mezipaměti a adaptaci obsahu, a posunulo se tak za proprietární, na dodavatelích závislá řešení. Vyřešilo problém zahlcení sítě inteligentní replikací obsahu na jejím okraji, čímž šetřilo kapacitu přenosové sítě (backhaul). Dále řešilo výzvu heterogenity zařízení zavedením standardizovaných metod, pomocí kterých síť mohla přizpůsobovat formát obsahu a datový tok, a zajistila tak použitelný zážitek napříč širokým spektrem mobilních zařízení a síťových podmínek, což byla významná překážka pro adopci služeb.

Vytvořením společné servisní architektury umožnilo CDS od 3GPP operátorům, poskytovatelům obsahu a výrobcům zařízení vzájemně spolupracovat a podporovat tak ekosystém pro mobilní obsah. Položilo základy pro efektivní doručování služeb, které definovaly mobilní zážitek, od streamované hudby a videa po bezdrátové aktualizace zařízení. Rámec přímo řešil ekonomická a technická omezení, která by mohla potlačit růst mobilních dat, a zajistil, že síťová infrastruktura se mohla vyvíjet tak, aby efektivně zvládala poptávku, a to nejen pouhým navyšováním surové šířky pásma.

## Klíčové vlastnosti

- Síťové ukládání obsahu do mezipaměti na strategických místech (např. na okraji RAN)
- Dynamická adaptace obsahu (transkódování, změna datového toku) pro různá zařízení a síťové podmínky
- Mechanismy směrování a přesměrování požadavků na lokální mezipaměti
- Standardizovaná rozhraní pro provisioning a správu obsahu
- Podpora různých typů obsahu včetně streamovaných médií a souborů
- Integrace s prvky jádra sítě pro řízení politik a účtování

## Definující specifikace

- **TR 22.906** (Rel-19) — IMS P2P Content Distribution Services
- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cds/)
