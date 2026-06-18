---
slug: "sand"
url: "/mobilnisite/slovnik/sand/"
type: "slovnik"
title: "SAND – Server and Network Assisted DASH"
date: 2025-01-01
abbr: "SAND"
fullName: "Server and Network Assisted DASH"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sand/"
summary: "3GPP architektura, která umožňuje komunikaci mezi DASH klientem a síťovými/serverovými entitami pro optimalizaci streamovacího přenosu. Umožňuje síti poskytovat klientovi doporučení, metriky a provozn"
---

SAND je 3GPP architektura umožňující komunikaci mezi DASH klientem a síťovými nebo serverovými entitami za účelem optimalizace streamovacího přenosu tím, že poskytuje doporučení a metriky pro chytřejší adaptační rozhodnutí.

## Popis

Server and Network Assisted [DASH](/mobilnisite/slovnik/dash/) (SAND) je standardizovaná architektura definovaná 3GPP pro zlepšení výkonu Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) (DASH) prostřednictvím spolupráce mezi klientem a sítí/poskytovatelem služeb. Tradiční DASH se spoléhá výhradně na heuristiku na straně klienta (jako je úroveň vyrovnávací paměti a naměřená propustnost) pro výběr kvality dalšího mediálního segmentu. SAND zavádí obousměrný komunikační kanál, který umožňuje externím entitám – SAND serveru nebo síťovým uzlům – odesílat pomocná data DASH klientovi a případně klientovi tyto informace zpětně hlásit.

Architektura zahrnuje několik klíčových komponent: DASH klienta, SAND server (nebo síťový podpůrný server) a komunikační kanál SAND. DASH klient je rozšířen o procesor zpráv SAND. SAND server může být provozován poskytovatelem obsahu, síťovým operátorem nebo třetí stranou. Komunikační kanál typicky používá požadavky HTTP POST/GET. Architektura definuje sadu typů zpráv, jako jsou zprávy s metrikami (od klienta k serveru hlásící stav přehrávače), zprávy s parametry (od serveru ke klientovi poskytující informace o síťových podmínkách, jako je dostupná šířka pásma nebo zahlcení) a provozní zprávy (jako je [SAMMO](/mobilnisite/slovnik/sammo/) pro [MBMS](/mobilnisite/slovnik/mbms/)).

Provozně může SAND server shromažďovat data ze síťových sond (např. [PCRF](/mobilnisite/slovnik/pcrf/), [PCEF](/mobilnisite/slovnik/pcef/)) nebo od jiných klientů, aby vytvořil přehled o síťových podmínkách. Poté může odeslat klientovi zprávu s parametry, která indikuje, že síťová cesta ke konkrétnímu [CDN](/mobilnisite/slovnik/cdn/) serveru je zahlcená, a navrhnout klientovi přepnout na alternativní server nebo preventivně snížit datový tok. Naopak klient může odeslat zprávu s metrikami hlásící stav své vyrovnávací paměti, což umožňuje serveru přizpůsobit své rady. Zprávy jsou definovány ve formátu [XML](/mobilnisite/slovnik/xml/), což zajišťuje interoperabilitu. SAND neukládá konkrétní akce klientovi; poskytuje doporučení, přičemž konečné adaptační rozhodnutí ponechává na logice klienta, čímž zachovává klientem řízenou povahu DASH a zároveň obohacuje jeho rozhodovací data.

## K čemu slouží

SAND byl vytvořen, aby řešil omezení čistě klientem řízené adaptace v DASH, která může vést k suboptimálním výsledkům jak pro kvalitu uživatelského zážitku (QoE), tak pro efektivitu sítě. Klient má pouze lokalizovaný, downstreamový pohled na síť. Nemůže vidět upstreamové zahlcení, nadcházející změny síťových politik nebo dostupnost efektivnějších způsobů doručování, jako je multicast. To může vést k tomu, že všichni klienti reagují na zahlcení podobně (způsobují oscilace), přicházejí o příležitosti využít vysílání nebo přetěžují konkrétní server.

Zavedený ve verzi 12 má SAND za cíl umožnit síťově asistované optimalizace bez narušení HTTP-based, klientem řízeného modelu DASH. Řeší problém informační asymetrie. Tím, že umožňuje síti – která má globální přehled o provozu, topologii a službách – komunikovat s klientem relevantní informace, SAND umožňuje stabilnější streamování, lepší využití síťových zdrojů (např. přesměrování na vysílání) a zlepšené celkové QoE. Byl motivován potřebou chytřejšího streamování ve spravovaných sítích (jako jsou sítě mobilních operátorů) a pro umožnění konvergentních unicast-broadcast služeb, čímž položil základy pro pokročilé funkce doručování médií v pozdějších verzích.

## Klíčové vlastnosti

- Definuje obousměrný komunikační kanál mezi DASH klientem a sítí/serverem
- Standardizuje formáty zpráv založené na XML pro metriky, parametry a provozní informace
- Umožňuje síti poskytovat doporučení ohledně zahlcení, zatížení serveru a alternativních cest
- Podporuje hlášení stavu přehrávače (vyrovnávací paměť, pozice) ze strany klienta na server
- Usnadňuje integraci s MBMS prostřednictvím vyhrazených provozních zpráv (např. SAMMO)
- Zachovává klientem řízenou adaptaci a zároveň obohacuje rozhodovací data

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MPD – Media Presentation Description](/mobilnisite/slovnik/mpd/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [SAMMO – SAND Message for MBMS Operations](/mobilnisite/slovnik/sammo/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [CDN – Content Delivery Network / Content Distribution Network](/mobilnisite/slovnik/cdn/)

## Definující specifikace

- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.957** (Rel-19) — Evaluation of MPEG DASH SAND for 3GPP

---

📖 **Anglický originál a plná specifikace:** [SAND na 3GPP Explorer](https://3gpp-explorer.com/glossary/sand/)
