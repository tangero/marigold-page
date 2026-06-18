---
slug: "iesg"
url: "/mobilnisite/slovnik/iesg/"
type: "slovnik"
title: "IESG – Internet Engineering Steering Group"
date: 2025-01-01
abbr: "IESG"
fullName: "Internet Engineering Steering Group"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iesg/"
summary: "Řídící orgán Internet Engineering Task Force (IETF), odpovědný za technické řízení a dohled nad procesy. Přestože není vytvořen 3GPP, je ve specifikacích 3GPP zmiňován v souvislosti se spoluprací a př"
---

IESG je řídící orgán Internet Engineering Task Force, na který se ve specifikacích 3GPP odkazuje pro jeho roli v řízení protokolů IETF přijatých pro mobilní sítě.

## Popis

Internet Engineering Steering Group (IESG) je výkonný orgán technického řízení Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)). V kontextu specifikací 3GPP je na IESG odkazováno proto, že systémy 3GPP rozsáhle začleňují protokoly vyvinuté IETF. IESG nedefinuje funkce specifické pro 3GPP, ale je odpovědný za schvalovací a standardizační proces IETF Request for Comments ([RFC](/mobilnisite/slovnik/rfc/)), které se stávají základem pro architektury 3GPP. Například protokoly jako Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro IMS multimediální telefonii, protokol Diameter pro autentizaci a autorizaci, [HTTP](/mobilnisite/slovnik/http/)/2 pro rozhraní založená na službách v jádru 5G a sady [TCP/IP](/mobilnisite/slovnik/tcp-ip/) jsou všechny standardizovány prostřednictvím procesů IETF, které dohlíží IESG.

Role IESG v ekosystému IETF spočívá v poskytování technického dohledu. Přezkoumává a schvaluje všechny IETF Internet-Drafts, které jsou navrženy k zařazení do Standards Track nebo Best Current Practice RFC. Toto přezkoumání zajišťuje soulad s architektonickými principy IETF, technickou kvalitu a dodržení správného procesu. IESG se skládá z Area Directors (ADs), kteří vedou jednotlivé technické oblasti IETF (např. Transport, Routing, Security, Applications). Když se 3GPP rozhodne použít protokol IETF, typicky odkazuje na konkrétní, stabilní RFC. Stabilita a autorita tohoto RFC jsou přímým důsledkem schválení IESG. 3GPP pak může tento protokol profilovat – definovat jeho konkrétní použití, rozšíření (prostřednictvím nových [AVP](/mobilnisite/slovnik/avp/) nebo hlaviček) a povinné funkce – pro svůj mobilní kontext, což je dokumentováno ve specifikacích 3GPP, jako je 29.835.

Proto zmínka o IESG v dokumentech 3GPP (např. v liaisons nebo normativních referencích) uznává řídící zdroj klíčových externích standardů. Zdůrazňuje kolaborativní vztah mezi oběma normalizačními orgány. Řízení ze strany IESG zajišťuje, že protokoly IETF, na které se 3GPP spoléhá, jsou robustní, otevřeně přezkoumávané a udržované, což následně snižuje riziko a podporuje globální interoperabilitu sítí 3GPP využívajících internetové technologie.

## K čemu slouží

IESG jako takový existuje, aby poskytoval vedení a zajišťoval technickou soudržnost výstupů [IETF](/mobilnisite/slovnik/ietf/), které využívají organizace po celém světě, včetně 3GPP. Jeho účel v kontextu 3GPP je nepřímý, ale zásadní: poskytuje autoritativní, stabilní základ internetových protokolů, na kterém 3GPP buduje své vrstvy služeb. Motivace 3GPP odkazovat na protokoly IETF, a tím i uznávat IESG, byla hnací silou snahy využít dobře zavedené, všudypřítomné a nevlastnické technologie pro datovou komunikaci.

Tento přístup pro 3GPP vyřešil několik problémů. Za prvé se vyhnul znovuvynalézání již existujících řešení pro běžné funkce, jako je signalizace relací ([SIP](/mobilnisite/slovnik/sip/)) nebo autentizace (Diameter). Za druhé zajistil bezproblémovou interoperabilitu mezi mobilními sítěmi a širším internetem. Přijetí standardů IETF usnadnilo konvergenci mezi světem telekomunikací a IT. Omezení předchozích, čistě telekomunikačně specifických protokolů (např. MAP založený na SS7) spočívalo v jejich složitosti a izolovanosti od internetového ekosystému, což zpomalovalo inovace služeb. Tím, že 3GPP stavělo na práci IETF, mohlo soustředit své normalizační úsilí na jedinečné aspekty rádiového rozhraní a mobility, a zároveň integrovat osvědčená řešení pro poskytování služeb založených na IP.

Historický kontext představuje přechod od komutovaných okruhů k plně IP sítím zahájený ve 3GPP Rel-4/5. To vyžadovalo novou sadu protokolů pro jádrovou síť založenou na IP. IETF se svým otevřeným procesem a správou ze strany IESG byl přirozeným zdrojem. Odkazy na IESG ve specifikacích 3GPP formalizují tuto závislost a uznávají řídící strukturu, která zaručuje kvalitu a otevřenost základních protokolů.

## Klíčové vlastnosti

- Poskytuje technické řízení a dohled nad procesy pro standardizační proces IETF.
- Skládá se z Area Directors, kteří jsou odpovědní za specifické technické domény.
- Schvaluje všechny IETF Standards Track a BCP RFC, čímž zajišťuje kvalitu a architektonickou konzistenci.
- Jeho výstupy (RFC) jsou normativně odkazovány 3GPP pro protokoly jako SIP, Diameter a TLS.
- Představuje autoritativní orgán pro internetové standardy používané v architekturách 3GPP.
- Usnadňuje spolupráci a liaison mezi IETF a externími SDO, jako je 3GPP.

## Definující specifikace

- **TR 29.835** (Rel-17) — Study on Port Allocation for 3GPP Interfaces
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks

---

📖 **Anglický originál a plná specifikace:** [IESG na 3GPP Explorer](https://3gpp-explorer.com/glossary/iesg/)
