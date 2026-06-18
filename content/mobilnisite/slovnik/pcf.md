---
slug: "pcf"
url: "/mobilnisite/slovnik/pcf/"
type: "slovnik"
title: "PCF – Positioning Calculation Function"
date: 2026-01-01
abbr: "PCF"
fullName: "Positioning Calculation Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcf/"
summary: "Funkce jádra sítě zodpovědná za výpočet geografické polohy uživatelského zařízení (UE) v síti 3GPP. Zpracovává měřicí data z UE a/nebo sítě, aby vypočítala odhad polohy pomocí různých metod, jako jsou"
---

PCF je funkce jádra sítě, která vypočítává geografickou polohu uživatelského zařízení (UE) zpracováním měřicích dat pomocí metod jako OTDOA nebo A-GNSS a výsledek doručuje žádajícím klientům.

## Popis

Funkce pro výpočet polohy (PCF) je klíčovou součástí architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP, zodpovědnou za výpočetní aspekt určení polohy mobilního zařízení. Působí jako 'motor' systému určování polohy. PCF přijímá nezpracovaná měřicí data a žádosti od centra pro správu polohy ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo jiných funkcí pro správu polohy ([LMF](/mobilnisite/slovnik/lmf/) v 5GC). Jejím hlavním úkolem je vybrat vhodnou metodu určování polohy, získat potřebná měření, provést výpočet polohy a vrátit odhadovanou polohu (zeměpisná šířka, délka, nadmořská výška) s přidruženou úrovní přesnosti a spolehlivosti.

PCF podporuje více standardizovaných metod určování polohy, z nichž každá má svůj vlastní výpočetní algoritmus. Pro metodu [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival) přijímá PCF od UE měření pozorovaných časových rozdílů mezi referenčními signály ze sousedních buněk. Používá databázi známých poloh vysílačů buněk a časových vztahů k řešení hyperbolických rovnic pro polohu UE. Pro metodu [UTDOA](/mobilnisite/slovnik/utdoa/) (Uplink Time Difference of Arrival) PCF zpracovává měření času příchodu uplinkového signálu UE, provedená více jednotkami pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)) v síti. Pro [A-GNSS](/mobilnisite/slovnik/a-gnss/) (Assisted [GNSS](/mobilnisite/slovnik/gnss/)) může PCF poskytovat asistenci dodáním efemeridních a almanachových dat o satelitech UE a následným výpočtem polohy na základě měření pseudovzdáleností odeslaných UE. Pro metodu E-CID (Enhanced Cell ID) PCF kombinuje identitu obsluhující buňky s dalšími měřeními, jako je RTT (Round Trip Time), AoA (Angle of Arrival) nebo úrovně přijímaného signálu, aby zpřesnila odhad polohy.

Architektonicky PCF rozhraní s několika síťovými prvky. Komunikuje s RAN (Radio Access Network) prostřednictvím SMLC (Serving Mobile Location Center) v UMTS/GSM nebo LMF v 5GC, aby získala měření založená na síti nebo aby nařídila RAN/UE provést měření. Může také přistupovat k externím zdrojům dat, jako jsou referenční sítě GNSS pro asistenční data A-GNSS nebo geografické informační systémy. Role PCF je čistě výpočetní a logická; přímo neinteraguje s UE ani sama neprovádí rádiová měření. Její výstup je doručen žadateli (např. GMLC), který následně formátuje a poskytne polohu konečnému klientovi LCS, kterým může být záchranná služba, komerční aplikace nebo vlastní služba síťového operátora.

## K čemu slouží

PCF byla vyvinuta za účelem poskytnutí standardizované, na síti založené schopnosti určovat polohu mobilních zařízení, poháněné primárně regulatorními požadavky na lokalizaci volajících v nouzi (např. E911 v USA, E112 v Evropě) a rostoucí komerční poptávkou po službách založených na poloze (LBS). Rané mobilní sítě měly velmi hrubé možnosti určení polohy, často omezené na identifikaci obsluhující buňky, která mohla pokrývat poloměr několika kilometrů, což je pro nouzové situace nebo přesné služby nepoužitelné.

Vytvoření specializované výpočetní funkce oddělilo složitý matematický úkol výpočtu polohy od funkcí správy a obsluhy klientů (GMLC). Tato modulární architektura umožnila nezávislý vývoj a optimalizaci technologií určování polohy. PCF umožnila zavedení přesnějších metod, jako jsou OTDOA a A-GNSS, které vyžadují sofistikované algoritmy zpracování signálu a výpočtu, které nebylo možné implementovat distribuovaně napříč jinými síťovými uzly.

Centralizací výpočetní logiky poskytuje PCF konzistentní rozhraní pro žádosti o polohu bez ohledu na použitou základní metodu určování polohy. Tato abstrakce umožňuje síti vybrat nejlepší dostupnou metodu (např. A-GNSS venku, OTDOA uvnitř) na základě schopností, požadavků na přesnost a podmínek UE/sítě, aniž by žadající klient musel rozumět technickým detailům. Vývoj PCF odráží neustálý tlak na vyšší přesnost, nižší latenci a podporu nových případů užití, od nouzových služeb až po sledování majetku v IoT a určování polohy vozidel v 5G.

## Klíčové vlastnosti

- Centralizovaná síťová funkce pro výpočet geografické polohy UE
- Podporuje více metod určování polohy: OTDOA, UTDOA, A-GNSS, E-CID
- Zpracovává nezpracovaná měřicí data z UE a/nebo sítě (LMU, RAN)
- Rozhraní s SMLC/LMF pro koordinaci a získávání měření
- Poskytuje odhady polohy s metrikami přesnosti a spolehlivosti
- Umožňuje dynamický výběr metody určování polohy na základě žádosti a schopností

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- … a dalších 61 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcf/)
