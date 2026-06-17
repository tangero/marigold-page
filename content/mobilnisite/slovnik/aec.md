---
slug: "aec"
url: "/mobilnisite/slovnik/aec/"
type: "slovnik"
title: "AEC – Acoustical Echo Cancellation"
date: 2025-01-01
abbr: "AEC"
fullName: "Acoustical Echo Cancellation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aec/"
summary: "AEC je technika zpracování signálu, která odstraňuje echo způsobené akustickým propojením mezi reproduktorem a mikrofonem v komunikačních zařízeních. Je nezbytná pro zajištění čisté hlasové kvality v"
---

AEC je technika zpracování signálu, která odstraňuje akustické echo mezi reproduktorem a mikrofonem, aby zajistila čistou hlasovou kvalitu v telefonii a hlasových službách.

## Popis

Acoustical Echo Cancellation (AEC) je sofistikovaný algoritmus digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) navržený k eliminaci akustického echa v plně duplexních hlasových komunikačních systémech. Akustické echo vzniká, když je zvuk z reproduktoru snímán mikrofonem ve stejném nebo blízkém fyzickém prostředí, čímž se vytváří zpožděná a často rušivá zpětnovazební smyčka pro mluvčího na vzdálené straně. V systémech 3GPP je AEC implementována primárně v uživatelském zařízení (UE), jako jsou mobilní telefony, a v síťových prvcích, jako jsou mediální brány nebo funkce mediálních prostředků ([MRF](/mobilnisite/slovnik/mrf/)) pro konferenční služby. Základní architektura zahrnuje adaptivní filtr, který modeluje akustickou cestu (impulzní odezvu) mezi reproduktorem a mikrofonem. Tento filtr generuje odhad signálu echa, který je následně odečten od vstupního signálu mikrofonu. Klíčovou součástí je adaptivní algoritmus, typicky varianta normalizovaných nejmenších středních čtverců (NLMS), který průběžně aktualizuje koeficienty filtru, aby sledoval změny v akustickém prostředí, jako je pohyb zařízení nebo osob v místnosti. Systém také zahrnuje detektor dvojitého mluvení, který pozastavuje adaptaci filtru, když mluví současně mluvčí na blízké i vzdálené straně, aby se zabránilo divergenci, a nelineární procesor (NLP) pro potlačení jakéhokoli zbytkového echa, které lineární adaptivní filtr nedokáže eliminovat. V architektuře 3GPP je funkce AEC specifikována pro hlasové kodeky a provoz v režimu hands-free, což zajišťuje interoperabilitu a konzistentní hlasovou kvalitu napříč sítěmi a zařízeními. Její role je klíčová pro udržení percepční kvality služby (QoS) pro hlasové hovory, zejména ve scénářích, jako jsou hands-free sady v automobilech, hands-free telefony a videokonference, kde je akustické propojení silné. Výkon se měří metrikami, jako je zesílení útlumu návratu echa ([ERLE](/mobilnisite/slovnik/erle/)) a schopnost rychlé konvergence za různých podmínek.

## K čemu slouží

AEC byla vytvořena k řešení základního problému akustického echa v telekomunikacích, které výrazně snižuje hlasovou kvalitu a může učinit konverzaci nesrozumitelnou. Před rozšířeným digitálním zpracováním signálu bylo řízení echa primitivní, často spoléhající na jednoduché vkládání útlumu nebo poloduplexní (push-to-talk) provoz, což vytvářelo nepřirozený konverzační zážitek. Nástup digitálních mobilních sítí a zařízení hands-free problém prohloubil, protože akustické propojení mezi reproduktorem a mikrofonem v jedné skříni se stalo běžným. Historickým motivem pro standardizaci AEC v rámci 3GPP, počínaje Release 5, bylo zajistit konzistentní, vysokou kvalitu hlasové služby, jak se sítě vyvíjely k podpoře pokročilých hlasových služeb a multimédií. Řeší omezení předchozích analogových nebo základních digitálních potlačovačů echa, které mohly způsobovat ořezávání, zkreslení řeči nebo selhání během dvojitého mluvení. Poskytnutím standardizovaného adaptivního přístupu k potlačování umožňuje 3GPP AEC plně duplexní, přirozenou konverzaci i v náročných akustických prostředích, což je zásadní pro přijetí mobilních hlasových služeb uživateli a pro nové aplikace, jako je voice-over-LTE (VoLTE) a videotelefonie.

## Klíčové vlastnosti

- Adaptivní filtrování pomocí NLMS algoritmů pro modelování akustické cesty
- Detekce dvojitého mluvení pro prevenci divergence filtru během simultánní řeči
- Nelineární procesor pro potlačení zbytkového echa
- Specifikované požadavky na výkon pro zesílení útlumu návratu echa (ERLE)
- Integrace s 3GPP hlasovými kodeky a profily hands-free
- Podpora širokopásmového a super-širokopásmového audia pro zvýšení čistoty hlasu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [AEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/aec/)
