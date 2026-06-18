---
slug: "ssr"
url: "/mobilnisite/slovnik/ssr/"
type: "slovnik"
title: "SSR – State Space Representation"
date: 2025-01-01
abbr: "SSR"
fullName: "State Space Representation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssr/"
summary: "Matematický model používaný v 3GPP pro reprezentaci a predikci stavu mobilního zařízení, zejména pro lokalizaci a správu mobility. Umožňuje efektivnější a přesnější sledování polohy díky modelování po"
---

SSR je matematický model používaný v 3GPP k reprezentaci a predikci stavu mobilního zařízení pro účely lokalizace a správy mobility prostřednictvím modelování jeho pohybové dynamiky.

## Popis

State Space Representation (SSR) je matematický rámec přijatý ve specifikacích 3GPP pro modelování stavu uživatelského zařízení (UE). 'Stav' typicky zahrnuje proměnné jako poloha, rychlost, zrychlení a případně další dynamické parametry. Tato reprezentace je zásadní pro pokročilé lokalizační techniky, kde síť nebo UE odhaduje polohu UE nikoli jako jediný bod, ale jako součást spojité trajektorie. Model funguje tak, že definuje stavový vektor obsahující tyto klíčové parametry a přechodový model stavu (často založený na fyzice, jako jsou modely konstantní rychlosti nebo zrychlení), který předpovídá, jak se stav v čase vyvíjí. Měření ze síťových uzlů (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) nebo satelitních systémů (jako [GNSS](/mobilnisite/slovnik/gnss/)) slouží jako pozorování, která jsou vkládána do odhadovacích algoritmů, nejčastěji Kalmanova filtru nebo jeho variant, za účelem aktualizace a zpřesnění předpovězeného stavu a snížení chyby odhadu.

Architektura pro lokalizaci založenou na SSR zahrnuje několik klíčových komponent. UE nebo lokalizační server (např. Location Management Function - [LMF](/mobilnisite/slovnik/lmf/)) udržuje model stavového prostoru. UE může hlásit své stavové informace (nebo měření, která umožňují serveru je vypočítat) do sítě. Specifikace jako 3GPP TS 37.355 (LTE Positioning Protocol - [LPP](/mobilnisite/slovnik/lpp/)) a TS 38.305 (NG-RAN; Stage 2 functional specification of User Equipment positioning in NG-RAN) definují protokoly a procedury pro výměnu těchto dat. Parametry modelu, včetně matic kovariance procesního a měřicího šumu, jsou kritické pro ladění výkonu filtru, což vyvažuje rychlou reakci na nová měření s vyhlazováním zašuměných dat.

Role SSR v síti je klíčová pro vysoce přesné lokalizační služby s nízkou latencí vyžadované v 5G a dalších generacích. Na rozdíl od jednodušších metod poskytujících okamžité polohy SSR poskytuje filtrovaný, prediktivní odhad. To je nezbytné pro případy užití jako komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)), sledování dronů a průmyslový IoT, kde pro bezpečnost a automatizaci není nutné znát pouze to, kde zařízení je, ale také kde bude. SSR se integruje s různými lokalizačními metodami, včetně metody rozdílu pozorovaného času příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)), metody rozdílu času příchodu v uplinku ([UTDOA](/mobilnisite/slovnik/utdoa/)) a metody vícečetného času zpátečního letu (Multi-RTT), tím, že poskytuje společný matematický rámec pro časovou fúzi těchto měření, což výrazně zlepšuje přesnost, zejména v náročném prostředí jako jsou městské kaňony nebo vnitřní prostory.

## K čemu slouží

SSR bylo zavedeno, aby řešilo omezení tradičních, diskrétních lokalizačních fixů v mobilních sítích. Dřívější lokalizační metody často poskytovaly nezávislé odhady polohy v konkrétních časech žádosti bez využití časové korelace a pohybové dynamiky UE. To vedlo k méně přesným a 'trhavým' lokalizačním stopám, zejména když byla měření zašuměná nebo vzácná. Pro nové případy užití 5G – jako je autonomní řízení, rozšířená realita a kritické komunikace – byla tato omezení nepřijatelná. Byla zde jasná potřeba metody, která by mohla poskytovat plynulé, prediktivní a vysoce přesné nepřetržité sledování polohy.

Vytvoření SSR bylo motivováno potřebou splnit přísné požadavky na lokalizaci v 5G definované 3GPP, které zahrnují přesnost na úrovni pod metr a ultranízkou latenci pro určité vertikály. Přijetím přístupu stavového prostoru, což je dobře zavedený koncept v teorii řízení a zpracování signálu, poskytlo 3GPP standardizovaný rámec pro filtrování a predikci. To umožňuje síti udržovat trvalé 'porozumění' kinematickému stavu UE, namísto toho, aby každá lokalizační událost byla řešena izolovaně. Řeší problém optimální časové integrace heterogenních měřicích dat (z buněčných signálů, [GNSS](/mobilnisite/slovnik/gnss/), senzorů), minimalizuje dopad jednotlivých měřicích chyb a poskytuje konzistentní trajektorii.

Historicky byly podobné filtrační techniky používány v proprietárních nebo nestandardních implementacích. Standardizace SSR v Rel-15, zejména v rámci architektury lokalizace 5G NR, zajistila interoperabilitu mezi síťovým vybavením a zařízeními od různých dodavatelů. Řešila výzvu podpory pokročilé mobility v hustých sítích a umožnila nové smlouvy o úrovni služeb (SLA) pro vertikální odvětví, která jsou závislá na spolehlivých a přesných informacích o poloze v reálném čase.

## Klíčové vlastnosti

- Modeluje kinematický stav UE (poloha, rychlost, zrychlení) jako časově se vyvíjející vektor
- Využívá Kalmanův filtr nebo podobné algoritmy pro optimální odhad a predikci stavu
- Integruje měření z více zdrojů (např. NR, LTE, GNSS) do jednotného rámce
- Definuje standardizované formáty hlášení a protokoly (prostřednictvím LPP) pro výměnu stavových informací
- Podporuje jak síťově řízené, tak UE-řízené lokalizační architektury
- Umožňuje nepřetržité sledování a prediktivní lokalizaci pro dynamické případy užití

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [SSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssr/)
