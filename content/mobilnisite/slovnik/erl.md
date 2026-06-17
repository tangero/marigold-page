---
slug: "erl"
url: "/mobilnisite/slovnik/erl/"
type: "slovnik"
title: "ERL – Echo Return Loss"
date: 2025-01-01
abbr: "ERL"
fullName: "Echo Return Loss"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/erl/"
summary: "ERL je metrika měřící útlum ozvěnových signálů v hlasových komunikačních systémech, která kvantifikuje, jak moc je ozvěna potlačena mezi přijímací a vysílací cestou. Je klíčová pro hodnocení kvality h"
---

ERL je metrika měřící útlum ozvěnových signálů mezi přijímací a vysílací cestou v hlasových komunikačních systémech, kde vysoké hodnoty indikují lepší výkon potlačení ozvěn pro kvalitu hlasu.

## Popis

Echo Return Loss (ERL) je klíčový parametr výkonu v telekomunikacích, definovaný jako logaritmický poměr (v decibelech) výkonu příchozího signálu k výkonu ozvěny vrácené v opačném směru. Kvantifikuje účinnost potlačení ozvěn v hlasových sítích, zejména ve scénářích, kde elektrické nebo akustické ozvěny mohou degradovat kvalitu hovoru. Z architektonického hlediska je ERL relevantní v koncových bodech, jako jsou handsety, brány a síťové uzly, kde hybridní obvody nebo komponenty digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) ozvěnu řídí. Jak funguje: Když hlasový signál putuje od vzdáleného mluvčího k místnímu zařízení, část se může vrátit zpět jako ozvěna kvůli nepřizpůsobení impedance nebo akustické vazbě; ERL měří útlum, který tato ozvěna utrpí před opětovným vysláním. Mezi klíčové zapojené komponenty patří hybridní transformátory, potlačovače ozvěn a hlasové kodeky, které společně usilují o maximalizaci ERL. Jeho role v sítích 3GPP je standardizována v specifikacích jako TS 26.115 pro testování kvality hlasu, což zajišťuje interoperabilitu a konzistentní uživatelský zážitek napříč zařízeními a sítěmi. ERL se měří během sestavování hovoru nebo hodnocení kvality pomocí testovacích signálů, přičemž vyšší hodnoty (např. >15 dB) indikují dostatečné potlačení ozvěn. Interaguje s dalšími metrikami, jako je Echo Cancellation ([EC](/mobilnisite/slovnik/ec/)) a Overall Loudness Rating ([OLR](/mobilnisite/slovnik/olr/)), při definování celkového hlasového výkonu. V moderních VoIP a VoLTE/VoNR systémech je ERL řízeno pomocí adaptivních algoritmů v DSP, které se dynamicky přizpůsobují síťovým podmínkám pro zachování srozumitelnosti. Porozumění ERL je nezbytné pro inženýry optimalizující hlasové služby, neboť nízká hodnota ERL vede k slyšitelným ozvěnám, nespokojenosti uživatelů a zvýšené zátěži pro potlačovače ozvěn.

## K čemu slouží

ERL existuje k řešení základního problému ozvěn v telefonních sítích, který trápí hlasovou komunikaci již od raných analogových systémů. Ozvěna vzniká z nepřizpůsobení impedance v hybridních obvodech nebo akustické zpětné vazby v handsetech, což způsobuje, že mluvčí slyší svůj vlastní hlas se zpožděním, což je rušivé a snižuje kvalitu hovoru. Historicky, bez řádného řízení ozvěn, se dálkové hovory s významným zpožděním staly nepoužitelnými. Motivací pro definici ERL jako metriky bylo poskytnout standardizovaný způsob kvantifikace útlumu ozvěn, což umožňuje výrobcům a operátorům navrhovat a nasazovat účinná řešení pro potlačení ozvěn. Řeší problém nekonzistentní kvality hlasu stanovením referenčních hodnot výkonu zařízení, což zajišťuje minimalizaci ozvěn na nepostřehnutelnou úroveň. V kontextu 3GPP je ERL součástí specifikací kvality hlasu pro služby založené na IMS, jako je VoLTE, a řeší výzvy paketových sítí, kde bylo třeba přizpůsobit tradiční mechanismy řízení ozvěn. Začleněním ERL do testovacích standardů pomáhá 3GPP udržovat vysokou kvalitu hlasových služeb při vývoji sítí z komutovaných na plně IP architektury, a podporuje tak srozumitelnou komunikaci napříč různými zařízeními a přístupovými technologiemi.

## Klíčové vlastnosti

- Kvantifikuje útlum ozvěny v decibelech (dB)
- Nezbytný pro testování a standardizaci kvality hlasu
- Měřen mezi přijímací a vysílací cestou v zařízeních
- Podporuje hodnocení výkonu potlačení ozvěn
- Integrován do specifikací hlasových kodeků a IMS v 3GPP
- Ovlivňuje vnímání srozumitelnosti a komfortu hovoru uživatelem

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements

---

📖 **Anglický originál a plná specifikace:** [ERL na 3GPP Explorer](https://3gpp-explorer.com/glossary/erl/)
