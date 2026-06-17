---
slug: "ifom"
url: "/mobilnisite/slovnik/ifom/"
type: "slovnik"
title: "IFOM – IP Flow Mobility"
date: 2025-01-01
abbr: "IFOM"
fullName: "IP Flow Mobility"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ifom/"
summary: "Funkce 3GPP umožňující současné použití 3GPP a ne-3GPP přístupových sítí (jako je Wi-Fi) pro různé toky IP dat z jednoho UE. Umožňuje operátorům přesměrovávat provoz specifických aplikací na nejvhodně"
---

IFOM je funkce 3GPP, která umožňuje jednomu uživatelskému zařízení současně směrovat různé toky IP dat přes 3GPP a ne-3GPP přístupové sítě, jako je Wi-Fi, na základě politiky operátora.

## Popis

IP Flow Mobility (IFOM) je pokročilé řešení správy mobility definované v architektuře Evolved Packet Core (EPC) od 3GPP, konkrétně pro scénáře zahrnující důvěryhodný ne-3GPP přístup. Jejím hlavním účelem je umožnit uživatelskému zařízení (UE) současně vytvářet a udržovat více IP toků přes různé přístupové sítě, jako jsou LTE a Wi-Fi, s možností přesouvat jednotlivé toky mezi těmito přístupy bez přerušení služby. Jedná se o podrobný mechanismus mobility na úrovni toku, což je významný vývoj oproti jednodušším metodám výběru přístupu, které zacházejí se vším provozem UE jako s jediným agregovaným přenosem.

Architektonicky IFOM spoléhá na rozšíření uzlů jádra sítě definovaných pro propojení s ne-3GPP přístupem, konkrétně evolved Packet Data Gateway (ePDG) pro nedůvěryhodný přístup a Trusted WLAN Access Gateway (TWAG) pro důvěryhodný přístup, ačkoli IFOM je primárně specifikováno pro důvěryhodný ne-3GPP přístup. Ústředním řídicím bodem je funkce Policy and Charging Rules Function (PCRF), která poskytuje síťové politiky určující, jak jsou IP toky mapovány na konkrétní přístupy. Tyto politiky, známé jako politiky Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo pravidla poskytovaná PCRF, jsou komunikovány do UE. UE, vybavené dvěma rádiovými rozhraními, je zodpovědné za implementaci rozhodnutí o vazbě toků, správu více IP adres (jedna na přístup) a provádění potřebného směrování paketů pro každý tok na správné rozhraní.

Technické fungování zahrnuje vytváření více připojení nebo přenosů Packet Data Network (PDN), jednoho na typ přístupu, ke stejné PDN (např. internetu). Každý tok je identifikován sadou parametrů IP 5-tice (zdrojová/cílová IP adresa, zdrojový/cílový port, protokol). UE a síť udržují vazbu každého aktivního toku na konkrétní přístup. Když politika nařídí předání toku – například přesunutí videoproudu z buněčné sítě na Wi-Fi z důvodu přetížení nebo cenových politik – UE aktualizuje vazbu toku. Tato aktualizace je signalizována do jádra sítě, čímž je zajištěno, že brána Packet Data Network Gateway (PGW) správně směruje sestupné pakety pro daný tok na odpovídající přístupovou bránu. Tento proces je pro aplikaci nepozorovatelný a zachovává kontinuitu IP relace pro každý jednotlivý tok.

## K čemu slouží

IFOM bylo vytvořeno, aby řešilo rostoucí heterogenitu přístupových sítí a potřebu inteligentního řízení provozu nad rámec jednoduchého výběru sítě. Před IFOM řešení jako Mobile IP nabízela síťovou mobilitu, ale zacházela se vším provozem UE jako s jedinou entitou, vynucující úplné předání mezi přístupy. Podobně rané mechanismy vykládání na Wi-Fi často spoléhaly na přerušení IP relace nebo byly omezeny na specifické aplikace. Rozšíření chytrých telefonů s více rádiovými rozhraními a snaha operátorů využít Wi-Fi nejen pro vykládání, ale jako spravovanou, integrovanou přístupovou technologii, vytvořila poptávku po podrobnější kontrole.

Základní problém, který IFOM řeší, je efektivní využití více dostupných rádiových cest pro optimalizaci kapacity, uživatelského zážitku a nákladů. Umožňuje operátorovi implementovat sofistikované politiky: například udržovat citlivý provoz na latenci, jako je hlas nebo hraní her, ve spravované síti LTE pro zaručenou kvalitu, zatímco vykládá náročné stahování tolerantní k zpoždění (jako aktualizace softwaru nebo streamování videa) na Wi-Fi. Tato podrobnost brání tomu, aby problém 'špatného Wi-Fi' degradoval všechny služby, a umožňuje řízení provozu na základě stavu sítě v reálném čase, tarifních plánů a požadavků aplikací. Jeho vytvoření bylo motivováno vizí služeb Always Best Connected ([ABC](/mobilnisite/slovnik/abc/)), které uživatelům poskytují nejlepší možný konektivní zážitek dynamickým výběrem optimální cesty pro každý služební tok.

## Klíčové vlastnosti

- Podrobná mobilita na úrovni IP toku mezi 3GPP a důvěryhodným ne-3GPP přístupem
- Současné vícepřístupové připojení PDN (MAPCON) ke stejnému APN
- Řízení politiky založené na síti přes PCRF a vynucování politiky na straně UE
- Plynulé předání jednotlivých toků bez přerušení IP relace
- Podpora procedur mobility toků iniciovaných UE i sítí
- Využívá rozhraní Dual-Stack Mobile IPv6 (DSMIPv6) nebo PMIP-based S2a/S2b pro signalizaci v jádru sítě

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 37.834** (Rel-12) — WLAN/3GPP Radio Interworking Study

---

📖 **Anglický originál a plná specifikace:** [IFOM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifom/)
