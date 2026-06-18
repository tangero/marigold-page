---
slug: "mcu"
url: "/mobilnisite/slovnik/mcu/"
type: "slovnik"
title: "MCU – Multipoint Communication Unit"
date: 2025-01-01
abbr: "MCU"
fullName: "Multipoint Communication Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcu/"
summary: "Síťová entita, která spravuje vícebodové komunikační relace, jako jsou konferenční hovory, prostřednictvím mixování a distribuce mediálních toků. Zavedena v Rel-4, umožňuje skupinovou komunikaci v IMS"
---

MCU je síťová entita zavedená ve 3GPP Release-4, která spravuje vícebodové relace, jako jsou konferenční hovory, prostřednictvím mixování a distribuce mediálních toků pro skupinovou komunikaci v IMS a službách pro kritickou komunikaci.

## Popis

Multipoint Communication Unit (MCU) je funkční entita v rámci architektury 3GPP, která usnadňuje vícebodové komunikační relace, kde více účastníků vyměňuje média v reálném čase. Funguje tak, že přijímá mediální toky (např. audio, video) od každého účastníka, zpracovává je – často prostřednictvím mixování, transkódování nebo přepínání – a poté distribuuje kombinované nebo vybrané toky zpět účastníkům. Architektura MCU může být centralizovaná, kdy je umístěna v síti (např. v aplikačním serveru IMS), nebo distribuovaná, s funkcemi rozdělenými mezi uživatelské zařízení a síťové uzly. Mezi klíčové komponenty patří jednotka pro zpracování médií, která zvládá konverzi kodeků a manipulaci s toky, řídicí jednotka, která spravuje signalizaci relací prostřednictvím protokolů jako [SIP](/mobilnisite/slovnik/sip/), a správce zdrojů, který přiděluje šířku pásma a výpočetní výkon. Její role v síti je klíčová pro služby, jako jsou hlasové a videokonference, push-to-talk ([PTT](/mobilnisite/slovnik/ptt/)) a skupinová komunikace pro kritickou komunikaci, protože zajišťuje, že všichni účastníci přijímají synchronizovaná média bez nutnosti peer-to-peer spojení mezi každou dvojicí, které by se špatně škálovalo. MCU se integruje s prvky jádra sítě, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS a framework Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), což umožňuje směrování s ohledem na službu a vynucení kvality služby (QoS). V průběhu releasů se vyvinula tak, aby podporovala pokročilé funkce, jako je adaptivní streamování s proměnným datovým tokem a vylepšení zabezpečení, což z ní činí všestrannou komponentu pro spotřebitelské i profesionální komunikační služby.

## K čemu slouží

MCU byla zavedena v Rel-4, aby řešila potřebu efektivní skupinové komunikace v IP sítích, zejména když se 3GPP posunulo směrem k plně IP systémům se zavedením IMS. Před její standardizací se vícebodové relace často spoléhaly na ad-hoc řešení nebo proprietární konferenční mosty, což vedlo k problémům s interoperabilitou, vysoké latenci a neefektivnímu využití síťových zdrojů. Vytvoření MCU poskytlo standardizovaný způsob správy mixování a distribuce médií, řešící problémy související se škálovatelností ve velkých konferencích a umožňující bezproblémovou integraci se službami 3GPP, jako je voice over LTE (VoLTE) a mission-critical push-to-talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Její vývoj byl motivován rostoucí poptávkou po kolaborativní komunikaci v komerčním i veřejně-bezpečnostním kontextu, kde je spolehlivá skupinová interakce zásadní. Postupem času, jak se služby rozšířily o video a sdílení dat, se MCU vyvinula tak, aby zvládala složitější typy médií, řešíc omezení dřívějších releasů, které se primárně zaměřovaly na audio. Centralizací zpracování médií snižuje zatížení šířky pásma a výpočetního výkonu na koncových uživatelských zařízeních, čímž zvyšuje celkovou efektivitu sítě a uživatelský zážitek ve scénářích od obchodních jednání až po koordinaci záchranných akcí.

## Klíčové vlastnosti

- Mixování a distribuce médií pro vícebodové relace
- Podpora zpracování audio, video a datových toků
- Integrace s architekturami IMS a služeb pro kritickou komunikaci
- Škálovatelnost pro zvládnutí velkého počtu účastníků
- Transkódování a adaptace pro heterogenní zařízení
- Bezpečnostní funkce, jako je šifrování a autentizace pro citlivou komunikaci

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [MCU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcu/)
