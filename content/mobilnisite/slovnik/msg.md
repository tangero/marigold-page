---
slug: "msg"
url: "/mobilnisite/slovnik/msg/"
type: "slovnik"
title: "MSG – Message phase of Facsimile transmission"
date: 2025-01-01
abbr: "MSG"
fullName: "Message phase of Facsimile transmission"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msg/"
summary: "MSG označuje přenosovou fázi (Message phase) v rámci relace faxového protokolu T.30. Je to klíčová fáze, ve které jsou vlastní obrazová data přenášena přes síť. Tato fáze je zásadní pro podporu legacy"
---

MSG je hlavní přenosová fáze faxového protokolu T.30, ve které jsou přenášena vlastní obrazová data, a která podporuje legacy faxové služby přes sítě 3GPP.

## Popis

Přenosová fáze (Message phase, MSG) je definovaný procedurální stav v protokolu [ITU-T](/mobilnisite/slovnik/itu-t/) T.30 pro skupinovou faxovou komunikaci 3 (Group 3). Relace T.30 je rozdělena na odlišné fáze: Vytvoření spojení (Call Establishment), Předpřenosová procedura (Pre-Message Procedure), Přenos zprávy (Message Transmission), Popřenosová procedura (Post-Message Procedure) a Uvolnění spojení (Call Release). Fáze MSG zahrnuje vlastní přenos faxových obrazových dat. Během této fáze je naskenovaný obraz dokumentu zakódován pomocí kompresních schémat Modified Huffman (MH), Modified READ ([MR](/mobilnisite/slovnik/mr/)) nebo Modified Modified READ (MMR) a přenášen jako série digitálních rámců přes navázané přenosové spojení (bearer connection).

V kontextu sítí 3GPP podpora fáze MSG zahrnuje vzájemné propojení (interworking) mezi 3GPP core sítí a faxovými terminálovými adaptéry nebo bránami (gateways). Pro okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) faxové služby k tomu dochází přes tradiční hlasový kanál (např. v GSM nebo UMTS), kde jsou modemové tóny nesoucí signalizaci T.30 a obrazová data fáze MSG zpracovávány jako audio. Síť musí zajistit transparentní přenos těchto tónů bez rušivého zpracování, jako je detekce hlasové aktivity nebo komprese, které by mohla data poškodit. V paketově přepínaných implementacích, jako je Fax over IP (FoIP) využívající protokol T.38, jsou data fáze MSG paketizována a přenášena přes IP síť se specifickými mechanismy pro redundanci a opravu chyb, aby se vyrovnalo se ztrátou paketů.

Technická implementace zahrnuje několik síťových funkcí. Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo IP Multimedia Subsystem (IMS) musí rozpoznat faxové volání na základě volaného čísla nebo časných tónů v přenosovém pásmu (Called Station Identification - [CSI](/mobilnisite/slovnik/csi/)). Po identifikaci může síť deaktivovat hlasové kodeky a povolit transparentní 64 kbps neomezený digitální přenos (v CS) nebo aktivovat zásobník protokolu T.38 (v PS). Během fáze MSG je úlohou sítě primárně poskytovat spolehlivý bitový kanál. Jakékoli překódování (transcoding), potlačení ozvěny (echo cancellation) nebo vyrovnávací paměti pro kolísání zpoždění (jitter buffers) musí být nakonfigurovány tak, aby zachovaly integritu vysokofrekvenčních modemových signálů, které tvoří obrazová data. Úspěšné dokončení fáze MSG je potvrzeno popřenosovou procedurou T.30, která zahrnuje signály potvrzení (MCF) nebo přecvičení (RTP).

## K čemu slouží

MSG, jak je definováno [ITU-T](/mobilnisite/slovnik/itu-t/) T.30, je základní operační fáze pro faxový přenos. Její podpora v rámci standardů 3GPP byla nezbytná pro zajištění zpětné kompatibility a pokračující služby pro faxové přístroje, které byly a v některých odvětvích stále jsou kritickým obchodním nástrojem. Rané mobilní sítě (GSM) potřebovaly podporovat fax jako základní telefonní službu vedle hlasu. Hlavním problémem bylo přizpůsobit síť primárně navrženou pro komprimovaný hlas tak, aby přenášela vysokofrekvenční analogové modemové signály faxové relace bez degradace.

Motivace pro její zařazení a pokračující odkazování ve specifikacích 3GPP vychází z potřeby vzájemného propojení (interworking) a transparentnosti služeb. Jak se sítě vyvíjely z okruhově přepínaných na paketově přepínané architektury, výzva se přesunula od zachování analogových tónů k spolehlivému transportu faxových dat v reálném čase přes IP sítě náchylné na zpoždění, kolísání zpoždění (jitter) a ztrátu paketů. Standard T.38, na který odkazují pozdější verze 3GPP, byl vyvinut speciálně k řešení tohoto problému a definuje, jak jsou fáze protokolu T.30, zejména kritická fáze MSG, zapouzdřeny a chráněny v IP paketech. Podpora fáze MSG umožňuje mobilním operátorům nabízet konvergenci pevných a mobilních služeb (fixed-mobile convergence) pro faxové služby a podporovat specializovaná zařízení, jako jsou lékařské nebo právní faxové přístroje, které spoléhají na tuto legacy technologii.

## Klíčové vlastnosti

- Definovaný procedurální stav v rámci faxového protokolu ITU-T T.30
- Fáze, ve které jsou přenášena vlastní data naskenovaného obrazu dokumentu
- Využívá standardy komprese obrazu jako MH, MR a MMR
- Vyžaduje transparentnost sítě nebo specifickou adaptaci (T.38) pro zachování integrity signálu
- Podporována přes okruhově přepínané (circuit-switched) přenosy i paketově přepínané IP sítě 3GPP
- Zahrnuje vzájemné propojení (interworking) s faxovými bránami (gateways) nebo terminálovými adaptéry v síti

## Definující specifikace

- **TS 23.045** (Rel-4) — GSM Group 3 Facsimile Service Procedures
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 43.045** (Rel-19) — Group 3 Fax Service in A/Gb Mode PLMN

---

📖 **Anglický originál a plná specifikace:** [MSG na 3GPP Explorer](https://3gpp-explorer.com/glossary/msg/)
