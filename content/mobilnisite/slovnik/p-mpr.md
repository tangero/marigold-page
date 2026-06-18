---
slug: "p-mpr"
url: "/mobilnisite/slovnik/p-mpr/"
type: "slovnik"
title: "P-MPR – Power Management Maximum Power Reduction"
date: 2025-01-01
abbr: "P-MPR"
fullName: "Power Management Maximum Power Reduction"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/p-mpr/"
summary: "P-MPR je schopnost uživatelského zařízení (UE), která mu umožňuje snížit svůj maximální vysílací výkon pod nominální maximální úroveň pro zvládnutí vnitřních tepelných omezení, dodržení limitů specifi"
---

P-MPR je maximální snížení výkonu, které může uživatelské zařízení (UE) uplatnit na svůj vysílací výkon, aby zvládlo tepelná omezení, dodrželo limity SAR nebo vyhovělo regionálním předpisům o výkonu.

## Popis

Power Management Maximum Power Reduction (P-MPR) je parametr definovaný ve specifikacích 3GPP, který představuje maximální hodnotu, o kterou smí nebo musí uživatelské zařízení (UE) snížit svůj vysílací výkon z důvodu omezení nesouvisejících s rádiovými frekvencemi (non-RF). Na rozdíl od jiných snížení výkonu, která zohledňují aspekty [RF](/mobilnisite/slovnik/rf/) jako modulační schéma a šířku pásma (např. [MPR](/mobilnisite/slovnik/mpr/), [A-MPR](/mobilnisite/slovnik/a-mpr/)), se P-MPR zabývá omezeními plynoucími z konstrukce UE a jeho provozního prostředí. Hlavní důvody pro uplatnění P-MPR jsou: 1) Řízení teploty: Aby se zabránilo přehřívání zařízení, zejména při dlouhodobém vysílání vysokým výkonem nebo když má kryt zařízení omezený odvod tepla. 2) Dodržení limitu specifické míry absorpce ([SAR](/mobilnisite/slovnik/sar/)): Aby byla zajištěna dodržovat regulačních bezpečnostních limitů pro energii rádiových frekvencí absorbovanou lidským tělem, což může vyžadovat snížení výkonu, když je zařízení drženo blízko těla. 3) Regionální předpisy o výkonu: Aby byly splněny specifické regulační požadavky jednotlivých zemí na maximální vysílací výkon v určitých kmitočtových pásmech nebo scénářích nasazení.

Technicky je P-MPR signalizovanou schopností UE. UE hlásí svou schopnost P-MPR síti, čímž oznamuje maximální snížení výkonu, které může potřebovat uplatnit. Skutečné uplatnění P-MPR je dynamické a řízené samotným UE na základě jeho vnitřních senzorů (např. teploty, přiblížení) a aktuálních provozních podmínek. Síť je o uplatněném P-MPR informována prostřednictvím řídicích informací v uplinku, což základnové stanici (gNB v NR, eNodeB v LTE) umožňuje odpovídajícím způsobem upravit své plánování a přizpůsobení spojení. Například pokud UE uplatní významné P-MPR, jeho efektivní maximální vysílací výkon se sníží, což může snížit dosažitelnou přenosovou rychlost v uplinku nebo pokrytí. Síťový plánovač pak může přidělit robustnější modulační a kódová schémata ([MCS](/mobilnisite/slovnik/mcs/)) nebo poskytnout více zdrojů, aby to kompenzoval.

Specifikace P-MPR zahrnuje podrobné požadavky pro různé třídy výkonu UE, kmitočtová pásma a přenosové scénáře. Je úzce spojena s definicemi Maximálního snížení výkonu (MPR) a Dodatečného maximálního snížení výkonu (A-MPR). MPR zohledňuje inherentní snížení výkonu potřebné kvůli zvolené modulaci (např. vysokovýkonná [QAM](/mobilnisite/slovnik/qam/)) a šířce přenosového pásma. A-MPR je dodatečné, sítí signalizované snížení pro splnění specifických emisních limitů v určitých geografických oblastech nebo síťových nasazeních. P-MPR je samostatné a jeho účinky jsou aditivní. Celkový povolený maximální výstupní výkon UE (P<sub>PowerClass</sub>) je efektivně snížen o součet MPR, A-MPR a P-MPR. Zavedení P-MPR se stalo stále kritičtějším s pokročilými zařízeními vybavenými více vysílači (pro agregaci nosných, [MIMO](/mobilnisite/slovnik/mimo/)), vyššími kmitočtovými pásmy (s větším útlumem na dráze vyžadujícím vyšší výkon) a kompaktními rozměry, což všechno zhoršuje tepelné výzvy a výzvy spojené s SAR.

## K čemu slouží

P-MPR bylo zavedeno, aby řešilo rostoucí složitost a omezení moderních mobilních zařízení, zejména chytrých telefonů. Starší verze 3GPP definovaly Maximální snížení výkonu ([MPR](/mobilnisite/slovnik/mpr/)) pro zvládnutí snížení výkonu souvisejícího s RF, ale formálně nezohledňovaly omezení nesouvisející s RF, která jsou vlastní fyzické konstrukci zařízení a jeho interakci s uživatelem. Jak se zařízení stávala výkonnějšími, multifunkčními a tenkými, řízení odvodu tepla a zajišťování shody s bezpečnostními standardy pro expozici člověka (SAR) se staly významnými technickými výzvami. Zařízení pracující na svém nominálním maximálním výkonu po delší dobu by se mohlo přehřát, což by vedlo k omezení výkonu, poškození součástek nebo nepohodlí uživatele. Podobně jsou limity SAR přísné a zařízení musí zajistit, aby je v žádném scénáři použití nepřekročilo.

Účelem P-MPR je poskytnout standardizovaný rámec ve specifikacích 3GPP, který umožňuje UE dynamicky řídit tato omezení při zachování transparentní komunikace se sítí. Před P-MPR mohli výrobci implementovat proprietární řízení teploty nebo SAR, které mohlo náhle snížit vysílací výkon bez vědomí sítě, což vedlo k neočekávaným výpadkům spojení nebo špatnému uživatelskému zážitku. Definováním P-MPR jako schopnosti a hlášeného parametru standard zajišťuje, že síť může být informována o výkonových omezeních UE a přizpůsobit své strategie přidělování zdrojů. To vede k robustnějšímu a předvídatelnějšímu výkonu systému. Je to obzvláště zásadní pro 5G NR, kde zařízení mohou používat kmitočty mmWave (s vysokoziskovým formováním svazku, které koncentruje energii) nebo pásma sub-6 GHz se širokou šířkou pásma a agregací nosných, přičemž oba scénáře mohou narážet na tepelné limity a limity SAR.

## Klíčové vlastnosti

- Dynamické snížení výkonu na základě vnitřního stavu UE (teplota, senzor přiblížení)
- Řeší omezení nesouvisející s RF: řízení teploty, dodržení SAR a regionální předpisy
- Hlášeno síti jako schopnost UE (např. prostřednictvím UE-EUTRA-Capability)
- Signalizováno síti v reálném čase prostřednictvím řídicích informací v uplinku (např. PHR)
- Aditivní k jiným snížením výkonu (MPR a A-MPR) pro výpočet celkového snížení výkonu
- Kritické pro zařízení s víceanténními systémy, agregací nosných a kompaktními rozměry

## Související pojmy

- [MPR – Allowed Maximum Power Reduction](/mobilnisite/slovnik/mpr/)
- [A-MPR – Additional Maximum Power Reduction](/mobilnisite/slovnik/a-mpr/)
- [SAR – Security Assurance Requirements](/mobilnisite/slovnik/sar/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [P-MPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-mpr/)
