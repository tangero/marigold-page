---
slug: "ptc"
url: "/mobilnisite/slovnik/ptc/"
type: "slovnik"
title: "PTC – Push to Talk over Cellular"
date: 2025-01-01
abbr: "PTC"
fullName: "Push to Talk over Cellular"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ptc/"
summary: "Soubor standardizovaných služeb mobilních sítí umožňující okamžitou hlasovou komunikaci typu vysílačka mezi jednotlivci nebo skupinami prostřednictvím mobilní sítě. Vyvinul se z raného POC až po stand"
---

PTC je soubor standardizovaných služeb mobilních sítí umožňující okamžitou hlasovou komunikaci typu vysílačka mezi jednotlivci nebo skupinami prostřednictvím mobilní sítě.

## Popis

Push to Talk over Cellular (PTC) je v rámci standardů 3GPP zastřešující termín pro standardizované služby poskytující okamžitou poloduplexní hlasovou komunikaci – podobnou tradiční vysílačce – přes infrastrukturu mobilní sítě. Uživatelský zážitek je charakterizován tlačítkem 'push-to-talk': jeho stisknutí uživateli přidělí právo mluvit k předem definovanému jednotlivci nebo skupině, jeho uvolnění vrátí kanál do stavu naslouchání. Služby PTC jsou definovány tak, aby fungovaly přes paketově přepínané sítě (LTE, 5G), přičemž jako hlavní platforma pro poskytování služeb využívají IP Multimedia Subsystem (IMS).

Architektura služeb PTC je postavena na IMS, které zajišťuje řízení relací, autentizaci a směrování médií. Mezi klíčové funkční komponenty patří PTC klient na uživatelském zařízení (UE), aplikační server PTC ([AS](/mobilnisite/slovnik/as/)), který spravuje skupinová volání, řízení práva mluvit a stav uživatele, a podkladová síť LTE nebo 5G pro přenos. Pro komunikace s kritickými požadavky standard definuje službu Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), která přidává přísné požadavky na spolehlivost, prioritu, zabezpečení a funkce jako tísňová volání, výstrahy bezprostředního nebezpečí a sdílení polohy. MCPTT se integruje s architekturou Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), která zahrnuje další entity jako Mission Critical Service Control Function (MCSCF) a Mission Critical Service User Database (MCSUDB).

Jak to funguje, zahrnuje kombinaci signalizace [SIP](/mobilnisite/slovnik/sip/) přes IMS pro zřizování relací a Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) pro přenos médií. Když uživatel zahájí PTC volání, klient odešle SIP INVITE na aplikační server PTC/MCPTT. Server spravuje řízení práva mluvit pomocí entity floor control server, která rozhoduje o žádostech více uživatelů, kteří chtějí mluvit. Uživateli, kterému je právo mluvit přiděleno, proudí hlasové pakety na server, který je následně replikuje a distribuuje všem účastníkům ve skupině. Systém podporuje různé typy hovorů: jeden-na-jednoho, jeden-na-více skupinové hovory a hromadné hovory. Klíčové pro jeho provoz je rychlé navázání hovoru a nízká vnímaná latence, dosažené předem navázanými signalizačními cestami IMS a neustálým IP připojením (kontext Packet Data Network).

Jeho role v síti je poskytovat standardizovanou, interoperabilní alternativu k proprietárním řešením push-to-talk a tradičním systémům pozemní mobilní radiokomunikace ([LMR](/mobilnisite/slovnik/lmr/)). Pro komerční operátory nabízí přidanou službu pro podnikový a spotřebitelský segment. Pro uživatele z oblasti veřejné bezpečnosti a kritické infrastruktury (např. policie, hasiči, energetika) poskytuje MCPTT komunikační nástroj založený na širokopásmovém připojení, bohatý na funkce, který může koexistovat s nebo nahradit starší systémy LMR, a nabízí tak široké pokrytí, vysokou šířku pásma pro potenciální sdílení videa nebo dat a hlubokou integraci s mobilitou a správou v mobilních sítích.

## K čemu slouží

PTC bylo vytvořeno, aby využilo všudypřítomné mobilní sítě k poskytnutí pohodlné, širokoplošné služby okamžitého hlasu, která řeší omezení tradičních vysílaček i okruhově přepínaných mobilních hovorů. Před standardizací existovaly proprietární služby push-to-talk (jako Nextel iDEN), ale byly vázané na dodavatele, omezené funkcemi a provozované na izolovaných sítích. Cílem standardizace 3GPP bylo vytvořit interoperabilní, IP-based službu, kterou může kterýkoli operátor nasadit ve svých sítích LTE/5G, a podpořit tak konkurenci a inovace.

Vývoj směrem k [MCPTT](/mobilnisite/slovnik/mcptt/) byl konkrétně motivován požadavky veřejné bezpečnosti. Starší systémy [LMR](/mobilnisite/slovnik/lmr/) (jako TETRA, P25) nabízely vynikající skupinovou komunikaci a spolehlivost, ale byly úzkopásmové, měly omezené pokrytí a jejich údržba byla nákladná. Potřeba širokopásmového nástupce založeného na standardech se stala zřejmou, zejména po událostech, které zdůraznily selhání komunikace mezi agenturami. Standard MCPTT od 3GPP, počínaje Rel-13, si kladl za cíl poskytnout globálně harmonizované řešení s dostupností, prioritou, možností přerušení, zabezpečením (end-to-end šifrování) a podporou multimédií na úrovni pro mise s kritickými požadavky. Řešil problém izolované a stárnoucí infrastruktury pro kritickou komunikaci tím, že nabídl budoucnost schopnou cestu na komerčních mobilních sítích, a zároveň zajišťoval nezbytnou kontrolu a robustnost pro život zachraňující operace.

## Klíčové vlastnosti

- Poloduplexní, okamžitá skupinová hlasová komunikace s uživatelským rozhraním push-to-talk
- Architektura založená na IMS pro řízení relací a integraci služeb
- Pokročilé mechanismy řízení práva mluvit pro správu mluvících ve skupinových hovorech
- Schopnosti pro mise s kritickými požadavky (MCPTT): priorita, přerušení, tísňová volání, zabezpečení
- Podpora dynamické správy skupin, přítomnosti a služeb polohy
- Funguje přes paketově přepínané sítě LTE a 5G, což umožňuje širokoplošné pokrytí

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [PTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptc/)
