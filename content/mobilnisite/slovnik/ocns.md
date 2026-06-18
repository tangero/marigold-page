---
slug: "ocns"
url: "/mobilnisite/slovnik/ocns/"
type: "slovnik"
title: "OCNS – Orthogonal Channel Noise Simulator"
date: 2025-01-01
abbr: "OCNS"
fullName: "Orthogonal Channel Noise Simulator"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ocns/"
summary: "Testovací a simulační mechanismus používaný k vytváření řízeného ortogonálního šumu kanálu v sítích UMTS. Je klíčový pro přesné modelování a testování výkonu systémů WCDMA za realistických podmínek ru"
---

OCNS je testovací mechanismus, který generuje řízený ortogonální šum kanálu za účelem modelování realistického rušení pro přesné testování výkonu systému WCDMA a plánování kapacity sítě v UMTS.

## Popis

Orthogonal Channel Noise Simulator (OCNS) je klíčový nástroj definovaný ve specifikacích 3GPP pro Universal Mobile Telecommunications System (UMTS). Jeho hlavní funkcí je generovat simulovaný provoz nebo šum na ortogonálních kanálech downlinku technologie Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)). Ve WCDMA jsou kanály rozlišeny pomocí ortogonálních proměnných rozprostíracích kódů ([OVSF](/mobilnisite/slovnik/ovsf/)). OCNS funguje tak, že generuje pseudonáhodnou bitovou sekvenci, která je následně rozprostřena pomocí určeného OVSF kódu a zakódována scrambling kódem základnové stanice. Tím vzniká signál, který je statisticky reprezentativní pro reálný uživatelský provoz nebo rušení, obsazuje konkrétní kanalizační kód, ale nepřenáší skutečná uživatelská data. Tento simulovaný signál je vložen do downlinkového přenosu, což umožňuje vytvoření řízeného zatíženého prostředí buňky.

Z architektonického hlediska je funkce OCNS implementována uvnitř Node B (základnové stanice) nebo ve specializovaných testovacích zařízeních, která emulují chování Node B. Je řízena a konfigurována Radio Network Controllerem ([RNC](/mobilnisite/slovnik/rnc/)) prostřednictvím specifické signalizace [NBAP](/mobilnisite/slovnik/nbap/) (Node B Application Part) nebo prostřednictvím lokálních správních rozhraní v testovacích sestavách. Mezi klíčové parametry, které lze konfigurovat, patří přidělený OVSF kód (definující kanál), úroveň vysílacího výkonu a charakteristiky pseudonáhodné sekvence. Úpravou výkonu a počtu použitých kódů mohou síťoví inženýři simulovat různé úrovně zatížení buňky, od lehce zatíženého až po plně vytíženého stavu.

Role OCNS v životním cyklu sítě je mnohostranná. Během plánování a nasazování sítě se používá v laboratorních a terénních testech k ověření výkonu přijímače základnové stanice, pokrytí buňky při zatížení a přesnosti předpovědí kapacity. V provozních sítích slouží jako zásadní nástroj pro drive testy a benchmarkování výkonu, což umožňuje izolaci konkrétních kanálů a měření klíčových ukazatelů výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)), jako je poměr signálu k rušení ([SIR](/mobilnisite/slovnik/sir/)) a bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)), za opakovatelných, řízených podmínek rušení. Je také nezbytný pro testování funkcí, jako jsou algoritmy řízení výkonu, procedury předávání hovoru (handover) a mechanismy řízení přístupu, aby bylo zajištěno jejich správné fungování, když buňka není nečinná. Bez OCNS by přesné modelování složitého prostředí rušení systému založeného na CDMA pro účely testování bylo výrazně obtížnější a méně přesné.

## K čemu slouží

OCNS byl vytvořen, aby vyřešil základní výzvu při testování a validaci sítí WCDMA/UMTS: potřebu přesně simulovat zatížené prostředí buňky. V systémech CDMA je výkon inherentně limitován rušením. Chování rádiového spoje, včetně řízení výkonu, předávání hovoru a kapacity, se zásadně liší mezi prázdnou a plně zatíženou buňkou. Před zavedením OCNS testování často spoléhalo na použití skutečného uživatelského zařízení (UE) ke generování zátěže, což bylo pro řízené laboratorní nebo terénní testy nepraktické, neškálovatelné a neopakovatelné.

Tato technologie řeší problém vytvoření předvídatelného a opakovatelného zdroje rušení. Generováním ortogonálního šumu kanálu napodobuje efekt více aktivních uživatelů sdílejících stejnou nosnou frekvenci. To umožňuje výrobcům zařízení a síťovým operátorům provádět důkladné testy shody, benchmarkování výkonu a optimalizaci sítě za realistických podmínek před komerčním spuštěním. Motivací byla potřeba zajistit stabilitu sítě a garance výkonu, protože složité interakce v rozhraní WCDMA nemohly být plně ověřeny pomocí jednoduchých testů jednotlivých spojů. OCNS poskytl standardizovanou metodu pro simulaci 'ostatních uživatelů' v buňce, což je nezbytné pro ověření systémové kapacity, pokrytí při zatížení a robustnosti klíčových algoritmů správy rádiových zdrojů (RRM).

## Klíčové vlastnosti

- Generuje pseudonáhodné šumové sekvence rozprostřené specifickými OVSF kódy.
- Umožňuje simulaci řízeného downlinkového rušení a zatížení buňky.
- Konfigurovatelný vysílací výkon na každý simulovaný kanál.
- Nezbytný pro testování výkonu přijímače Node B a algoritmů RRM.
- Používá se pro drive testy a ověřování KPI za opakovatelných podmínek zatížení.
- Standardizované řízení prostřednictvím signalizace NBAP z RNC v provozních kontextech.

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study

---

📖 **Anglický originál a plná specifikace:** [OCNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocns/)
