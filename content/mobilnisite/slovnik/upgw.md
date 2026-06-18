---
slug: "upgw"
url: "/mobilnisite/slovnik/upgw/"
type: "slovnik"
title: "UPGW – User Plane Gateway"
date: 2025-01-01
abbr: "UPGW"
fullName: "User Plane Gateway"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/upgw/"
summary: "Funkční entita zavedená ve 3GPP Release 14 pro sítě 5G, odpovědná za přeposílání a zpracování provozu uživatelské roviny. Hraje klíčovou roli v síťových řezech a edge computingu tím, že umožňuje flexi"
---

UPGW je funkční entita definovaná ve 3GPP Release 14 pro sítě 5G, která přeposílá a zpracovává uživatelskou rovinu provozu. Umožňuje flexibilní nasazení pro síťové řezy a edge computing tím, že ji odděluje od řídicí roviny.

## Popis

User Plane Gateway (UPGW) je architektonická komponenta jádra sítě definovaná v rámci architektury systému 5G. Funguje jako specializovaná entita uživatelské roviny, která zajišťuje přeposílání, směrování a zpracování paketů uživatelských dat. Z architektonického hlediska je UPGW součástí konceptu User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), ale ve studiích raného 5G (např. TR 38.801, TR 38.912) je specificky zdůrazňována jako potenciální brána pro provoz. Rozhraní k rádiové přístupové síti (RAN) zajišťuje přes rozhraní N3 a k datové síti přes rozhraní N6, přičemž je řízena funkcí Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) přes rozhraní N4.

Její činnost zahrnuje kontrolu paketů, buffering a vynucování QoS na základě politik poskytovaných řídicí rovinou. UPGW může aplikovat pravidla pro směrování provozu, provádět hlubokou kontrolu paketů pro služebně-aware směrování a podporovat funkce jako uplink classifier a branching point, jak jsou definovány pro UPF. Je klíčovým prvkem pro tzv. local breakout, který umožňuje směrovat provoz do místních datových sítí nebo edge computing aplikací bez nutnosti procházet centrálním jádrem, čímž se snižuje latence.

V kontextu síťových řezů může být UPGW instancována jako součást konkrétního síťového řezu, aby poskytovala izolované prostředky uživatelské roviny přizpůsobené požadavkům služby, jako je enhanced Mobile Broadband (eMBB) nebo Ultra-Reliable Low-Latency Communications ([URLLC](/mobilnisite/slovnik/urllc/)). Její nasazení může být centralizované nebo distribuované na okraji sítě, což usnadňuje scénáře multi-access edge computing ([MEC](/mobilnisite/slovnik/mec/)). Role UPGW je nedílnou součástí dosažení cílů 5G v podobě flexibilního, softwarově definovaného sítění a efektivního využívání zdrojů.

## K čemu slouží

UPGW byla zavedena, aby vyřešila potřebu flexibilnější a škálovatelnější architektury uživatelské roviny v sítích 5G, což znamená posun od monolitických uzlů Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) předchozích generací. Tradiční architektury 4G EPC těsně propojovaly funkce řídicí a uživatelské roviny, což omezovalo flexibilitu nasazení a ztěžovalo optimalizaci pro různé požadavky služeb, jako je nízká latence nebo vysoká propustnost. Snaha o síťové řezy, edge computing a servisně orientované architektury si vyžádala disagregovaný přístup.

Její vytvoření bylo motivováno požadavkem na podporu široké škály 5G případů užití, od massive IoT po kritické komunikace. Oddělením uživatelské roviny mohou operátoři nasazovat instance UPGW blíže uživateli na okraji sítě, aby minimalizovali latenci pro aplikace jako autonomní řízení nebo průmyslová automatizace. Také umožňuje efektivnější směrování a zpracování provozu, což otevírá možnosti inovativních modelů poskytování služeb. Koncept UPGW položil základy pro standardizovanou [UPF](/mobilnisite/slovnik/upf/) definovanou v 5G Fázi 1 (Release 15) a poskytl studijní základ pro vývoj uživatelské roviny.

## Klíčové vlastnosti

- Přeposílání a směrování provozu uživatelské roviny
- Podpora local breakout a edge computingu
- Vynucování QoS a značkování paketů
- Funkce pro směrování provozu a branching point
- Integrace se síťovými řezy pro izolované datové cesty
- Rozhraní k řídicí rovině přes servisně orientovanou architekturu (N4)

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TR 38.801** (Rel-14) — Study on new radio access technology: Radio access architecture and interfaces
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [UPGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/upgw/)
