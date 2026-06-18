---
slug: "fcs"
url: "/mobilnisite/slovnik/fcs/"
type: "slovnik"
title: "FCS – Frame Checking Sequence"
date: 2025-01-01
abbr: "FCS"
fullName: "Frame Checking Sequence"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fcs/"
summary: "Frame Checking Sequence je kontrolní součet nebo kód pro detekci chyb připojený k datovému rámci nebo paketu na fyzické nebo spojové vrstvě. Umožňuje přijímači detekovat chyby přenosu způsobené šumem"
---

FCS je detekční kontrolní součet (checksum) připojený k datovému rámci, který umožňuje přijímači ověřit integritu dat detekcí chyb přenosu před jejich zpracováním.

## Popis

Frame Checking Sequence je základní mechanismus pro detekci chyb používaný na více vrstvách a rozhraních v systémech 3GPP, zejména na fyzické vrstvě a v protokolech spojové vrstvy. Jedná se o vypočítanou hodnotu odvozenou z bitů přenášeného rámce (hlavičky a datové části), která je před přenosem připojena k rámci. Mezi běžné algoritmy pro generování FCS patří Cyklický redundantní součet ([CRC](/mobilnisite/slovnik/crc/)) s konkrétními polynomy definovanými pro různé kanály a protokoly. Při příjmu přijímací entita nezávisle přepočítá FCS na základě přijatých bitů a porovná jej s přijatou hodnotou FCS. Pokud se shodují, je rámec považován za bezchybný a je přijat k dalšímu zpracování. Pokud se neshodují, je rámec zahozen, což spustí procedury pro ošetření chyb, jako je žádost o opakovaný přenos (v režimu s potvrzením) nebo je počítán jako ztracený rámec.

V kontextu radiového přístupu 3GPP je FCS nedílnou součástí transportních kanálů a zpracování na fyzické vrstvě. Například v UMTS a LTE je ke každému transportnímu bloku ([TB](/mobilnisite/slovnik/tb/)) před kanálovým kódováním připojen CRC. Velikost tohoto CRC (např. 24 bitů) je specifikována v příslušných specifikacích fyzické vrstvy (řada 25, řada 36). To umožňuje UE nebo základnové stanici ověřit integritu dekódovaného transportního bloku po zpětné korekci chyb. Neúspěšný CRC indikuje chybu dekódování a tato informace je využívána pro řízení výkonu ve vnější smyčce a procesy Hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)). V HARQ neúspěšný CRC (indikovaný [NACK](/mobilnisite/slovnik/nack/)) spouští opakovaný přenos.

Mimo fyzickou vrstvu se FCS používá v protokolech spojové vrstvy, jako je protokol Řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) v nepotvrzovaném režimu ([UM](/mobilnisite/slovnik/um/)) a potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)). Zde chrání RLC protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). V Protokolu konvergence paketových dat (PDCP) je pro řídicí signalizační zprávy používán kontrolní součet integrity (který funguje podobně jako FCS) pro ochranu proti úmyslnému poškození. Dále pro služby přepojování okruhů používají protokoly jako korekce chyb V.42 (odkazováno v TS 27.010) FCS pro spolehlivou modemovou komunikaci. Implementační detaily – polynom, počáteční hodnota a rozsah výpočtu – jsou v každé specifikaci pečlivě definovány, aby byla zajištěna interoperabilita mezi vysílači a přijímači.

## K čemu slouží

Primárním účelem Frame Checking Sequence je zajistit integritu digitálních dat přenášených přes náchylné kanály, bezdrátové i kabelové. Radiové kanály jsou inherentně náchylné k šumu, útlumu a interferencím, které mohou během přenosu změnit bity. Bez detekce chyb by poškozená data byla zpracována vyššími vrstvami, což by vedlo k zkomolenému hlasu, poškozeným souborům nebo nesprávným signalizačním příkazům a vážně by degradovalo kvalitu služby a stabilitu sítě. FCS poskytuje výpočetně efektivní metodu pro detekci velké většiny náhodných chyb bitů.

Jeho vytvoření a standardizace byly motivovány potřebou spolehlivé digitální komunikace. Rané digitální systémy vyžadovaly způsob automatické kontroly chyb bez lidského zásahu. FCS, zejména využívající algoritmy CRC, nabídl výhodný kompromis: vysokou schopnost detekce chyb při relativně nízké režii (malý počet extra bitů na rámec) a nízké výpočetní náročnosti. Řeší omezení jednoduchých kontrol parity, které mohou detekovat pouze lichý počet chyb bitů. Tím, že umožňuje přijímačům zahazovat poškozené rámce, tvoří FCS základ spolehlivých protokolů pro přenos dat. Je to nezbytný první krok před tím, než může fungovat jakýkoli mechanismus opakovaného přenosu (jako ARQ nebo HARQ), protože tyto mechanismy spoléhají na kladné/záporné potvrzení založené na výsledku kontroly FCS.

## Klíčové vlastnosti

- Detekce náhodných a shlukových chyb pomocí algoritmů CRC.
- Konfigurovatelná délka CRC (např. 8, 16, 24, 32 bitů) na základě požadované odolnosti.
- Nedílná součást zpracování transportního bloku na fyzické vrstvě pro HARQ.
- Používá se u RLC PDU pro ověření integrity v nepotvrzovaném a potvrzovaném režimu.
- Podporuje řízení výkonu ve vnější smyčce poskytováním měření míry chyb bloků (BLER).
- Standardizované polynomy a výpočetní postupy zajišťují interoperabilitu.

## Související pojmy

- [CRC – Cyclic Redundancy Check](/mobilnisite/slovnik/crc/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 28.403** (Rel-19) — WLAN Performance Measurements
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [FCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fcs/)
