---
slug: "btr"
url: "/mobilnisite/slovnik/btr/"
type: "slovnik"
title: "BTR – Background Data Transfer Request"
date: 2025-01-01
abbr: "BTR"
fullName: "Background Data Transfer Request"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/btr/"
summary: "BTR je mechanismus 3GPP umožňující přenosy dat na pozadí pro aplikace v reálném čase nezávislé, jako jsou aktualizace softwaru a synchronizace obsahu. Umožňuje síti naplánovat doručení dat v období ní"
---

BTR je mechanismus 3GPP, který umožňuje přenosy dat na pozadí pro aplikace v reálném čase nezávislé tím, že naplánuje jejich doručení v období nízkého vytížení sítě za účelem optimalizace zdrojů a minimalizace narušení služeb.

## Popis

Background Data Transfer Request (BTR) je standardizovaná servisní funkce 3GPP navržená pro správu neurgentního, na zpoždění tolerantního datového provozu v mobilních sítích. Funguje jako součást architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) a je konkrétně definována v 3GPP TS 29.154, která popisuje rozhraní N40 mezi Application Function ([AF](/mobilnisite/slovnik/af/)) a Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). Základní mechanismus spočívá v tom, že aplikační server (vystupující jako AF) signalizuje síťovému PCRF, že má připravena data na pozadí k doručení konkrétnímu uživatelskému zařízení (UE). Tato signalizace nese parametry jako identifikátor cílového UE, odhadovaný objem dat a případně časová okna nebo náznaky priority pro přenos.

Architektonicky BTR využívá stávající komponenty PCC. Když AF (např. server pro aktualizace softwaru) zjistí, že jsou pro UE k dispozici data na pozadí, odešle přes rozhraní N40 zprávu BTR do PCRF. PCRF, který spravuje profil předplatitele a je informován o stavu sítě, tuto žádost zpracuje. Vyhodnotí ji vůči předplaceným politikám uživatele, aktuálnímu vytížení sítě a dalším pravidlům PCC. Na základě tohoto vyhodnocení se PCRF může rozhodnout přenos na pozadí autorizovat a následně nainstalovat odpovídající pravidla Policy and Charging Control (PCC) v Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo, v 5G, v Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)).

Nainstalovaná pravidla PCC efektivně vytvoří vyhrazený bearer nebo QoS Flow označený pro provoz na pozadí. Tato pravidla instruují uzly uživatelské roviny, aby zacházely s přidruženými IP pakety s nižší prioritou QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/) nebo [5QI](/mobilnisite/slovnik/5qi/)), typicky s takovou, která je určena pro negarantovanou přenosovou rychlost a na zpoždění tolerantní data. Síť pak může naplánovat přenos těchto dat v obdobích nižšího využití rádiových zdrojů nebo nižšího vytížení sítě, například v mimoprovozních hodinách. Toto plánování je řízeno Radio Access Network (RAN) na základě QoS označení, bez nutnosti explicitní, okamžité interakce od koncového uživatele. Proces je transparentní pro aplikace na popředí v UE, které nadále fungují s přiřazenými vysoce prioritními zdroji.

Úlohou BTR je poskytnout síťově řízený rámec pro optimalizaci doručování hromadného, strojového nebo aktualizačního provozu aplikací. Posouvá paradigma od modelu, kde aplikace pokoušejí provést přenosy na pozadí příležitostně (a potenciálně soupeří s uživatelským provozem), k modelu, kde je síť informována a může činit inteligentní rozhodnutí o plánování. Tím se zlepšuje celková efektivita sítě, snižuje se riziko kongescí způsobených nekoordinovaným provozem na pozadí a může přispět k lepší výdrži baterie UE díky potenciální konsolidaci datových přenosů do méně častých, ale efektivnějších síťových aktivací.

## K čemu slouží

BTR byl zaveden, aby řešil rostoucí výzvu správy časově nekritického datového provozu v čím dál více vytížených mobilních sítích. Před jeho standardizací aplikace provádějící úlohy na pozadí – jako jsou aktualizace operačního systému, synchronizace cloudových záloh nebo přednačítání obsahu – zahajovaly datové přenosy bez vědomí sítě. Tyto přenosy mohly nastat kdykoliv a přímo konkurovat uživatelským aktivitám na popředí (např. streamování videa, prohlížení webu) o stejné rádiové a síťové zdroje jádra sítě. Toto soupeření mohlo vést k znatelnému zhoršení kvality zážitku u služeb citlivých na latenci a k neefektivnímu využití kapacity sítě během špičky.

Vytvoření BTR bylo motivováno potřebou chytřejší správy provozu a vzestupem komunikací Machine-to-Machine (M2M) a Internetu věcí (IoT), kde je mnoho datových přenosů inherentně na zpoždění tolerantních. 3GPP uznalo, že ne všechna data jsou stejná; některá mohou být odložena bez dopadu na uživatele. BTR poskytuje potřebný signalizační protokol, který umožňuje důvěryhodným poskytovatelům aplikací informovat síť o takových odložitelných datech, a tím umožnit síťově asistovanou optimalizaci. To je v souladu s širšími snahami 3GPP ve vydáních 13 a novějších o zlepšení efektivity sítě, podpoře různorodých požadavků služeb a implementaci sofistikovanější kontroly politik.

Řešením problému nekoordinovaného provozu na pozadí pomáhá BTR mobilním síťovým operátorům (MNO) vyrovnávat špičky provozu, zlepšovat spektrální efektivitu a poskytovat konzistentnější kvalitu služeb. Pro poskytovatele aplikací nabízí standardizovaný způsob, jak zajistit, že jejich aktualizace na pozadí se nakonec dokončí, aniž by byly nadměrně omezovány nebo blokovány síťovými politikami. Pro koncové uživatele je výhodou lepší celkový zážitek, protože jejich interaktivní služby čelí menší konkurenci od neviditelných úloh na pozadí a výdrž baterie jejich zařízení může být zachována díky efektivnějšímu plánování dat.

## Klíčové vlastnosti

- Standardizovaná signalizace AF-PCRF přes rozhraní N40 pro žádosti o přenos na pozadí
- Síťově řízené plánování založené na politice, předplatném a aktuálním vytížení
- Využití nižších prioritních tříd QoS (např. standardizovaný Delay-Tolerant QCI) pro datový tok
- Podpora parametrů jako odhadovaný objem přenosu a volitelná časová okna pro doručení
- Bezproblémová integrace se stávající architekturou 3GPP PCC pro vynucování politik
- Transparentní fungování vůči UE a jeho aplikacím na popředí

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 29.154** (Rel-19) — Nt Reference Point Protocol

---

📖 **Anglický originál a plná specifikace:** [BTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/btr/)
