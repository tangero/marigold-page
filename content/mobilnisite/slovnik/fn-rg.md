---
slug: "fn-rg"
url: "/mobilnisite/slovnik/fn-rg/"
type: "slovnik"
title: "FN-RG – Fixed Network Residential Gateway"
date: 2026-01-01
abbr: "FN-RG"
fullName: "Fixed Network Residential Gateway"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fn-rg/"
summary: "Fixed Network Residential Gateway (FN-RG) je standardizovaná síťová funkce, která propojuje pevný širokopásmový přístup uživatele (např. optické vlákno nebo DSL) se sítí 5G Core. Umožňuje systému 5G s"
---

FN-RG je standardizovaná síťová funkce, která propojuje pevný širokopásmový přístup uživatele se sítí 5G Core a umožňuje jeho správu jako důvěryhodného typu přístupu mimo 3GPP (non-3GPP) pro konvergenci.

## Popis

Fixed Network Residential Gateway (FN-RG) je klíčový architektonický prvek definovaný v rámci systému 5G (5GS) pro podporu konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)). Funguje jako standardizovaná, důvěryhodná propojovací funkce pro přístup mimo 3GPP (TNGF), speciálně navržená pro scénáře pevného přístupu v domácnostech nebo firmách. FN-RG slouží jako koncový bod pro pevnou síť uživatele (např. optické vlákno nebo [DSL](/mobilnisite/slovnik/dsl/) linku) a navazuje zabezpečené, standardizované rozhraní ([N2](/mobilnisite/slovnik/n2/) a N3) se sítí 5G Core (5GC). To umožňuje funkcím 5GC pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) spravovat relace a datové toky pro zařízení připojená přes pevnou síť, jako by byla připojena přes 3GPP rádiový přístup.

Z architektonického hlediska obsahuje FN-RG komponenty řídicí i uživatelské roviny. V řídicí rovině implementuje rozhraní N2 směrem k AMF, přenášející signalizaci Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) pro zařízení za touto bránou. Také podporuje ukončení rozhraní N1, což umožňuje uživatelskému zařízení (UE) – což může být router, set-top box nebo jakékoli IP zařízení v domácnosti – komunikovat s jádrem 5GC. Pro autentizaci a zabezpečení FN-RG komunikuje s funkcí autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)) a funkcí bezpečnostní kotvy (SEAF) pomocí standardních 5G autentizačních procedur přes referenční bod N2, čímž zajišťuje, že pevný přístup je důvěryhodným vstupním bodem do sítě 5G.

V uživatelské rovině implementuje FN-RG rozhraní N3 směrem k UPF. Zapouzdřuje a přeposílá datové pakety uživatele z pevné sítě do tunelů [GTP-U](/mobilnisite/slovnik/gtp-u/) směrovaných k příslušné UPF, jak určí funkce pro správu relací (SMF). To umožňuje bezproblémové směrování provozu a uplatňování 5G politik kvality služeb (QoS), včetně 5G identifikátorů QoS (5QI) a reflexivní QoS, na toky pocházející z pevné sítě. Role FN-RG tedy spočívá v abstrakci podkladové technologie pevného přístupu (např. xDSL, PON) a její prezentaci 5GC jako standardizované, spravovatelné přístupové větve, což umožňuje jednotné řízení politik, účtování a správu mobility napříč přístupy 3GPP i mimo 3GPP.

## K čemu slouží

FN-RG byl zaveden k řešení problému fragmentované správy sítě a poskytování služeb v konvergovaných prostředích operátorů. Historicky pevné a mobilní sítě fungovaly jako oddělené sila s odlišnými jádry (např. Broadband Network Gateway (BNG) pro pevné sítě, Packet Data Network Gateway (PGW) pro mobilní), což vedlo k duplicitním funkcím, nekonzistentním uživatelským politikám a neschopnosti nabízet skutečně bezproblémové služby. Vzestup 5G a jeho cloudové, službami řízené architektury (SBA) představoval příležitost ke sjednocení funkcí jádra sítě. FN-RG to umožňuje tím, že dovoluje, aby jediné 5G Core sloužilo jako jednotná kotva pro mobilní i pevný přístup.

Jeho vytvoření bylo motivováno snahou průmyslu směřující k konvergenci pevných a mobilních sítí (FMC), což je klíčový trend pro operátory vlastnící jak pevné, tak mobilní aktiva. Integrací pevného přístupu jako důvěryhodného typu přístupu mimo 3GPP (non-3GPP) do 5GS mohou operátory využít pokročilé schopnosti 5GC – jako je síťové dělení (network slicing), edge computing (MEC) a jednotná autentizace – pro své pevné širokopásmové účastníky. To umožňuje vytváření inovativních konvergovaných služeb, jako je jediné předplatné pro domácnost, mobil a IoT, s konzistentní bezpečností, rodičovskou kontrolou a politikami směrování citlivými na aplikaci, uplatňovanými bez ohledu na to, jak se uživatel připojí.

Dále FN-RG řeší omezení dřívějších proprietárních bran tím, že poskytuje standardizované rozhraní podle 3GPP. Tato standardizace snižuje závislost na dodavateli, zjednodušuje integraci sítě a zajišťuje interoperabilitu mezi zařízeními pro pevný přístup a jádrem 5G od různých dodavatelů. Budoucí vývoj pevné sítě zajišťuje tím, že ji sladí s agilními, softwarově definovanými principy 5G, což umožňuje rychlejší nasazování nových služeb a efektivnější využití síťových zdrojů v celé doméně operátora.

## Klíčové vlastnosti

- Standardizovaná rozhraní N2 (řídicí rovina) a N3 (uživatelská rovina) k 5G Core
- Podporuje 5G autentizační a bezpečnostní procedury (např. 5G-AKA) pro důvěryhodný přístup mimo 3GPP (non-3GPP)
- Umožňuje jednotné řízení politik a vynucování QoS pro pevný provoz prostřednictvím 5G funkce pro řízení politik (PCF)
- Umožňuje bezproblémovou správu relací a mobility pomocí 5G AMF a SMF
- Usnadňuje konvergované účtování pro pevné a mobilní služby prostřednictvím 5G funkce pro účtování (CHF)
- Poskytuje základ pro uplatnění 5G síťového dělení (network slicing) na služby pevného širokopásmového připojení

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [FN-RG na 3GPP Explorer](https://3gpp-explorer.com/glossary/fn-rg/)
