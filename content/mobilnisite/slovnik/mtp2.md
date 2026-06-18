---
slug: "mtp2"
url: "/mobilnisite/slovnik/mtp2/"
type: "slovnik"
title: "MTP2 – Message Transfer Part layer 2"
date: 2025-01-01
abbr: "MTP2"
fullName: "Message Transfer Part layer 2"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mtp2/"
summary: "MTP2 je vrstva datového spoje signalizačního protokolu SS7, která zajišťuje spolehlivý přenos signalizačních zpráv bod-bod přes jeden spoj. Zpracovává detekci/opravu chyb, číslování sekvencí a řízení"
---

MTP2 je vrstva datového spoje signalizačního protokolu SS7, která zajišťuje spolehlivý, bezchybný přenos zpráv bod-bod přes jeden spoj prostřednictvím detekce chyb, číslování sekvencí a řízení toku.

## Popis

Message Transfer Part layer 2 (MTP2) je druhá vrstva zásobníku signalizačního protokolu [SS7](/mobilnisite/slovnik/ss7/), odpovídající vrstvě datového spoje (Layer 2) modelu [OSI](/mobilnisite/slovnik/osi/). Funguje nad fyzickým spojením poskytovaným [MTP1](/mobilnisite/slovnik/mtp1/) a pod síťovou vrstvou [MTP3](/mobilnisite/slovnik/mtp3/). Hlavní odpovědností MTP2 je zajistit spolehlivý, v pořadí a bezchybný přenos signalizačních jednotek ([SU](/mobilnisite/slovnik/su/)) přes jeden signalizační datový spoj mezi dvěma sousedními signalizačními body. Transformuje surový bitový proud z MTP1 na strukturovaný, rámcovaný protokol s robustními mechanismy pro řízení chyb.

MTP2 funguje tak, že zapouzdřuje zprávy vyšších vrstev do rámců proměnné délky nazývaných signalizační jednotky. Existují tři typy: Vyplňovací signalizační jednotky (FISU) pro stav nečinnosti spoje, Jednotky stavu spoje (LSSU) pro sdělení stavu spoje (např. mimo zarovnání, normální) a Zprávové signalizační jednotky ([MSU](/mobilnisite/slovnik/msu/)), které nesou skutečnou datovou část z MTP3 nebo uživatelské části. Každá SU obsahuje sadu polí: Příznak (oddělovač), Zpětné a dopředné pořadová čísla (BSN, [FSN](/mobilnisite/slovnik/fsn/)) pro číslování sekvencí a potvrzení, Ukazatel délky, Kontrolní součet pro detekci chyb (pomocí [CRC](/mobilnisite/slovnik/crc/)) a řídicí pole. Protokol používá pro řízení toku mechanismus posuvného okna a pro opravu chyb využívá kladné potvrzování s opakovaným přenosem. Pokud je chyba detekována pomocí CRC, je rámec zahozen a přenesen znovu.

Klíčové součásti MTP2 zahrnují vysílač, který segmentuje zprávy do SU a spravuje vysílací pořadové číslo a vyrovnávací paměť pro opakovaný přenos, a přijímač, který kontroluje CRC, potvrzuje správně přijaté SU a znovu sestavuje sekvenci. Provádí také inicializační postupy zarovnání pro uvedení spoje do provozu a nepřetržité monitorování pro detekci poruch spoje. V síťové architektuře poskytuje MTP2 MTP3 virtuálně bezchybný spoj. Jeho výkon přímo ovlivňuje signalizační zpoždění a využití spoje. V systémech 3GPP je MTP2 nezbytná pro provoz tradičních SS7 spojů založených na TDM, které propojují uzly jádra sítě jako MSC, SGSN a HLR pro správu mobility a signalizaci související s hovory, před migrací na přenos založený na IP s využitím adaptací SIGTRAN jako M2UA nebo M2PA.

## K čemu slouží

MTP2 byla vytvořena k vyřešení problému nespolehlivého fyzického přenosu pro kritické signalizační zprávy. Zatímco MTP1 poskytuje fyzické spojení, nenabízí žádnou ochranu proti bitovým chybám, ztrátám nebo duplikaci. Signalizační informace pro řízení hovorů a služeb účastníků jsou příliš důležité na to, aby byly poškozeny. Účelem MTP2 je přidat vrstvu spolehlivosti k surovému spoji a zajistit, aby každá zpráva doručená do síťové vrstvy (MTP3) byla neporušená a ve správném pořadí.

Historicky řešila omezení dřívějších signalizačních systémů, kterým chyběly robustní protokoly vrstvy spoje, což vedlo k vyšší míře neúspěšnosti hovorů. Implementací detekce chyb pomocí kontrolního součtu CRC-16, automatického opakovaného přenosu poškozených rámců a číslování sekvencí MTP2 garantuje integritu dat přes jeden skok. Zavedla také řízení toku, aby zabránila rychlému vysílači v zahlcení pomalého přijímače, což je klíčová funkce pro udržení stability v sítích s uzly různé výpočetní kapacity.

V kontextu mobilních sítí 3GPP byl účelem MTP2 umožnit spolehlivý přenos protokolů MAP, CAP a BSSAP přes globálně nasazenou infrastrukturu SS7. Tvořila spolehlivý 'kanál', přes který byly prováděny roamingové dohody, doručování SMS a předávání hovorů. Její návrh pro 64 kbit/s TDM spoje byl optimální pro danou éru, ale později se stal motivací pro vývoj SIGTRAN, protože komplexní procedury MTP2 se stavem byly méně efektivní přes paketové IP sítě ve srovnání s jednoduššími protokoly jako SCTP.

## Klíčové vlastnosti

- Poskytuje detekci chyb pomocí 16bitového kontrolního součtu cyklickým kódem (CRC)
- Implementuje opravu chyb prostřednictvím automatického opakovaného dotazu (ARQ) typu Go-Back-N
- Spravuje číslování sekvencí a potvrzování pro doručení ve správném pořadí
- Provádí inicializaci, zarovnání a monitorování chyb signalizačního spoje
- Realizuje řízení toku pomocí mechanismu posuvného okna
- Generuje a zpracovává Vyplňovací a Jednotky stavu spoje pro údržbu spoje

## Související pojmy

- [MTP1 – Message Transfer Part layer 1](/mobilnisite/slovnik/mtp1/)
- [MTP3 – Message Transfer Part layer 3](/mobilnisite/slovnik/mtp3/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [MTP2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtp2/)
