---
slug: "adu"
url: "/mobilnisite/slovnik/adu/"
type: "slovnik"
title: "ADU – Application Data Unit"
date: 2025-01-01
abbr: "ADU"
fullName: "Application Data Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adu/"
summary: "ADU je základní datová obalová jednotka pro multimediální aplikace v sítích 3GPP, která představuje kompletní, nezávisle dekódovatelný kus dat aplikační vrstvy. Slouží jako základní kontejner pro přen"
---

ADU je základní, nezávisle dekódovatelná datová obalová jednotka, která slouží jako základní kontejner pro přenos dat multimediálních aplikací v sítích 3GPP.

## Popis

Application Data Unit (ADU) je klíčový koncept v architektuře pro doručování multimediálních služeb 3GPP, definovaný jako samostatná datová jednotka generovaná aplikační vrstvou, která obsahuje kompletní sémantický význam. V praktické implementaci ADU typicky odpovídá jednomu mediálnímu snímku nebo přístupové jednotce při multimediálním streamování – například jednomu videosnímku (I-snímek, P-snímek nebo B-snímek v H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/)), jednomu audiosnímku v kodecích [AAC](/mobilnisite/slovnik/aac/) nebo [AMR](/mobilnisite/slovnik/amr/), nebo časovanému textovému vzorku pro titulky. ADU slouží jako atomární jednotka pro zpracování na aplikační vrstvě, obsahuje všechna data potřebná pro dekódování a prezentaci na straně přijímače spolu s časovacími informacemi klíčovými pro synchronizaci médií.

Architektonicky existují ADU na rozhraní mezi aplikační vrstvou a podpůrnými transportními protokoly. Když aplikace generuje obsah, zabalí mediální data do ADU, z nichž každé má definovaný časový razítko prezentace (PTS) a časové razítko dekódování ([DTS](/mobilnisite/slovnik/dts/)), které určují, kdy má být obsah dekódován a zobrazen. Tyto ADU jsou poté předány transportním protokolům, jako je RTP (Real-time Transport Protocol) pro streamování nebo [FLUTE](/mobilnisite/slovnik/flute/) (File Delivery over Unidirectional Transport) pro doručování souborů, které mohou ADU dále segmentovat nebo paketizovat pro přenos sítí. Specifikace služeb 3GPP Packet-switched Streaming Service (PSS) a Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) definují, jak se ADU mapují na transportní protokoly, s konkrétními pravidly pro fragmentaci a opětovné sestavení, když velikost ADU překročí omezení maximální přenosové jednotky.

Klíčové komponenty ADU zahrnují datovou část obsahující skutečná mediální data, časovací informace pro synchronizaci, pořadová čísla pro uspořádání a volitelné metadata popisující charakteristiky obsahu. Ve streamovacích scénářích jsou ADU typicky doručována v pořadí prezentace s přesnými časovými vztahy udržovanými prostřednictvím časových razítek RTP. Pro stahovací služby mohou být ADU doručována asynchronně s časovacími informacemi zachovanými pro pozdější přehrávání. Koncept ADU umožňuje důležité síťové funkce, jako je adaptivní streamování s proměnným datovým tokem – kde jsou různé kvalitní reprezentace stejného obsahu zakódovány jako samostatné sekvence ADU – a mechanismy odolnosti proti chybám, kde mohou být přenášena redundantní ADU pro kompenzaci ztráty paketů.

Role ADU se rozprostírá napříč celým řetězcem doručování multimédií, od přípravy obsahu na serveru po přehrávání na klientském zařízení. Obsahové servery balí média do ADU podle specifikací kodeků a požadavků služeb, zatímco klientská zařízení ADU ukládají do vyrovnávací paměti a zpracovávají pro plynulé přehrávání. Síťové prvky, jako jsou proxy a brány, mohou kontrolovat hranice ADU pro implementaci politik kvality služeb, tvarování provozu nebo operací překódování. Standardizovaná struktura ADU zajišťuje, že všechny komponenty v doručovacím řetězci sdílejí společné porozumění segmentaci médií, což umožňuje efektivní zpracování a předvídatelné chování napříč heterogenními sítěmi a zařízeními.

## K čemu slouží

Koncept Application Data Unit byl zaveden, aby řešil základní výzvy v doručování multimediálního obsahu přes paketově přepínané mobilní sítě. Před standardizací ADU v 3GPP používaly multimediální aplikace proprietární metody datové enkapsulace, které vedly k problémům s interoperabilitou mezi zařízeními různých výrobců a k nekonzistentnímu chování v různých síťových podmínkách. Absence standardizované atomární jednotky pro aplikační data ztěžovala implementaci efektivních mechanismů vyrovnávací paměti, obnovy po chybách a synchronizace v prostředích mobilních sítí s omezenými zdroji.

ADU řeší několik kritických problémů v mobilním doručování multimédií. Za prvé poskytují jasnou hranici mezi sémantikou aplikační vrstvy a mechanismy transportní vrstvy, což umožňuje každé vrstvě optimalizovat své operace nezávisle. Vývojáři aplikací se mohou soustředit na kódování médií a logiku prezentace, zatímco síťoví inženýři mohou optimalizovat transportní protokoly pro bezdrátové podmínky. Za druhé ADU umožňují přesnou synchronizaci médií tím, že nesou časovací informace, které přečkají síťová zpoždění a chvění, čímž zajišťují synchronizaci obrazu a zvuku u videohovorů a plynulé přehrávání u streamovacích služeb. Za třetí usnadňují adaptaci kvality tím, že slouží jako přepínací bod mezi různými reprezentacemi datového toku v scénářích adaptivního streamování.

Vznik ADU byl motivován evolucí od okruhově přepínaných hlasových služeb k paketově přepínaným multimediálním službám v sítích 3G. Když operátoři začali nabízet videostreamování, videotelefonii a multimediální zprávy, potřebovali standardizovaný způsob, jak efektivně balit a doručovat různé typy médií. Předchozí přístupy, které zacházely s médii jako s kontinuálními bajtovými proudy, postrádaly strukturu potřebnou pro odolnost proti chybám, náhodný přístup a adaptaci šířky pásma v proměnných bezdrátových podmínkách. Koncept ADU tuto potřebnou strukturu poskytl, zároveň zachoval kompatibilitu s existujícími internetovými protokoly a standardy kodeků, což umožnilo úspěšné nasazení bohatých multimediálních služeb napříč sítěmi 3G, 4G a 5G.

## Klíčové vlastnosti

- Samostatná enkapsulace média s kompletním sémantickým významem
- Přesné časovací informace včetně časových razítek prezentace a dekódování
- Standardizované mapování na transportní protokoly jako RTP a FLUTE
- Podpora adaptivního streamování prostřednictvím přepínání kvalitních reprezentací
- Odolnost proti chybám prostřednictvím schopnosti redundantního přenosu
- Struktura nezávislá na kodeku podporující více typů médií

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G

---

📖 **Anglický originál a plná specifikace:** [ADU na 3GPP Explorer](https://3gpp-explorer.com/glossary/adu/)
