---
slug: "nup"
url: "/mobilnisite/slovnik/nup/"
type: "slovnik"
title: "NUP – National User Part"
date: 2025-01-01
abbr: "NUP"
fullName: "National User Part"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nup/"
summary: "Varianta protokolu uživatelské části (User Part) signalizačního systému č. 7 (SS7) definovaná pro použití v rámci telekomunikační sítě jedné země. Zpracovává národně specifické řízení hovorů a signali"
---

NUP je národní varianta protokolu uživatelské části (User Part) systému signalizace č. 7 (SS7) pro signalizaci spojenou s hovory a okruhy v rámci sítě jedné země, která přizpůsobuje mezinárodní standard místním směrovacím a regulatorním potřebám.

## Popis

Národní uživatelská část (National User Part, NUP) je součástí zásobníku protokolů signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)/C7), která pracuje na vrstvě uživatelské části (User Part), což je analogické aplikační vrstvě v modelu [OSI](/mobilnisite/slovnik/osi/). SS7 je základní signalizační systém pro okruhově přepínané telekomunikační sítě, který umožňuje navázání, správu a ukončení hovorů a služeb. Uživatelská část definuje procedury a zprávy pro konkrétní služby. Zatímco [ISDN](/mobilnisite/slovnik/isdn/) uživatelská část ([ISUP](/mobilnisite/slovnik/isup/)) je mezinárodně standardizovaná varianta pro řízení hovorů mezi zeměmi, NUP je národně definovaná adaptace tohoto protokolu. Je specifikována jednotlivými národními telekomunikačními správami nebo normalizačními orgány, aby splňovala domácí požadavky.

Z architektonického hlediska NUP pracuje mezi přepínacími body služeb ([SSP](/mobilnisite/slovnik/ssp/)) a mezi SSP a tranzitními ústřednami v rámci národní sítě. Pro spolehlivé, nespojované směrování signalizačních zpráv využívá služby přenosové části zpráv ([MTP](/mobilnisite/slovnik/mtp/)) úrovní 1–3. Protokol NUP definuje národně specifické typy zpráv, parametry a procedury pro základní řízení hovorů, jako je zpráva počáteční adresy ([IAM](/mobilnisite/slovnik/iam/)), zpráva o úplnosti adresy ([ACM](/mobilnisite/slovnik/acm/)), zpráva o odpovědi (ANM) a uvolnění (REL). Tyto zprávy nesou volané číslice, číslo volajícího, identifikační kód okruhu a další informace související s hovorem. Klíčový rozdíl oproti ISUP spočívá v kódování parametrů, definici národně specifických parametrů (např. pro výběr operátora, fakturační informace nebo směrování tísňových služeb) a někdy i v konečných automatech řídících navázání a uvolnění hovoru.

Jak to funguje: dochází k výměně NUP zpráv po vyhrazených signalizačních spojích k rezervaci a správě trunek (hlasových okruhů). Například při uskutečnění hovoru výchozí ústředna vytvoří NUP zprávu IAM obsahující volané číslo a odešle ji prostřednictvím sítě SS7 do další ústředny. Každá následující ústředna zprávu zpracuje, vybere odchozí trunku a přepošle IAM, dokud není dosaženo cíle. Úspěšný postup hovoru spustí zpět k volajícímu zprávy ACM a ANM. NUP zajišťuje, že jsou správně zpracovány národní číslovací plány, kódy operátorů a specifické předpisy pro účtování nebo odposlech. Její role je klíčová pro bezproblémový provoz národní páteřní sítě PSTN/PLMN a pro rozhraní na národních hranicích s mezinárodním protokolem ISUP.

## K čemu slouží

NUP existuje, aby překlenula propast mezi potřebou mezinárodní interoperability a realitou národních regulatorních a technických rozdílů v telekomunikacích. Protokol ISUP, standardizovaný ITU-T, poskytuje společný jazyk pro signalizaci přeshraničních hovorů. Jednotlivé země však často mají pro své domácí sítě jedinečné požadavky, které mezinárodní standard nepokrývá. To mohou být specifické interpretace číslovacích plánů, identifikační kódy operátorů pro liberalizované trhy, mandáty pro zákonný odposlech, směrování tísňových služeb (jako 911, 112) a národní formáty pro účtování nebo poplatky. Použití čistého ISUP v domácím provozu by mohlo být neefektivní nebo nevyhovující.

Před rozšířenou standardizací mnoho zemí vyvinulo proprietární signalizační systémy, což vedlo k fragmentaci. Motivací pro NUP byla snaha využít robustní a spolehlivou infrastrukturu SS7 a zároveň umožnit národní přizpůsobení. Řeší problém adaptace globálního standardu na místní potřeby bez narušení mezinárodní konektivity. Definováním národní varianty uživatelské části může země zajistit bezproblémové zpracování hovorů v rámci svých hranic a zároveň používat standardní ISUP na mezinárodních bránách. Tento přístup řešil omezení dřívějších národních systémů tím, že poskytoval strukturovanou, zprávami orientovanou signalizační metodu, která zlepšila rychlost navazování hovorů, spolehlivost a podporu pokročilých služeb, jako je bezplatné volání nebo volání na kreditní kartu, v národním kontextu.

Historicky byly implementace NUP běžné v mnoha národních sítích během vývoje od analogové k digitální signalizaci. Její specifikace v dokumentech 3GPP (jako je slovní specifikace 21.905) uznává její roli v ekosystému, zejména pro starší jádrové sítě GSM rozhraní s národními PSTN. Zatímco moderní sítě stále více používají signalizaci založenou na IP (SIP, Diameter), NUP zůstává v provozu v mnoha starších okruhově přepínaných jádrech, což zajišťuje zpětnou kompatibilitu a kontinuitu služeb pro tradiční telefonní služby.

## Klíčové vlastnosti

- Národně definovaná varianta protokolu uživatelské části (User Part) systému SS7 pro domácí řízení hovorů.
- Pracuje nad přenosovou částí zpráv (MTP) pro spolehlivé doručování signalizačních zpráv.
- Definuje národně specifické typy zpráv, parametry a procedury stavů hovoru.
- Zpracovává národní číslovací plány, výběr operátora a regulatorní požadavky.
- Spolupracuje s mezinárodním protokolem ISUP na národních bránových ústřednách.
- Spravuje zřízení, dohled a uvolnění hlasových okruhů (trunek) v rámci země.

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nup/)
