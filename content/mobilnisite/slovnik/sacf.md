---
slug: "sacf"
url: "/mobilnisite/slovnik/sacf/"
type: "slovnik"
title: "SACF – Single Association Control Function"
date: 2025-01-01
abbr: "SACF"
fullName: "Single Association Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sacf/"
summary: "Funkční entita v rámci architektury služby CAMEL (Customized Applications for Mobile network Enhanced Logic), která řídí jediné přidružení neboli dialog mezi gsmSCF (funkce řízení služeb) a gsmSSF (fu"
---

SACF je funkční entita CAMEL, která řídí jediné přidružení mezi gsmSCF a gsmSSF a spravuje stav a provádění jedné interakce služby CAMEL.

## Popis

Single Association Control Function (SACF) je klíčovou součástí architektury [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile network Enhanced Logic), která umožňuje operátorské inteligentní síťové služby v mobilních sítích 2G, 3G a novějších. Nachází se uvnitř gsmSCF (Service Control Function), což je uzel hostující servisní logiku CAMEL. SACF je zodpovědná za řízení jediného přidružení neboli dialogu mezi gsmSCF a gsmSSF (Service Switching Function) v [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/). Toto přidružení odpovídá provádění služby CAMEL pro jednu konkrétní relaci účastníka, například předplacené volání nebo službu přizpůsobeného směrování. SACF spravuje celý životní cyklus této interakce služby.

Architektonicky je SACF logická funkce definovaná uvnitř gsmSCF. Když je zahájeno volání nebo relace spuštěná CAMEL, gsmSSF odešle zprávu Initial [DP](/mobilnisite/slovnik/dp/) (Detection Point) do gsmSCF. gsmSCF pro toto konkrétní přidružení vytvoří instanci SACF. SACF poté provádí servisní logiku CAMEL (např. skript nebo program), komunikuje s gsmSSF prostřednictvím operací [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part) a udržuje stav dialogu. Zpracovává následné události hlášené gsmSSF, jako je přijetí hovoru, odpojení nebo specifická oznámení, a posílá zpět příkazy do gsmSSF, například Continue, Connect, ReleaseCall nebo RequestReportBCSMEvent. SACF zajišťuje, že servisní logika je prováděna správně v souladu s detekovanými body a profilem služeb účastníka.

Klíčovými součástmi činnosti SACF jsou správa stavu dialogu, dohled nad časovači a správa prostředků. Udržuje kontextové informace pro přidružení, včetně identity účastníka, čísla volaného, aktuálního stavu hovoru a jakýchkoli akumulovaných dat pro službu (např. odečtený kredit). SACF komunikuje s dalšími funkcemi CAMEL, jako je Multiple Association Control Function ([MACF](/mobilnisite/slovnik/macf/)), která může dohlížet na více SACF, ale samotná SACF se zaměřuje na jediný dialog. Její role je klíčová pro zajištění, že služba [IN](/mobilnisite/slovnik/in/) (Intelligent Network) je konzistentně aplikována po celou dobu hovoru, od sestavení do ukončení, a že všechny síťové prostředky jsou spravovány vhodně pod kontrolou servisní logiky.

## K čemu slouží

SACF byla vytvořena jako součást standardu [CAMEL](/mobilnisite/slovnik/camel/), aby poskytla strukturovaný, škálovatelný model pro řízení inteligentních síťových služeb v mobilních sítích. Před CAMEL vyžadovala implementace operátorských služeb, jako je předplacená služba nebo virtuální privátní sítě, proprietární, nestandardní řešení, která bylo obtížné spravovat a zajišťovat jejich interoperabilitu. Architektura CAMEL zavedla standardizovaný způsob oddělení řízení služeb (gsmSCF) od přepojování hovorů (gsmSSF). SACF slouží jako centrální řídicí entita pro jednu instanci služby, čímž řeší problém správy složitosti a stavu interakce služby.

Její zavedení ve verzi 8 (ačkoli samotný CAMEL začal dříve) zdokonalilo architekturu řídicí roviny pro pokročilé služby. SACF řeší potřebu dobře definované funkční entity, která dokáže zvládnout dialog mezi servisní logikou a síťovou přepojovací funkcí. Zajišťuje, že každé vyvolání služby je izolované, stavové a může být spravováno nezávisle, což je klíčové pro spolehlivost a škálovatelnost. Tím, že existuje vyhrazená řídicí funkce pro každé přidružení, může síť efektivně podporovat miliony souběžných služeb CAMEL s jasným omezením chyb a správou prostředků. SACF je zásadní pro umožnění výnosových, přizpůsobených služeb ve standardizovaném, více-dodavatelském prostředí.

## Klíčové vlastnosti

- Řídí jediné přidružení/dialog CAMEL mezi gsmSCF a gsmSSF
- Provádí servisní logiku CAMEL pro konkrétní relaci účastníka
- Spravuje stav a životní cyklus interakce služby
- Zpracovává zprávy CAP (Initial DP, EventReportBCSM atd.)
- Vydává příkazy CAP do gsmSSF (Connect, Continue, ReleaseCall)
- Udržuje kontext a dohled nad časovači pro přidružení

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [MACF – Multiple Association Control Function](/mobilnisite/slovnik/macf/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SACF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacf/)
