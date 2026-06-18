---
slug: "bssap-le"
url: "/mobilnisite/slovnik/bssap-le/"
type: "slovnik"
title: "BSSAP-LE – Base Station System Application Part Location Services Extension"
date: 2025-01-01
abbr: "BSSAP-LE"
fullName: "Base Station System Application Part Location Services Extension"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bssap-le/"
summary: "BSSAP-LE je rozšíření protokolu BSSAP, které umožňuje služby lokalizace (LCS) v sítích GSM. Zajišťuje komunikaci mezi střediskem SMLC (Serving Mobile Location Center) a řadičem základnových stanic BSC"
---

BSSAP-LE je rozšíření protokolu BSSAP, které umožňuje služby lokalizace v sítích GSM tím, že zajišťuje komunikaci mezi střediskem SMLC (Serving Mobile Location Center) a řadičem základnových stanic BSC (Base Station Controller) pro polohovací operace.

## Popis

BSSAP-LE (Base Station System Application Part Location Services Extension) je klíčový protokol v architektuře GSM, který rozšiřuje standardní protokol [BSSAP](/mobilnisite/slovnik/bssap/) o podporu služeb lokalizace ([LCS](/mobilnisite/slovnik/lcs/)). Funguje jako aplikační protokol v systému základnových stanic [BSS](/mobilnisite/slovnik/bss/), který umožňuje komunikaci mezi střediskem [SMLC](/mobilnisite/slovnik/smlc/) (Serving Mobile Location Center) a řadičem [BSC](/mobilnisite/slovnik/bsc/) (Base Station Controller) pro určování polohy mobilního zařízení. Protokol je definován v 3GPP specifikacích 03.071 a 43.059, které podrobně popisují funkční požadavky a signalizační procedury pro služby lokalizace v sítích GSM.

Architektura protokolu představuje BSSAP-LE jako rozšíření stávajícího zásobníku protokolu BSSAP, využívající stejné podkladové transportní mechanismy a zároveň přidávající specializované zprávy a procedury pro služby lokalizace. Funguje přes rozhraní A mezi BSC a ústřednou [MSC](/mobilnisite/slovnik/msc/), přičemž MSC funguje jako směrovací bod pro zprávy související s lokalizací mezi SMLC a BSC. Protokol definuje specifické typy zpráv pro polohovací požadavky, hlášení měření a doručování výsledků polohy, což umožňuje přesnou koordinaci mezi síťovými prvky během polohovacích operací.

BSSAP-LE podporuje více polohovacích metod včetně Enhanced Observed Time Difference ([E-OTD](/mobilnisite/slovnik/e-otd/)), Assisted [GPS](/mobilnisite/slovnik/gps/) (A-GPS) a lokalizace založené na Cell-ID. Protokol pokrývá celý životní cyklus polohovací transakce, od počátečního požadavku na polohu až po konečné doručení polohy. Klíčové součásti zahrnují komponentu BSSMAP-LE pro zprávy nesouvisející s okruhy a komponentu DTAP-LE pro zprávy aplikační části přímého přenosu. Protokol řídí časovou synchronizaci, sběr měření a koordinaci výpočtů polohy mezi síťovými prvky.

Při provozu BSSAP-LE zajišťuje výměnu informací souvisejících s lokalizací mezi SMLC (které řídí výpočty polohy) a BSC (které řídí rádiové zdroje a sběr měření). Když je zahájen požadavek na polohu, zprávy BSSAP-LE koordinují nastavení polohovacích měření, sběr časových informací z více základnových stanic a doručení vypočtených odhadů polohy. Protokol zahrnuje mechanismy zpracování chyb, parametry kvality služby pro přesnost určení polohy a podporu pro požadavky lokalizace iniciované ze sítě i z mobilního zařízení.

Návrh protokolu zajišťuje zpětnou kompatibilitu se stávajícími implementacemi BSSAP a zároveň poskytuje specializovanou funkcionalitu potřebnou pro služby lokalizace. Zahrnuje bezpečnostní prvky pro autentizaci a autorizaci požadavků na polohu, což je zvláště důležité pro nouzové služby a scénáře zákonného odposlechu. BSSAP-LE představuje klíčový vývojový krok v sítích GSM, který jim umožnil splnit regulatorní požadavky na lokalizaci volajících v nouzových situacích a zároveň podporovat komerční služby založené na poloze.

## K čemu slouží

BSSAP-LE byl vytvořen pro uspokojení rostoucí potřeby přesného určování polohy mobilních zařízení v sítích GSM, která byla hnána regulatorními požadavky na nouzové služby a komerční poptávkou po službách založených na poloze. Před jeho zavedením sítím GSM chyběly standardizované mechanismy pro přesné určování polohy, což omezovalo jejich schopnost podporovat lokalizaci volajících v nouzových situacích (požadavky E911/E112) a komerční lokalizační aplikace. Protokol vyřešil základní problém koordinace polohovacích měření a výpočtů mezi různými síťovými prvky standardizovaným způsobem.

Na vývoj BSSAP-LE motivovalo několik klíčových faktorů: regulatorní požadavky, které nutily operátory poskytovat přesné informace o poloze pro nouzová volání, komerční příležitosti ve službách založených na poloze a potřeba standardizovaných rozhraní mezi komponentami systému určování polohy. Před BSSAP-LE existovala proprietární řešení, ale postrádala interoperabilitu a škálovatelnost. Protokol poskytl standardizovaný způsob komunikace mezi SMLC a BSC, což umožnilo konzistentní implementaci napříč zařízeními různých výrobců.

Historicky vytvoření BSSAP-LE ve verzi 7 (Release 7) představovalo významný pokrok ve schopnostech sítí GSM, což umožnilo sítím 2G splnit vyvíjející se požadavky na služby lokalizace při zachování kompatibility se stávající infrastrukturou. Protokol překonal omezení dřívějších přístupů tím, že poskytl komplexní rámec pro všechny aspekty poskytování lokalizační služby, od koordinace měření až po doručení výsledků. Umožnil sítím GSM podporovat stejné možnosti lokalizačních služeb, které se vyvíjely pro sítě 3G, a zajistil tak kontinuitu služeb během vývoje sítě.

## Klíčové vlastnosti

- Standardizované rozhraní mezi SMLC a BSC pro služby lokalizace
- Podpora více polohovacích metod včetně E-OTD a A-GPS
- Kompletní správa transakce polohovacích operací (end-to-end)
- Parametry kvality služby pro požadavky na přesnost určení polohy
- Bezpečnostní mechanismy pro autentizaci požadavků na polohu
- Zpětná kompatibilita se stávajícími implementacemi BSSAP

## Související pojmy

- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [E-OTD – Enhanced Observed Time Difference](/mobilnisite/slovnik/e-otd/)
- [A-GPS – Assisted Global Positioning System](/mobilnisite/slovnik/a-gps/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [BSSAP-LE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bssap-le/)
