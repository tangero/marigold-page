---
slug: "rbs"
url: "/mobilnisite/slovnik/rbs/"
type: "slovnik"
title: "RBS – Radio Base Station"
date: 2017-01-01
abbr: "RBS"
fullName: "Radio Base Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rbs/"
summary: "Rádiová základnová stanice (RBS) je síťový prvek, který poskytuje rádiové rozhraní pro uživatelské zařízení (UE) v buňkové síti. Zajišťuje rádiový přenos a příjem, modulaci/demodulaci a základní správ"
---

RBS (Rádiová základnová stanice) je síťový prvek poskytující rádiové rozhraní pro uživatelská zařízení, který zajišťuje rádiový přenos, příjem a základní správu zdrojů jako fyzický přístupový bod v buňkové síti.

## Popis

Rádiová základnová stanice (RBS) je základní komponentou rádiové přístupové sítě (RAN), konkrétně v sítích 3GPP UMTS (Universal Mobile Telecommunications System) a [HSPA](/mobilnisite/slovnik/hspa/) (High Speed Packet Access). Odpovídá prvku Node B v architektuře UMTS. RBS je zodpovědná za všechny rádiové funkce mezi uživatelským zařízením (UE) a jádrem sítě. Fyzicky se skládá z antén, transceiverů (TRX), zesilovačů, kombajnerů a jednotek pro zpracování základního pásma, které jsou často umístěny v skříni nebo přístřešku. V hierarchické architektuře UMTS RAN se připojuje k řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) prostřednictvím rozhraní Iub.

Provozně RBS vykonává kritické funkce, jako je modulace a demodulace rádiových signálů, kanálové kódování a dekódování, rozprostření a sběru pro [CDMA](/mobilnisite/slovnik/cdma/) (Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)), regulaci výkonu pro řízení interference a zpracování procedur fyzické vrstvy, jako je vyhledávání buněk a náhodný přístup. Spravuje rádiové zdroje jedné nebo více buněk a provádí příkazy od RNC pro nastavení rádiového přenosu, provedení předání spojení a dynamické přidělení kanálu. RBS také provádí měření na uplinkových signálech, jako je síla a kvalita přijímaného signálu, a hlásí je RNC pro optimalizaci sítě a rozhodování o mobilitě.

V síťovém ekosystému tvoří RBS buňku vzdušného rozhraní. Její strategie nasazení – včetně výběru místa, náklonu antény a vysílacího výkonu – určuje oblast pokrytí a kapacitu. Pokročilé implementace RBS podporují funkce jako Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)), agregace nosných a sofistikované režimy úspory energie. Zatímco ve 4G LTE a 5G NR je ekvivalentní funkce zajišťována prvky eNodeB a gNodeB (s integrovanou funkcionalitou RNC), termín RBS zůstává specificky spojen s infrastrukturou 3G UMTS/HSPA. Její spolehlivost a výkon jsou prvořadé, neboť je primárním kontaktním bodem pro připojení koncových uživatelů.

## K čemu slouží

Rádiová základnová stanice byla vytvořena, aby poskytla fyzické rádiové rozhraní pro sítě 3G UMTS, které umožnilo vysokorychlostní datové a hlasové služby. Před 3G používaly sítě 2G základnové přenosové stanice ([BTS](/mobilnisite/slovnik/bts/)) s odlišnými technologiemi vzdušného rozhraní, jako je [TDMA](/mobilnisite/slovnik/tdma/) v GSM. RBS byla navržena k implementaci širokopásmové [CDMA](/mobilnisite/slovnik/cdma/) (WCDMA) rádiové technologie specifikované 3GPP, která nabídla vyšší datové rychlosti, lepší spektrální účinnost a lepší podporu multimediálních služeb ve srovnání s 2G. Řešila problém poskytnutí standardizované, škálovatelné hardwarové platformy pro nasazení pokrytí 3G.

Architektura RBS oddělila funkce rádiového přenosu/příjmu (v RBS) od řídicí a správcovské inteligence (v RNC), což umožnilo centralizovanou správu rádiových zdrojů napříč více základnovými stanicemi. Tento hierarchický návrh řešil omezení dřívějších, více monolitických návrhů základnových stanic tím, že umožnil efektivní makro-diverzitu, měkká předání spojení a koordinaci interference mezi buňkami. Vytvoření RBS bylo motivováno potřebou síťového prvku, který by dokázal efektivně zvládnout složitosti CDMA vzdušných rozhraní, včetně rychlé regulace výkonu a správy rozprostřovacích kódů, a zároveň byl nákladově efektivní pro nasazení a údržbu.

## Klíčové vlastnosti

- Implementuje rozhraní WCDMA/HSPA pro 3G UMTS
- Připojuje se k řadiči rádiové sítě (RNC) prostřednictvím rozhraní Iub
- Provádí modulaci/demodulaci, kanálové kódování, rozprostření
- Provádí příkazy rychlé uzavřené smyčky regulace výkonu z RNC
- Podporuje více buněk a sektorů z jedné jednotky
- Poskytuje měření fyzické vrstvy pro optimalizaci sítě

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B

---

📖 **Anglický originál a plná specifikace:** [RBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rbs/)
