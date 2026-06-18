---
slug: "pcef"
url: "/mobilnisite/slovnik/pcef/"
type: "slovnik"
title: "PCEF – Policy and Charging Enforcement Function"
date: 2025-01-01
abbr: "PCEF"
fullName: "Policy and Charging Enforcement Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcef/"
summary: "Základní funkce jádra sítě v architektuře Policy and Charging Control (PCC), která vynucuje dynamická rozhodnutí o politice (např. blokování, omezení šířky pásma) a uplatňuje pravidla účtování pro dat"
---

PCEF je základní funkce jádra sítě v architektuře PCC, která vynucuje dynamická rozhodnutí o politice a uplatňuje pravidla účtování pro datové relace uživatele na bráně.

## Popis

Policy and Charging Enforcement Function (PCEF) je klíčová logická entita v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) 3GPP, zavedená ve vydání 7. Nachází se na hranici mezi jádrem mobilní sítě a externími paketovými datovými sítěmi (např. internet). Funkčně je PCEF integrována do brány, která zpracovává provoz v uživatelské rovině, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) v GPRS/UMTS, Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v EPS (LTE) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. Jejím hlavním úkolem je v reálném čase vynucovat rozhodnutí o politice a účtování přijatá funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)).

PCEF funguje tak, že zachycuje datové toky uživatele (identifikované IP 5-tičí nebo jinými filtry) a uplatňuje konkrétní pravidla předaná PCRF. Tato pravidla jsou přenášena přes referenční bod Gx (nebo N7 v 5GC) a jsou zapouzdřena v pravidlech Policy and Charging Control (PCC). Každé PCC pravidlo obsahuje informace pro vynucení a účtování. Pro vynucení PCEF provádí funkce jako gating (blokování nebo povolování toků), řízení šířky pásma (nastavení maximálního přenosového výkonu pro uplink/downlink, QoS Class Identifier), správu priority a přesměrování. Pro účtování PCEF uplatňuje způsob účtování (online, offline nebo obojí), identifikuje příslušný účtovací klíč a hlásí události využití (např. objem, dobu trvání) do Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy nebo do Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) přes rozhraní Gz.

Její činnost je dynamická a vázaná na relaci. PCEF komunikuje s PCRF během zřizování, změny a ukončení relace. Může také spouštět aktualizace tím, že informuje PCRF o událostech, které detekuje v uživatelské rovině, jako je změna polohy uživatele, vyčerpání kvóty nebo zahájení nového toku dat služby. Tato zpětná vazba v uzavřené smyčce umožňuje velmi podrobnou a rychle reagující kontrolu politiky. Například když uživatel spustí video stream, může PCEF na pokyn od PCRF dynamicky otevřít vyhrazený nosič se zaručeným přenosovým výkonem, uplatnit specifické sazby účtování a po skončení streamu snížit QoS. Tato architektura centralizuje logiku politiky v PCRF, zatímco vysoce výkonné vynucování decentralizuje do brán jako bodů zúžení provozu prostřednictvím PCEF.

## K čemu slouží

PCEF byla vytvořena k řešení omezení statických, předem nakonfigurovaných mechanismů politiky a účtování v dřívějších mobilních datových sítích (před vydáním 7). Zpočátku byly řízení politiky (jako řízení přístupu a QoS) a účtování do značné míry oddělené, statické funkce konfigurované přímo na bráně. To ztěžovalo implementaci dynamických, na službu orientovaných a uživatelsky specifických politik v reálném čase. Operátoři nemohli snadno nabízet vrstvené služební plány, kontroly utrácení v reálném čase nebo optimalizované QoS pro konkrétní aplikace jako VoIP nebo video.

Zavedení architektury [PCC](/mobilnisite/slovnik/pcc/) s PCEF jako jejím výkonným prvkem bylo motivováno potřebou standardizovaného, flexibilního a centralizovaného rámce pro řízení politiky. Oddělilo logiku rozhodování o politice (PCRF) od jejího vynucování (PCEF), což umožnilo interakci v reálném čase mezi řídicí rovinou a uživatelskou rovinou sítě. Tím se vyřešily klíčové obchodní a technické problémy: umožnilo sofistikovanou diferenciaci služeb, což umožnilo nové výnosové modely jako sponzorovaná data, zero-rating a kvalita na požádání. Technicky poskytlo nástroje pro efektivní správu síťových zdrojů, zajišťující, že kritické služby dostávají potřebnou šířku pásma, a zároveň zabraňovalo tomu, aby jakýkoli jednotlivý uživatel nebo služba přetížila síť.

Dále integrovalo účtování přímo s vynucováním politiky, což umožnilo přesné, na tok založené účtování, které mohlo být sladěno s marketingovými nabídkami (např. datové balíčky pro sociální média). Role PCEF na bráně z ní činí ideální bod pro vynucování, protože všechen uživatelský provoz jí musí procházet, což umožňuje komplexní přehled a kontrolu. Její vytvoření bylo základním krokem k následným mobilním širokopásmovým sítím, které jsou orientované na služby, zpeněžitelné a efektivně spravované.

## Klíčové vlastnosti

- Vynucuje dynamická PCC pravidla (gating, QoS, omezení šířky pásma) na provoz v uživatelské rovině
- Integrována do brány datové relace (GGSN, P-GW, UPF)
- Komunikuje s PCRF přes rozhraní Gx/N7 pro poskytování pravidel a hlášení událostí
- Aplikuje účtování založené na toku a hlásí využití do OCS (Gy) a/nebo OFCS (Gz)
- Podporuje detekci toku dat služby a spouštění relací PCRF
- Umožňuje dynamické řízení QoS, včetně zřizování vyhrazeného nosiče

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 26.924** (Rel-19) — MTSI QoS Improvement Study
- **TS 29.154** (Rel-19) — Nt Reference Point Protocol
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.250** (Rel-19) — Nu Reference Point Stage 3 Specification
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcef/)
