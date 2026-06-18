---
slug: "prach"
url: "/mobilnisite/slovnik/prach/"
type: "slovnik"
title: "PRACH – Physical Random Access Channel"
date: 2025-01-01
abbr: "PRACH"
fullName: "Physical Random Access Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prach/"
summary: "PRACH je uplinkový fyzický kanál používaný UE k zahájení komunikace se sítí, primárně pro počáteční přístup, obnovení spojení a předání spojení (handover). Je zásadní pro navázání uplinkové synchroniz"
---

PRACH je uplinkový fyzický kanál používaný zařízením k zahájení síťové komunikace pro přístup, předání spojení (handover) nebo synchronizaci, který tvoří základ pro všechna následná přenosy dat.

## Popis

Physical Random Access Channel (PRACH) je základní uplinkový kanál v 3GPP bezdrátových technologiích, včetně UMTS ([UTRA](/mobilnisite/slovnik/utra/)) a LTE/5G NR ([E-UTRA](/mobilnisite/slovnik/e-utra/)/NR). Jeho primární funkcí je umožnit uživatelskému zařízení (UE) dosáhnout uplinkové synchronizace se sítí a vyžádat si počáteční alokaci prostředků, pokud nemá k dispozici vyhrazený kanál pro žádost o naplánování. Procedura PRACH, často nazývaná procedura náhodného přístupu (Random Access, [RA](/mobilnisite/slovnik/ra/)), je vstupním bodem pro přechod UE z klidového nebo neaktivního stavu do stavu připojeného, což jí umožňuje přenášet data nebo signalizaci.

Činnost PRACH zahrnuje vysílání specifické preambulové sekvence. V LTE a 5G NR síť konfiguruje sadu dostupných preambulových sekvencí, které jsou odvozeny od Zadoff-Chu sekvencí známých svými dobrými autokorelačními a zkříženě korelačními vlastnostmi. UE náhodně vybere jednu preambuli z určené podmnožiny (konkurenční přístup, contention-based) nebo použije konkrétně přiřazenou preambuli (konkurenčně volný přístup, contention-free, např. pro handover). UE poté tuto preambuli vysílá na specifickém časovo-frekvenčním zdroji definovaném konfiguračním indexem PRACH, který určuje číslo systémového rámce, číslo podrámce a frekvenční pozici. Formát preambule definuje délku a strukturu přenosu, což umožňuje přizpůsobení různým velikostem buněk a scénářům.

Po odeslání preambule UE naslouchá v nakonfigurovaném okně odpovědi na náhodný přístup (Random Access Response, [RAR](/mobilnisite/slovnik/rar/)) od sítě. RAR, odeslaný na [PDCCH](/mobilnisite/slovnik/pdcch/) a [PDSCH](/mobilnisite/slovnik/pdsch/), obsahuje příkaz časového předstihu (timing advance) pro úpravu časování vysílání UE, počáteční uplinkové povolení pro následný přenos Zprávy 3 (např. žádost o [RRC](/mobilnisite/slovnik/rrc/) připojení) a dočasný Cell Radio Network Temporary Identifier ([C-RNTI](/mobilnisite/slovnik/c-rnti/)). Pokud UE obdrží RAR odpovídající její odeslané preambuli, pokračuje zbývajícími kroky procedury RA. V případě konkurenčního přístupu, pokud více UE vybere stejnou preambuli, dojde ke kolizi, což vyžaduje mechanismus odmlčení a retransmise.

Z architektonického hlediska je PRACH fyzický kanál definovaný ve specifikacích fyzické vrstvy (PHY) (TS 25.211, 36.211, 38.211). Jeho konfigurace a parametry jsou řízeny vyššími vrstvami prostřednictvím signalizace RRC, jak je podrobně popsáno v protokolových specifikacích RRC (TS 25.331, 36.331, 38.331). Konfigurace PRACH zahrnuje parametry jako index kořenové sekvence, formát preambule, časové/frekvenční zdroje a parametry stupňování výkonu. Přijímač eNodeB/gNB provádí na přijímaném signálu korelační detekci, aby identifikoval vyslanou preambuli a odhadl časovou odchylku, což je zásadní pro navázání a udržení uplinkové ortogonality v systémech OFDMA/SC-FDMA.

## K čemu slouží

PRACH existuje, aby řešil základní problém počátečního přístupu a uplinkové synchronizace ve sdíleném bezdrátovém médiu. Než může UE zahájit plánovanou komunikaci, musí nejprve upozornit síť na svou přítomnost a zarovnat své vysílací časování, aby zabránilo rušení ostatních uživatelů. Při absenci vyhrazeného řídicího kanálu je mechanismus náhodného přístupu nezbytný, aby si UE mohla vyžádat zřízení takového kanálu.

Historicky byly metody počátečního přístupu v systémech před 3GPP a raných celulárních sítích často jednodušší, ale méně efektivní a škálovatelné. Návrh PRACH v UMTS a jeho evoluce přes LTE a 5G NR byla motivována potřebou robustní, nízkolatenční a kapacitně škálovatelné metody přístupu vhodné pro husté sítě a širokou škálu scénářů nasazení. Řeší omezení pevných přístupových slotů a neortogonálních preambulí zavedením konfigurovatelných Zadoff-Chu sekvencí s zónami nulové autokorelace, čímž zlepšuje detekční výkon a snižuje míru falešných poplachů v prostředích s vysokou interferencí.

Evoluce PRACH také podporuje nové případy užití. Například v LTE-A a 5G NR byly zavedeny nové formáty preambule pro velmi velké buňky (např. pro pokrytí venkovských oblastí) a pro scénáře s vysokou rychlostí (např. vysokorychlostní vlaky). Návrh PRACH v NR navíc podporuje flexibilní numerologii a širokou šířku pásma, což umožňuje efektivní přístup v milimetrovém spektru a pro různé služby, jako je massive IoT a komunikace s ultra-spolehlivým nízkým zpožděním (URLLC), kde je klíčový rychlý a spolehlivý přístup.

## Klíčové vlastnosti

- Podporuje jak procedury náhodného přístupu s konkurencí (contention-based), tak bez konkurence (konkurenčně volné, contention-free, vyhrazené).
- Využívá Zadoff-Chu sekvence pro generování preambule, které poskytují optimální autokorelační vlastnosti a nízkou vzájemnou korelaci.
- Konfigurovatelné formáty preambule pro podporu různých poloměrů buněk a prostředí šíření (např. dlouhé preambule pro velké buňky).
- Flexibilní mapování na časové a frekvenční zdroje, definované konfiguračními indexy PRACH v SIB2.
- Mechanismus stupňování výkonu, při kterém UE zvyšuje vysílací výkon pro retransmise preambule, není-li přijata žádná odpověď na náhodný přístup (RAR).
- Propojení s vrstvou MAC pro řízení odmlčení a řešení kolizí během procedury náhodného přístupu.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [PRACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/prach/)
