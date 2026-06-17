---
slug: "lapm"
url: "/mobilnisite/slovnik/lapm/"
type: "slovnik"
title: "LAPM – Link Access Procedure for Modems"
date: 2025-01-01
abbr: "LAPM"
fullName: "Link Access Procedure for Modems"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lapm/"
summary: "LAPM je protokol linkové vrstvy používaný pro opravu chyb a kompresi dat v modemové komunikaci, standardizovaný doporučením ITU-T V.42. V 3GPP je odkazován pro okruhově přepínané datové služby, zajišť"
---

LAPM (Link Access Procedure for Modems, procedura přístupu k lince pro modemy) je standardizovaný protokol linkové vrstvy používaný v okruhově přepínaných službách 3GPP pro opravu chyb a kompresi přes analogová modemová spojení.

## Popis

Link Access Procedure for Modems (LAPM) je protokol linkové vrstvy s opravou chyb definovaný ve standardu [ITU-T](/mobilnisite/slovnik/itu-t/) V.42 a odkazovaný ve specifikacích 3GPP pro okruhově přepínané datové služby. Je speciálně navržen pro použití přes analogová modemová spojení, aby poskytoval spolehlivý přenos dat detekcí a opravou chyb vznikajících v důsledku šumu na lince a dalších rušivých vlivů. LAPM je založen na principech [HDLC](/mobilnisite/slovnik/hdlc/) a funguje tak, že mezi dvěma modemy naváže logické spojení, segmentuje data do rámců a používá automatické opakování dotazu ([ARQ](/mobilnisite/slovnik/arq/)) pro retransmisi chybně přijatých rámců, čímž vyšším vrstvám prezentuje datový proud bez chyb.

Protokol funguje tak, že během fáze handshaku modemů vyjedná spojení. Po jeho navázání jsou data z koncového zařízení (např. počítače nebo faxu) formátována do LAPM rámců. Každý rámec obsahuje hlavičku s adresní a řídicí informací, informační pole proměnné délky a kontrolní sekvenci rámce ([FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb. Řídicí pole spravuje sekvenční čísla pro provoz s potvrzováním (modulo 8 nebo 128). Když je rámec přijat se správnou FCS, přijímací modem odešle potvrzení; pokud je detekována chyba nebo je rámec ztracen, negativní potvrzení spustí retransmisi. LAPM často pracuje ve spojení s kompresními protokoly, jako je V.42bis, aby se zvýšila efektivní propustnost.

V kontextu 3GPP je LAPM relevantní pro okruhově přepínaná data ([CSD](/mobilnisite/slovnik/csd/)) a faxové služby v GSM a UMTS. Když se mobilní stanice účastní datového hovoru (např. vytáčeného internetu nebo faxu skupiny 3), modemová funkce v síti (např. ve funkci pro propojování sítě - [IWF](/mobilnisite/slovnik/iwf/)) může používat LAPM k zajištění integrity dat přes rozhraní rádiového přístupu a segment PSTN. Úlohou protokolu je maskovat nedokonalosti analogové přenosové cesty a poskytovat čistý, spolehlivý bitový kanál pro koncové uživatelské aplikace. Ačkoli je LAPM s nástupem paketově přepínaných mobilních dat z velké části zastaralý, byl klíčový pro umožnění raných mobilních datových a faxových služeb s přijatelnou kvalitou a spolehlivostí.

## K čemu slouží

LAPM byl vyvinut, aby řešil inherentní nespolehlivost analogových modemových spojení přes telefonní sítě, která jsou náchylná k šumu, zkreslení a útlumu signálu. Před protokoly s opravou chyb, jako je LAPM, byly modemové přenosy dat náchylné ke korupci, což vyžadovalo, aby retransmise řešily protokoly vyšších vrstev nebo aplikace, což vedlo ke špatnému výkonu a uživatelskému zážitku. LAPM poskytl standardizované řešení na linkové vrstvě, které dokázalo chyby transparentně detekovat a opravovat, čímž významně zlepšil spolehlivost vytáčených dat, faxu a dalších okruhově přepínaných služeb.

V rámci 3GPP bylo zařazení LAPM motivováno potřebou podporovat propojení s tradičními datovými službami PSTN/[ISDN](/mobilnisite/slovnik/isdn/), jako je fax a modemový přístup k internetu, přes mobilní sítě. Raná mobilní data ([CSD](/mobilnisite/slovnik/csd/)) v podstatě emulovala modemové spojení přes rádiový spoj; proto bylo použití robustního protokolu pro opravu chyb, jako je LAPM, nezbytné pro kompenzaci jak chyb na rádiovém kanálu, tak potenciálního šumu v propojené pevné síti. Řešil problém dosažení přijatelné míry bitových chyb pro služby dat citlivých na zpoždění v reálném čase, jako je fax, kde by retransmise na vyšších vrstvách byla nepraktická.

Historicky LAPM (V.42) konkuroval jiným protokolům pro opravu chyb, jako je MNP (Microcom Networking Protocol). Jeho přijetí jako standardu ITU z něj učinilo univerzální volbu, která zajišťovala interoperabilitu mezi modemy od různých výrobců. Pro 3GPP umožnilo odkazování na tento dobře zavedený protokol mobilním sítím bezproblémově se připojovat k rozsáhlé instalované základně pevných modemů a faxových zařízení, což usnadnilo rané přijetí mobilních datových a faxových služeb bez nutnosti změn stávajícího koncového uživatelského zařízení nebo síťových funkcí pro propojování.

## Klíčové vlastnosti

- Detekce a oprava chyb pomocí ARQ (Automatic Repeat Request, automatické opakování dotazu)
- Rámcová struktura založená na HDLC s kontrolní sekvencí rámce (FCS) pro zajištění integrity
- Podpora sekvenčního číslování modulo 8 a 128 pro řízení toku
- Vyjednávání během handshaku modemů za účelem kompatibility a výběru parametrů
- Často spárován s kompresí dat V.42bis pro zvýšení efektivní propustnosti
- Transparentní provoz poskytující vyšším vrstvám spolehlivý bitový proud

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [LAPM na 3GPP Explorer](https://3gpp-explorer.com/glossary/lapm/)
