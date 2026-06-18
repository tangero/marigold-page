---
slug: "sna"
url: "/mobilnisite/slovnik/sna/"
type: "slovnik"
title: "SNA – Spending-Status-Notification-Answer"
date: 2026-01-01
abbr: "SNA"
fullName: "Spending-Status-Notification-Answer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sna/"
summary: "Spending-Status-Notification-Answer (SNA) je zpráva protokolu Diameter používaná v Online Charging Systems (OCS). Je odeslána z OCS k síťové funkci (např. CTF) jako odpověď na Spending-Status-Notifica"
---

SNA je zpráva protokolu Diameter odeslaná z Online Charging System (OCS) k síťové funkci jako odpověď na požadavek, která přenáší rozhodnutí o řízení kreditu, jako je přidělení servisních jednotek nebo zamítnutí požadavku.

## Popis

Spending-Status-Notification-Answer (SNA) je klíčový příkaz Diameter v referenčním bodě Ro dle 3GPP, který se používá pro online řízení kreditu. Funguje jako součást Diameter Credit-Control Application ([DCCA](/mobilnisite/slovnik/dcca/)) definované v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 4006, ale s rozšířeními a AVPs (Attribute-Value Pairs) specifickými pro 3GPP. Tato zpráva je odpovědí od Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) směrem k síťovému prvku fungujícímu jako Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), například Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo aplikační server, který dříve odeslal Spending-Status-Notification-Request ([SNR](/mobilnisite/slovnik/snr/)).

Architektura zahrnuje CTF, která detekuje servisní událost vyžadující autorizaci kreditu (např. zahájení datové relace, IMS hovoru nebo aplikační služby). CTF sestaví zprávu SNR obsahující podrobnosti jako identitu účastníka, požadovanou službu a požadované servisní jednotky. Ta je odeslána k OCS přes rozhraní Ro. OCS následně tento požadavek zpracuje: dotazuje se na zůstatek účtu účastníka, aplikuje příslušné tarify a pravidla politik a učiní rozhodnutí o řízení kreditu. Zpráva SNA je nositelem tohoto rozhodnutí. Obsahuje [AVP](/mobilnisite/slovnik/avp/) Result-Code udávající úspěch nebo selhání (např. DIAMETER_SUCCESS, DIAMETER_CREDIT_LIMIT_REACHED) a v případě úspěchu zahrnuje AVP Granted-Service-Unit specifikující množství kvóty (čas, objem nebo peněžní hodnota) přidělené pro službu.

Její fungování je v zásadě stavové. OCS udržuje pro účastníka relaci řízení kreditu. Zpráva SNA může CTF instruovat, aby pokračovala ve službě, ukončila ji nebo spustila reautorizaci po spotřebování přidělených jednotek. Může také obsahovat AVPs pro přesměrování účastníka na portál pro doplnění kreditu, udání doby platnosti kvóty nebo poskytnutí informací o zbývajících zůstatcích. SNA je tedy klíčovým mechanismem pro autorizaci služeb řízenou politikami a kontrolu utrácení v reálném čase u předplacených a hybridních scénářů fakturace, což umožňuje služby jako datové balíčky, kontroly výdajových limitů a notifikace v reálném čase.

## K čemu slouží

Zpráva SNA byla vytvořena, aby splnila požadavky sofistikovaných Online Charging Systems (OCS) v sítích 3GPP. Tradiční offline účtování (postpaid) nemohlo podporovat předplacené služby nebo kontroly utrácení v reálném čase. SNA jako součást protokolu rozhraní Ro řeší problém autorizace a správy kvót v reálném čase. Umožňuje síťovým operátorům nabízet předplacené služby pro hlas, SMS a data s okamžitou kontrolou, čímž předchází úniku výnosů a umožňuje pokročilé funkce jako politiky spravedlivého používání a diferenciaci služeb.

Historicky, před standardizací rozhraní pro online účtování, dodavatelé implementovali proprietární protokoly, což vedlo k problémům s interoperabilitou a brzdilo inovace. Standardizace rozhraní Ro a příkazu SNA v 3GPP Release 5 poskytla jednotný způsob, jak jakákoli síťová funkce (GGSN, P-CSCF, AS) může vyžádat a přijímat rozhodnutí o kreditu od jakéhokoli kompatibilního OCS. Tím byly odstraněny limity fragmentovaných řešení závislých na dodavateli. Podnítilo to vznik živého ekosystému účtovacích systémů a síťových prvků, což umožnilo komplexní balíčky služeb, kontroly zůstatku v reálném čase a bezproblémovou integraci s IMS a později s architekturami založenými na službách 5G. SNA je klíčovým prvkem umožňujícím komerční modely, které definují moderní mobilní služby.

## Klíčové vlastnosti

- Příkaz Diameter (kód 8388636) používaný na referenčním bodě Ro
- Přenáší rozhodnutí OCS o autorizaci kreditu (přidělit/zamítnout/přesměrovat)
- Obsahuje AVP Granted-Service-Unit pro přidělení kvóty (čas, objem)
- Podporuje výsledkové kódy pro úspěch, dosažení kreditního limitu a další selhání
- Umožňuje řízení utrácení v reálném čase na bázi relací pro předplacené služby
- Integrální součást architektury 3GPP Online Charging System (OCS)

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [SNR – Spending Status Notification Request](/mobilnisite/slovnik/snr/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification

---

📖 **Anglický originál a plná specifikace:** [SNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sna/)
