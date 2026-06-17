---
slug: "lcld"
url: "/mobilnisite/slovnik/lcld/"
type: "slovnik"
title: "LCLD – Low Complexity Low Delay"
date: 2025-01-01
abbr: "LCLD"
fullName: "Low Complexity Low Delay"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcld/"
summary: "LCLD označuje soubor funkcí 3GPP a vylepšení kodeků navržený pro podporu služeb s přísnými požadavky na nízkou latenci a nízkou složitost, jako je immersivní komunikace a rozšířená realita. Optimalizu"
---

LCLD je soubor funkcí 3GPP a vylepšení kodeků navržený pro podporu služeb s nízkou latencí a nízkou složitostí, jako je immersivní komunikace, optimalizací zpracování zvuku a videa za účelem snížení zpoždění a výpočetní náročnosti.

## Popis

Low Complexity Low Delay (LCLD, nízká složitost a nízké zpoždění) je v 3GPP služebně orientovaný koncept, který zahrnuje technické specifikace a optimalizace kodeků zaměřené na umožnění aplikací s náročnými omezeními latence a složitosti. Primárně se zaměřuje na multimediální služby a zahrnuje vylepšení zvukových a video kodeků – jako je například kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo Versatile Video Coding (VVC) – za účelem minimalizace času kódování a dekódování při zachování přijatelné kvality. Toho je dosaženo prostřednictvím algoritmických vylepšení, zjednodušených režimů zpracování a efektivních schémat paketizace, která snižují celkové zpoždění od snímání signálu k jeho přehrání. Z architektonického hlediska jsou funkce LCLD implementovány jak v uživatelském zařízení (UE), tak v síťových prvcích, přičemž specifikace jako 26.249 podrobně popisují požadavky na výkon a 26.996 pokrývá konfigurace kodeků.

Jak LCLD funguje, zahrnuje vícevrstvý přístup. Na úrovni kodeku modifikace zahrnují rychlejší transformační algoritmy, redukované vyrovnávací paměti look-ahead a adaptivní řízení přenosové rychlosti (bitrate), které upřednostňuje nízkou latenci před maximální kompresí. Například v hlasové komunikaci mohou režimy LCLD deaktivovat některé postprocesní filtry nebo používat kratší délky rámců ke snížení zpoždění zpracování. U video služeb se používají techniky jako je přeřazování snímků s nízkým zpožděním (low-delay picture reordering) nebo kódování na bázi řezů (slice-based encoding). Tyto optimalizace jsou vyjednány během nastavení relace prostřednictvím signalizačních protokolů, jako je Session Description Protocol (SDP), což umožňuje zařízením dohodnout se na parametrech kompatibilních s LCLD. Dále jsou integrovány síťové aspekty, jako je priorizace QoS a podpora edge computingu, za účelem dalšího snížení přenosové latence.

Role LCLD v síti je klíčová pro nově vznikající případy užití, jako je rozšířená realita ([AR](/mobilnisite/slovnik/ar/)), virtuální realita (VR) a interaktivní hraní her v reálném čase, kde zpoždění nad několik milisekund může degradovat uživatelský zážitek. Standardizací operací s nízkou složitostí a nízkým zpožděním 3GPP zajišťuje interoperabilitu napříč zařízeními a sítěmi, což umožňuje škálovatelné nasazení immersivních služeb. LCLD také souzní s možnostmi systému 5G, jako je dělení sítě (network slicing) pro enhanced mobile broadband (eMBB) a ultra-reliable low-latency communication (URLLC), a poskytuje tak ucelený rámec pro aplikace citlivé na latenci. Vývoj LCLD od verze Rel-18 dále odráží pokračující snahy o vyvážení výkonu s energetickou spotřebou zařízení a náklady, což činí pokročilé služby dostupnými na širším spektru hardwaru.

## K čemu slouží

LCLD bylo zavedeno, aby řešilo rostoucí poptávku po službách multimedií v reálném čase, které vyžadují nízkou latenci i nízkou výpočetní složitost – výzvy, kterým předchozí standardy kodeků plně nedostály. Jak aplikace, jako je rozšířená realita (XR) a cloudové hraní her, získávaly na popularitě, stávající kodeky – optimalizované pro vysokou efektivitu komprese – často přinášely významná zpoždění kódování a vysoké výpočetní zatížení, což omezovalo jejich vhodnost pro mobilní zařízení s omezenými zdroji. Vytvoření LCLD v Rel-18 bylo motivováno potřebou definovat standardizované a efektivní metody pro poskytování immersivních zážitků bez nadměrného vybíjení baterie nebo vysokých nákladů.

Historicky se předchozí přístupy v 3GPP zaměřovaly buď na kodeky s vysokou kvalitou (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/) pro hlas) nebo na obecné video kódování, které obětovalo latenci ve prospěch lepší komprese. To vytvořilo mezeru pro služby, kde je celkové zpoždění (end-to-end) klíčové, jako je holografická komunikace v reálném čase nebo taktilní internet. LCLD tuto mezeru vyplňuje specifikací optimalizovaných profilů kodeků a síťového chování, které minimalizují zpoždění a zároveň udržují složitost na zvládnutelné úrovni, což umožňuje nasazení na běžných chytrých telefonech a zařízeních IoT. Zároveň řeší omezení dřívějších verzí standardů, kterým chyběla jednotná doporučení pro multimédia s nízkou latencí napříč oblastmi zvuku a videa.

Význam LCLD sahá až k naplnění vize 5G o propojení průmyslu a spotřebitelů plynulými a responzivními službami. Snížením výpočetní náročnosti snižuje náklady na zařízení a spotřebu energie, což podporuje širší adopci. Dále LCLD podporuje dělení sítě (network slicing) tím, že poskytuje parametry specifické pro službu, které lze namapovat na řezy URLLC, a zajišťuje tak celkové (end-to-end) výkonnostní záruky. Jak se 3GPP dále vyvíjí, očekává se, že LCLD bude začleňovat pokroky v kodecích založených na strojovém učení a další integraci s platformami edge computingu.

## Klíčové vlastnosti

- Optimalizuje zvukové a video kodeky pro snížení latence kódování a dekódování
- Definuje režimy zpracování s nízkou složitostí pro minimalizaci výpočetní náročnosti na zařízeních
- Podporuje rychlé vyjednávání relací a adaptivní řízení přenosové rychlosti pro služby v reálném čase
- Integruje se s mechanismy QoS v 5G a dělením sítě pro vytváření celkových (end-to-end) přenosových cest s nízkým zpožděním
- Umožňuje immersivní aplikace jako AR/VR a cloudové hraní her s přísnými rozpočty pro zpoždění
- Specifikuje požadavky na výkon a metodiky testování pro zajištění interoperability

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.249** (Rel-19) — Immersive Audio Split Rendering (ISAR)
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization

---

📖 **Anglický originál a plná specifikace:** [LCLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcld/)
