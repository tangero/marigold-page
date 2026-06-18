---
slug: "leo"
url: "/mobilnisite/slovnik/leo/"
type: "slovnik"
title: "LEO – Low-Earth Orbiting satellites"
date: 2026-01-01
abbr: "LEO"
fullName: "Low-Earth Orbiting satellites"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/leo/"
summary: "Satelity obíhající ve výškách 500–2000 km, charakteristické nízkou latencí a vysokou přenosovou rychlostí. V rámci 3GPP jsou integrovány jako komponenty neterestriální sítě (NTN) za účelem poskytnutí"
---

LEO je komponenta neterestriální sítě (NTN) v systémech 3GPP, která se skládá ze satelitů obíhajících ve výškách 500–2000 km a poskytuje globální pokrytí 5G s nízkou latencí a vysokou přenosovou rychlostí i pro odlehlé oblasti.

## Popis

Satelity na nízké oběžné dráze (Low-Earth Orbiting – LEO) jsou umělé satelity obíhající Zemi ve výškách typicky v rozmezí 500 až 2000 kilometrů. V rámci architektury 3GPP, počínaje studijními položkami ve verzi 14 a konkrétně od verze 15 dále, jsou satelity LEO primárním zaměřením pro neterestriální sítě ([NTN](/mobilnisite/slovnik/ntn/)). Jsou integrovány jako vzdušné přístupové uzly nebo přenosové uzly za účelem poskytnutí nepřerušované kontinuity služeb 5G (a dalších generací) a globálního pokrytí. Na rozdíl od satelitů na geostacionární oběžné dráze ([GEO](/mobilnisite/slovnik/geo/)) se satelity LEO pohybují vůči zemskému povrchu rychle, což vede ke kratším oběžným periodám (přibližně 90–120 minut) a menším pokrytím (buňkám) na zemi, které jsou v neustálém pohybu.

Z pohledu síťové architektury může satelit LEO v rámci 3GPP NTN fungovat jako uzel rádiového přístupu (v podstatě jako základnová stanice ve vesmíru), jako transparentní užitečné zatížení (přímý převodník signálu) nebo jako regenerativní užitečné zatížení (s funkcí základnové stanice na palubě). Při funkci transparentního užitečného zatížení satelit pouze zesiluje a převádí frekvenci signálu mezi pozemní bránou (Next Generation NodeB – gNB) a uživatelským zařízením (UE). Brána je připojena k 5G jádru sítě. V regenerativní architektuře satelit obsahuje plnohodnotný gNB, který signál zpracovává na oběžné dráze a připojuje se přímo k jádru sítě prostřednictvím mezisatelitního spoje nebo vyhrazené pozemní brány. Klíčovou technickou výzvou je zvládnutí vysokého Dopplerova posunu způsobeného vysokou rychlostí satelitu, velkých šířkových zpoždění (ačkoli výrazně nižších než u GEO) a nepřetržitých předávání spojení (handover), která jsou vyžadována, jak se svazky pohybují po Zemi.

Integrace zahrnuje významná vylepšení protokolů 5G New Radio (NR) a jádra sítě. Fyzická vrstva (pokrytá specifikacemi jako 38.101 a 38.108) je upravena pro práci s většími hodnotami časového předstihu, specifickými referenčními signály pro sledování a kompenzaci Dopplerova frekvenčního posunu. Vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a procedury správy mobility jsou vylepšeny pro podporu předvídatelného pohybu satelitů, dlouhých dob setrvání v buňce a efektivního předávání spojení mezi pohyblivými svazky nebo mezi satelitní a terestriální sítí. Jádro sítě podporuje kontinuitu služeb pro uživatelská zařízení (UE) pohybující se do a ze satelitního pokrytí. Konečnou rolí satelitů LEO v 3GPP je rozšíření dosahu služeb 5G na letadla, lodě a odlehlé pozemní oblasti, čímž vzniká skutečně globální síťová struktura.

## K čemu slouží

Integrace satelitů LEO do standardů 3GPP je hnána potřebou poskytnout všudypřítomné, bezproblémové připojení mimo dosah tradičních terestriálních sítí. Pokrytí terestriálními buňkovými sítěmi je ekonomicky a geograficky omezené, což zanechává rozsáhlé oceánské, vzdušné a odlehlé venkovské oblasti bez služeb. Předchozí satelitní komunikační systémy fungovaly v proprietárních izolovaných prostředích, s vysokou latencí (zejména systémy [GEO](/mobilnisite/slovnik/geo/)) a bez integrace s běžnými mobilními zařízeními spotřebitelů nebo jádry sítí. To vytvořilo mezeru v pokrytí pro kritické služby, jako jsou námořní komunikace, připojení za letu a reakce na katastrofy.

Práce 3GPP na [NTN](/mobilnisite/slovnik/ntn/), s LEO jako základním kamenem, si klade za cíl toto vyřešit tím, že učiní satelitní přístup nativní součástí systému 5G. To umožňuje standardnímu 5G smartphonu, s určitými vylepšeními, potenciálně se připojit přímo k síti satelitů LEO bez specializovaného hardwaru, což umožňuje globální roaming a kontinuitu služeb. Motivace zahrnuje podporu cílů udržitelného rozvoje OSN v oblasti konektivity, umožnění služeb internetu věcí (IoT) v zemědělství a logistice napříč odlehlými regiony a poskytnutí odolné záložní podpory pro terestriální sítě při výpadcích nebo katastrofách.

Technicky byly satelity LEO zvoleny před GEO, protože jejich nižší nadmořská výška (500–2000 km vs 36 000 km) vede k mnohem nižšímu šířkovému zpoždění (20–40 ms vs 500+ ms), což je činí vhodnými pro služby 5G citlivé na latenci. Rozmach mega-konstelací (jako je Starlink od SpaceX) prokázal komerční životaschopnost hustých sítí LEO, což vedlo 3GPP ke standardizaci rozhraní a procedur pro využití této nové infrastruktury. Standardizace zajišťuje interoperabilitu mezi různými satelitními operátory a operátory terestriálních sítí, podporuje konkurenční ekosystém a předchází závislosti na jediném dodavateli.

## Klíčové vlastnosti

- Výška oběžné dráhy 500–2000 km umožňující nízkou latenci (20–40 ms)
- Vysoká rychlost vůči Zemi vyžadující pokročilou kompenzaci Dopplerova jevu
- Mohou fungovat jako transparentní (přímý převodník) nebo regenerativní (s gNB na palubě) užitečné zatížení
- Integrovány do 5G jako komponenta neterestriální sítě (NTN)
- Poskytují pohyblivé pokrytí buňkami na zemském povrchu
- Umožňují připojení přímo k zařízení nebo prostřednictvím brány

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [LEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/leo/)
