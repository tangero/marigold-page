---
slug: "cllm"
url: "/mobilnisite/slovnik/cllm/"
type: "slovnik"
title: "CLLM – Consolidated Link Layer Management"
date: 2025-01-01
abbr: "CLLM"
fullName: "Consolidated Link Layer Management"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cllm/"
summary: "CLLM je standardizovaný řídicí protokol definovaný v 3GPP pro rozhraní A-bis mezi řadičem základnových stanic (BSC) a základnovou přenosovou stanicí (BTS) v sítích GSM/EDGE. Poskytuje jednotný rámec p"
---

CLLM je standardizovaný protokol 3GPP pro rozhraní A-bis, který poskytuje jednotný rámec pro dohled na vrstvě spojení, správu poruch a monitorování výkonu v sítích GSM/EDGE.

## Popis

Consolidated Link Layer Management (CLLM) je klíčový řídicí protokol specifikovaný v 3GPP TS 48.016, který funguje přes rozhraní A-bis v rámci GSM rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)). Rozhraní A-bis spojuje řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) s jednou nebo více základnovými přenosovými stanicemi ([BTS](/mobilnisite/slovnik/bts/)) a přenáší jak uživatelský provoz (hlas a data), tak signalizaci řídicí roviny. Primární úlohou CLLM je správa fyzických přenosových okruhů (např. linky E1/T1 nebo paketová připojení), které toto rozhraní tvoří. Funguje na vrstvě spojení (vrstva 2) modelu [OSI](/mobilnisite/slovnik/osi/) a poskytuje standardizovaný mechanismus pro dohled, detekci poruch, jejich izolaci a procedury obnovy nezávisle na podkladovém fyzickém médiu.

Architektonicky jsou funkce CLLM implementovány v síťových prvcích BSC a BTS. Protokol definuje vztah typu master-slave, přičemž BSC typicky vystupuje jako řídicí entita (master) a BTS jako spravovaná entita (slave) pro daný okruh. Komunikace probíhá prostřednictvím vyhrazených zpráv CLLM vložených do struktury protokolu vrstvy 2 rozhraní A-bis. Tyto zprávy nesou informace o stavu okruhu, alarmech, měřeních výkonu a konfiguračních parametrech. CLLM spravuje logické kanály multiplexované přes fyzický okruh, monitoruje jejich integritu a zajišťuje správné přidělení a funkčnost zdrojů.

Mezi klíčové provozní procedury patří nepřetržitý dohled nad okruhem prostřednictvím mechanizmů heartbeat, okamžité hlášení poruch (např. ztráta signálu, ztráta synchronizace rámců) a monitorování výkonu sběrem statistik chyb, jako je bitová chybovost ([BER](/mobilnisite/slovnik/ber/)) a chyby kontrolního součtu [CRC](/mobilnisite/slovnik/crc/). Při detekci poruchy CLLM spouští automatické akce obnovy, které mohou zahrnovat resetování okruhu, přepnutí na záložní cestu v redundantních konfiguracích nebo upozornění systémů správy vyšších vrstev. Protokol také podporuje administrativní funkce, jako je blokování/odblokování okruhu pro údržbu a získávání historických dat o výkonu pro analýzu trendů.

Konstrukce CLLM je nedílnou součástí spolehlivosti sítě. Poskytnutím konsolidovaného pohledu na všechny parametry vrstvy spojení zjednodušuje diagnostiku poruch a snižuje prostoje sítě. Jeho standardizovaná povaha zajišťuje interoperabilitu mezi zařízeními BSC a BTS od různých dodavatelů, což byl v počátcích nasazení GSM významný problém. Efektivní mechanizmy hlášení v CLLM navíc zabraňují zahlcení rozhraní A-bis řídicím provozem, čímž šetří šířku pásma pro uživatelské služby při zachování robustního dohledu nad transportní infrastrukturou.

## K čemu slouží

CLLM byl vytvořen, aby řešil kritickou potřebu spolehlivé a standardizované správy fyzických přenosových okruhů v sítích GSM, konkrétně na rozhraní A-bis. Před jeho standardizací dodavatelé implementovali proprietární řešení správy okruhů, což vedlo k problémům s interoperabilitou při míchání zařízení od různých výrobců v jedné síti. Tato roztříštěnost zvyšovala provozní složitost, bránila nasazení více dodavateli a ztěžovala a prodlužovala izolaci poruch a odstraňování problémů, což nakonec ovlivňovalo dostupnost sítě a náklady na údržbu.

Základní problém, který CLLM řeší, je poskytnutí jednotného, na dodavateli nezávislého protokolu pro dohled nad vrstvou spojení mezi [BSC](/mobilnisite/slovnik/bsc/) a [BTS](/mobilnisite/slovnik/bts/). Rozhraní A-bis je vysokokapacitní, vícekanálové spojení klíčové pro provoz sítě; jakékoli selhání přímo ovlivňuje služby pro stovky či tisíce účastníků. CLLM umožňuje konzistentní monitorování stavu okruhu, rychlou detekci poruch (jako je ztráta signálu nebo chyby synchronizace) a automatické spouštění procedur obnovy. Tato proaktivní správa je nezbytná pro dosažení vysoké spolehlivosti a dostupnosti požadované ve veřejných telekomunikačních sítích.

Historicky jeho zavedení v 3GPP Release 8 konsolidovalo a formalizovalo osvědčené postupy pro správu vrstvy spojení, které se vyvinuly během dřívějších nasazení GSM. Definováním komplexní sady procedur pro správu poruch, konfiguraci a výkon na vrstvě spojení poskytl CLLM síťovým operátorům mocný nástroj k automatizaci dohledu, snížení manuálních zásahů a zlepšení střední doby do opravy (MTTR). Tato standardizace byla klíčovým faktorem pro konkurenční trh více dodavatelských zařízení v sítích GSM, což operátorům umožnilo větší flexibilitu v návrhu sítě a nákupu při zachování robustní provozní kontroly.

## Klíčové vlastnosti

- Standardizované mechanizmy dohledu nad okruhem a heartbeat pro nepřetržité monitorování dostupnosti
- Správa poruch s interoperabilitou mezi dodavateli včetně automatické detekce a hlášení selhání okruhu
- Schopnosti monitorování výkonu sběrem chybovosti a metrik kvality pro analýzu trendů
- Podpora administrativních řídicích operací, jako je blokování, odblokování a reset okruhu
- Fungování přes různá fyzická média (např. E1/T1, transport založený na IP) na rozhraní A-bis
- Efektivní návrh protokolu minimalizující režii správy na kritických transportních okruzích

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [CLLM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cllm/)
