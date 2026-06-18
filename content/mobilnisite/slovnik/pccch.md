---
slug: "pccch"
url: "/mobilnisite/slovnik/pccch/"
type: "slovnik"
title: "PCCCH – Packet Common Control Channel"
date: 2025-01-01
abbr: "PCCCH"
fullName: "Packet Common Control Channel"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pccch/"
summary: "Logický kanál v sítích GPRS a UMTS používaný pro přenos společných řídicích signalizačních informací souvisejících s paketově orientovanými službami. Přenáší klíčové zprávy pro přidělování zdrojů, spr"
---

PCCCH je logický kanál v sítích GPRS a UMTS, který přenáší společný řídicí signalizační provoz pro paketově orientované služby, umožňuje přidělování zdrojů, správu mobility a navazování relací pro uživatele mobilních dat.

## Popis

Packet Common Control Channel (PCCCH) je logický kanál definovaný v architekturách GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) a UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) pro služby General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a paketově orientované služby UMTS. Funguje na rozhraní síť–mobilní stanice (downlink) a mobilní stanice–síť (uplink) jako sdílený zdroj pro řídicí signalizaci. Na rozdíl od vyhrazených řídicích kanálů je PCCCH využíván více mobilními stanicemi a přenáší nezbytné signalizační zprávy potřebné pro zahájení a udržování paketových datových relací.

Architektonicky je PCCCH namapován na fyzické rádiové zdroje. V GERAN je typicky namapován na Packet Data Channel ([PDCH](/mobilnisite/slovnik/pdch/)), který sám využívá časové sloty na GSM nosné. PCCCH zahrnuje několik podkanálů: Packet Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)) pro uplinkové přístupové požadavky, Packet Paging Channel ([PPCH](/mobilnisite/slovnik/ppch/)) pro downlinkové pagingové hovory, Packet Access Grant Channel ([PAGCH](/mobilnisite/slovnik/pagch/)) pro přidělování zdrojů a Packet Notification Channel (PNCH) pro oznámení služeb typu point-to-multipoint. Tato struktura umožňuje síti efektivně spravovat kolize, volat mobilní stanice, přidělovat zdroje a upozorňovat skupiny.

Jeho činnost je klíčová pro procedury připojení k paketové službě a přenosu dat. Když mobilní stanice chce zahájit datovou relaci, použije PRACH k odeslání žádosti o kanál. Síť odpoví na PAGCH podrobnostmi o okamžitém přidělení, čímž alokuje vyhrazený kanál pro paketový provoz. PPCH se používá k upozornění mobilní stanice na příchozí data nebo k jejímu převedení z klidového stavu do stavu připravenosti pro přenos dat. Díky centralizaci těchto řídicích funkcí na společném kanálu PCCCH optimalizuje využití rádiových zdrojů, snižuje signalizační režii ve srovnání s použitím kanálů pro řízení okruhově orientovaných služeb pro paketová data a poskytuje vyhrazenou řídicí rovinu pro paketové služby GPRS/UMTS.

## K čemu slouží

PCCCH byl zaveden, aby vyřešil základní potřebu vyhrazeného a efektivního mechanismu řídicí signalizace pro paketově orientované služby v sítích GSM a UMTS. Před GPRS byly sítě GSM primárně okruhově orientované a používaly řídicí kanály jako CCCH (Common Control Channel) pro navazování hovorů a správu mobility. Tyto kanály nebyly optimalizovány pro dávkový, nespojovaný charakter paketových dat, což vedlo k neefektivnímu využití rádiových zdrojů a pomalejšímu navazování relací pro datové služby.

Vytvoření PCCCH jako součásti standardu GPRS (Release 97/98, s formální definicí v Release 5) poskytlo řídicí rovinu přizpůsobenou pro paketová data. Vyřešil problém prokládání signalizace pro řízení paketových dat se signalizací pro okruhově orientované služby na sdílených zdrojích, čímž snížil kolize a latenci. Umožnil nezbytné procedury v paketovém režimu, jako je oznámení o změně buňky, paketový paging a udělení uplinkového přístupu specificky pro datové uživatele, což bylo klíčové pro komerční úspěch služeb mobilního internetu jako WAP a raného webového prohlížení. PCCCH vytvořil základní řídicí architekturu, která se později vyvíjela v EDGE a UMTS, oddělila řídicí paradigma pro hlas a data a připravila cestu pro moderní mobilní širokopásmový přístup.

## Klíčové vlastnosti

- Poskytuje sdílený logický kanál pro řídicí signalizaci paketově orientovaných služeb
- Skládá se z podkanálů PRACH, PPCH, PAGCH a PNCH pro specifické funkce
- Umožňuje efektivní náhodný přístup a přidělování zdrojů pro datové relace iniciované mobilní stanicí
- Podporuje paging mobilních stanic v paketovém klidovém režimu
- Optimalizuje využití rádiových zdrojů obsluhou více uživatelů na společném kanálu
- Usnadňuje síťově řízené procedury mobility pro uživatele připojené k paketové službě

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [PCCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pccch/)
