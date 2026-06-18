---
slug: "oci"
url: "/mobilnisite/slovnik/oci/"
type: "slovnik"
title: "OCI – Overload Control Information"
date: 2025-01-01
abbr: "OCI"
fullName: "Overload Control Information"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/oci/"
summary: "Overload Control Information (OCI) je signalizační mechanismus používaný v sítích IMS a 5G core k prevenci přetížení serveru. Umožňuje síťové funkci (NF) signalizovat svou úroveň zatížení ostatním NF,"
---

OCI je signalizační mechanismus používaný v sítích IMS a 5G core, který umožňuje síťové funkci signalizovat svou úroveň zatížení ostatním, což umožňuje omezení (throttling) nebo přesměrování požadavků za účelem prevence přetížení serveru.

## Popis

Overload Control Information (OCI) je mechanismus na úrovni protokolu navržený pro správu a zmírnění stavů přetížení v rámci IP Multimedia Subsystem (IMS) a architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) pro 5G. Funguje tak, že umožňuje síťové funkci, která zažívá vysoké zatížení (přetížená entita), informovat své partnerské funkce (klienty) o svém aktuálním stavu kapacity. Tyto informace jsou typicky vloženy do odpovědí protokolu, jako jsou [SIP](/mobilnisite/slovnik/sip/) odpovědi v IMS (např. 503 Service Unavailable) nebo v rámci zpráv [HTTP](/mobilnisite/slovnik/http/)/2 v 5G core (např. odpověď Nudm_UEContextManagement). OCI obsahuje parametry, které klientovi dávají pokyny, jak upravit svůj provoz požadavků. Mezi klíčové parametry patří hodnota 'retry-after', která určuje dobu, po kterou by se klient měl zdržet odesílání nových požadavků, a potenciálně i podrobnější řízení, jako je pravděpodobnostní faktor, kdy je klient instruován, aby před odesláním zahodil určité procento nových požadavků. V 5G SBA je OCI formalizováno jako součást procedur řízení přetížení v TS 29.500. Spotřebitelská [NF](/mobilnisite/slovnik/nf/) (klient) odesílající požadavek na službu k produkující NF (server) zahrnuje do požadavku své vlastní preference řízení přetížení. Pokud je producent přetížen, může odpovědět s OCI, které obsahuje prvek 'load control information', určující redukční faktor a dobu platnosti. Spotřebitelská NF pak musí tuto redukci aplikovat na svou rychlost požadavků směrem k danému producentovi. Mechanismus je dynamický a stavový, což umožňuje správu zatížení v reálném čase. Funguje ve spojení s dalšími funkcemi odolnosti, jako je vyvažování zátěže (load balancing) a bezstavový návrh, aby se zajistilo, že přetížení jednoho bodu nepovede k řetězovému selhání v širší síti.

## K čemu slouží

OCI bylo vytvořeno za účelem řešení kritického problému signalizačního přetížení v plně IP core sítích, který se stal významným s nasazením IMS pro multimediální služby. Tradiční telefonní ústředny měly hardwarové mechanismy řízení přetížení, ale softwarové, IP-připojené [NF](/mobilnisite/slovnik/nf/) jsou náchylné k zahlcení signalizačními bouřemi – náhlými špičkami v provozu, které mohou být způsobeny hromadnými událostmi volání, síťovými poruchami nebo útoky. Bez standardizovaného mechanismu řízení přetížení by přetížený server mohl spadnout, náhodně zahazovat spojení nebo přestat reagovat, což by vedlo k řetězovému selhání ovlivňujícímu služby v celé síti. OCI poskytuje elegantní a kooperativní způsob, jak takové stavy zvládnout. Umožňuje přetížené NF proaktivně se chránit tím, že instruuje své partnery, aby snížili svou zátěž požadavků, namísto pouhého odmítání požadavků, což by mohlo vést k agresivním opakováním ze strany klientů a problém zhoršit. Jeho zavedení v Release 6 pro IMS a pozdější zdokonalení pro 5G [SBA](/mobilnisite/slovnik/sba/) bylo motivováno potřebou robustních, škálovatelných a samoregulačních sítí, které mohou udržet kontinuitu služeb pro prioritní uživatele (např. tísňová volání) i při extrémním zatížení, čímž plní regulatorní a spolehlivostní požadavky.

## Klíčové vlastnosti

- Pásmová signalizace (in-band) stavů zatížení v rámci standardních protokolových zpráv (SIP, HTTP/2)
- Podporuje jak tvrdé omezení (throttling) (timer retry-after), tak pravděpodobnostní redukci provozu
- Umožňuje přetíženým uzlům řídit rychlost příchozích požadavků od partnerů
- Obsahuje doby platnosti, aby byly řídicí informace časově omezené
- Umožňuje zpracování s prioritou, což umožňuje kritickým požadavkům obejít omezení
- Integrální součást procedur řízení přetížení definovaných 3GPP pro IMS a 5GC

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SBA – Scene-Based Audio (Ambisonics)](/mobilnisite/slovnik/sba/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TR 29.843** (Rel-16) — 5GC Load and Overload Control Study
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [OCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/oci/)
