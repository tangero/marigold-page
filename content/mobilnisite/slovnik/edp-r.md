---
slug: "edp-r"
url: "/mobilnisite/slovnik/edp-r/"
type: "slovnik"
title: "EDP-R – Event Detection Point - Request"
date: 2025-01-01
abbr: "EDP-R"
fullName: "Event Detection Point - Request"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/edp-r/"
summary: "Event Detection Point - Request (EDP-R) je typ EDP, ve kterém funkce spínání služeb oznámí funkci řízení služeb událost a explicitně žádá o instrukce. Zpracování hovoru je pozastaveno až do přijetí od"
---

EDP-R je typ bodu detekce událostí (Event Detection Point), ve kterém funkce spínání služeb (service switching function) pozastaví zpracování hovoru, aby oznámila funkci řízení služeb (service control function) výskyt události a explicitně požádala o instrukce pro řízení v reálném čase.

## Popis

Event Detection Point - Request (EDP-R) je klíčový, na řízení orientovaný podtyp bodu detekce událostí v rámci služeb [CAMEL](/mobilnisite/slovnik/camel/) a IMS dle 3GPP. EDP-R představuje detekční bod nakonfigurovaný pro plnou interakci typu požadavek-odpověď. Když zpracování hovoru nebo relace ve funkci spínání služeb (Service Switching Function, [SSF](/mobilnisite/slovnik/ssf/)) – jako je [MSC](/mobilnisite/slovnik/msc/) nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/) – dosáhne EDP-R, pozastaví veškeré další zpracování daného hovoru/relace. SSF následně sestaví detailní služební požadavek, zabalí příslušná data hovoru (např. volané/volající číslo, lokalitu, služební klíč) a odešle je určené funkci řízení služeb (Service Control Function, [SCF](/mobilnisite/slovnik/scf/)) nebo aplikačnímu serveru (Application Server, [AS](/mobilnisite/slovnik/as/)) pomocí protokolů jako CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) či Diameter/[SIP](/mobilnisite/slovnik/sip/) pro IMS.

Architektura stojí na tomto pozastavení a delegování kontroly. SSF přejde do čekacího stavu a drží prostředky hovoru až do přijetí odpovědi od SCF/AS. Vzdálená služební logika požadavek analyzuje, provede své obchodní pravidla (např. zkontroluje kredit, uplatní zákaz hovoru, rozhodne o speciálním směrování) a vrátí řídicí příkaz. Tyto příkazy jsou standardizované instrukce jako 'Continue' (pokračovat v běžném zpracování), 'Connect' (směrovat na konkrétní číslo nebo prostředek), 'ReleaseCall' (ukončit hovor) nebo 'RequestReportBCSMEvent' (aktivovat další EDP). Po přijetí odpovědi SSF příkaz vykoná a obnoví zpracování stavu hovoru z místa určeného instrukcí. Tento mechanismus umožňuje externímu SCF/AS mít rozhodující, reálný vliv na průběh hovoru.

EDP-R se aktivují pro klíčová rozhodovací místa v modelu hovoru. Mezi běžné příklady patří bod 'Collected_Info' ve vycházejícím BCSM (po načtení vytočených číslic, pro rozhodnutí o směrování), bod 'O_Answer' (pro zahájení účtování) nebo bod 'Route_Select_Failure' (pro uplatnění alternativní směrovací logiky). Konfigurace toho, které EDP jsou aktivovány jako EDP-R, je součástí profilu služby staženého do SSF při zahájení hovoru (např. přes CAMEL Subscription Information). Tento model je hlavní pracovní sílou pro implementaci interaktivních služeb náročných na řízení, jako je předplacené účtování (kde každé sestavení a přijetí hovoru vyžaduje kontrolu kreditu a účtování v reálném čase), filtrování hovorů, inteligentní směrování (např. podle denní doby) a služby interakce s uživatelem (např. hlasové menu).

## K čemu slouží

EDP-R byl vyvinut jako klíčový mechanismus pro uskutečnění hlavního slibu architektury Inteligentní sítě (IN) a CAMEL: externí, centralizované řízení zpracování hovorů. Před příchodem IN se jakákoli služba vyžadující rozhodování v reálném čase (jako předplacené hovory) musela implementovat přímo v ústředně, což vedlo k závislosti na dodavateli a pomalým inovacím. Koncept EDP-R to vyřešil vytvořením standardizovaného rozhraní založeného na protokolu, kde může ústředna na definovaných místech doslova 'požádat o instrukce'.

Toto vyřešilo zásadní obchodní a technické problémy. Umožnilo vytvoření samostatné, výkonné infrastruktury bodu řízení služeb (Service Control Point, SCP), která mohla spravovat služby pro miliony účastníků v celé síti bez ohledu na používané dodavatele ústředen. Pro předplacené služby umožnil odečítání kreditu z centrálního účtu v reálném čase s okamžitým ukončením hovoru při jeho vyčerpání. Pro služby virtuální privátní sítě (VPN) umožnil centralizaci komplexních soukromých číslovacích plánů a směrovací logiky. Povaha EDP-R jako 'požadavku' (request) je to, co činí tyto služby interaktivními a řízenými sítí, nikoli pouze sledovanými. Zatímco pozastavení zpracování hovoru zavádí malé zpoždění, je zásadní pro zajištění, že instrukce služební logiky je aplikována dříve, než hovor pokračuje nesprávným směrem. EDP-R je tedy klíčovou technologií umožňující širokou škálu výnosových, síťově hostovaných přidružených služeb, které definovaly mobilní zážitek přesahující pouhou konektivitu.

## Klíčové vlastnosti

- Spustí plnou interakci typu požadavek-odpověď mezi SSF (MSC, CSCF) a SCF/AS, při čemž pozastaví zpracování hovoru
- Umožňuje externí řízení směrování hovorů, účtování, spojení a ukončení v reálném čase
- Používá standardizované řídicí příkazy (Continue, Connect, ReleaseCall atd.) vrácené služební logikou
- Zásadní pro implementaci interaktivních služeb, jako je předplacené účtování, filtrování hovorů a inteligentní směrování
- Aktivuje se na klíčových rozhodovacích bodech základního modelu stavu hovoru (Basic Call State Model, např. Collected_Info, O_Answer)
- Spoléhá na protokoly CAMEL Application Part (CAP) nebo Diameter/SIP pro dialog služebního řízení

## Související pojmy

- [EDP-N – Event Detection Point - Notification](/mobilnisite/slovnik/edp-n/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SCF – Service Control Function (IN context), Service Capability Feature (VHE/OSA context)](/mobilnisite/slovnik/scf/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [EDP-R na 3GPP Explorer](https://3gpp-explorer.com/glossary/edp-r/)
