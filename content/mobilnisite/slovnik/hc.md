---
slug: "hc"
url: "/mobilnisite/slovnik/hc/"
type: "slovnik"
title: "HC – Header Compression"
date: 2025-01-01
abbr: "HC"
fullName: "Header Compression"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hc/"
summary: "Technika, která před přenosem po rádiovém spoji zmenšuje velikost hlaviček paketů (např. IP, UDP, RTP) za účelem úspory cenné šířky pásma a snížení latence. Je nezbytná pro efektivní přenos hlasu (VoI"
---

HC (komprese hlaviček) je technika, která před přenosem po rádiovém spoji zmenšuje velikost hlaviček paketů za účelem úspory šířky pásma a snížení latence. Je klíčová pro efektivní přenos hlasu a dalšího provozu v reálném čase.

## Popis

Komprese hlaviček (Header Compression, HC) je vrstva protokolu zvyšující výkon, která funguje mezi vrstvou PDCP (Packet Data Convergence Protocol) a protokoly jádra sítě v 3GPP rádiových přístupových sítích (UTRAN, [E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN). Jejím hlavním úkolem je potlačit redundanci v po sobě jdoucích hlavičkách paketů patřících do stejného toku před jejich odesláním přes rozhraní vzduchu. Typický hlasový paket VoIP může mít například 40bajtovou hlavičku IPv4/UDP/RTP pro pouhých 15–30 bajtů hlasové užitečné zátěže, což představuje obrovskou režii. Algoritmy HC identifikují ve hlavičkách statická pole (jako zdrojové/cílové IP adresy) a předvídatelná pole (jako pořadová čísla). Pro první paket v toku se odešle plná hlavička a kompresor s dekompresorem vytvoří sdílený kontext – uloženou kopii této hlavičky. Pro následující pakety se přenášejí pouze měnící se pole (deltas) a identifikátor kontextu, čímž se hlavička dramaticky zmenší na několik bajtů.

Specifikace 3GPP přijímají a profilují robustní algoritmy komprese hlaviček standardizované [IETF](/mobilnisite/slovnik/ietf/), především RObust Header Compression (ROHC) definovaný v RFC 5795. V systémech 3GPP je za provádění HC zodpovědná vrstva PDCP. PDCP entita na vysílací straně (např. v UE pro uplink nebo v gNB pro downlink) funguje jako kompresor. Klasifikuje pakety do toků, vytváří a udržuje kompresní kontexty a odesílá komprimované pakety. Odpovídající PDCP entita na přijímací straně funguje jako dekompresor a pomocí kontextu rekonstruuje původní plné hlavičky před předáním paketů do vyšších vrstev. Rámec ROHC je díky své stavové operaci a zpětnovazebním mechanismům vysoce odolný vůči ztrátě paketů a chybovým spojům, což umožňuje dekompresoru v případě ztráty synchronizace vyžádat aktualizaci kontextu.

HC se aplikuje pro každý rádiový přenosový kanál (radio bearer) a je klíčová pro efektivitu všech služeb v reálném čase. Pro Voice over LTE (VoLTE) a Voice over NR (VoNR) je povinné používat profily ROHC pro RTP/UDP/IP, aby byla služba spektrálně efektivní. Významně také prospívá dalším aplikacím s nízkou latencí a malými pakety, jako jsou hry nebo zasílání zpráv IoT. Snížením režie hlaviček HC snižuje počet potřebných rádiových zdrojových bloků na paket, což síti umožňuje obsloužit více uživatelů, zkrátit dobu přenosu paketu (snížit latenci) a zlepšit celkovou kapacitu systému a uživatelský komfort, zejména na okrajích buňky, kde jsou rádiové podmínky špatné.

## K čemu slouží

Komprese hlaviček (Header Compression) byla zavedena, aby řešila závažnou neefektivitu přenosu provozu v reálném čase s malou užitečnou zátěží po rádiových spojích s omezenou a drahou šířkou pásma. V raných sítích 3G, s nástupem paketově spínaných služeb, se ukázalo, že protokoly jako IP, UDP a RTP – navržené pro drátové sítě s hojnou šířkou pásma – nesou významnou režii hlaviček. Pro hlasové služby migrující z okruhově spínaných na paketově spínané (VoIP) mohla tato režie tvořit 60–80 % celkové velikosti paketu, což plýtvalo vzácnými rádiovými zdroji a zvyšovalo latenci kvůli delší době přenosu.

Motivací pro standardizaci HC v rámci 3GPP, počínaje Release 4, bylo umožnit efektivní VoIP a další multimediální služby v reálném čase přes UMTS. Omezení předchozích přístupů (jako jednoduchá Van Jacobsonova komprese pro TCP/IP) spočívala v jejich nedostatečné robustnosti na ztrátových bezdrátových spojích a v podpoře celé sady internetových protokolů. Přijetí rámce ROHC od [IETF](/mobilnisite/slovnik/ietf/) organizací 3GPP poskytlo robustní, standardizované řešení schopné komprimovat hlavičky pro toky IP, UDP, RTP a [ESP](/mobilnisite/slovnik/esp/) (pro [IPSec](/mobilnisite/slovnik/ipsec/)), a to i při vysoké chybovosti paketů. To bylo klíčovým prvkem umožňujícím vizi plně IP jádra sítě a následné nasazení VoLTE, díky čemuž se paketově spínaný hlas stal životaschopnou a efektivní alternativou k tradičnímu okruhově spínanému hlasu.

## Klíčové vlastnosti

- Dramaticky snižuje režii hlaviček IP/UDP/RTP z přibližně 40–60 bajtů na 1–4 bajty na paket
- Implementuje rámec IETF RObust Header Compression (ROHC) a jeho profily
- Funguje ve vrstvě PDCP v zásobnících rádiových protokolů 3GPP (LTE, NR)
- Stavová komprese založená na sdíleném kontextu mezi kompresorem a dekompresorem
- Zahrnuje robustní zpětnovazební mechanismy pro obnovu po chybě a synchronizaci kontextu
- Nezbytná pro spektrální efektivitu služeb VoLTE, VoNR a dalších služeb v reálném čase s nízkou latencí

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping

---

📖 **Anglický originál a plná specifikace:** [HC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hc/)
