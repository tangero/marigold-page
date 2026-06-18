---
slug: "edp-n"
url: "/mobilnisite/slovnik/edp-n/"
type: "slovnik"
title: "EDP-N – Event Detection Point - Notification"
date: 2025-01-01
abbr: "EDP-N"
fullName: "Event Detection Point - Notification"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/edp-n/"
summary: "Event Detection Point - Notification (EDP-N) je typ EDP, kdy funkce přepínání služeb (SSF) oznámí funkci řízení služeb (SCF) událost, ale nepožaduje instrukce. Zpracování hovoru pokračuje bez přerušen"
---

EDP-N je typem bodu detekce událostí, kdy funkce přepínání služeb (SSF) notifikuje funkci řízení služeb (SCF) o události bez vyžádání instrukcí, což umožňuje nepřerušené zpracování hovoru pro monitorování nebo účtování.

## Popis

Event Detection Point - Notification (EDP-N) je specifický podtyp bodu detekce událostí zavedený pro zjemnění modelu řízení služeb, zejména v rámci [CAMEL](/mobilnisite/slovnik/camel/) a IMS. Na rozdíl od [EDP-R](/mobilnisite/slovnik/edp-r/) (Request) představuje EDP-N detekční bod konfigurovaný pouze pro notifikaci. Když stav hovoru nebo relace dosáhne EDP-N, funkce přepínání služeb ([SSF](/mobilnisite/slovnik/ssf/)) – implementovaná např. v [MSC](/mobilnisite/slovnik/msc/) pro okruhově přepínané hovory nebo v [S-CSCF](/mobilnisite/slovnik/s-cscf/) pro IMS relace – odešle hlášení určené funkci řízení služeb ([SCF](/mobilnisite/slovnik/scf/)) nebo aplikačnímu serveru ([AS](/mobilnisite/slovnik/as/)). Klíčový rozdíl spočívá v tom, že toto hlášení je jednosměrnou komunikací; SSF nepřeruší zpracování hovoru, aby čekala na instrukce. Po odeslání notifikace okamžitě pokračuje v normálním průběhu hovoru/relace podle základního modelu stavu hovoru.

Hlavní architektonickou rolí EDP-N je umožnit pozorování a hlášení informací bez přímého zásahu. Notifikační zpráva obsahuje relevantní data události (např. fakt, že hovor byl přijat, byla přijata konkrétní [DTMF](/mobilnisite/slovnik/dtmf/) číslice nebo vypršel časovač relace). SCF/AS tyto informace přijme a může je použít pro účely jako přírůstkové účtování, zaznamenávání událostí, statistickou analýzu nebo spouštění dalších procesů neovlivňujících hovor. Tento mechanismus je klíčový pro služby, které vyžadují povědomí o událostech hovoru, ale nepotřebují měnit jeho cestu v reálném čase. Například u služeb s účtováním po skončení hovoru nebo s paušálem může síť potřebovat zaznamenávat události přijetí hovoru pro účtovací záznamy, aniž by musela hovor přerušit.

V rámci protokolové interakce mezi SSF a SCF (např. při použití CAP – CAMEL Application Part) je EDP-N vyvolán a odeslána konkrétní hlášením zpráva. SCF potvrdí příjem, ale SSF neočekává ani neprovádí žádný další příkaz související s řízením hovoru. To z hlediska zpracování hovoru činí EDP-N méně invazivní a s nižší latencí ve srovnání s EDP-R. Jsou definovány pro různé body v modelu hovoru, často pro události, které jsou informačními milníky spíše než rozhodovacími body. Konfigurace toho, zda je detekční bod aktivován jako EDP-N nebo EDP-R, je součástí profilu servisní logiky poskytnutého SSF na začátku řízení služby.

## K čemu slouží

EDP-N byl zaveden pro řešení specifické potřeby v rámci paradigmatu řízení služeb v inteligentních sítích a IMS: potřeby pasivního monitorování a hlášení událostí bez režie a potenciální latence plné interakce typu žádost-odpověď. V raných fázích CAMEL se model primárně zaměřoval na EDP-R, kdy ústředna přerušila zpracování a čekala na instrukce. Ačkoli výkonný, tento model zaváděl zpoždění zpracování a složitost pro scénáře, kde servisní logika pouze potřebovala být informována o události, nikoli ji řídit.

Vytvoření EDP-N to vyřešilo poskytnutím odlehčeného notifikačního mechanismu. Umožnil efektivnější implementaci služeb, jako je podrobné zaznamenávání hovorů, aktualizace účtování na základě událostí (kde se fakturace zaznamenává, ale neomezuje v reálném čase), spouštění zákonného odposlechu a analytika využívání služeb. Tím, že nepřerušují zpracování hovoru, EDP-N snižují zátěž SCF/AS u nekritických interakcí a zlepšují celkovou dobu navazování hovoru pro služby vyžadující pouze monitorování. Představoval vývoj směrem k jemnějšímu a efektivnějšímu rozhraní řízení služeb, s poznáním, že ne všechny interakce služeb vyžadují obousměrné řízení. Toto zjemnění bylo obzvláště důležité s tím, jak sítě rostly a servisní logika se stávala složitější, což vyžadovalo jasné oddělení mezi interakcemi ovlivňujícími řízení a interakcemi pouze pro pozorování.

## Klíčové vlastnosti

- Poskytuje jednosměrnou notifikaci z SSF (MSC, CSCF) do SCF/AS bez přerušení zpracování hovoru
- Používá se pro monitorování, zaznamenávání, ne-reálné účtování a sběr statistických dat
- Snižuje latenci při navazování hovoru ve srovnání s interakcemi EDP-R
- Přenáší data specifická pro událost (např. čas přijetí hovoru, detekovaná DTMF číslice) do servisní logiky
- Definován pro informační milníky v modelu stavu hovoru/relace
- Součást architektury řízení služeb CAMEL a IMS, specifikován v protokolech CAP a Diameter/SIP

## Související pojmy

- [EDP-R – Event Detection Point - Request](/mobilnisite/slovnik/edp-r/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [EDP-N na 3GPP Explorer](https://3gpp-explorer.com/glossary/edp-n/)
