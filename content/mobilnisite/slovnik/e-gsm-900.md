---
slug: "e-gsm-900"
url: "/mobilnisite/slovnik/e-gsm-900/"
type: "slovnik"
title: "E-GSM 900 – Extended GSM 900"
date: 2025-01-01
abbr: "E-GSM 900"
fullName: "Extended GSM 900"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-gsm-900/"
summary: "Rozšíření standardního kmitočtového pásma GSM 900, které přidává 10 MHz spektra (880-890 MHz pro uplink / 925-935 MHz pro downlink) pro zvýšení kapacity sítě. Je definováno specifickými vzorci pro čís"
---

E-GSM 900 je rozšíření pásma GSM 900, které přidává 10 MHz spektra (880-890 MHz pro uplink / 925-935 MHz pro downlink) pro zvýšení kapacity a je definováno specifickými vzorci pro číslování kanálů pro tento rozšířený rozsah.

## Popis

E-GSM 900 je definované kmitočtové pásmo v rámci rodiny GSM představující rozšíření primárního pásma GSM 900. Standardní pásmo GSM 900 (P-GSM) typicky pracuje v rozsazích 890-915 MHz pro uplink a 935-960 MHz pro downlink a poskytuje 124 rádiových kmitočtových kanálů. Rozšíření E-GSM 900 přidává dalších 10 MHz spektra na spodním konci, konkrétně rozsahy 880-890 MHz pro uplink a 925-935 MHz pro downlink. To poskytuje dalších 50 rádiových kmitočtových kanálů a významně navyšuje celkovou kapacitu dostupnou pro služby GSM v pásmu 900 MHz.

Technická definice E-GSM 900 je přesně zachycena ve vzorcích pro číslování kanálů specifikovaných v dokumentu 3GPP TS 45.005. Je definováno Absolutní číslo rádiového kmitočtového kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/)) pro rozšířený rozsah. Pro uplink se nosná frekvence Fl(n) vypočítá jako 890 + 0,2 * n MHz, kde 'n' je ARFCN. Pro odpovídající downlink je frekvence Fu(n) rovna Fl(n) + 45 MHz. Rozšíření E-GSM konkrétně pokrývá ARFCN v rozsahu pod hodnotami primárního pásma (např. ARFCN 0-124 pro P-GSM, přičemž E-GSM přidává kanály pod tímto rozsahem). Uvedený přesný vzorec, Fl(n)=890+0,2*n a [FI](/mobilnisite/slovnik/fi/)(n)=890+0,2*(n‑1024), používá odlišnou notaci, kde 'n' je ARFCN a FI pravděpodobně označuje downlinkovou frekvenci, přičemž offset 1024 je dědictvím systému číslování kanálů GSM, který v určitých kontextech pro downlink používá offset 1024.

Z pohledu nasazení sítě mohou mobilní operátoři spektrum E-GSM 900 využít k nasazení dalších GSM nosných, čímž se uvolní přetížení v oblastech s vysokým provozem. Zařízení, včetně základnových stanic ([BTS](/mobilnisite/slovnik/bts/)) a mobilních terminálů, musí podporovat rozšířený kmitočtový rozsah. Charakteristiky šíření v rozsahu 880-915 MHz jsou podobné standardnímu pásmu 900 MHz, nabízejí dobré pokrytí a prostupnost budovami, což činí z E-GSM cenný prostředek pro zvýšení kapacity bez obětování pokrytí. Přestože je technologie GSM v éře 4G a 5G do značné míry považována za zastaralou, pásmo 900 MHz včetně jeho části E-GSM zůstává strategicky důležité. Toto spektrum je často přebudováváno (refarmováno) nebo znovu využíváno pro modernější technologie, jako je UMTS (jako Band VIII), LTE (Band 8) a dokonce 5G NR (n8), a to díky jeho vynikajícím vlastnostem šíření pro pokrytí rozsáhlých oblastí.

## K čemu slouží

E-GSM 900 bylo zavedeno za účelem řešení akutního nedostatku spektra a kapacitních omezení, kterým čelili operátoři GSM sítí, zejména v Evropě a dalších regionech, kde bylo GSM 900 primárním buněčným pásmem. Jak v pozdních 90. a raných 2000 letech explodoval počet účastníků, původní alokace 2x25 MHz (uplink/downlink) pro P-GSM se stala nedostatečnou pro zvládnutí provozu, což vedlo k přetížení, přerušeným hovorům a špatné kvalitě služeb. Účelem definice rozšíření E-GSM bylo formálně přidělit a standardizovat využití přilehlého spektra, které bylo někdy dostupné nebo mohlo být uvolněno, a poskytnout standardizovanou cestu pro rozšíření kapacity.

Historicky byla část spektra E-GSM využívána pro jiné účely, například pro analogové systémy NMT. Jak byly tyto zastaralé systémy vyřazovány, regulátoři toto spektrum přealokovali na digitální služby GSM. Standardizace E-GSM 900 v 3GPP (zejména ve verzi 12, ačkoli bylo využíváno dříve) zajistila globální harmonizaci zařízení a plánů kanálů. To umožnilo výrobcům terminálů a síťových prvků vyrábět produkty podporující celý rozsah, což umožnilo bezproblémový roaming a efektivní využití infrastruktury. Vyřešilo to problém nestandardních, proprietárních implementací rozšířeného pásma.

V širším kontextu představuje E-GSM 900 klasický příklad správy spektra a vývoje technologie. Jeho vznik byl motivován praktickou potřebou získat více kapacity z vysoce hodnotného nízkofrekvenčního pásma. Přestože jeho přímé využití pro GSM provoz pokleslo, definice tohoto pásma zůstává klíčová. Stanovila technické parametry pro blok spektra, který se stal klíčovým aktivem pro modernizaci sítí a slouží jako základ pro přebudování (refarming), které podporuje nasazení 3G, 4G a 5G v 'pokrytové vrstvě' pod 1 GHz.

## Klíčové vlastnosti

- Rozšiřuje pásmo GSM 900 o 10 MHz (spárované 2x10 MHz) na spodním okraji.
- Definováno specifickými vzorci ARFCN (Absolutní číslo rádiového kmitočtového kanálu) ve specifikacích 3GPP.
- Přidává kapacitu pro GSM sítě a pomáhá zmírňovat přetížení.
- Využívá spektrum v rozsazích 880-890 MHz pro uplink a 925-935 MHz pro downlink.
- Vyžaduje podpůrnou síťovou infrastrukturu a mobilní zařízení.
- Poskytuje spektrum s vynikajícími charakteristikami šíření pro pokrytí rozsáhlých oblastí.

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [E-GSM 900 na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-gsm-900/)
