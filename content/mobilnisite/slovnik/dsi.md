---
slug: "dsi"
url: "/mobilnisite/slovnik/dsi/"
type: "slovnik"
title: "DSI – Digital Speech Interpolation"
date: 2025-01-01
abbr: "DSI"
fullName: "Digital Speech Interpolation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dsi/"
summary: "Digital Speech Interpolation (DSI) je technika komprese hlasu, která zvyšuje kapacitu přenosových kanálů využitím tichých period v lidské řeči. Dynamicky přiděluje šířku pásma pouze během aktivních ře"
---

DSI je technika komprese hlasu, která zvyšuje přenosovou kapacitu využitím tichých period v řeči k dynamickému přidělování šířky pásma, což umožňuje sdílení jednoho kanálu více konverzacemi.

## Popis

Digital Speech Interpolation (DSI) funguje na principu, že typická obousměrná telefonní konverzace obsahuje významná období ticha, jako jsou pauzy mezi větami a doba naslouchání. Systém používá detekci hlasové aktivity (VAD) k rozlišení mezi aktivní řečí a tichem nebo šumem na pozadí. Během aktivní řeči jsou digitální řečové vzorky paketizovány a přenášeny přes kanál. Během tichých period není kanál této konverzaci přidělen, čímž se uvolňuje šířka pásma pro jiné uživatele.

Základní architektura zahrnuje detektor řeči, vyrovnávací paměť a řídicí jednotku. Detektor řeči analyzuje příchozí signál k identifikaci úseků mluveného slova. Tyto úseky jsou pak umístěny do paketů s příslušnými adresními informacemi. Klíčovou součástí je logika přidělování, která dynamicky přiřazuje dostupné sloty kanálu aktivním mluvčím z fondu uživatelů. Toto statistické multiplexování umožňuje, aby počet podporovaných uživatelů překročil počet fyzických přenosových kanálů.

V kontextu 3GPP je DSI zmíněno ve specifikacích jako 21.905 (Vocabulary) a 43.050 (Transmission planning aspects of the speech service in the [GERAN](/mobilnisite/slovnik/geran/)). Jeho role spočívá především v optimalizaci využití přenosových zdrojů v core síti a backhaulových spojích, zejména pro okruhově spínané hlasové služby. Zvyšuje efektivitu trunku mezi síťovými uzly, čímž snižuje potřebný počet fyzických linek E1/T1 a s tím spojené náklady.

## K čemu slouží

DSI bylo vytvořeno k řešení vysokých nákladů a omezené dostupnosti přenosových linek, zejména v dálkové a mezinárodní telefonii. Před technikami jako je DSI vyžadovalo každé hlasové volání vyhrazený 64 kbps kanál (DS0) po celou dobu svého trvání, bez ohledu na skutečnou řečovou aktivitu. To bylo velmi neefektivní, protože velká část šířky pásma byla během tichých period promrhána.

Historický kontext spočívá v přechodu od analogové k digitální telefonii, kde se maximalizace návratnosti investic do nákladné digitální přenosové infrastruktury stala prvořadou. DSI tento problém vyřešilo aplikací statistického multiplexování na hlasový provoz, což umožnilo operátorům obsloužit více účastníků se stejnými fyzickými zdroji. Přímo řešilo omezení pevného přidělování kanálů, což umožnilo významné úspory nákladů a zvýšení kapacity bez degradace vnímané kvality hlasu pro koncového uživatele.

## Klíčové vlastnosti

- Detekce hlasové aktivity (VAD) pro rozlišení řeči od ticha
- Dynamické přidělování šířky pásma na základě řečové aktivity
- Statistické multiplexování více hlasových kanálů
- Paketizace aktivních úseků řeči
- Zvýšená efektivita trunku pro přenosové spoje
- Transparentní provoz pro koncové uživatele bez vnímané ztráty kvality

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [DSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsi/)
