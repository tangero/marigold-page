---
slug: "ns-vci"
url: "/mobilnisite/slovnik/ns-vci/"
type: "slovnik"
title: "NS-VCI – Network Service Virtual Connection Identifier"
date: 2025-01-01
abbr: "NS-VCI"
fullName: "Network Service Virtual Connection Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ns-vci/"
summary: "Jedinečný identifikátor pro virtuální spojení síťové služby (NS-VC) na rozhraní Iur-g. Rozlišuje jednotlivá logická spojení používaná k přenosu synchronizačních informací mezi BSC a serverem síťové sy"
---

NS-VCI je jedinečný identifikátor pro virtuální spojení síťové služby (Network Service Virtual Connection) na rozhraní Iur-g, který rozlišuje logická spojení přenášející synchronizační informace mezi BSC a serverem síťové synchronizace BSS.

## Popis

Identifikátor virtuálního spojení síťové služby (NS-VCI) je klíčový adresní prvek v rámci synchronizační architektury 3GPP, konkrétně definovaný pro rozhraní Iur-g mezi řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a serverem síťové synchronizace [BSS](/mobilnisite/slovnik/bss/) ([NSS](/mobilnisite/slovnik/nss/)). Podle 3GPP TS 48.016 je NS-VCI číselný nebo alfanumerický štítek, který jednoznačně identifikuje jedno virtuální spojení síťové služby ([NS-VC](/mobilnisite/slovnik/ns-vc/)) v kontextu virtuálního spoje síťové služby ([NS-VL](/mobilnisite/slovnik/ns-vl/)). Tento identifikátor používají oba koncové body i mezilehlé síťové prvky k přiřazení paketů synchronizačních dat ke správnému logickému spojení, čímž zajišťuje, že časové informace jsou doručeny zamýšlenému BSC nebo zdroji synchronizace.

Během provozu je NS-VCI zahrnut v hlavičkách protokolu zpráv procházejících přes NS-VC. Když je synchronizační reference odeslána z NSS do BSC, umožňuje NS-VCI přenosové síti směrovat data ke konkrétnímu NS-VC zřízenému pro daný BSC. Podobně, když BSC komunikuje zpět s NSS, používá NS-VCI k označení, ke kterému spojení zpráva patří. Identifikátor je typicky přiřazen během fáze zřízení NS-VC prostřednictvím signalizace řídicí roviny a po dobu trvání spojení zůstává konstantní. Jeho platnost je obecně lokální pro NS-VL nebo segment rozhraní Iur-g, což znamená, že stejná hodnota NS-VCI může být bez konfliktu znovu použita v různých částech sítě.

NS-VCI hraje klíčovou roli v síťové správě a řešení problémů. Sledováním hodnot NS-VCI mohou operátoři monitorovat stav a výkon jednotlivých synchronizačních spojení, diagnostikovat problémy související s distribucí časování a efektivně spravovat zdroje. Také usnadňuje škálovatelnost, protože více NS-VC (každé s jedinečným NS-VCI) může být multiplexováno přes jeden fyzický nebo virtuální spoj, což umožňuje mnoha BSC přijímat synchronizaci z centrálního NSS bez nutnosti vyhrazených fyzických okruhů. Tento identifikátor je základním prvkem virtualizovaného, flexibilního synchronizačního modelu propagovaného 3GPP pro sítě GSM a UMTS.

## K čemu slouží

NS-VCI byl vytvořen, aby poskytl standardizovaný mechanismus pro identifikaci a správu jednotlivých synchronizačních spojení ve virtualizovaném přenosovém prostředí. Před jeho zavedením byla synchronizační propojení často bod-od-bod fyzická spojení bez potřeby složité adresace, ale jak se sítě vyvíjely k využití sdílené paketové přenosové infrastruktury, stala se nutností možnost multiplexovat více logických synchronizačních toků přes stejnou infrastrukturu. NS-VCI řeší problém rozlišování mezi různými [NS-VC](/mobilnisite/slovnik/ns-vc/), které mohou sdílet společné síťové cesty, a zajišťuje, že synchronizační data jsou správně přiřazena k cílovému [BSC](/mobilnisite/slovnik/bsc/).

Jeho účel je hluboce spjat s efektivitou a škálovatelností distribuce synchronizace v moderních rádiových přístupových sítích. Použitím identifikátorů mohou operátoři dynamicky zřizovat a rušit synchronizační spojení při změnách topologie sítě nebo při přidávání či odebírání základnových stanic, aniž by museli rekonfigurovat fyzické propojení. NS-VCI umožňuje přesnou kontrolu a monitorování každého synchronizačního kanálu, což je klíčové pro udržování vysoce kvalitního časování v celé síti, zejména v hustých nasazeních, kde je přesná synchronizace životně důležitá pro správu rušení a výkon přechodů mezi buňkami.

Historicky byl NS-VCI standardizován v 3GPP Release 8 spolu s konceptem NS-VC, aby řešil omezení dřívějších synchronizačních metod, kterým chyběly formální identifikační schémata. Podporuje interoperabilitu mezi zařízeními od různých výrobců tím, že poskytuje společný odkaz pro synchronizační spojení, a usnadňuje tak přechod k flexibilnějším a nákladově efektivnějším synchronizačním řešením v sítích 2G a 3G.

## Klíčové vlastnosti

- Jedinečný identifikátor pro virtuální spojení síťové služby (NS-VC)
- Používá se pro směrování a správu synchronizačních dat na rozhraní Iur-g
- Přiřazuje se během zřízení NS-VC prostřednictvím signalizace řídicí roviny
- Umožňuje multiplexování více NS-VC přes sdílené přenosové spoje
- Nezbytný pro škálovatelnost a dynamickou správu synchronizačních spojení
- Podporuje síťové monitorování a řešení problémů prostřednictvím sledování spojení

## Související pojmy

- [NS-VC – Network Service Virtual Connection](/mobilnisite/slovnik/ns-vc/)
- [NS-VL – Network Service Virtual Link](/mobilnisite/slovnik/ns-vl/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NS-VCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-vci/)
