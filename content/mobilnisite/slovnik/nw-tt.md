---
slug: "nw-tt"
url: "/mobilnisite/slovnik/nw-tt/"
type: "slovnik"
title: "NW-TT – Network-side Time-Sensitive Networking Translator"
date: 2026-01-01
abbr: "NW-TT"
fullName: "Network-side Time-Sensitive Networking Translator"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nw-tt/"
summary: "Síťový překladač TSN (NW-TT) je síťová funkce 5G, která propojuje systémy 5G s drátovými sítěmi Time-Sensitive Networking (TSN). Překládá TSN protokoly a časové informace, čímž umožňuje deterministick"
---

NW-TT je síťová funkce 5G, která propojuje systémy 5G s drátovými sítěmi Time-Sensitive Networking (TSN) překladem TSN protokolů a časových informací pro deterministickou komunikaci.

## Popis

Síťový překladač Time-Sensitive Networking (NW-TT) je funkční entita definovaná v architektuře 5G Core sítě, konkrétně zavedená ve 3GPP Release 16 pro podporu integrace se systémy [IEEE](/mobilnisite/slovnik/ieee/) Time-Sensitive Networking ([TSN](/mobilnisite/slovnik/tsn/)). TSN je soubor standardů IEEE Ethernetu, které poskytují deterministickou latenci, spolehlivost a synchronizaci pro časově kritické aplikace běžně používané v průmyslové automatizaci, automobilových sítích a profesionální audio/video technice. NW-TT funguje jako brána nebo překladač umístěný na rozhraní mezi systémem 5G (zahrnujícím 5G Core a Radio Access Network) a externí TSN sítí. Jeho primární role spočívá v mapování a převodu mezi 5G QoS toky a TSN streamy, čímž zajišťuje, že časově citlivá data procházející sítí 5G splňují požadavky TSN na ohraničenou latenci, nízký jitter a bezproblémovou synchronizaci.

Architektonicky je NW-TT logická funkce, která může být nasazena jako samostatný síťový prvek nebo integrována do stávajících funkcí 5G Core, jako je User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Rozhraní se systémem 5G zajišťuje prostřednictvím standardních rozhraní (např. N6 směrem k datovým sítím) a s TSN sítí prostřednictvím ethernetových rozhraní podporujících TSN protokoly. Mezi klíčové komponenty NW-TT patří překladová vrstva pro konverzi protokolů, modul časové synchronizace, který se sladí s hlavním hodinovým zdrojem (Grandmaster) TSN, a mechanismy formování provozu pro vynucení TSN plánování a řízení. NW-TT se účastní TSN řídicí roviny komunikací s Centralized Network Controller ([CNC](/mobilnisite/slovnik/cnc/)) v TSN doméně, kde si vyměňuje informace o požadavcích streamů a síťových zdrojích. Také interaguje s funkcemi řídicí roviny 5G Core, jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), aby zavedl QoS toky odpovídající charakteristikám TSN streamů.

Provozně NW-TT plní několik kritických úkolů. Ukončuje TSN protokoly jako IEEE 802.1AS pro časování a synchronizaci, IEEE 802.1Qbv pro časově řízené plánování a IEEE 802.1Qci pro filtrování a řízení na úrovni jednotlivých streamů. Pro provoz ve směru uplink (od UE k TSN síti) NW-TT přijímá 5G pakety, odstraní 5G zapouzdření, aplikuje TSN značkování a plánování na základě přidruženého ID streamu a přepošle je do TSN sítě v přesně naplánovaných časech. Pro provoz ve směru downlink přijímá TSN rámce, mapuje je na příslušné 5G QoS toky a může aplikovat 5G specifické zapouzdření před odesláním přes UPF směrem k UE. NW-TT také zajišťuje synchronizaci hodin distribucí časových informací z hlavního hodinového zdroje (Grandmaster) TSN napříč systémem 5G, čímž zajišťuje, že všechny prvky (včetně Device-side TSN Translator, [DS-TT](/mobilnisite/slovnik/ds-tt/), v UE) jsou sladěny na společný časový referenční bod. Tato end-to-end časová synchronizace je zásadní pro koordinované průmyslové procesy, kde se akce musí odehrávat v přesných mikrosekundových intervalech.

## K čemu slouží

NW-TT byl vytvořen, aby vyřešil výzvu integrace bezdrátových sítí 5G do stávajících ekosystémů drátového Time-Sensitive Networking ([TSN](/mobilnisite/slovnik/tsn/)), které jsou rozšířené v průmyslové automatizaci, výrobě a dalších kritických doménách. Před jeho zavedením 5G postrádalo nativní podporu pro deterministické komunikační záruky vyžadované TSN, jako je ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) s přesnou časovou synchronizací. Průmyslové sítě tradičně spoléhaly na drátový Ethernet s TSN rozšířeními pro dosažení deterministického výkonu, ale flexibilita a mobilita 5G byly žádoucí pro aplikace jako mobilní roboti, bezdrátové senzory a rozšířená realita v továrnách. NW-TT tento rozdíl překlenuje tím, že umožňuje, aby se 5G jevilo jako virtuální TSN most uvnitř TSN sítě, což umožňuje bezproblémové propojení bez kompromisů v deterministických vlastnostech.

Historicky průmyslové komunikační systémy používaly proprietární fieldbusy nebo standardní Ethernet bez přísných časových záruk, což stačilo pro méně kritickou automatizaci. Vzestup Průmyslu 4.0 a chytré výroby vyžadoval vyšší flexibilitu, bezdrátovou konektivitu a interoperabilitu, což vedlo k přijetí standardů TSN. Bezdrátové technologie jako Wi-Fi nebo 5G před Release 16 však nemohly splnit přísné požadavky TSN na ohraničenou latenci a synchronizaci. Release 16 3GPP konkrétně cílila na vertikální průmysly vylepšením 5G pro URLLC a zavedením podpory TSN. NW-TT spolu s DS-TT tvoří framework pro překlad TSN v systému 5G, což umožňuje 5G transparentně přenášet TSN streamy. Tím se řeší omezení předchozích přístupů, kde byly bezdrátové spoje považovány za nespolehlivé a nevhodné pro časově kritické řídicí smyčky.

Dále NW-TT usnadňuje konvergenci operační technologické (OT) a informačně technologické (IT) sítě tím, že poskytuje standardizovanou překladovou vrstvu. Umožňuje síťovým operátorům a podnikům využít vysokou šířku pásma, nízkou latenci a možnosti síťového řezání (network slicing) 5G, přičemž zachovávají investice do TSN infrastruktury. Řešením nesouladu v protokolech a časování odemyká NW-TT nové případy užití, jako jsou bezdrátové programovatelné logické automaty (PLC), synchronizované víceosé řízení pohybu a monitorování v reálném čase na flexibilních výrobních linkách. Jeho vytvoření bylo motivováno poptávkou průmyslu po bezdrátovém determinismu, což vedlo 3GPP k rozšíření 5G nad rámec vylepšeného mobilního širokopásmového přístupu do oblastí průmyslových misí kritických aplikací.

## Klíčové vlastnosti

- Překlad protokolů mezi 5G QoS toky a TSN streamy
- Časová synchronizace s hlavním hodinovým zdrojem (Grandmaster) TSN
- Formování provozu pro deterministickou latenci a jitter
- Spolupráce s TSN Centralized Network Controller (CNC)
- Podpora klíčových TSN standardů (např. IEEE 802.1AS, 802.1Qbv)
- Integrace s 5G Core UPF a řídicí rovinou

## Související pojmy

- [DS-TT – Device-side TSN Translator](/mobilnisite/slovnik/ds-tt/)
- [TSN – AF Time Sensitive Networking Application Function](/mobilnisite/slovnik/tsn/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.519** (Rel-17) — TSN AF to DS-TT/NW-TT Protocol Aspects
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TR 28.839** (Rel-18) — Technical Report
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.565** (Rel-19) — Time Synchronization Function Services
- **TS 32.282** (Rel-18) — Charging management; Time Sensitive Networking
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [NW-TT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nw-tt/)
