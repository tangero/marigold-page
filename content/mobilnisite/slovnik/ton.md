---
slug: "ton"
url: "/mobilnisite/slovnik/ton/"
type: "slovnik"
title: "TON – Type Of Number"
date: 2025-01-01
abbr: "TON"
fullName: "Type Of Number"
category: "Identifier"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/ton/"
summary: "TON je parametr v telekomunikační signalizaci, který kategorizuje formát volaného nebo volajícího čísla, například jako mezinárodní, tuzemské nebo účastnické číslo. Je klíčový pro správné směrování ho"
---

TON je parametr v telekomunikační signalizaci, který kategorizuje formát volaného čísla (např. mezinárodní nebo tuzemské) za účelem zajištění správného směrování hovoru.

## Popis

Type Of Number (TON) je základní parametr definovaný ve specifikacích 3GPP, používaný primárně v signalizačních protokolech jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) a Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)). Jedná se o číselný kód, který doprovází volané číslo (např. v informačním prvku Called Party Number nebo Calling Party Number) a udává číslovací plán a formát přidružených číslic. Síťové prvky, jako jsou Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)), Gateway MSCs ([GMSC](/mobilnisite/slovnik/gmsc/)) a Home Location Registers ([HLR](/mobilnisite/slovnik/hlr/)), používají TON k správné interpretaci čísla. Například hodnota TON sděluje ústředně, zda následující číslice představují mezinárodní číslo (vyžadující kód země), tuzemské významné číslo, místní účastnické číslo nebo kód speciální služby.

TON funguje ve spojení s Numbering Plan Identification ([NPI](/mobilnisite/slovnik/npi/)) a poskytuje tak úplný kontext pro číslo. Zatímco NPI specifikuje číslovací plán (např. ISDN/telefonie, data, telex), TON definuje sémantickou kategorii v rámci tohoto plánu. Mezi běžné hodnoty TON patří 'International Number' (mezinárodní číslo), 'National Number' (tuzemské číslo), 'Network Specific Number' (používané pro negeografická čísla, jako jsou bezplatná linky), 'Subscriber Number' (účastnické číslo) a 'Abbreviated Number' (zkrácené číslo). Když uživatel vytočí číslo, koncový terminál nebo původní síť převede vytočené číslice do kanonického formátu a přiřadí příslušný TON na základě vzorů vytáčení (jako úvodní '+' nebo '00' pro mezinárodní volání). Tato strukturovaná informace je poté přenášena v signalizačních zprávách během procesu sestavování hovoru.

V jádrové síti rozhodnutí o směrování zásadně závisí na správné interpretaci TON. GMSC provádějící dotazování pro mobilně ukončovaný hovor analyzuje TON a číslice ze zprávy Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)), aby určil, jak dotazovat HLR. Pokud TON indikuje mezinárodní číslo, může GMSC potřebovat extrahovat Mobile Country Code (MCC) pro vyhledání v HLR. Pro přenositelnost čísel a služby inteligentní sítě pomáhá TON v aktivaci správné servisní logiky. Jeho role sahá až do IP Multimedia Subsystem (IMS), kde je používán v Tel URI a při propojování s Public Switched Telephone Network (PSTN) za účelem zachování konzistentní interpretace čísel napříč hybridními sítěmi.

## K čemu slouží

TON existuje, aby řešil základní problém nejednoznačné interpretace čísel v globálních telekomunikačních sítích. Bez indikátoru TON by sekvence číslic jako '441234567890' mohla být interpretována jako tuzemské číslo z Velké Británie nebo jako mezinárodní číslo z jiné země, což by vedlo k chybnému směrování hovorů. Před standardizovanými indikátory typu čísla se sítě spoléhaly na složité, na operátorovi specifické tabulky analýzy číslic a heuristiku, které byly náchylné k chybám a bránily mezinárodní interoperabilitě.

Vznik TON byl motivován potřebou jasného mechanismu na úrovni protokolu, který by sděloval povahu telefonního čísla v rámci signalizačních zpráv. To se stalo obzvláště kritickým s nástupem digitálních signalizačních systémů, jako je Signaling System No. 7 (SS7), a globalizací telefonie. Umožňuje síťovým ústřednám zpracovávat čísla deterministicky, což podporuje efektivní směrování hovorů, přesné účtování (např. rozlišení mezi místními a mezinárodními hovory) a podporu pokročilých funkcí, jako jsou bezplatná (800) čísla, která mají specifický TON. Poskytuje základní vrstvu pro přenositelnost čísel a roaming tím, že zajišťuje, že domovská síť může správně identifikovat formát čísel poskytovaných navštívenou sítí.

## Klíčové vlastnosti

- Definuje kategorie formátu čísla (např. mezinárodní, tuzemské, účastnické)
- Používá se v parametrech signalizace SS7 ISUP a MAP
- Nezbytný pro správné směrování hovorů a dotazování HLR
- Funguje ve spojení s Numbering Plan Identification (NPI)
- Podporuje vzájemné propojování mezi sítěmi PSTN/PLMN a IMS
- Umožňuje správnou kategorizaci účtování na základě typu čísla

## Související pojmy

- [NPI – Numbering Plan Identifier](/mobilnisite/slovnik/npi/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [TON na 3GPP Explorer](https://3gpp-explorer.com/glossary/ton/)
