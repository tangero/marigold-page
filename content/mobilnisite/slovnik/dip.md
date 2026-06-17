---
slug: "dip"
url: "/mobilnisite/slovnik/dip/"
type: "slovnik"
title: "DIP – Dominant Interferer Proportion ratio"
date: 2025-01-01
abbr: "DIP"
fullName: "Dominant Interferer Proportion ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dip/"
summary: "Klíčový ukazatel výkonnosti (KPI) používaný v 3GPP rádiových testech ke kvantifikaci vlivu jediného dominantního rušivého signálu. Měří poměr výkonu od nejsilnějšího rušiče k celkovému výkonu rušení-p"
---

DIP je klíčový ukazatel výkonnosti používaný v 3GPP rádiových testech, který měří poměr výkonu od nejsilnějšího rušiče k celkovému výkonu rušení-plus-šum. Kvantifikuje tak vliv jediného dominantního rušivého signálu.

## Popis

Poměr Dominant Interferer Proportion (DIP) je kritická metrika definovaná v 3GPP specifikacích pro testy shody (např. TS 36.101, 37.145) pro hodnocení výkonu přijímačů uživatelských zařízení (UE) za přítomnosti specifických rušivých podmínek. Nejde o měření v síti, ale o parametr laboratorního testu. Matematicky je DIP definován jako poměr středního výkonu (I_d) jediného, konfigurovaného dominantního rušivého signálu k celkovému střednímu výkonu rušení plus šumu (I_total). Vyjádřeno jako DIP = I_d / I_total. Zbývající výkon rušení (I_total - I_d) je typicky konfigurován jako aditivní bílý Gaussovský šum ([AWGN](/mobilnisite/slovnik/awgn/)) nebo specifikovaný zdroj šumu/rušení.

V testovacím uspořádání je požadovaný signál (požadovaný kanál) generován na specifické úrovni referenční citlivosti. Dominantní rušivý signál, což je často další signál LTE/5G NR na sousedním kanálu nebo ko-kanálu, je poté vstřikován na řízené úrovni výkonu. AWGN nebo jiné zdroje rušení poskytují základní 'šumové pozadí'. Měněním poměru DIP mohou testovací inženýři simulovat reálné scénáře, kdy je UE vystaveno silnému, specifickému zdroji rušení – například blízké základnové stanici pracující na sousední frekvenci nebo výkonnému UE v těsné blízkosti – uprostřed obecného šumu na pozadí a dalších menších rušičů.

Poměr DIP je klíčový pro definici testů přijímače pro metriky jako Adjacent Channel Selectivity ([ACS](/mobilnisite/slovnik/acs/)), Blokování a In-band/Out-of-band emise. Například v testu ACS je požadovaný signál na přiděleném kanálu a dominantní rušič je umístěn na sousedním kanálu. Poměr DIP definuje, jak velkou část celkového rozpočtu pro rušení zabírá tento jediný signál na sousedním kanálu oproti širokopásmovému šumu. Tím se testuje schopnost přijímače tento specifický, silný sousední signál potlačit. Výkon UE (měřený propustností nebo chybovostí) musí splňovat minimální požadavky v rozsahu hodnot DIP, což zajišťuje robustnost v heterogenních scénářích nasazení s mixem makro, small cell a zařízení-zařízení přenosů.

Z architektonického hlediska je DIP parametr řízený testovacími přístroji (jako je emulátor kanálu nebo generátor signálu) v provedeném nebo radiačním testovacím uspořádání. Je základní součástí metodologie 3GPP pro zajištění, že návrhy přijímačů jsou nejen citlivé, ale také selektivní a odolné. Standardizací testů s definovanými hodnotami DIP zaručuje 3GPP základní výkon pro všechna kompatibilní zařízení, což je zásadní pro předvídatelný výkon sítě, zejména v hustých městských nasazeních, sdíleném spektru (jako [CBRS](/mobilnisite/slovnik/cbrs/)) a scénářích s vysokým mezilinkovým rušením, jako jsou plně duplexní nebo pokročilé [MIMO](/mobilnisite/slovnik/mimo/) systémy.

## K čemu slouží

DIP byl zaveden, aby vytvořil realističtější a standardizovanou metodu pro testování odolnosti přijímačů UE vůči specifickým, silným zdrojům rušení. Před jeho formální definicí často používaly testy přijímačů zjednodušené modely rušení, jako je čistý [AWGN](/mobilnisite/slovnik/awgn/) nebo jediný rušič bez šumu na pozadí. Tyto modely neodrážely přesně reálná rádiová prostředí, kde přijímač typicky čelí kombinaci několika dominantních rušičů (např. od blízké buňky) a množství nízké úrovně agregovaného rušení a tepelného šumu.

Klíčový problém, který DIP řeší, je poskytnutí řízeného, opakovatelného způsobu simulace tohoto scénáře 'dominantní rušič plus šumové pozadí'. To je klíčové, protože přijímací algoritmy, jako jsou algoritmy pro odhad kanálu, ekvalizaci a potlačení rušení, se chovají odlišně, když jeden rušič dominuje profilu rušení, oproti situaci, kdy je rušení šumového charakteru. Například pokročilé techniky interference rejection combining ([IRC](/mobilnisite/slovnik/irc/)) nebo successive interference cancellation (SIC) jsou specificky navrženy pro potlačení silných, strukturovaných rušičů. Testování založené na DIP ověřuje účinnost těchto technik za standardizovaných podmínek.

Historicky, jak se mobilní sítě vyvíjely z homogenních makro nasazení k hustým, heterogenním sítím (HetNets) se small buňkami, dramaticky vzrostla pravděpodobnost, že UE zažije velmi silný signál od blízké small buňky, zatímco se snaží připojit k vzdálenější makro buňce. Podobně v LTE a 5G NR s dynamickým sdílením spektra a komunikací zařízení-zařízení se řízení dominantního mezilinkového rušení stalo hlavní výzvou. Metrika DIP a související testovací případy byly vyvinuty, aby zajistily, že přijímače UE mohou udržet konektivitu a propustnost v těchto náročných, realistických rušivých prostředích. Poskytuje výrobcům zařízení jasný cíl pro návrh přijímače a umožňuje síťovým operátorům mít důvěru ve výkon zařízení, což je základní pro plánování sítě a efektivitu spektra.

## Klíčové vlastnosti

- Kvantifikuje podíl jediného dominantního rušiče na celkovém výkonu rušení.
- Používá se jako řízený parametr v 3GPP testovacích případech shody pro výkon přijímače.
- Umožňuje realistickou simulaci rušivých scénářů heterogenních sítí v laboratorních testech.
- Podporuje testování funkcí přijímače jako Adjacent Channel Selectivity (ACS) a blokování.
- Aplikovatelné napříč více technologiemi rádiového přístupu (UTRA, E-UTRA, NR).
- Definováno s konkrétními hodnotami (např. 0 %, 50 %, 100 %) v testovacích specifikacích pro zajištění konzistentního benchmarkingu.

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.963** (Rel-19) — Feasibility Study on UMTS/HSDPA UE Interference Cancellation
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.766** (Rel-15) — LTE BS Interference Cancellation Receiver Study
- **TS 36.829** (Rel-11) — Feasibility Study on LTE UE Interference Cancellation
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [DIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dip/)
