---
slug: "pid"
url: "/mobilnisite/slovnik/pid/"
type: "slovnik"
title: "PID – Packet Identification"
date: 2025-01-01
abbr: "PID"
fullName: "Packet Identification"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pid/"
summary: "Pole v protokolové datové jednotce, které jednoznačně identifikuje konkrétní paket nebo datový tok. Používá se pro multiplexování, demultiplexování, směrování a aplikaci specifických zpracovatelských"
---

PID (identifikátor paketu) je pole v protokolové datové jednotce, které jednoznačně identifikuje konkrétní paket nebo datový tok pro multiplexování, demultiplexování, směrování a aplikaci specifických zpracovatelských pravidel.

## Popis

Identifikátor paketu (PID) označuje číselný identifikátor přiřazený paketu nebo proudu paketů, aby se odlišil od ostatních za účelem zpracování, směrování nebo správy. V systémech 3GPP není PID jediný univerzální identifikátor, ale koncept implementovaný v rámci specifických protokolových vrstev a kontextů. Primární aplikace je ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) pro Robust Header Compression ([ROHC](/mobilnisite/slovnik/rohc/)). Zde je PID klíčovou součástí kontextu ROHC, což je stav udržovaný samostatně pro každý komprimovaný tok paketů mezi kompresorem a dekompresorem.

Jak to funguje v ROHC: kompresor přiřadí každému odlišnému toku paketů (např. specifickému IP toku s jedinečnými zdrojovými/cílovými adresami a porty) Context Identifier ([CID](/mobilnisite/slovnik/cid/)), který funguje jako PID. Tento CID je zahrnut v komprimované hlavičce paketu. Když dekompresor paket přijme, použije CID k nalezení správného kontextového stavu, který obsahuje informace o statických a dynamických polích potřebných k rekonstrukci původní plné hlavičky. Tento mechanismus umožňuje současnou kompresi a dekompresi více nezávislých toků paketů přes jeden rádiový bearer bez záměny.

Mimo ROHC se koncept PID objevuje i v jiných oblastech. V kontextu [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) se identifikátory používají k rozlišení různých vysílacích relací. V raných specifikacích [GPRS](/mobilnisite/slovnik/gprs/) mohl PID odkazovat na identifikátory používané v síťových vrstvách pro směrování dat mezi [SGSN](/mobilnisite/slovnik/sgsn/) a externími paketovými datovými sítěmi. Jeho role je v zásadě o umožnění multiplexování: umožňuje síti přenášet mnoho odlišných logických kanálů nebo datových toků přes sdílené fyzické a logické zdroje a zajišťuje, že každý paket je doručen správné aplikační nebo zpracovatelské entitě vyšší vrstvy.

## K čemu slouží

Potřeba identifikace paketů (Packet Identification) vznikla ze základního požadavku podporovat více simultánních datových relací a aplikací přes jediné fyzické spojení. Rané okruhově spínané hovory vyžadovaly vyhrazený kanál, ale paketově spínaná data přinesla výzvu efektivního sdílení šířky pásma mezi různými toky (např. prohlížení webu, e-mail, VoIP). Bez možnosti označit pakety by příjemce nedokázal oddělit prokládaná data patřící různým aplikacím nebo relacím, což by vedlo ke chaosu.

V konkrétním kontextu komprese hlaviček, která byla klíčová pro efektivní využití vzácných rádiových zdrojů v systémech 2,5G a 3G, PID vyřešil problém správy kontextu pro více toků. Jednoduchá schémata komprese hlaviček zvládla jeden tok, ale reálná zařízení spouštějí více aplikací. PID (jako Context ID v [ROHC](/mobilnisite/slovnik/rohc/)) umožňuje jediné kompresní/dekompresní jednotce udržovat nezávislý stav pro četné toky, což dramaticky zlepšuje spektrální účinnost bez omezení funkčnosti. Tím se odstranilo omezení dřívějších, méně škálovatelných kompresních metod.

PID tedy existuje pro umožnění efektivity a multiplexování. Je to základní nástroj pro správu složitosti vrstvených protokolových zásobníků, který umožňuje efektivní mapování sémantiky vyšších vrstev (jako IP adresy a porty) na transportní mechanismy nižších vrstev. Tím, že poskytuje úchyt pro asociaci paketu s jeho specifickým zpracovatelským kontextem, umožňuje pokročilé funkce jako komprese, rozlišení kvality služeb (QoS) a doručování multicastových služeb, které jsou všechny nezbytné pro moderní, funkcemi bohatý mobilní broadband.

## Klíčové vlastnosti

- Jednoznačně identifikuje tok paketů v rámci specifického protokolového kontextu
- Umožňuje multiplexování více toků přes jeden bearer
- Jádrová součást identifikace kontextu ROHC (Context ID)
- Používá se pro správné demultiplexování a načtení kontextu na straně příjemce
- Podporuje efektivní kompresi hlaviček pro více simultánních relací
- Může být implementován jako pole v různých protokolových vrstvách (např. PDCP, LLC)

## Související pojmy

- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [Multiplexing](/mobilnisite/slovnik/multiplexing/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification

---

📖 **Anglický originál a plná specifikace:** [PID na 3GPP Explorer](https://3gpp-explorer.com/glossary/pid/)
