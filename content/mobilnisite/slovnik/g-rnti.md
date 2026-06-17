---
slug: "g-rnti"
url: "/mobilnisite/slovnik/g-rnti/"
type: "slovnik"
title: "G-RNTI – GERAN Radio Network Temporary Identity"
date: 2025-01-01
abbr: "G-RNTI"
fullName: "GERAN Radio Network Temporary Identity"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/g-rnti/"
summary: "Dočasný identifikátor přidělený sítí mobilní stanici (MS) pro komunikaci přes rozhraní GERAN. Jednoznačně identifikuje MS na sdílených rádiových kanálech (jako PACCH) pro efektivní adresování během př"
---

G-RNTI je dočasný identifikátor přidělený sítí pro jednoznačnou identifikaci mobilní stanice na sdílených rádiových kanálech GERAN při adresování během přenosu dat, volání a přidělování zdrojů v sítích GPRS/EDGE.

## Popis

[GERAN](/mobilnisite/slovnik/geran/) Radio Network Temporary Identity (G-RNTI) je klíčový identifikátor používaný v GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network (GERAN) pro podporu paketově orientovaných služeb přes [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Je přidělen mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) sítí, konkrétně Packet Control Unit (PCU), která je často umístěna v Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)), když MS aktivuje Packet Data Protocol (PDP) kontext nebo provádí aktualizaci buňky ve stavu ready. G-RNTI slouží jako dočasná, buňkově specifická nebo směrovací oblastí specifická adresa MS na rádiovém rozhraní, primárně používaná na Packet Associated Control Channel (PACCH) a dalších paketových datových kanálech.

Strukturně se G-RNTI skládá ze dvou hlavních částí: Temporary Flow Identity (TFI) a Temporary Logical Link Identity (TLLI). TFI je 5bitová hodnota identifikující konkrétní Temporary Block Flow (TBF), což je logické spojení pro přenos [LLC](/mobilnisite/slovnik/llc/) PDU v jednom směru (uplink nebo downlink) mezi MS a sítí. TLLI je 32bitová identita, která jednoznačně identifikuje logické spojení mezi MS a SGSN. Síť odvozuje G-RNTI z TLLI a používá jej pro zprávy řízení rádiových zdrojů. Když síť potřebuje adresovat konkrétní MS na sdíleném kanálu, jako je PACCH (který se používá pro řídicí signalizaci spojenou s přenosem paketových dat), zahrne G-RNTI do hlavičky zprávy, takže odpoví pouze zamýšlená MS.

Jeho role v síti je mnohostranná. Během downlink přenosu dat používá síť G-RNTI k volání MS nebo k označení přidělení zdrojů na Packet Data Channel (PDCH). Pro uplink přenosy zahrne MS své G-RNTI do přístupových burst při žádosti o zdroje. G-RNTI je zásadní pro efektivní multiplexování více uživatelů na stejných fyzických rádiových zdrojích. Protože je dočasný a může být přepřidělen, pomáhá šetřit trvalou identitu účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) před zbytečným přenosem přes rozhraní, čímž zvyšuje bezpečnost. Platnost G-RNTI je vázána na stav a polohu MS; může být změněno během převzetí služeb buňkou nebo aktualizací směrovací oblasti. Správa přidělování a uvolňování G-RNTI je klíčovou součástí procedur řízení rádiových zdrojů (RR) v paketově orientovaném provozu GERAN.

## K čemu slouží

G-RNTI bylo zavedeno k řešení potřeby efektivní a bezpečné identifikace mobilních stanic během paketových datových relací přes [GERAN](/mobilnisite/slovnik/geran/). V původním návrhu GSM pro přepojování okruhů se pro signalizaci používala Temporary Mobile Subscriber Identity (TMSI), ale přerušovaná, nespojovaná povaha paketových dat vyžadovala dynamičtější identifikátor vázaný na aktivní datové toky. G-RNTI řeší problém multiplexování více uživatelů na sdílených paketových datových kanálech bez neustálých dlouhých výměn identit. Poskytuje stručnou značku, kterou síť může použít k rychlému adresování konkrétního Temporary Block Flow (TBF) MS pro přenos datových bloků nebo související řídicí signalizaci.

Jeho vytvoření bylo motivováno vývojem GPRS jako nadstavby nad sítěmi GSM. Byl potřebný nový řídicí mechanismus pro paketově orientovanou doménu, který se lišil od vyhrazených spojení používaných v přepojování okruhů. G-RNTI, odvozené z TLLI, které je samo odvozeno z P-TMSI (Packet TMSI), vytváří bezpečný řetězec dočasných identifikátorů, čímž chrání trvalou identitu uživatele. Umožňuje efektivní přidělování rádiových zdrojů, protože síť může plánovat datové bloky pro různé uživatele na stejném fyzickém kanálu a používat krátké G-RNTI k označení zamýšleného příjemce v hlavičce bloku.

Dále G-RNTI podporuje správu mobility ve stavu ready. Když se MS pohybuje mezi buňkami, síť může přepřidělit nové G-RNTI, což umožňuje nepřetržité řízení datové relace bez znovunavázání logického spojení v jádře sítě (identifikovaného TLLI). Toto oddělení mezi rádiově specifickou dočasnou identitou (G-RNTI) a dočasnou identitou v jádře sítě (TLLI/P-TMSI) je klíčovým architektonickým principem, umožňujícím nezávislou optimalizaci procedur rádiového přístupu a jádra sítě. G-RNTI je tedy základním prvkem umožňujícím výkon a škálovatelnost datových služeb GPRS a EDGE.

## Klíčové vlastnosti

- Dočasný identifikátor přidělený na dobu trvání paketové datové relace nebo specifické asociace s buňkou
- Skládá se z TFI (identifikujícího Temporary Block Flow) a je odvozen z TLLI
- Primárně používán pro adresování na Packet Associated Control Channel (PACCH) a pro přidělování zdrojů
- Specifický pro buňku nebo směrovací oblast, může se měnit při událostech mobility
- Zvyšuje bezpečnost tím, že se vyhne přenosu trvalých identit účastníka přes rozhraní
- Umožňuje efektivní multiplexování více uživatelů na sdílených paketových datových kanálech (PDCH)

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [G-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-rnti/)
