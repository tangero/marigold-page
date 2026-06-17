---
slug: "aul"
url: "/mobilnisite/slovnik/aul/"
type: "slovnik"
title: "AUL – Autonomous Uplink"
date: 2025-01-01
abbr: "AUL"
fullName: "Autonomous Uplink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aul/"
summary: "Autonomous Uplink (AUL) je funkce 4G LTE, která umožňuje uživatelskému zařízení (UE) vysílat uplink data bez čekání na explicitní plánovací povolení od eNodeB. Snižuje režii řídicí signalizace a uplin"
---

AUL je funkce LTE, která umožňuje uživatelskému zařízení vysílat uplink data bez plánovacího povolení tím, že autonomně vybírá zdroje z předem nakonfigurovaného poolu, čímž snižuje latenci a signalizační režii.

## Popis

Autonomous Uplink (AUL) je přístupová metoda založená na soutěžení (contention-based), zavedená v LTE za účelem zvýšení efektivity uplinku, zejména pro sporadický provoz s nízkou latencí. V konvenčním uplinku LTE musí UE nejprve odeslat Plánovací žádost (Scheduling Request, SR) na eNodeB a poté obdržet Uplink povolení (Uplink Grant, UL Grant) přes Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)), než může vysílat data na Physical Uplink Shared Channel (PUSCH). Tento proces založený na povolení zavádí latenci v řídicí rovině a signalizační režii, což je neefektivní pro malé, často se opakující datové pakety typické pro IoT nebo aplikace v reálném čase. AUL tento proces obchází tím, že umožňuje UE vysílat okamžitě pomocí předem nakonfigurovaných rádiových zdrojů, a funguje tedy v režimu 'bez povolení' (grant-free) nebo 'nakonfigurovaného povolení' (configured grant).

Architektura pro AUL zahrnuje konfiguraci UE sadou uplink zdrojů prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) ze strany eNodeB. Tato konfigurace, detailně popsaná v 3GPP TS 36.331, zahrnuje parametry jako periodicita zdroje, přidělení časových a frekvenčních zdrojů (např. konkrétní subrámy a resource blocks), schéma modulace a kódování (Modulation and Coding Scheme, [MCS](/mobilnisite/slovnik/mcs/)) a parametry řízení výkonu. Tyto zdroje jsou semistaticky přiděleny a mohou být sdíleny mezi více UEs, což z AUL činí soutěživou přístupovou metodu. Vrstva Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v UE, dle TS 36.321, spravuje autonomní výběr a použití těchto zdrojů na základě příchodu dat, aniž by vyžadovala dynamická povolení.

Provozně, když má UE uplink data k odeslání, autonomně vybere zdroj ze svého nakonfigurovaného poolu povolení a okamžitě vysílá na PUSCH. Protože stejný pool zdrojů může sdílet více UEs, mohou nastat kolize. Systém spoléhá na robustní návrh fyzické vrstvy, včetně specifických sekvencí demodulačních referenčních signálů (Demodulation Reference Signal, [DM-RS](/mobilnisite/slovnik/dm-rs/)) a potenciálně procesů Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) nakonfigurovaných pro autonomní retransmise, aby se s touto soutěživostí vypořádal. eNodeB provádí na nakonfigurovaných zdrojích slepou detekci (blind detection), aby tato vysílání přijal. AUL je úzce integrována s dalšími funkcemi LTE, jako je Semi-Persistent Scheduling (SPS), ale liší se tím, že nevyžaduje pro aktivaci každého přenosu signalizaci [L1](/mobilnisite/slovnik/l1/)/[L2](/mobilnisite/slovnik/l2/), čímž se latence redukuje v podstatě pouze na dobu přenosu.

V širším síťovém kontextu se AUL nachází v LTE rádiové přístupové síti (E-UTRAN) a ovlivňuje procedury uplink MAC a fyzické vrstvy. Jejím úkolem je optimalizovat využití rádiových zdrojů pro typy provozu, u kterých je režie dynamického plánování nepoměrná vůči velikosti přenášeného payloadu. Minimalizací řídicí signalizace zlepšuje spektrální efektivitu a snižuje spotřebu energie na UE, což je klíčové pro IoT zařízení s omezenou kapacitou baterie. Také podporuje komunikaci s nízkou latencí odstraněním zpoždění pro získání povolení, což odpovídá potřebám nově se objevujících služeb, které předcházely 5G URLLC.

## K čemu slouží

AUL byla vytvořena za účelem řešení neefektivit tradičního plánování uplinku založeného na povolení v LTE pro specifické profily provozu. Standardní plánovací mechanismus LTE, ačkoli je vysoce efektivní pro souvislé datové toky, zavádí významnou latenci a režii řídicí signalizace pro krátké, burstovité datové přenosy. Každý přenos vyžaduje vícestupňový proces: SR, přijetí povolení a následný datový přenos. Pro aplikace jako hlášení dat ze senzorů, pakety Voice over IP nebo průmyslové řídicí příkazy může být tato režie větší než samotný datový payload, což plýtvá rádiovými zdroji a životností baterie.

Historický kontext vývoje AUL v Release 15 je zakořeněn v úsilí průmyslu směrem k hromadné komunikaci mezi stroji (massive Machine-Type Communications, mMTC) a ultra-spolehlivé komunikaci s nízkou latencí (ultra-reliable low-latency communications, URLLC) jako součásti evoluce k 5G. Ještě předtím, než byla plně standardizována 5G New Radio (NR), byla zde potřeba vylepšit LTE, aby tyto případy užití efektivně podporovalo. Předchozí přístupy v LTE, jako Semi-Persistent Scheduling (SPS), snížily signalizaci, ale stále vyžadovaly počáteční explicitní aktivační povolení. Motivací pro AUL byla potřeba skutečně bezpovolení (grant-free) přístupové metody, kde by UE mohlo vysílat okamžitě po vygenerování dat, což radikálně snižuje latenci a signalizační zátěž sítě.

Odstraněním těchto omezení AUL umožňuje škálovatelnější a efektivnější podporu IoT zařízení a služeb s nízkou latencí v sítích LTE. Umožňuje sítím zvládnout obrovské množství zařízení vysílajících malé datové pakety, aniž by byly zahlceny plánovacími žádostmi a povoleními, čímž zlepšuje celkovou kapacitu systému. Toto vylepšení pozici LTE jako způsobilé platformy pro rané služby typu 5G, zajišťuje hladší evoluční cestu a koexistenci s novými funkcemi 5G NR, jako je přístup k uplinku bez povolení (grant-free uplink access).

## Klíčové vlastnosti

- Přenos v uplinku bez povolení (grant-free), který eliminuje latenci spojenou s plánovací žádostí/povolením
- Autonomní výběr předem nakonfigurovaných časově-frekvenčních zdrojů ze strany UE
- Soutěživý přístup (contention-based) umožňující sdílení zdrojů mezi více UEs
- Semistatická konfigurace parametrů poolu zdrojů prostřednictvím signalizace RRC
- Podpora slepé detekce a dekódování na přijímači eNodeB
- Integrace s procesy HARQ pro autonomní retransmise

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [AUL na 3GPP Explorer](https://3gpp-explorer.com/glossary/aul/)
