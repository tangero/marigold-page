---
slug: "ml-mc-ppp"
url: "/mobilnisite/slovnik/ml-mc-ppp/"
type: "slovnik"
title: "ML/MC-PPP – Multi-Link/Multi-Class Point-to-Point Protocol"
date: 2025-01-01
abbr: "ML/MC-PPP"
fullName: "Multi-Link/Multi-Class Point-to-Point Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ml-mc-ppp/"
summary: "Protokol umožňující sdružování více fyzických připojení a podporu rozlišování tříd provozu přes jeden logický PPP spoj. Poskytuje škálovatelnou šířku pásma a QoS pro přenosové sítě v systémech 3GPP, p"
---

ML/MC-PPP je protokol, který spojuje více fyzických připojení do jednoho logického PPP spoje za účelem poskytnutí škálovatelné šířky pásma a QoS (Quality of Service) s podporou prioritizace provozu pro přenosové sítě, jako je např. backhaul UTRAN.

## Popis

[ML](/mobilnisite/slovnik/ml/)/MC-PPP (Multi-Link/Multi-Class Point-to-Point Protocol) je základní přenosový protokol ve standardech 3GPP, který rozšiřuje standardní [PPP](/mobilnisite/slovnik/ppp/) o dvě klíčové funkce: agregaci spojů a rozlišování tříd provozu. Byl specifikován pro optimalizaci využití přenosových zdrojů na rozhraních jako Iub a Iur. Protokol funguje tak, že vytváří PPP relaci, která může zahrnovat více nezávislých fyzických spojů, například několik linek E1. Tyto spoje jsou sdružovány pomocí procedury Multi-Link PPP (ML-PPP) definované v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 1990, která řídí distribuci datových paketů přes dostupné spoje. To zahrnuje proces fragmentace, kdy jsou větší pakety rozděleny na menší fragmenty, z nichž každý je označen pořadovým číslem a hlavičkou multilink, což umožňuje správné znovusestavení na přijímací straně bez ohledu na pořadí nebo spoj použitý pro přenos.

Aspekt Multi-Class ([MC](/mobilnisite/slovnik/mc/)) je rozšíření specifické pro 3GPP, které zavádí v rámci PPP podsložku pro zpracování různých požadavků na QoS. Definuje několik tříd provozu (např. pro řídicí signalizaci, konverzační hlas, streamované video, interaktivní a na pozadí probíhající data). Každá třída je identifikována identifikátorem třídy ([CID](/mobilnisite/slovnik/cid/)) obsaženým ve speciální hlavičce MC-PDU, která je předřazena datům před zpracováním multilink. Tato hlavička umožňuje přijímací straně upřednostňovat zpracování a přeposílání paketů na základě jejich třídy. Z architektonického hlediska se ML/MC-PPP nachází na vrstvě spojů dat (Layer 2) přenosového zásobníku. Na rozhraní Iub běží mezi Node B a [RNC](/mobilnisite/slovnik/rnc/), typicky přes fyzické vrstvy [TDM](/mobilnisite/slovnik/tdm/). Protokol komunikuje s fyzickou vrstvou pod ním a s adaptačními vrstvami ATM nebo IP (používajícími AAL2 nebo UDP/IP) nad ním, které následně přenášejí skutečné pakety rámcového protokolu (FP) UTRAN.

Jeho fungování zahrnuje koordinovaný proces navázání a běhu. Během inicializace si oba koncové body vyjednají možnosti multilink a multiclass pomocí PPP Link Control Protocol (LCP) a vyhrazeného Multiclass Network Control Protocol (MC-NCP). Jakmile je svazek aktivní, příchozí data z vyšších vrstev jsou nejprve klasifikována. Vrstva MC přidá příslušnou hlavičku MC-PDU. Vrstva ML poté toto MC-PDU zpracuje, případně jej fragmentuje, přidá multilink hlavičku s pořadovým číslem a identifikací svazku a výsledné fragmenty distribuuje přes členské spoje pomocí plánovacího algoritmu (často round-robin nebo na základě kapacity spoje). Na přijímací straně jsou fragmenty shromážděny, seřazeny a znovu sestaveny do původního MC-PDU. Hlavička MC je poté analyzována, aby byl datový blok zařazen do správné prioritní fronty pro doručení vyšším vrstvám. Tento mechanismus zajišťuje efektivní využití všech sdružených spojů a zároveň garantuje, že vysoce prioritní řídicí provoz zaznamená minimální zpoždění, což je zásadní pro handovery a řízení hovorů.

## K čemu slouží

ML/MC-PPP byl vyvinut pro splnění rostoucích přenosových požadavků sítí 3G UMTS v době jejich standardizace. Koncem 90. let a počátkem roku 2000 přechod z 2G na 3G sliboval výrazně vyšší přenosové rychlosti a nové multimediální služby. To kladlo zvýšené nároky na stávající backhaulovou infrastrukturu, která z velké části závisela na jednotlivých TDM linkách. Účel ML/MC-PPP byl dvojí: za prvé poskytnout nákladově efektivní a škálovatelnou metodu pro zvýšení kapacity backhaulu bez nutnosti kompletní přestavby infrastruktury, a za druhé zavést standardizovaný rámec QoS na vrstvě spojů dat pro typy provozu specifické pro UMTS.

Před ML/MC-PPP znamenalo zvýšení šířky pásma instalaci rozhraní s vyšší rychlostí (např. přechod z E1 na STM-1), což byla nákladná a narušující aktualizace. ML/MC-PPP umožňoval plynulejší, přírůstkové zvyšování kapacity přidáním dalších linek E1 do logického svazku. Dále, zatímco ATM mělo vlastní schopnosti QoS, jeho nasazení bylo složité a drahé. ML/MC-PPP přineslo jednodušší mechanismus QoS založený na PPP pro přenos založený na TDM, který byl běžnější. Řešilo omezení standardního PPP, které bylo 'jednotřídním' protokolem typu best-effort nevhodným pro mix signalizace kritické na zpoždění a přerušovaného datového provozu v UMTS. Integrací podpory více tříd přímo do vrstvy spojů zajistil, že politiky QoS mohou být vynucovány již od prvního přeskoku v přenosové síti, čímž se zlepšil výkon koncových služeb v reálném čase.

## Klíčové vlastnosti

- Sdružuje více nezávislých fyzických spojů (ML) do jednoho vysokokapacitního logického připojení.
- Zavádí rozlišování tříd provozu (MC) s identifikátory tříd pro správu QoS.
- Využívá procedury PPP Multilink (podle RFC 1990) pro fragmentaci a znovusestavení.
- Používá vyhrazený Multiclass Network Control Protocol (MC-NCP) pro vyjednávání schopností.
- Funguje přes fyzické vrstvy TDM (E1, T1) běžně používané v raných nasazeních 3G.
- Poskytuje standardizované přenosové řešení pro rámcový protokol UTRAN přes rozhraní Iub/Iur.

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)
- [TDM – Time Division Multiplexing](/mobilnisite/slovnik/tdm/)

## Definující specifikace

- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface

---

📖 **Anglický originál a plná specifikace:** [ML/MC-PPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ml-mc-ppp/)
