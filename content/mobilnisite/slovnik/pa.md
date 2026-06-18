---
slug: "pa"
url: "/mobilnisite/slovnik/pa/"
type: "slovnik"
title: "PA – Pedestrian A"
date: 2025-01-01
abbr: "PA"
fullName: "Pedestrian A"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pa/"
summary: "Pedestrian A (PA) je standardizovaný model útlumu signálu používaný v 3GPP k simulaci podmínek šíření rádiového signálu pro pěší uživatele pohybující se nízkou rychlostí (např. 3 km/h). Představuje pr"
---

PA je standardizovaný model útlumu (fading) signálu podle 3GPP, který simuluje šíření rádiového signálu pro pěší s nízkou rychlostí v prostředí s přiměřeným vícecestným šířením, a to pro testování výkonu bezdrátových systémů.

## Popis

Pedestrian A (PA) je statistický model kanálu definovaný ve specifikacích 3GPP pro emulaci šíření rádiových vln pro scénáře mobility pěších uživatelů v celulárních sítích. Je součástí rodiny modelů kanálů (např. Pedestrian B, Vehicular A) používaných pro testování shody, hodnocení výkonu a simulaci bezdrátových komunikačních systémů. Model PA charakterizuje prostředí s nízkou rychlostí, typicky 3 km/h, s přiměřeným rozprostřením zpoždění, které odráží typická městská nebo předměstská prostředí, kde se uživatelé pohybují pěšky. Modeluje vícecestný útlum (fading) způsobený odrazy, ohyby a rozptylem od budov, terénu a dalších překážek, přičemž využívá strukturu s čárovým zpožděním (tapped-delay line, [TDL](/mobilnisite/slovnik/tdl/)) se specifickými zpožděními drah, jejich výkony a Dopplerovskými spektry.

Technicky je model PA implementován jako soubor parametrů v časové oblasti, který definuje více šířících se drah, z nichž každá má přidružené zpoždění, střední výkon a rozdělení útlumu (často Rayleighovo nebo Riceovo). Například při testování LTE a NR zahrnuje dráhy se zpožděními až několik set nanosekund a relativními výkony, které s rostoucím zpožděním klesají. Model zohledňuje Dopplerův posun způsobený pohybem uživatele, který vyvolává frekvenční disperzi a časově proměnné podmínky na kanálu. V systémových simulacích se aplikuje na řetězec zpracování základního pásma za účelem posouzení metrik, jako je bitová chybovost ([BER](/mobilnisite/slovnik/ber/)), bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)), propustnost a pokrytí za realistických podmínek útlumu. Je široce používán v konformních zkouškách rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) pro uživatelská zařízení (UE) a základnové stanice, jak je specifikováno v dokumentech jako TS 36.101 a TS 38.101.

Role PA v síti je primárně ve fázích návrhu, testování a nasazení. Během výzkumu a vývoje (R&D) jej inženýři používají k hodnocení výkonu přijímače, jako je odhad kanálu, ekvalizace a algoritmy [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output), aby zajistili, že zvládnou reálný útlum. Při certifikaci regulační orgány a operátoři vyžadují, aby zařízení splňovala minimální standardy výkonu za podmínek PA, čímž se zaručí spolehlivý servis pro pěší uživatele. Model také napomáhá v nástrojích pro plánování sítě při predikci pokrytí a kapacity v městských oblastech, což ovlivňuje umístění základnových stanic a nastavení parametrů. Díky poskytování reprodukovatelného a standardizovaného prostředí s útlumem umožňuje PA spravedlivé srovnání zařízení a technologií různých výrobců.

Model PA se často srovnává s jinými modely, jako je Pedestrian B ([PB](/mobilnisite/slovnik/pb/)), který má větší rozprostření zpoždění pro disperznější kanály, nebo s Vozidlovými modely pro vyšší rychlosti. Jeho parametry jsou odvozeny z empirických měření a jsou pravidelně zpřesňovány v novějších vydáních 3GPP, aby odrážely vyvíjející se scénáře nasazení, jako jsou vyšší kmitočtová pásma v 5G. Model podporuje jak režim s frekvenčním duplexem ([FDD](/mobilnisite/slovnik/fdd/)), tak s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)) a lze jej přizpůsobit různým šířkám pásma a nosným kmitočtům. Celkově je PA základním nástrojem pro zajištění toho, aby bezdrátové systémy poskytovaly konzistentní výkon v běžných případech použití pěšími uživateli.

## K čemu slouží

Model kanálu PA byl vytvořen za účelem poskytnutí standardizované a realistické reprezentace šíření rádiového signálu pro uživatele s nízkou mobilitou, čímž řeší potřebu konzistentního testování výkonu v rámci telekomunikačního průmyslu. Před jeho přijetím v 3GPP Release 8 používali výrobci a operátoři proprietární nebo ad-hoc modely útlumu, což vedlo k neporovnatelným výsledkům a možným problémům s interoperabilitou v nasazených sítích. To ztěžovalo záruku, že uživatelská zařízení budou spolehlivě fungovat za typických podmínek pěšího pohybu, jako je chůze ve městech, kde vícecestný útlum výrazně ovlivňuje kvalitu signálu. Motivace pro PA pramenila z nasazování systémů 3G a LTE, které vyžadovaly důkladné testování shody pro zajištění kvality služby a souladu s předpisy.

Historicky vývoj PA ovlivnily modely kanálů, jako jsou ty od ITU-R (např. ITU-R M.1225), ale 3GPP jej přizpůsobilo speciálně pro celulární scénáře. Řeší problém hodnocení, jak pokročilé technologie, jako je OFDMA v LTE nebo NR, zvládají časově proměnné kanály s přiměřeným rozprostřením zpoždění. Definováním přesných parametrů pro zpoždění drah, jejich výkony a Dopplerův jev umožňuje PA reprodukovatelné simulace a testy, které validují návrhy přijímačů, včetně kódování pro opravu chyb, hybridního ARQ a adaptivní modulace. To je kritické pro dosažení cílových hodnot výkonu ve standardech jako LTE-Advanced a 5G, kde jsou datové rychlosti a spolehlivost prvořadé.

Dále PA řeší omezení jednodušších modelů (např. kanálů s aditivním bílým Gaussovským šumem), které nezachycují efekty reálného útlumu, což vede k nadměrně optimistickým predikcím výkonu. Umožňuje plánovačům sítí vyhodnocovat díry v pokrytí a kapacitní omezení v oblastech s vysokou koncentrací pěších, což informuje o investicích do infrastruktury. Jak se sítě vyvíjely směrem k 5G s kmitočty v pásmu mmWave, byly modely typu PA rozšířeny o prostorové charakteristiky pro testování formování svazku. Jeho pokračující používání až po Release 19 dokládá jeho trvající relevanci pro zajištění toho, aby bezdrátové systémy poskytovaly robustní konektivitu pro každodenní mobilitu uživatelů.

## Klíčové vlastnosti

- Modeluje mobilitu pěších uživatelů s nízkou rychlostí 3 km/h.
- Definuje vícecestný útlum (fading) s přiměřeným rozprostřením zpoždění.
- Používá strukturu s čárovým zpožděním (TDL) se specifickými parametry drah.
- Začleňuje Dopplerův posun pro časově proměnné efekty na kanálu.
- Standardizován pro testování shody v LTE a 5G.
- Podporuje hodnocení výkonu přijímačů a systémů MIMO.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.827** (Rel-17) — Study on Audio-Visual Service Production Stage 1
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.714** — 3GPP TR 36.714
- **TS 36.715** — 3GPP TR 36.715
- … a dalších 31 specifikací

---

📖 **Anglický originál a plná specifikace:** [PA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pa/)
