---
slug: "fd"
url: "/mobilnisite/slovnik/fd/"
type: "slovnik"
title: "FD – File Distribution"
date: 2026-01-01
abbr: "FD"
fullName: "File Distribution"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fd/"
summary: "File Distribution je služební schopnost v rámci architektur 3GPP, zejména pro Proximity Services (ProSe) a V2X, která umožňuje efektivní vysílání nebo skupinové vysílání souborů do skupiny uživatelský"
---

FD je služební schopnost 3GPP pro ProSe a V2X, která umožňuje efektivní vysílání (broadcast) nebo skupinové vysílání (multicast) souborů do skupiny zařízení pro účely, jako jsou aktualizace softwaru nebo distribuce obsahu.

## Popis

File Distribution je schopnost na servisní vrstvě, která usnadňuje přenos souborů od poskytovatele obsahu nebo aplikačního serveru k více přijímajícím uživatelským zařízením (UE). Nejde o jediný protokol, ale o soubor architektonických funkcí a procedur definovaných napříč specifikacemi servisní a aplikační vrstvy. Klíčovým prvkem pro FD jsou základní schopnosti sítě pro vysílání/skupinové vysílání (broadcast/multicast), jako je evolved Multimedia Broadcast Multicast Service (eMBMS) v 4G/5G nebo komunikace přes postranní spoj (sidelink) pro přímý přenos mezi zařízeními. Služba FD spravuje oznámení relace, doručení souboru a hlášení o příjmu.

Architektura typicky zahrnuje File Distribution Server (nebo Application Server), jádrovou síť pro vysílání/skupinové vysílání (např. [BM-SC](/mobilnisite/slovnik/bm-sc/) pro eMBMS) a uživatelská zařízení (UE). Proces začíná přípravou souboru pro distribuci na serveru, často včetně jeho segmentace na menší zdrojové bloky pro dopřednou korekci chyb (např. pomocí kódů Raptor nebo RaptorQ definovaných pro [MBMS](/mobilnisite/slovnik/mbms/)). Tím vznikne opravný tok vedle zdrojového toku, který umožňuje UE obnovit ztracené pakety bez zpětné vazby. Služba poté oznámí nadcházející relaci distribuce souboru prostřednictvím mechanismu oznámení služby a poskytne UE potřebné parametry pro připojení k relaci, jako je popis relace, časování a [TMGI](/mobilnisite/slovnik/tmgi/) (Temporary Mobile Group Identity).

Během fáze distribuce jsou data souboru doručována přes přenosový kanál pro vysílání/skupinové vysílání. UE sledují přenos a používají opravná data k rekonstrukci původního souboru. Pro FD založenou na [ProSe](/mobilnisite/slovnik/prose/), specifikovanou pro veřejnou bezpečnost a [V2X](/mobilnisite/slovnik/v2x/), může distribuce probíhat přes PC5 postranní spoje (sidelink) mezi UE bez síťové infrastruktury. Zde může jedno UE (distributor) vysílat soubor sousedním UE v dosahu. Specifikace 3GPP definují protokoly pro správu relací, řízení zahlcení a zabezpečení pro takový přímý FD. Služba také zahrnuje mechanismy, pomocí kterých server může získat hlášení o doručení, udávající kolik UE soubor úspěšně přijalo, což je klíčové pro aplikace jako bezdrátové aktualizace firmwaru (FOTA).

## K čemu slouží

File Distribution byla vytvořena, aby řešila potřebu efektivního, škálovatelného a síťově šetrného šíření objemných dat do velkých skupin uživatelů nebo zařízení. Doručování pomocí unicastu (samostatný proud pro každé UE) je pro oblíbený obsah nebo povinné aktualizace vysoce neefektivní, způsobuje zahlcení sítě a plýtvá rádiovými prostředky. FD využívá technologie vysílání/skupinového vysílání k přenosu dat jednou přes sdílený rádiový prostředek, čímž obslouží všechna zainteresovaná UE v oblasti pokrytí současně.

Její zavedení v Rel-14 bylo silně motivováno vývojem Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) pro veřejnou bezpečnost a nástupem komunikace Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). Případy užití, jako je distribuce bezpečnostně kritických map, aktualizací softwaru pro vozové parky nebo multimediálního obsahu davu na akci, vyžadovaly standardizovanou metodu pro skupinový přenos souborů. Předtím takové služby spoléhaly na proprietární aplikace nebo neefektivní unicastové stahování. FD standardizuje postupy, což umožňuje interoperabilitu mezi zařízeními a sítěmi od různých výrobců. Řeší problém zahlcených unicastových spojů v hustých scénářích (jako jsou stadiony nebo dopravní zácpy) a podporuje provoz mimo síť pro veřejnou bezpečnost, kde si zařízení musí soubory sdílet přímo, když je buněčná infrastruktura nedostupná nebo poškozená.

## Klíčové vlastnosti

- Využívá eMBMS pro efektivní síťové doručování pomocí vysílání/skupinového vysílání.
- Podporuje přímou distribuci souborů založenou na ProSe přes PC5 postranní spoj (sidelink) pro scénáře mimo síť.
- Zahrnuje dopřednou korekci chyb na aplikační vrstvě (AL-FEC) pro spolehlivý příjem bez zpětné vazby.
- Definuje procedury oznámení a objevování služby pro nastavení relace.
- Obsahuje mechanismy pro hlášení o doručení poskytovateli obsahu.
- Umožňuje řízení zahlcení pro distribuci přes postranní spoj za účelem spravedlivého řízení rádiových prostředků.

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [AL-FEC – Application Layer Forward Error Correction](/mobilnisite/slovnik/al-fec/)

## Definující specifikace

- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.784** (Rel-16) — Discreet Listening for Mission Critical Services
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [FD na 3GPP Explorer](https://3gpp-explorer.com/glossary/fd/)
