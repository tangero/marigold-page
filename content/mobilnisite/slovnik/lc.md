---
slug: "lc"
url: "/mobilnisite/slovnik/lc/"
type: "slovnik"
title: "LC – Link Characteristics"
date: 2025-01-01
abbr: "LC"
fullName: "Link Characteristics"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lc/"
summary: "Soubor parametrů a metrik, které popisují vlastnosti a výkon komunikačního spoje mezi síťovými uzly. Zahrnuje atributy jako šířka pásma, zpoždění, jitter, chybovost a dostupnost. Tyto charakteristiky"
---

LC je soubor parametrů a metrik popisujících vlastnosti a výkon komunikačního spoje, včetně atributů jako šířka pásma, zpoždění, jitter, chybovost a dostupnost.

## Popis

Link Characteristics (LC) ve standardech 3GPP označují kvantifikovatelné atributy, které definují chování a kvalitu přenosového spoje propojujícího síťové funkce, například mezi Radio Network Controller (RNC) a uzlem core sítě nebo mezi různými prvky core sítě. Tyto charakteristiky nejsou samostatným protokolem ani funkcí, ale konceptuálním rámcem používaným napříč různými oblastmi specifikací k modelování, konfiguraci a monitorování podkladové přenosové sítě, která přenáší uživatelskou a řídicí rovinu. Klíčové parametry typicky zahrnují šířku pásma (maximální a dostupnou propustnost), přenosové zpoždění (jednosměrné a round-trip), variaci zpoždění (jitter), míru ztráty paketů, bitovou chybovost a metriky dostupnosti/spolehlivosti. Tyto jsou často definovány v kontextu IP přenosu nebo [ATM](/mobilnisite/slovnik/atm/) přenosu ve starších vydáních.

Specifikace Link Characteristics je klíčová pro několik provozních procesů. Během plánování a dimenzování sítě inženýři používají parametry LC k zajištění, že přenosové spoje jsou zřízeny s dostatečnou kapacitou a kvalitou pro splnění smluv o úrovni služeb (SLA) pro nadřazené služby 3GPP. Ve fázích provozu systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a manažery prvků ([EM](/mobilnisite/slovnik/em/)) shromažďují měření výkonu související s těmito charakteristikami ke sledování stavu spoje, detekci degradace a spouštění alarmů nebo nápravných akcí, jako je přesměrování provozu. Dále se parametry LC používají v algoritmech pro vyvažování zátěže, řízení zahlcení a rozhodování o směrování uvnitř sítě. Například charakteristiky rozhraní Iu mezi RNC a [MSC](/mobilnisite/slovnik/msc/) nebo SGSN přímo ovlivňují vnímanou kvalitu hlasových hovorů a datových relací.

Z architektonické perspektivy jsou Link Characteristics definovány v technických specifikacích pokrývajících aspekty přenosové sítě (např. TS 25.414 pro rozhraní Iu, TS 29.122 pro rozhraní T8), managementu (TS 32.855 pro správu výkonu) a požadavků na služby (TS 26.110 pro rozpočty zpoždění specifické pro kodek). Tvoří část informačních modelů používaných rozhraními správy jako je Itf-N. Charakteristiky jsou často spojeny s objektem Network Resource Model (NRM) reprezentujícím přenosový spoj, což umožňuje systémům správy získávat a nastavovat prahové hodnoty a přijímat notifikace, když se charakteristiky odchylují od očekávaných rozsahů. To umožňuje automatizaci s uzavřenou smyčkou, kdy může systém správy korelovat degradaci služby (např. vysokou ztrátu paketů VoIP) s konkrétními problémy výkonu spoje (např. vysoký jitter na backhaul spoji).

## K čemu slouží

Koncept Link Characteristics byl formalizován, aby řešil rostoucí složitost oddělení funkcí rádiové sítě a core sítě od podkladové přenosové infrastruktury. V raných mobilních sítích byl přenos často dedikovaná, předvídatelná TDM síť. S migrací na paketově orientovaný IP přenos se charakteristiky spojů staly proměnlivými a méně předvídatelnými kvůli statistickému multiplexování a sdíleným prostředkům. To přineslo výzvy v zaručování kvality služeb (QoS) od konce ke konci pro služby reálného času, jako je hlas a video. Definování standardizovaných Link Characteristics poskytlo společný jazyk pro výrobce zařízení, síťové operátory a vývojáře systémů správy k jednotnému specifikování požadavků, konfiguraci parametrů a měření výkonu.

Jeho vytvoření bylo motivováno potřebou efektivního síťového managementu a zajištění služeb. Bez standardizovaného modelu pro vlastnosti spojů by bylo nemožné automatizovat správu chyb a výkonu nebo implementovat pokročilé řízení provozu. Link Characteristics umožňují operátorům převádět vysoké úrovně [KPI](/mobilnisite/slovnik/kpi/) služeb (např. míru přerušení hovoru, [MOS](/mobilnisite/slovnik/mos/) pro streamování videa) na měřitelné KPI přenosové sítě. Řeší také problém interoperability více dodavatelů v rovině managementu, protože různé síťové prvky mohou hlásit data o výkonu pomocí stejných definic charakteristik. To je nezbytné pro integrovaný síťový management v moderních, disagregovaných sítích, kde RAN, přenos a core mohou pocházet od různých dodavatelů.

## Klíčové vlastnosti

- Standardizovaná sada parametrů výkonu přenosu (zpoždění, jitter, ztráta)
- Integrace do Network Resource Models (NRM) pro správu
- Podpora pro historické měření výkonu i monitorování v reálném čase
- Použití pro plánování a dimenzování přenosové sítě
- Umožňuje korelaci mezi degradací služby a problémy přenosu
- Definováno pro různé typy rozhraní (Iu, Iur, T8, N3, N9)

## Definující specifikace

- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.302** (Rel-19) — LSA Controller IRP Management Operations
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access

---

📖 **Anglický originál a plná specifikace:** [LC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lc/)
