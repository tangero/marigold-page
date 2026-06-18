---
slug: "cph"
url: "/mobilnisite/slovnik/cph/"
type: "slovnik"
title: "CPH – Call Party Handling"
date: 2025-01-01
abbr: "CPH"
fullName: "Call Party Handling"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cph/"
summary: "CPH je soubor procedur a schopností v rámci architektury služeb CAMEL (Customized Applications for Mobile network Enhanced Logic) pro správu účastníků mobilního hovoru. Umožňuje operátorům sítí poskyt"
---

CPH je soubor procedur a schopností CAMEL pro správu účastníků hovoru, který umožňuje pokročilé služby řízení hovoru, jako je čekání na hovor, hold nebo konferenční hovor, prostřednictvím dynamické manipulace s větvemi (call legs) hovoru.

## Popis

Call Party Handling (CPH) je klíčová funkční komponenta architektury Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile network Enhanced Logic), standardizované organizací 3GPP. Definuje mechanismy, pomocí kterých může Řídicí funkce služeb (Service Control Function – [SCF](/mobilnisite/slovnik/scf/)), typicky umístěná v Řídicím bodu služeb (Service Control Point – [SCP](/mobilnisite/slovnik/scp/)), instruovat Komutační funkci služeb (Service Switching Function – [SSF](/mobilnisite/slovnik/ssf/)) v rámci Mobilní ústředny (Mobile Switching Center – [MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC, aby manipulovala s jednotlivými spojeními (neboli 'větvemi' – 'legs'), které tvoří hovor. Větev hovoru představuje spojení mezi sítí a jedním účastníkem. CPH poskytuje základní operace pro vytváření, připojování, rozdělování a uvolňování těchto větví, což umožňuje vytváření složitých stavů hovoru.

Architektonicky CPH funguje prostřednictvím protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)), který přenáší dialog mezi SCF a SSF. SSF, integrovaná v MSC, funguje jako spouštěcí bod a správce komutačních zdrojů. Když dojde k události hovoru odpovídající předplacené CAMEL spoušti (např. sestavení hovoru), SSF pozastaví zpracování hovoru a nahlásí to SCF. SCF, která hostuje servisní logiku, pak může vydat CPH operace jako 'Connect', 'SplitLeg' nebo 'MoveLeg' směrem k SSF prostřednictvím zpráv CAP. SSF tyto příkazy vykoná řízením komutační matice a přenosových spojení a poté výsledek ohlásí zpět SCF. Toto oddělení servisní logiky (SCF) a komutace (SSF/MSC) je základním principem Inteligentní sítě.

Klíčové součásti CPH zahrnují události CPH detekčních bodů (Detection Point – [DP](/mobilnisite/slovnik/dp/)) a související operace. Detekční body jako O_Answer a T_Answer umožňují SCF být informována o tom, kdy je větev hovoru přijata. Mezi hlavní operace patří: Connect (pro zřízení nové větve hovoru k účastníkovi), Disconnect (pro uvolnění konkrétní větve), SplitLeg (pro oddělení jedné větve od vícesměrného spojení a její převedení do stavu hold) a MoveLeg (pro přenos větve z jednoho segmentu hovoru do jiného, což je zásadní pro přesměrování hovoru). SCF udržuje model asociace segmentů hovoru (Call Segment Association – CSA), což je logický pohled na to, jak jsou větve hovoru seskupeny do segmentů hovoru (např. větev v hold v jednom segmentu, aktivní dvousměrný hovor v jiném).

Úlohou CPH je poskytnout detailní řízení nezbytné pro pokročilé telefonní služby. Například pro implementaci služby Čekání na hovor použije SCF CPH k převedení existující aktivní větve do hold (pomocí SplitLeg) a k připojení nové příchozí větve. Pro třísměrnou konferenci by SCF připojila třetí větev a sloučila ji s existujícím segmentem hovoru. Tato úroveň řízení, standardizovaná napříč dodavateli, umožňuje vytváření přenositelných, na síti centrických služeb, které jsou nezávislé na schopnostech účastnického terminálu, a zajišťuje tak konzistentní uživatelský zážitek.

## K čemu slouží

CPH bylo vytvořeno, aby odstranilo omezení tradičního, na ústředně založeného řízení hovoru, které bylo rigidní a zavedení nových telefonních služeb činilo pomalým, závislým na dodavateli a nákladným procesem. Před koncepty Inteligentní sítě, jako je CAMEL, byly pokročilé funkce (např. přesměrování hovoru, vícesměrný hovor) pevně zabudovány do jednotlivých ústředen MSC. Zavedení nové služby vyžadovalo softwarové aktualizace všech ústředen od jednoho dodavatele, což brzdilo inovace a vedlo k dlouhé době uvedení na trh. Architektura CAMEL, s CPH jako klíčovým enablerem, byla vyvinuta k oddělení servisní logiky od komutační infrastruktury.

Hlavní problém, který CPH řeší, je poskytnutí standardizovaného, abstrahovaného rozhraní pro externí servisní logiku, aby mohla dynamicky manipulovat s účastníky hovoru. To umožňuje síťovým operátorům a poskytovatelům služeb třetích stran rychle vytvářet a nasazovat funkčně bohaté komunikační služby z centralizované platformy (SCP). Umožňuje sofistikované scénáře hovoru zahrnující více než dva účastníky nebo dynamické změny topologie hovoru, které jsou základní pro obchodní a prémiové služby pro spotřebitele. CPH poskytlo potřebnou sadu nástrojů v rámci protokolu CAMEL, aby byly tyto služby možné standardizovaným způsobem napříč různými dodavateli síťového vybavení.

Historicky bylo CPH zavedeno ve fázi CAMEL Phase 2 (3GPP Release 5) jako rozšíření základního řízení hovoru z CAMEL Phase 1. Phase 1 umožňovala hlavně řízení směrování hovoru (např. předplacené hovory, bezplatná linka). Phase 2 a CPH byly motivovány potřebou podpory širšího portfolia přidaných služeb, jako je explicitní přesměrování hovoru, čekání na hovor a konferenční hovor typu meet-me, které vyžadují aktivní správu větví hovoru během probíhajícího hovoru. Tento vývoj byl klíčový pro GSM sítě, aby mohly konkurovat pevným službám ISDN, a později pro vytvoření základu pro řízení služeb v IP Multimedia Subsystem (IMS), kde se aplikují podobné principy řízení session a účastníků.

## Klíčové vlastnosti

- Umožňuje dynamické vytváření, připojování a uvolňování jednotlivých větví (call legs) v rámci hovorové session.
- Poskytuje standardizované CAMEL operace (Connect, Disconnect, SplitLeg, MoveLeg) pro manipulaci s účastníky hovoru.
- Podporuje model asociace segmentů hovoru (Call Segment Association – CSA) pro logické seskupování větví hovoru.
- Umožňuje interakce služeb během hovoru spouštěné detekčními body (Detection Points – DPs), jako jsou O_Answer a T_Answer.
- Umožňuje implementaci pokročilých telefonních služeb, jako je čekání na hovor, hold, přesměrování a vícesměrný konferenční hovor.
- Umožňuje síťově-centrické vykonávání servisní logiky nezávislé na schopnostech uživatelského zařízení.

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging

---

📖 **Anglický originál a plná specifikace:** [CPH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cph/)
