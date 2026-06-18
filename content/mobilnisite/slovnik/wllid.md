---
slug: "wllid"
url: "/mobilnisite/slovnik/wllid/"
type: "slovnik"
title: "WLLID – WLAN Link Layer ID"
date: 2025-01-01
abbr: "WLLID"
fullName: "WLAN Link Layer ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wllid/"
summary: "WLLID je jedinečný identifikátor pro spojení na vrstvě WLAN linky, standardizovaný v 3GPP pro scénáře integrovaných sítí. Umožňuje síti rozlišovat a spravovat jednotlivá WLAN spojení, zejména pro směr"
---

WLLID je standardizovaný jedinečný identifikátor 3GPP pro spojení na vrstvě WLAN linky, používaný k rozlišení a správě jednotlivých WLAN spojení pro směrování provozu a agregaci s mobilními sítěmi.

## Popis

[WLAN](/mobilnisite/slovnik/wlan/) Link Layer ID (WLLID) je klíčový identifikátor definovaný ve specifikacích 3GPP k jedinečnému reprezentování spojení na linkové vrstvě vytvořeného přes bezdrátovou lokální síť (WLAN). Funguje jako úchyt na síťové vrstvě pro konkrétní asociaci WLAN mezi uživatelským zařízením (UE) a přístupovým bodem WLAN ([AP](/mobilnisite/slovnik/ap/)) nebo důvěryhodným přístupovým bránovým zařízením WLAN ([TWAG](/mobilnisite/slovnik/twag/)). WLLID je využíván v jádru sítě, konkrétně entitami jako Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo evolved Packet Data Gateway (ePDG), k odkazování a řízení WLAN spoje jako součásti mechanismů politiky a směrování provozu 3GPP.

Architektonicky je WLLID zaveden k překlenutí propasti mezi postupy 3GPP mobilních sítí a přístupem přes ne-3GPP WLAN. Je přidělován a spravován během procedur připojení a autentizace WLAN, jako jsou ty definované pro důvěryhodný přístup WLAN založený na S2a nebo prostřednictvím politik ANDSF. Identifikátor je přenášen ve signalizačních zprávách 3GPP, například mezi UE a síťovými funkcemi řízení politik, což síti umožňuje korelovat IP toky nebo kontexty přenosových kanálů s konkrétním podkladovým WLAN spojem. Tato korelace je nezbytná pro provádění rozhodnutí na straně sítě, jako je přesun konkrétního IP toku z mobilního připojení [PDN](/mobilnisite/slovnik/pdn/) na připojení WLAN nebo naopak, což je proces klíčový pro Access Network Discovery and Selection ([ANDS](/mobilnisite/slovnik/ands/)) a IP Flow Mobility ([IFOM](/mobilnisite/slovnik/ifom/)).

Jeho role je klíčová ve scénářích vyžadujících těsnou integraci mezi 3GPP a WLAN, jako je například agregace LTE-WLAN ([LWA](/mobilnisite/slovnik/lwa/)) nebo obecnější architektury směrování provozu definované od Release 12 dále. WLLID poskytuje potřebnou granularitu, aby síť mohla aplikovat politiky na úrovni jednotlivých spojů, sledovat kvalitu spoje a provádět plynulé předávání spojení bez narušení uživatelských relací. Abstrahuje specifika WLAN MAC adresy nebo BSSID a poskytuje stabilní, síťově spravovaný identifikátor, který přetrvává přes potenciální opětovné asociace WLAN nebo roamingové události, čímž zjednodušuje správu sítě a vynucování politik v heterogenních prostředích.

## K čemu slouží

WLLID byl vytvořen k řešení výzvy správy a identifikace jednotlivých WLAN připojení v rámci politik a architektur jádra sítě 3GPP. Před jeho standardizací mohly sítě 3GPP přistupovat k WLAN jako k monolitické, nedůvěryhodné IP přístupové síti bez možnosti rozlišit mezi více souběžnými WLAN spoji, které by si UE mohlo vytvořit, nebo aplikovat podrobnou kontrolu specifickou pro konkrétní spoj. Toto omezení bránilo pokročilému směrování provozu, plynulé mobilitě a efektivní agregaci zdrojů mezi mobilními a WLAN technologiemi.

Motivace vycházela z tlaku průmyslu na hlubší integraci WLAN s mobilními sítěmi, přesahujícího jednoduché odlehčování provozu směrem k inteligentnější, síťově řízené agregaci a směrování definovanému v Release 12 a později. Koncepty jako LTE-WLAN Radio Level Integration (LWIP) a později LWA vyžadovaly, aby síť měla přehled a kontrolu nad konkrétním používaným WLAN rádiovým spojem. WLLID poskytuje tuto nezbytnou úchytku, umožňující síťovým funkcím odkazovat se na WLAN spoj, monitorovat jej a spravovat se stejnou mírou specifičnosti jako u mobilního rádiového přenosového kanálu. Řeší problém nejednoznačné identifikace spoje, umožňuje přesné vynucování politik, korelaci účtování a správu mobility v konvergovaných přístupových scénářích, čímž naplňuje požadavky na vylepšený uživatelský zážitek a síťovou efektivitu v architekturách 5G a nad rámec 5G.

## Klíčové vlastnosti

- Jednoznačná identifikace spojení na vrstvě WLAN linky v rámci signalizace 3GPP
- Umožňuje síťové řízení politik a směrování provozu pro konkrétní WLAN spoje
- Usnadňuje korelaci mezi IP toky a podkladovými přenosovými kanály ne-3GPP přístupu
- Podporuje architektury jako agregace LTE-WLAN (LWA) a důvěryhodný přístup WLAN
- Abstrahuje identifikátory nižších vrstev WLAN (např. BSSID) pro stabilní správu sítě
- Používán síťovými funkcemi jako ANDSF a PCRF pro rozhodování o výběru přístupu

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)

## Definující specifikace

- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe

---

📖 **Anglický originál a plná specifikace:** [WLLID na 3GPP Explorer](https://3gpp-explorer.com/glossary/wllid/)
