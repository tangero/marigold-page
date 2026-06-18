---
slug: "stec"
url: "/mobilnisite/slovnik/stec/"
type: "slovnik"
title: "STEC – Slant Total Electron Content"
date: 2025-01-01
abbr: "STEC"
fullName: "Slant Total Electron Content"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/stec/"
summary: "Slant Total Electron Content (STEC) je měření celkového počtu volných elektronů podél dráhy signálu procházejícího ionosférou od satelitu k přijímači. Je to klíčový parametr pro korekci polohových chy"
---

STEC je celkový počet volných elektronů podél dráhy signálu od satelitu k přijímači. Jedná se o klíčový parametr pro korekci ionosférických zpoždění GNSS v sítích 3GPP.

## Popis

Slant Total Electron Content (STEC) je geofyzikální parametr představující integrál hustoty volných elektronů podél konkrétní přímé dráhy mezi satelitem globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) a přijímačem na zemském povrchu nebo v jeho blízkosti. Měří se v jednotkách celkového obsahu elektronů ([TECU](/mobilnisite/slovnik/tecu/)), kde 1 TECU = 10^16 elektronů na metr čtvereční. V kontextu norem 3GPP je STEC klíčový datový prvek používaný pro pokročilé polohovací techniky, zejména pro korekci chyb GNSS měření způsobených ionosférou. Ionosféra, vrstva atmosféry ionizovaná slunečním zářením, zpomaluje a ohýbá rádiové signály, což způsobuje proměnlivé zpoždění, jež je hlavním zdrojem chyb v satelitním určování polohy.

Z architektonického hlediska se data STEC využívají v rámci funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5G jádru sítě nebo ve vylepšeném středisku pro určování polohy mobilních stanic ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE. Síť může uživatelským zařízením (UE) pomáhat s výpočty polohy poskytováním informací nebo korekčních dat STEC. Proces zahrnuje několik komponent: referenční sítě GNSS (např. nepřetržitě pracující referenční stanice - [CORS](/mobilnisite/slovnik/cors/)), které nepřetržitě sledují satelitní signály a počítají STEC; tyto hodnoty jsou následně zpracovány k vytvoření ionosférických modelů nebo korekčních datových proudů. Tyto korekce mohou být doručeny do UE pomocí řídicí roviny (např. LTE Positioning Protocol - [LPP](/mobilnisite/slovnik/lpp/), NR Positioning Protocol - NRPPa) nebo metodami uživatelské roviny.

Technický princip: Surová měřitelná data GNSS (pseudodosah a fáze nosné vlny) naměřená přijímačem jsou ovlivněna ionosférou. Zpoždění je frekvenčně závislé (disperzní). Použitím dvoupásmových přijímačů GNSS (např. přijímajících signály [L1](/mobilnisite/slovnik/l1/) a L5 z [GPS](/mobilnisite/slovnik/gps/)) lze STEC podél dráhy satelit-přijímač přímo odhadnout, protože rozdíl naměřených pseudodosahů na dvou frekvencích je úměrný STEC. Vzorec zahrnuje rozdíl mezi pseudodosahy (nebo fázemi nosné vlny) dělený známou konstantou související s frekvencemi. Jakmile je STEC odhadnut pro referenční stanici, může být interpolován nebo modelován pro poskytnutí korekcí pro blízká UE. Specifikace 3GPP definují, jak mohou být tyto informace STEC nebo z nich odvozené modely vertikálního TEC (VTEC) zabaleny a přeneseny do UE za účelem zlepšení jejího polohového řešení.

Klíčové komponenty v ekosystému 3GPP zahrnují prvky asistenčních dat GNSS definované v LPP, které mohou obsahovat korekce ionosférického zpoždění modelované z dat STEC. Specifikace (např. 37.355 pro LPP, 38.305 pro architekturu NR positioning) detailně popisují formáty a procedury. Úlohou STEC je posunout přesnost určování polohy GNSS z úrovně metrů na úroveň decimetrů nebo dokonce centimetrů při použití s technikami RTK (Real-Time Kinematic) nebo PPP (Precise Point Positioning). To je zvláště klíčové pro náročné aplikace, jako je autonomní řízení, navigace dronů a precizní zemědělství, kde je přesnost pod úrovní metru nezbytná.

## K čemu slouží

Integrace dat STEC do norem 3GPP byla motivována rostoucí poptávkou po vysokopřesném určování polohy napříč četnými odvětvími. Tradiční samostatné GNSS, dokonce i se standardními asistenčními daty, je omezeno na přesnost několika metrů kvůli chybám ze satelitních hodin, drah a nejvíce proměnlivě, ionosféry. Ionosférické zpoždění může způsobit chyby od několika metrů až přes 20 metrů v závislosti na sluneční aktivitě, denní době a geografické poloze. Předchozí přístupy spoléhaly na jednopásmové přijímače používající obecné ionosférické modely (jako je Klobucharův model), které korigují pouze asi 50-70 % chyby. To bylo nedostatečné pro nové případy užití v Release 16 a novějších, jako je V2X, průmyslový IoT a rozšířená realita.

Korekce založené na STEC řeší toto základní omezení tím, že poskytují mnohem přesnější, lokalizované a informace o ionosférických podmínkách v reálném čase. Problém, který řeší, je největší proměnný zdroj chyb v satelitním určování polohy. Začleněním dat STEC do síťově asistovaných a síťově založených polohovacích protokolů umožňuje 3GPP zařízením masového trhu dosáhnout přesnosti, která byla dříve vyhrazena pro drahé geodetické přístroje s dedikovanými korekčními službami. To byl klíčový faktor pro polohování jako službu 5G.

Historicky byly vysokopřesné GNSS korekce doručovány prostřednictvím satelitních augmentačních systémů (SBAS) nebo privátních pozemních sítí (např. RTK sítí). Iniciativa 3GPP, zejména v Release 16 s vylepšeními 5G positioningu, si kladla za cíl využít všudypřítomnou mobilní síť jako spolehlivý kanál pro doručování těchto korekcí s nízkou latencí. Tato konvergence telekomunikací a geolokace vytváří škálovatelnou a standardizovanou platformu. Zavedení STEC jako definovaného parametru ve specifikacích 3GPP (jako je 37.355) umožňuje interoperabilitu mezi různými poskytovateli korekčních služeb GNSS a výrobci zařízení, což podporuje ekosystém pro přesné polohování jako nedílnou součást nabídky mobilních služeb.

## Klíčové vlastnosti

- Kvantifikuje hustotu elektronů v ionosféře podél konkrétní dráhy od satelitu k přijímači
- Umožňuje výpočet ionosférického zpoždění signálu pro vysokopřesnou korekci GNSS
- Odvozeno z dvoupásmových GNSS měření (rozdílů pseudodosahu nebo fáze nosné vlny)
- Může být modelováno a rozesíláno do UE prostřednictvím polohovacích protokolů 3GPP (LPP/NRPPa)
- Kritický vstup pro techniky RTK (Real-Time Kinematic) a PPP (Precise Point Positioning)
- Měří se v jednotkách TECU (Total Electron Content Units)

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [RTK – Real-Time Kinematic](/mobilnisite/slovnik/rtk/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [STEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/stec/)
