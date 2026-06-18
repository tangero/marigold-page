---
slug: "umsc"
url: "/mobilnisite/slovnik/umsc/"
type: "slovnik"
title: "UMSC – UMTS Mobile Services Switching Centre"
date: 2025-01-01
abbr: "UMSC"
fullName: "UMTS Mobile Services Switching Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/umsc/"
summary: "Ústřední přepínací uzel jádrové sítě v obvodu spínané doméně (CS) 3G UMTS, odpovědný za řízení hovorů, správu mobility a přepojování obvodu spínaných hlasových a datových služeb. Jedná se o funkční ev"
---

UMSC je ústřední přepínací uzel jádrové sítě v obvodu spínané doméně (CS) 3G UMTS, který zpracovává řízení hovorů, správu mobility a přepojování pro obvodu spínané služby; vyvinul se z GSM MSC.

## Popis

UMTS Mobile Services Switching Centre (UMSC) je klíčovou součástí obvodu spínané ([CS](/mobilnisite/slovnik/cs/)) domény jádrové sítě v sítích 3G Universal Mobile Telecommunications System (UMTS). Funkčně je ekvivalentní Mobile-services Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) ze sítě GSM, ale je navržen pro rozhraní s UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) namísto GSM Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)). UMSC provádí přepojování, směrování a řízení tradičních obvodu spínaných služeb, jako jsou hlasové hovory a obvodu spínaná data (např. fax). Zajišťuje také kritické funkce správy mobility pro účastníky ve své servisní oblasti.

Architektonicky se UMSC připojuje k UTRAN přes rozhraní Iu-CS, které přenáší uživatelský provoz (hlasové kanály) a signalizaci pro řízení hovorů a správu mobility. Na straně jádrové sítě komunikuje s dalšími UMSC nebo legacy MSC pomocí Network-to-Network Interface ([NNI](/mobilnisite/slovnik/nni/)), typicky založeného na protokolech Signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)). Také se připojuje k Home Location Register (HLR) a Visitor Location Register (VLR) – často umístěným společně s UMSC jako UMSC/VLR – pro správu účastnických dat a lokalizace. UMSC je zodpovědný za navázání, správu a ukončení obvodu spínaných spojení, provádění předávání hovorů mezi radiovými síťovými řadiči (RNC) a generování záznamů o hovorech (CDR) pro účtování.

Během provozu, když mobilní uživatel zahájí hlasový hovor, UTRAN směruje signalizaci k jeho obsluhujícímu UMSC. UMSC autentizuje uživatele, načte profil účastníka z VLR, určí směrování a vytvoří obvodu spínanou cestu k cíli (k dalšímu mobilnímu zařízení nebo pevné síti). Během hovoru, pokud se uživatel pohybuje, UMSC koordinuje s RNC provedení předání hovoru, čímž zajišťuje nepřerušenost služby. S příchodem 3GPP Release 4 architektura umožnila rozdělení na MSC Server (zpracovávající signalizaci) a Media Gateway (MGW, zpracovávající média), ale termín UMSC může označovat kombinovaný uzel nebo serverovou funkci v této rozdělené architektuře.

## K čemu slouží

UMSC byl vytvořen jako nezbytná evoluce GSM MSC pro podporu nové 3G UMTS rádiové přístupové technologie. Zatímco GSM MSC byly navrženy pro BSS založené na Time Division Multiple Access (TDMA), UMTS zavedlo Wideband Code Division Multiple Access (WCDMA) a novou architekturu rádiové sítě (UTRAN) s odlišnými protokoly a rozhraními (např. Iu namísto A-interface). UMSC poskytoval most mezi touto novou rádiovou technologií a stávající globální obvodu spínanou telefonní sítí, čímž zajišťoval zpětnou kompatibilitu a kontinuitu hlasových služeb během přechodu ze 2G na 3G.

Jeho vývoj řešil potřebu přepínače jádrové sítě, který by zvládal vyšší datové rychlosti a nové scénáře mobility 3G, a zároveň stále podporoval rozsáhlou instalovanou základnu obvodu spínaných služeb. Řešil problém integrace UTRAN do veřejné telefonní sítě (PSTN) a dalších mobilních sítí. UMSC a jím reprezentovaná obvodu spínaná doména se však staly legacy s plnou migrací odvětví na plně IP sítě a Voice over LTE (VoLTE) / Voice over NR (VoNR), které jsou zpracovávány IP Multimedia Subsystem (IMS) v paketově spínané doméně.

## Klíčové vlastnosti

- Řízení hovorů a přepojování pro obvodu spínané hlasové a datové služby
- Správa mobility (aktualizace polohy, předání hovoru) pro účastníky v CS doméně
- Rozhraní k UTRAN přes Iu-CS rozhraní (RANAP signalizace)
- Propojení s dalšími MSC a PSTN pomocí SS7/ISUP
- Integrace s HLR/VLR pro správu účastnických dat
- Generování záznamů o účtovaných datech pro využití obvodu spínaných služeb

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [UMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/umsc/)
