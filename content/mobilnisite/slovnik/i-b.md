---
slug: "i-b"
url: "/mobilnisite/slovnik/i-b/"
type: "slovnik"
title: "I/B – Interactive / Background"
date: 2025-01-01
abbr: "I/B"
fullName: "Interactive / Background"
category: "QoS"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/i-b/"
summary: "Standardizovaná třída QoS pro paketově přepínané služby v sítích 3GPP. Definuje dvě priority zpracování provozu pro nereálnocasové datové služby, což umožňuje diferencované přidělování zdrojů a plánov"
---

I/B je standardizovaná třída kvality služeb (QoS) definující dvě priority zpracování provozu pro nereálnocasové datové služby za účelem rozlišení mezi interaktivními aplikacemi a přenosy na pozadí.

## Popis

Interactive / Background (I/B) je základní třída provozu kvality služeb (QoS) definovaná v rámci paketově přepínané domény 3GPP, konkrétně pro kontext protokolu paketových dat (PDP). Je jednou ze čtyř hlavních standardizovaných tříd QoS vedle tříd Konverzační, Proudění a Na pozadí. Třída I/B je navržena pro nereálnocasové, elastické aplikace, kde zpoždění end-to-end není kriticky omezeno, ale uživatel očekává interaktivní odezvu nebo předvídatelný přenos dat. Třída je dále rozdělena na dvě odlišné priority zpracování provozu: Interaktivní a Na pozadí. Podtřída Interaktivní je určena pro aplikace jako webový prohlížeč, databázové dotazy nebo přístup k serveru, kde existuje vzor požadavek-odpověď a uživatel aktivně čeká na odpověď. Podtřída Na pozadí je pro aplikace jako doručování e-mailů, stahování souborů ([FTP](/mobilnisite/slovnik/ftp/)) nebo aktualizace softwaru, kde k přenosu dochází bez přímé interakce s uživatelem a které snášejí delší zpoždění.

Z architektonického hlediska jsou parametry třídy I/B vyjednány během procedury Aktivace kontextu PDP mezi uživatelským zařízením (UE) a uzlem podpory brány [GPRS](/mobilnisite/slovnik/gprs/) (GGSN) v jádru sítě. Klíčové atributy QoS pro kontext I/B zahrnují samotnou Třídu provozu, Prioritu přidělení/zachování ([ARP](/mobilnisite/slovnik/arp/)), Prioritu zpracování provozu (THP) specificky pro podtřídu Interaktivní a indikátory Maximálního bitového toku ([MBR](/mobilnisite/slovnik/mbr/)) / Garantovaného bitového toku ([GBR](/mobilnisite/slovnik/gbr/)). Významně, provoz I/B je ne-GBR, což znamená, že síť negarantuje konstantní bitový tok, ale poskytuje službu typu 'best-effort' s prioritizací. Priorita zpracování provozu (THP) s hodnotami 1, 2 nebo 3 (kde 1 je nejvyšší) je klíčovým rozlišovacím prvkem v rámci podtřídy Interaktivní a umožňuje plánovači v rádiové přístupové síti (RAN) upřednostňovat pakety z jednoho interaktivního kontextu před jiným při přetížení.

V rámci rádiové přístupové sítě (např. UTRAN nebo [E-UTRAN](/mobilnisite/slovnik/e-utran/)) používá NodeB nebo eNodeB signalizované parametry QoS pro přenos (mapované z kontextu PDP) k rozhodování o plánování na rádiovém rozhraní. Pakety označené třídou Interaktivní a vysokou THP jsou typicky naplánovány dříve než pakety s třídou Na pozadí nebo nižší THP, za předpokladu podobných podmínek kanálu. Tím je zajištěno, že požadavek uživatele na načtení webové stránky je vyřízen rychleji než souběžná synchronizace souboru na pozadí. Uzel podpory GPRS pro obsluhu (SGSN) a GGSN provádějí funkce policingu a formování provozu na základě dohodnutého Maximálního bitového toku, aby zabránily nadměrné spotřebě síťových zdrojů jedním uživatelem. Třída I/B je základním kamenem QoS architektury 3GPP, neboť umožňuje efektivní statistické multiplexování datového provozu a zároveň poskytuje základní úroveň diferenciace služeb, která je klíčová pro správu síťových zdrojů a vnímanou kvalitu uživatelského zážitku u naprosté většiny internetových aplikací.

## K čemu slouží

Třída QoS I/B byla vytvořena, aby řešila základní výzvu efektivní podpory různorodých internetových datových aplikací přes mobilní sítě, které byly původně navrženy pro hlas. Před zavedením standardizovaných tříd QoS byl veškerý paketový provoz považován za nediferencovaný 'best-effort', což vedlo ke špatnému uživatelskému zážitku, kdy interaktivní aplikace citlivé na zpoždění mohly být vytlačeny hromadnými přenosy na pozadí. Zavedení třídy I/B v Rel-8 (navazující na dřívější koncepty QoS pro [GPRS](/mobilnisite/slovnik/gprs/)/UMTS) poskytlo standardizovaný mechanismus, který síti umožňuje rozlišovat mezi provozem s aktivní účastí uživatele a provozem na pozadí iniciovaným strojem.

Tato diferenciace řeší problém soupeření o zdroje a umožňuje síťovým operátorům implementovat politiky, které zlepšují vnímaný výkon pro koncové uživatele. Například při přetížení sítě může být relace webového prohlížení upřednostněna před stahováním souborů v režimu peer-to-peer, čímž je zajištěna interaktivní odezva pro daného uživatele. Umožňuje také vytváření diferencovaných nabídek služeb nebo tarifů, kde prémiový datový tarif může přiřadit vyšší Prioritu zpracování provozu (THP) interaktivnímu provozu uživatele ve srovnání se základním tarifem. Třída I/B jako součást širšího QoS rámce byla klíčovým prvkem umožňujícím mobilní datovou revoluci, neboť dovolila mobilním sítím přejít z pouhých přenosových kanálů na inteligentní platformy schopné řídit výkon aplikací.

## Klíčové vlastnosti

- Definuje nereálnocasovou třídu provozu bez garantovaného bitového toku (non-GBR)
- Je rozdělena na priority zpracování provozu Interaktivní a Na pozadí
- Pro podrobné plánování interaktivního provozu používá parametr Priority zpracování provozu (THP) s hodnotami 1, 2, 3
- Klíčové parametry jsou vyjednány během Aktivace kontextu PDP (Třída provozu, ARP, THP, MBR)
- Umožňuje diferencované zacházení v plánovači rádiové přístupové sítě (RAN, např. UTRAN, E-UTRAN)
- Základní prvek pro statistické multiplexování a efektivní využití zdrojů pro datové služby

## Definující specifikace

- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping

---

📖 **Anglický originál a plná specifikace:** [I/B na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-b/)
