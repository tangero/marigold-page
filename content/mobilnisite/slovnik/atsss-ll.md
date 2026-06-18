---
slug: "atsss-ll"
url: "/mobilnisite/slovnik/atsss-ll/"
type: "slovnik"
title: "ATSSS-LL – Access Traffic Steering, Switching and Splitting - Low-Layer"
date: 2026-01-01
abbr: "ATSSS-LL"
fullName: "Access Traffic Steering, Switching and Splitting - Low-Layer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/atsss-ll/"
summary: "ATSSS-LL je funkce 3GPP umožňující inteligentní správu provozu s více přístupy na nižší vrstvě (L2/L3) pro PDU Session. Umožňuje dynamické směrování, přepínání a rozdělování toků uživatelských dat pře"
---

ATSSS-LL je funkce 3GPP pro správu provozu na nižší vrstvě, která dynamicky směruje, přepíná a rozděluje datové toky v rámci 3GPP a ne-3GPP přístupových sítí v rámci jedné PDU Session na základě aktuálních podmínek a politik.

## Popis

ATSSS-LL (Access Traffic Steering, Switching and Splitting - Low-Layer) je klíčovou součástí rámce [ATSSS](/mobilnisite/slovnik/atsss/) organizace 3GPP, standardizovanou od Release 16. Funguje na vrstvě datového spoje (vrstva 2) a síťové vrstvě (vrstva 3) za účelem správy provozu v uživatelské rovině pro jednu [PDU](/mobilnisite/slovnik/pdu/) Session, která je současně připojena k 3GPP přístupové síti (jako je 5G New Radio) i k ne-3GPP přístupové síti (jako je důvěryhodná Wi-Fi). Hlavní architektonickou entitou implementující funkce ATSSS-LL je User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která funguje jako multi-access PDU Session Anchor. UPF je vybavena schopností ATSSS-LL, která zahrnuje klasifikátory a směrovací funkci. Klasifikátor, konfigurovaný prostřednictvím politik řídicí roviny ze Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), kontroluje příchozí uplinkové nebo downlinkové pakety a přiřazuje je konkrétnímu přístupovému rameni (3GPP, ne-3GPP nebo oběma) na základě filtrů, jako je 5-tice (zdrojová/cílová IP/adresa/port, protokol). Směrovací funkce pak provede rozhodnutou akci: směrování (odesílání všech paketů toku přes jeden vybraný přístup), přepínání (přesunutí probíhajícího toku z jednoho přístupu na druhý) nebo rozdělování (distribuce paketů jednoho toku přes více přístupů). Pro rozdělování ATSSS-LL podporuje mechanismy jako Multi-Path Transmission Control Protocol ([MPTCP](/mobilnisite/slovnik/mptcp/)) na transportní vrstvě nebo obecnou adaptační vrstvu definovanou 3GPP (ATSSS-LL-A), která se nachází mezi IP vrstvou a podkladovými přístupově specifickými vrstvami spojů a přidává sekvenční čísla pro přeřazení paketů. UPF i uživatelské zařízení (UE) musí podporovat stejné mechanismy ATSSS-LL, aby tyto operace koordinovaly. Výkonnostní měření (např. latence, ztráty) z obou přístupů mohou být vrácena do řídicí roviny pro dynamickou úpravu směrovacích politik a optimalizaci výkonu aplikací. Tato integrace na nižší vrstvě umožňuje rychlá, síťově asistovaná rozhodnutí, která jsou transparentní pro většinu aplikací na vyšších vrstvách, a poskytuje tak robustní a efektivní datovou rovinu s více přístupy.

## K čemu slouží

ATSSS-LL byl vytvořen pro řešení rostoucí potřeby bezproblémového a efektivního využívání více souběžných přístupových technologií, což je základním kamenem návrhu systému 5G. Před [ATSSS](/mobilnisite/slovnik/atsss/) se zařízení mohla připojit k více sítím (např. k mobilní a Wi-Fi), ale obvykle je používala vzájemně výlučně nebo staticky (jako je mobilita IP toků), často spoléhala na řešení na vyšší vrstvě typu end-to-end, jako je [MPTCP](/mobilnisite/slovnik/mptcp/), která vyžadovala podporu aplikací a nebyla řízena sítí. To vedlo k neoptimálnímu využití zdrojů, neschopnosti rychle reagovat na změny sítě a k roztříštěnému uživatelskému zážitku. Účelem ATSSS-LL je dát jádru sítě 3GPP (konkrétně 5GC) přímou kontrolu na nižší vrstvě nad tím, jak je provoz uživatele distribuován přes dostupné přístupové cesty. To řeší klíčové problémy: zlepšuje celkovou propustnost a kapacitu spojením přístupových spojů, zvyšuje spolehlivost a odolnost připojení prostřednictvím okamžitého převzetí služeb při selhání (přepínání) mezi přístupy a snižuje latenci směrováním citlivého provozu na nejlépe fungující cestu. Motivací byla vize služeb Always-Best-Connected a potřeba podpory náročných případů užití, jako jsou ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a vylepšené mobilní širokopásmové připojení (eMBB), kde by jediný přístup mohl být nedostatečný. Fungováním na nižších vrstvách a správou pomocí síťových politik poskytuje ATSSS-LL standardizovanou, optimalizovanou a transparentní službu s více přístupy, která je lepší než předstandardní nebo čistě klientské implementace.

## Klíčové vlastnosti

- Dynamické směrování provozu na základě aktuálních síťových podmínek a politik operátora
- Bezproblémové přepínání přístupů pro kontinuitu služeb a spolehlivost
- Rozdělení provozu přes 3GPP a ne-3GPP přístupy pro zvýšení propustnosti
- Podpora více režimů směrování: Aktivní-Rezervní, Nejmenší zpoždění, Vyrovnávání zátěže, Na základě priority
- Implementace mechanismů na nižší vrstvě: MPTCP Proxy a adaptační vrstva definovaná 3GPP (ATSSS-LL-A)
- Provoz řízený sítí s politikami poskytovanými SMF pro UPF a UE

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [MPTCP – Multi-Path TCP Protocol](/mobilnisite/slovnik/mptcp/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service

---

📖 **Anglický originál a plná specifikace:** [ATSSS-LL na 3GPP Explorer](https://3gpp-explorer.com/glossary/atsss-ll/)
