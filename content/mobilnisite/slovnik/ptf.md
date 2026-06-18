---
slug: "ptf"
url: "/mobilnisite/slovnik/ptf/"
type: "slovnik"
title: "PTF – Power Transfer Function"
date: 2025-01-01
abbr: "PTF"
fullName: "Power Transfer Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptf/"
summary: "Power Transfer Function (PTF) je model definovaný 3GPP pro charakterizaci charakteristik přenosu výkonu mezi anténami základnové stanice, zejména v systémech Multi-Transmitter Multi-Receiver (MTMR). J"
---

PTF je model definovaný 3GPP, který charakterizuje charakteristiky přenosu výkonu mezi anténami základnové stanice a je nezbytný pro přesné testování beamformingu a MIMO metodou Over-the-Air v 5G NR.

## Popis

Power Transfer Function (PTF) je technický model specifikovaný 3GPP pro kvantifikaci efektivního přenosu výkonu mezi různými anténními porty nebo elementy uvnitř základnové stanice, zejména těch využívajících architektury Multi-Transmitter Multi-Receiver (MTMR). V moderních základnových stanicích 5G New Radio (NR) (gNB) jsou anténní systémy složitá pole s více aktivními prvky podporujícími beamforming a Massive [MIMO](/mobilnisite/slovnik/mimo/). PTF poskytuje standardizovaný způsob popisu vazby a izolace mezi těmito prvky, který není přímo reprezentován pouze tradičními S-parametry, neboť zohledňuje celý aktivní [RF](/mobilnisite/slovnik/rf/) řetězec včetně zesilovačů a beamformingových vah.

Z architektonického hlediska je PTF definován v kontextu konduktivního rozhraní základnové stanice (bod konektoru před anténními prvky) a jejího záření metodou Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)). Modeluje vztah mezi výkonem vstřikovaným do vysílacího (Tx) anténního portu základnové stanice a výkonem přijímaným na jiném přijímacím (Rx) anténním portu, s uvážením všech vnitřních vazebních cest a zamýšlených beamformingových diagramů. Funkce je v podstatě souborem komplexních koeficientů, které reprezentují přenosovou funkci mezi libovolným párem Tx-Rx anténních portů pro danou beamformingovou konfiguraci. Tento model je zásadní pro testování shody, kde přímé kabelové připojení k jednotlivým anténním prvkům je často nemožné.

PTF funguje tak, že je charakterizován během návrhu a kalibrace základnové stanice. Výrobci změří nebo vypočítají koeficienty PTF, které pak mohou být použity k odvození ekvivalentních požadavků pro konduktivní testování z požadavků na výkon OTA specifikovaných v 3GPP. Například požadavek na nežádoucí emise měřené OTA ve vzdáleném poli může být pomocí modelu PTF převeden na limit pro výkon měřený na konduktivní referenční rovině. To umožňuje reprodukovatelné a přesné testování klíčových ukazatelů výkonu, jako je výkon vysílače, citlivost přijímače a nežádoucí emise, v kontrolovaném laboratorním prostředí pomocí kabelových spojů, a to i pro pokročilé beamformingové gNB.

Jeho role v síťovém ekosystému je primárně v oblasti testování, standardizace a certifikace zařízení. Poskytnutím rigorózního matematického modelu pro přenos výkonu PTF zajišťuje, že základnové stanice 5G NR s integrovanými aktivními anténami mohou být testovány konzistentně a v souladu s normami. Překlenuje propast mezi tradičním paradigmatem konduktivního testování a realitou OTA moderních základnových stanic, čímž zajišťuje, že síťové zařízení poskytuje slibovaný výkon z hlediska přesnosti beamu, řízení interference a zisků prostorového multiplexování MIMO, které jsou základem pro kapacitní a pokrytí cíle 5G.

## K čemu slouží

PTF byl vytvořen, aby řešil zásadní výzvu testování zavedenou technologií 5G New Radio a její závislostí na aktivních anténních systémech ([AAS](/mobilnisite/slovnik/aas/)) s integrovanými rádiovými jednotkami. Tradiční základnové stanice měly oddělené rádiové jednotky a pasivní antény, což umožňovalo provádět veškeré testování pomocí konduktivních kabelů na standardizovaných rozhraních. U AAS jsou anténa a rádio integrovány a anténní porty nejsou pro testování fyzicky přístupné, což vyžaduje měření metodou Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)), která jsou složitá, drahá a méně opakovatelná.

Základní problém, který PTF řeší, je umožnění přesného, reprodukovatelného konduktivního testování pro základnové stanice, které jsou z podstaty navrženy pro provoz OTA. Bez PTF by každý výkonnostní test pro beamforming, výstupní výkon a citlivost přijímače vyžadoval nastavení v anechoické komoře, což by drasticky zvýšilo náklady a čas na testování shody a výzkum a vývoj. PTF poskytuje model, který umožňuje převod požadavků OTA zpět na konduktivní referenční rovinu, čímž zachovává přísnost testovacího režimu při zachování praktičnosti.

Historicky, před Rel-15 a rozšířeným nasazením AAS pro 5G NR, takový model nebyl nutný. Jeho vývoj byl motivován potřebou průmyslu škálovat výrobu a certifikaci základnových stanic 5G s massive [MIMO](/mobilnisite/slovnik/mimo/). Řeší omezení předchozích testovacích metodologií, které nedokázaly adekvátně charakterizovat vzájemně závislé chování více transceiverů a anténních prvků v beamformingovém systému. PTF je tedy klíčovým enablerem pro komerční nasazení pokročilého síťového vybavení 5G, neboť zajišťuje shodu výkonu nákladově efektivním způsobem.

## Klíčové vlastnosti

- Modeluje přenos výkonu mezi Tx a Rx anténními porty v systémech MTMR
- Umožňuje převod mezi požadavky testování OTA a konduktivního testování
- Definován komplexními koeficienty pro každý pár anténních portů a stav beamu
- Kritický pro testování integrovaných aktivních anténních systémů (AAS)
- Podporuje testování shody pro RF požadavky základnových stanic 5G NR
- Usnadňuje reprodukovatelné laboratorní testování výkonu beamformingu a MIMO

## Související pojmy

- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)

## Definující specifikace

- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements

---

📖 **Anglický originál a plná specifikace:** [PTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptf/)
