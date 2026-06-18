---
slug: "retap"
url: "/mobilnisite/slovnik/retap/"
type: "slovnik"
title: "RETAP – Remote Electrical Tilting Application Part"
date: 2025-01-01
abbr: "RETAP"
fullName: "Remote Electrical Tilting Application Part"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/retap/"
summary: "RETAP je protokol v rámci frameworku AISG, který standardizuje komunikaci mezi RET řadiči a anténními jednotkami pro dálkové řízení elektrického náklonu. Zajišťuje interoperabilitu napříč dodavateli,"
---

RETAP je protokol v rámci frameworku AISG, který standardizuje komunikaci pro dálkové řízení elektrického náklonu mezi RET řadiči a anténními jednotkami za účelem zajištění interoperability mezi různými dodavateli.

## Popis

Remote Electrical Tilting Application Part (RETAP) je standardizovaný aplikační protokol definovaný v ekosystému Antenna Interface Standards Group (AISG), specifikovaný v 3GPP TS 37.460 a souvisejících dokumentech. Usnadňuje komunikaci mezi řídicími jednotkami [RET](/mobilnisite/slovnik/ret/) (například v základnových stanicích nebo systémech správy sítě) a zařízeními pro dálkový elektrický náklon připojenými k anténám. RETAP funguje přes fyzická rozhraní, jako jsou koaxiální kabely nebo vyhrazené řídicí linky, a používá architekturu master-slave, kde RET řadič funguje jako master a anténní jednotka jako slave, a vyměňují si příkazy a odpovědi pro nastavení náklonu.

Z architektonického hlediska je RETAP součástí zásobníku protokolů AISG, který zahrnuje nižší vrstvy pro přenos a fyzickou konektivitu. Definuje formáty zpráv, procedury a zpracování chyb pro řízení elektrického náklonu, včetně příkazů pro nastavení konkrétního úhlu náklonu, čtení aktuálního stavu náklonu a provádění kalibrace. Protokol zajišťuje spolehlivou a bezpečnou komunikaci s funkcemi, jako jsou kontrolní součty a mechanismy potvrzení, aby se zabránilo chybnému nastavení. Ve specifikacích 3GPP je RETAP integrován do rozhraní správy, jako je Itf-N, což operátorům umožňuje automatizovat řízení náklonu prostřednictvím systémů správy sítě.

Klíčovými součástmi RETAP jsou protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) pro příkazy a odpovědi, které zapouzdřují parametry, jako je cílový úhel náklonu, identifikace zařízení a provozní režimy. Protokol podporuje jak konfigurace point-to-point, tak multi-drop, což umožňuje řízení více RET zařízení z jednoho řadiče. Funguje tak, že naváže komunikační relaci, odešle příkazy pro nastavení náklonu s přesnými hodnotami úhlů (často ve stupních) a ověří provedení prostřednictvím stavových hlášení. To umožňuje dynamickou optimalizaci anténních diagramů pro tvarování pokrytí, snížení interference a správu kapacity.

Role RETAP v síti je klíčová pro interoperabilitu, protože umožňuje bezproblémovou spolupráci zařízení od různých dodavatelů v RET systémech. Tvoří základ automatizovaných funkcí optimalizace sítě v [SON](/mobilnisite/slovnik/son/), kde jsou úpravy náklonu spouštěny na základě dat monitorování výkonu. V 5G a dalších generacích se RETAP vyvíjí, aby podporoval pokročilé anténní systémy, jako je Massive [MIMO](/mobilnisite/slovnik/mimo/), s vylepšeními pro rychlejší řídicí smyčky a integraci s inteligentními řadiči RAN. Celkově RETAP standardizuje rozhraní pro dálkové řízení elektrického náklonu, snižuje složitost nasazení a umožňuje efektivní správu RAN.

## K čemu slouží

RETAP byl vytvořen, aby řešil problémy s interoperabilitou v raných nasazeních [RET](/mobilnisite/slovnik/ret/), kde proprietární protokoly různých dodavatelů antén a základnových stanic bránily bezproblémové integraci. Před RETAP čelili operátoři závislosti na jednom dodavateli a zvýšeným nákladům kvůli nekompatibilním řídicím rozhraním, což bránilo optimalizaci sítí ve velkém měřítku. Protokol standardizuje komunikaci pro dálkové řízení elektrického náklonu, umožňuje prostředí s více dodavateli a snižuje provozní překážky.

Historicky, jak se RET od Release 6 dále začalo v sítích 3GPP více přijímat, stala se potřeba společného protokolu zřejmou pro podporu automatizované správy sítě a funkcí [SON](/mobilnisite/slovnik/son/). RETAP řeší problémy, jako jsou nekonzistentní sady příkazů, nespolehlivá komunikace a nedostatek zabezpečení při řízení náklonu. Byl motivován snahou průmyslu prostřednictvím AISG vytvořit otevřený standard, což usnadnilo rozsáhlé nasazení RET a posunulo schopnosti samooptymalizujících se sítí.

V kontextu standardů 3GPP byl vývoj RETAP poháněn požadavky operátorů na flexibilní a nákladově efektivní nasazení sítí. Řeší omezení ad-hoc řídicích metod tím, že poskytuje robustní, standardizované rozhraní, které podporuje současné i budoucí anténní technologie. Tím, že umožňuje přesné dálkové řízení, pomáhá RETAP optimalizovat rádiový výkon, snižovat interference a zlepšovat uživatelský zážitek, což je v souladu s vývojem směrem k softwarově definovaným a automatizovaným architekturám RAN.

## Klíčové vlastnosti

- Standardizovaný aplikační protokol pro komunikaci RET v rámci frameworku AISG
- Podpora příkazů pro nastavení, čtení a kalibraci úhlů elektrického náklonu
- Architektura master-slave se spolehlivou výměnou zpráv a zpracováním chyb
- Interoperabilita napříč zařízeními od více dodavatelů antén a základnových stanic
- Integrace se systémy správy sítě pro automatizované řízení
- Bezpečnostní funkce pro zabránění neoprávněným úpravám náklonu

## Související pojmy

- [RET – Remote Electrical Tilting](/mobilnisite/slovnik/ret/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 37.460** (Rel-19) — Iuant Interface Introduction
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [RETAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/retap/)
