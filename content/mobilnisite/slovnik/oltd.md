---
slug: "oltd"
url: "/mobilnisite/slovnik/oltd/"
type: "slovnik"
title: "OLTD – Open Loop Transmit Diversity"
date: 2025-01-01
abbr: "OLTD"
fullName: "Open Loop Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/oltd/"
summary: "Open Loop Transmit Diversity (OLTD, přenosová diverzita s otevřenou smyčkou) je technika přenosové diverzity zavedená ve 3GPP Release 11 pro UMTS/HSPA, specifikovaná v TS 25.331. Zlepšuje odolnost dow"
---

OLTD je technika přenosové diverzity v UMTS/HSPA, která zlepšuje odolnost signálu na downlinku vůči útlumu (fading) bez nutnosti zpětné vazby o kanálu od UE, čímž zvyšuje pokrytí a spolehlivost.

## Popis

Open Loop Transmit Diversity (OLTD, přenosová diverzita s otevřenou smyčkou) je schéma přenosové diverzity na downlinku používané v sítích 3G Universal Mobile Telecommunications System (UMTS) a High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)). Jako technika s otevřenou smyčkou funguje bez spoléhání se na explicitní, rychlou zpětnou vazbu o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) od uživatelského zařízení (UE). Místo toho využívá předdefinované deterministické metody k vysílání stejného signálu z více antén, čímž využívá prostorovou diverzitu pro potlačení útlumu kanálu a zlepšení spolehlivosti signálu na přijímací straně.

Architektura zahrnuje Node B (základnovou stanici) vybavenou alespoň dvěma vysílacími anténami. Běžnou implementací OLTD je Space-Time Transmit Diversity (STTD), což je forma Alamoutiho kódování. Ve STTD jsou dvojice po sobě jdoucích symbolů zakódovány napříč dvěma anténami a dvěma časovými sloty. Pro symboly s1 a s2 anténa 1 vysílá s1 a s2 v po sobě jdoucích slotech, zatímco anténa 2 vysílá -s2* a s1* (kde * značí komplexně sdružené číslo). Toto kódování vytváří ortogonální strukturu. UE s jednou nebo více přijímacími anténami používá odpovídající kombinační algoritmus (např. Maximum Ratio Combining) k dekódování původních symbolů. Zisk z diverzity je dosažen proto, že signály ze dvou vysílacích antén procházejí nezávislými útlumovými drahami; pokud je jedna dráha v hlubokém útlumu, druhá pravděpodobně není, což přijímači umožňuje rekonstruovat signál.

Klíčovými komponentami jsou kodér přenosové diverzity v Node B a kombajnér diverzity v UE. OLTD funguje transparentně vůči vyšším vrstvám. Radio Network Controller (RNC) konfiguruje použití OLTD pro rádiové spojení prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), jak je specifikováno v TS 25.331. Jeho role v síti je primárně zlepšovat výkon společných kanálů (jako Primary Common Pilot Channel ([P-CPICH](/mobilnisite/slovnik/p-cpich/))) a dedikovaných kanálů ve scénářích, kde je zpětná vazba v uzavřené smyčce nedostupná, nespolehlivá nebo příliš pomalá. Zlepšuje pokrytí na downlinku, výkon na okraji buňky a celkovou spolehlivost spojení, což je zvláště prospěšné pro hlasové hovory a uživatele s nízkorychlostními daty.

## K čemu slouží

OLTD byla vyvinuta k řešení problému degradace downlinkového signálu způsobené vícestanovým útlumem (multipath fading) v mobilním prostředí, zejména pro uživatele na okraji buňky nebo v podmínkách silného útlumu. Před rozšířeným použitím přenosové diverzity se sítě spoléhaly primárně na přijímací diverzitu (více antén na UE) nebo jednodušší vysílání z jedné antény, což bylo na straně základnové stanice méně efektivní. Schémata přenosové diverzity s uzavřenou smyčkou existovala, ale vyžadovala nepřetržitou, přesnou zpětnou vazbu vah kanálu od UE k Node B, což spotřebovávalo kapacitu uplinku a přinášelo zpoždění zpětné vazby a potenciální chyby.

Vytvoření Open Loop Transmit Diversity, standardizované ve 3GPP Release 11 pro vylepšení [HSPA](/mobilnisite/slovnik/hspa/), bylo motivováno potřebou robustní, nízkokomplexní diverzitní techniky, která nezávisela na zpětné vazbě. To ji činí ideální pro scénáře s vysokou mobilitou (kde se zpětná vazba rychle stává zastaralou) nebo pro společné kanály, které musí přijímat všechna UE bez dedikovaných smyček zpětné vazby. OLTD zlepšuje rozpočet spojení a snižuje potřebný vysílací výkon pro danou kvalitu služby, čímž prodlužuje výdrž baterie UE a zvyšuje celkovou kapacitu a pokrytí sítě. Vyřešila omezení schémat závislých na zpětné vazbě tím, že poskytovala konstantní, spolehlivý zisk z diverzity, což z ní učinilo základní technologii pro zlepšení odolnosti downlinku v 3G sítích.

## Klíčové vlastnosti

- Funguje bez rychlé zpětné vazby o stavu kanálu od UE
- Používá předdefinované prostoro-časové kódování (např. Alamouti/STTD)
- Zlepšuje odolnost signálu vůči vícestanovému útlumu
- Zvyšuje pokrytí na downlinku a výkon na okraji buňky
- Transparentní provoz vůči vyšším vrstvám UE
- Konfigurovatelné RNC prostřednictvím signalizace RRC

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [OLTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/oltd/)
