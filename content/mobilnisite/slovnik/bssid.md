---
slug: "bssid"
url: "/mobilnisite/slovnik/bssid/"
type: "slovnik"
title: "BSSID – Basic Service Set Identifier"
date: 2025-01-01
abbr: "BSSID"
fullName: "Basic Service Set Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bssid/"
summary: "Jedinečný 48bitový identifikátor pro Wi-Fi Basic Service Set (BSS), ekvivalentní MAC adrese přístupového bodu. Ve standardech 3GPP se používá pro WLAN interoperabilitu k identifikaci konkrétních příst"
---

BSSID je jedinečný 48bitový identifikátor, ekvivalentní MAC adrese, pro Wi-Fi Basic Service Set používaný v 3GPP WLAN interoperabilitě k identifikaci konkrétních přístupových bodů.

## Popis

Basic Service Set Identifier (BSSID) je základní identifikátor v sítích [IEEE](/mobilnisite/slovnik/ieee/) 802.11 (Wi-Fi), který jednoznačně identifikuje Basic Service Set ([BSS](/mobilnisite/slovnik/bss/)), což je v podstatě jeden přístupový bod a jeho přidružené stanice. V kontextu standardů 3GPP se BSSID stává klíčovým pro scénáře interoperability mezi mobilními a WLAN sítěmi definované od Release 12. BSSID je 48bitová adresa, která typicky odpovídá [MAC](/mobilnisite/slovnik/mac/) adrese rádiového rozhraní bezdrátového přístupového bodu. Když uživatelské zařízení (UE) s mobilními i Wi-Fi schopnostmi provádí objevování a výběr sítě, může hlásit zjištěné BSSID mobilní síťové infrastruktuře, což umožňuje síťově řízené směrování provozu mezi mobilním a Wi-Fi přístupem.

Z architektonické perspektivy informace o BSSID proudí přes více prvků 3GPP sítě. UE měří a shromažďuje informace o BSSID během procedur skenování WLAN. Tyto informace mohou být nahlášeny do rádiové přístupové sítě (eNodeB/gNodeB) prostřednictvím měřicích hlášení (specifikovaných v 36.305 a 38.305) nebo do jádra sítě prostřednictvím signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo funkce Access Traffic Steering, Switching and Splitting ([ATSSS](/mobilnisite/slovnik/atsss/)) v 5GC mohou použít informace o BSSID k poskytnutí politik pro výběr konkrétních Wi-Fi přístupových bodů UE. Policy and Charging Rules Function (PCRF) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) mohou také využít informace o BSSID pro uplatnění QoS a tarifních politik specifických pro určité Wi-Fi přístupové body.

V provozu BSSID umožňuje několik klíčových funkcí v 3GPP-WLAN interoperabilitě. Pro síťově řízený výběr WLAN může síť nařídit UE, aby se připojilo ke konkrétním BSSID na základě síťových podmínek, informací o předplatném nebo požadavků služby. Pro správu mobility informace o BSSID pomáhají při bezproblémovém předávání mezi mobilními a Wi-Fi sítěmi, zejména ve scénářích jako LTE-WLAN Aggregation ([LWA](/mobilnisite/slovnik/lwa/)) nebo ATSSS v 5G. Síť může také použít BSSID pro lokalizační služby, jak je specifikováno v 36.355 a 37.355, kde měření BSSID přispívá k určení polohy UE, když GPS není dostupné nebo je nedostatečné.

Technická implementace zahrnuje přenos BSSID v různých protokolových zprávách 3GPP. V LTE se objevuje v konfiguracích a hlášeních měření WLAN mezi UE a eNodeB. V 5G je součástí informací o WLAN mobilitě hlášených UE. BSSID funguje spolu s dalšími identifikátory WLAN, jako je SSID (Service Set Identifier) a HESSID (Homogeneous Extended Service Set Identifier), aby poskytly úplný obraz dostupných Wi-Fi sítí. Zatímco SSID identifikuje název sítě, který může být vysílán více přístupovými body, BSSID jednoznačně identifikuje konkrétní fyzický přístupový bod, což umožňuje přesné síťové řízení a správu.

## K čemu slouží

Integrace BSSID do standardů 3GPP řeší rostoucí potřebu bezproblémové interoperability mezi mobilními a Wi-Fi sítěmi, protože mobilní operátoři stále více nasazují heterogenní sítě kombinující licencované mobilní spektrum s nelicencovaným Wi-Fi spektrem. Před Release 12 byla 3GPP-WLAN interoperabilita relativně základní, zaměřená primárně na objevování přístupové sítě prostřednictvím SSID bez možnosti rozlišit konkrétní přístupové body. Toto omezení ztěžovalo operátorům implementaci sofistikovaného směrování provozu, vyvažování zátěže a uplatňování politik napříč konkrétními Wi-Fi přístupovými body v rámci jejich spravovaných sítí.

Zařazení BSSID do specifikací 3GPP umožňuje síťově řízený výběr konkrétních Wi-Fi přístupových bodů namísto pouze Wi-Fi sítí obecně. To řeší několik praktických výzev nasazení: operátoři mohou směrovat provoz na konkrétní přístupové body na základě aktuálních podmínek zatížení, uplatňovat různé QoS politiky pro různé fyzické lokality, implementovat přesnější lokalizační služby a umožnit pokročilé funkce jako LTE-WLAN Aggregation, kde jsou konkrétní rádiové spoje spravovány na detailní úrovni. Bez identifikace BSSID by síť pouze věděla, že je UE připojeno k určitému SSID, ale ne ke kterému konkrétnímu přístupovému bodu, což omezuje možnosti optimalizace.

Historicky motivace vycházela z rostoucího nasazení Wi-Fi v sítích operátorů, potřeby lepšího řízení provozu v hustých městských prostředích a snahy efektivně využívat všechny dostupné rádiové zdroje. BSSID poskytuje potřebnou úroveň podrobnosti, aby síť mohla činit inteligentní rozhodnutí o tom, který konkrétní Wi-Fi přístupový bod by mělo UE použít, s ohledem na faktory jako síla signálu, zatížení, kapacita backhaulového připojení a výsady předplatného. To představuje významný vývoj oproti dřívějším přístupům k 3GPP-WLAN interoperabilitě, které považovaly všechny přístupové body se stejným SSID za ekvivalentní.

## Klíčové vlastnosti

- 48bitový jedinečný identifikátor ekvivalentní MAC adrese
- Umožňuje síťově řízený výběr konkrétních Wi-Fi přístupových bodů
- Podporuje hlášení měření pro objevování a výběr WLAN
- Umožňuje přesné lokalizační služby využívající Wi-Fi přístupové body
- Umožňuje detailní uplatňování politik na fyzický přístupový bod
- Integruje se s LTE-WLAN Aggregation (LWA) a 5G ATSSS

## Související pojmy

- [HESSID – Homogeneous Extended Service Set Identifier](/mobilnisite/slovnik/hessid/)
- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [BSSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/bssid/)
