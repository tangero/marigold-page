---
slug: "ari"
url: "/mobilnisite/slovnik/ari/"
type: "slovnik"
title: "ARI – Access Request Identifier"
date: 2025-01-01
abbr: "ARI"
fullName: "Access Request Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ari/"
summary: "Access Request Identifier (ARI) je jedinečný identifikátor přiřazený mobilní stanici během procedury paketového přístupu v sítích GPRS/EDGE. Odlišuje žádost stanice o přístup od ostatních, které soutě"
---

ARI je jedinečný identifikátor přiřazený mobilní stanici v sítích GPRS/EDGE, který odlišuje její žádost o přístup od ostatních při soutěžení o zdroje na kanálu PRACH.

## Popis

Access Request Identifier (ARI) je klíčovou součástí procedury paketového přístupu definované v 3GPP TS 44.060 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) v systémech [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Funguje v rámci vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a procedur Random Access Channel ([RACH](/mobilnisite/slovnik/rach/)). Když mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) potřebuje zahájit přenos dat v uplinku nebo odpovědět na příkaz sítě, musí nejprve požádat o zdroje. To provede odesláním zprávy Packet Channel Request na Packet Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)). Tato žádost obsahuje ARI, který slouží jako dočasná identita pro řešení kolizí pro tento konkrétní pokus o přístup.

Generování a zpracování ARI se řídí specifickým protokolem. MS vybere nebo vypočítá hodnotu ARI na základě parametrů vysílaných sítí a své vlastní Temporary Logical Link Identity ([TLLI](/mobilnisite/slovnik/tlli/)). BSS sítě po přijetí více souběžných pokusů o přístup použije ARI k jednoznačné identifikaci každé žádající MS. Po úspěšném přenosu na PRACH síť odpoví zprávou Packet Uplink Assignment na Packet Access Grant Channel (PAGCH). Tato zpráva je adresována pomocí stejné hodnoty ARI, což umožní pouze té MS, která odeslala původní žádost s tímto konkrétním ARI, aby přiřazení rozpoznala a jednala podle něj, čímž se vyřeší kolize.

Role ARI přesahuje pouhou identifikaci; je nedílnou součástí procesu vytváření Temporary Block Flow (TBF). TBF je fyzické spojení používané pro přenos LLC PDU v jednom směru mezi MS a sítí. ARI je součástí úvodního handshake, který vede k přidělení uplinkových rádiových zdrojů (timeslotů) a k vytvoření uplinkového TBF. Jeho správná interpretace ze strany MS i BSS zajišťuje, že rádiové zdroje jsou přiděleny zamýšlenému uživatelskému zařízení, čímž se udržuje pořádek a efektivita ve sdíleném rádiovém prostředí.

Z architektonického hlediska funguje ARI na rozhraní mezi MS a BSS, konkrétně v rámci Packet Control Unit (PCU). Jedná se o přechodný identifikátor, jehož platnost je omezena na bezprostřední přístupovou proceduru a buňku, kde byla žádost podána. Na rozdíl od trvalejších identifikátorů, jako je TLLI nebo IMSI, je ARI krátkodobý a je zahozen po dokončení fáze bezprostředního přidělení zdrojů nebo pokud pokus o přístup selže. Tento návrh minimalizuje signalizační režii a vyhýbá se dlouhodobé správě identit pro přechodné stavy.

## K čemu slouží

Access Request Identifier byl vytvořen k řešení základního problému řešení kolizí na sdíleném, soutěživém rádiovém přístupovém kanálu. V raných sítích GSM navržených primárně pro hlas byl procedura náhodného přístupu jednodušší. Se zavedením GPRS pro paketová data potřebovala síť efektivní metodu pro zpracování více datově schopných zařízení, která se současně pokoušejí o přístup k síti bez předchozí koordinace. ARI poskytuje mechanismus k rozlišení těchto souběžných žádostí, což zajišťuje, že přidělení zdrojů je doručeno správnému zařízení.

Před standardizovanými procedurami paketového přístupu, nebo při jejich absenci, by bylo řešení kolizí méně efektivní, což by vedlo k většímu zpoždění přístupu, zvýšenému počtu retransmisí a snížení celkové kapacity systému pro datové služby. ARI jako součást strukturovaného protokolu přístupu a přidělování umožňuje BSS spravovat žádosti o uplinkové zdroje od potenciálně desítek MS v buňce. Řeší omezení spočívající v neexistenci vyhrazené, předem vytvořené signalizační cesty, přes kterou by datová zařízení mohla žádat o zdroje, což je klíčový rozdíl oproti nastavování spojově orientovaných hovorů.

Historicky bylo jeho specifikace v TS 44.060 spolu s protokolem MAC pro GPRS/EDGE zásadní pro umožnění efektivních, spravedlivých a spolehlivých paketových datových služeb přes GSM rádiové rozhraní. Podpírá dynamickou a na požádání fungující povahu přidělování paketových zdrojů, což je základní princip oddělující datové služby 2.5G/3G od tradiční spojově orientované telefonie. Bez identifikátoru jako je ARI by síť nebyla schopna spolehlivě spojit přidělení uplinkového zdroje s konkrétní MS, která o něj požádala, v vytíženém rádiovém prostředí.

## Klíčové vlastnosti

- Jednoznačně identifikuje žádost mobilní stanice o paketový kanál na PRACH
- Umožňuje řešení kolizí řízené sítí během uplinkového přístupu
- Používá se BSS k adresování zprávy Packet Uplink Assignment správné MS
- Nedílná součást úvodní fáze vytváření Temporary Block Flow (TBF)
- Krátkodobý identifikátor s platností omezenou na buňku a bezprostřední přístupovou proceduru
- Hodnota je odvozena z parametrů specifických pro MS a informací vysílaných sítí

## Související pojmy

- [TLLI – Temporary Logical Link Identifier](/mobilnisite/slovnik/tlli/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [PAGCH – Packet Access Grant Channel](/mobilnisite/slovnik/pagch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [ARI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ari/)
