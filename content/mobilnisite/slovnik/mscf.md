---
slug: "mscf"
url: "/mobilnisite/slovnik/mscf/"
type: "slovnik"
title: "MSCF – Messaging Service Control Function"
date: 2025-01-01
abbr: "MSCF"
fullName: "Messaging Service Control Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mscf/"
summary: "Funkce v jádru sítě v IP multimediální podsystému (IMS) zodpovědná za řízení přidaných služeb zasílání zpráv. Zpracovává servisní logiku, správu interakcí a účtování služeb jako je chat, messaging bot"
---

MSCF je aplikační server IMS, který řídí přidané služby zasílání zpráv tím, že zpracovává servisní logiku, správu interakcí a účtování funkcí jako je chat a odložené doručování.

## Popis

Messaging Service Control Function (MSCF) je specializovaný aplikační server ([AS](/mobilnisite/slovnik/as/)) v architektuře IP multimediálního podsystému (IMS) dle 3GPP, definovaný primárně pro řízení a provádění pokročilých služeb zasílání zpráv. Je to logická funkce umístěná ve služební vrstvě, která komunikuje s hlavními prvky IMS, jako je Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), přes rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control). MSCF hostí servisní logiku pro messagingové aplikace přesahující základní [SMS](/mobilnisite/slovnik/sms/) nebo [MMS](/mobilnisite/slovnik/mms/), jako jsou chatovací místnosti, messaging boti, služby automatické odpovědi a odložené doručování zpráv. Funguje jako řídicí mozek těchto služeb, určuje, jak jsou zprávy zpracovávány, směrovány a jak s nimi interagovat na základě profilů účastníků a servisní logiky.

Operačně, když je messagingový [SIP](/mobilnisite/slovnik/sip/) požadavek (jako MESSAGE požadavek pro chatovou službu) směrován S-CSCF, je na základě počátečních filtračních kritérií (iFC) v profilu účastníka předán MSCF. MSCF následně provede svou servisní logiku. To může zahrnovat interakci s dalšími síťovými prvky: může komunikovat s Messaging Service Delivery Function (MSDF) pro vlastní ukládání a doručování zpráv, s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data účastníka a s online a offline systémy účtování ([OCS](/mobilnisite/slovnik/ocs/)/OFCS) přes rozhraní Ro/Rf pro účtování. Pro chatovou službu MSCF spravuje stav relace pro chatovací místnosti, zpracovává pozvánky účastníků a vynucuje přístupové politiky. Pro službu s botem interpretuje uživatelské zprávy, spouští logiku bota a formuluje odpovědi.

Architektonicky je MSCF klíčovou součástí messagingové architektury založené na IMS definované v TS 23.140. Umožňuje oddělení řízení služby (MSCF) od doručování a ukládání zpráv (MSDF). Toto oddělení umožňuje flexibilní nasazení, kdy lze servisní logiku aktualizovat nezávisle na mechanismech doručování. MSCF používá pro všechny své interakce standardní protokoly IMS, především SIP a Diameter. Jeho implementace zajišťuje, že pokročilé služby zasílání zpráv jsou bezproblémově integrovány do ekosystému IMS, využívají schopnosti IMS pro registraci, autentizaci, směrování a účtování, čímž poskytují uživatelům konzistentní a bezpečnou službu.

## K čemu slouží

MSCF byl vytvořen, aby poskytl standardizovaný řídicí rámec pro pokročilé služby zasílání zpráv založený na IMS, což představuje posun za omezení tradičních SMS v přepojovaných okruzích a proprietárních messagingových aplikací. Před jeho definicí byly přidané messagingové služby často implementovány jako samostatné, izolované aplikace s malou integrací do jádra sítě, což vedlo k nekonzistentní uživatelské zkušenosti, složitému účtování a obtížím při vytváření interoperabilních služeb napříč různými operátory a zařízeními.

Jeho účelem je řešit problém fragmentace služeb a umožnit vytváření bohatých, interaktivních messagingových funkcí v kontrolovaném prostředí IMS. Standardizací MSCF umožnil 3GPP operátorům nasadit společnou platformu pro řízení služeb, která by mohla podporovat širokou škálu messagingových aplikací – od jednoduchého chatu po komplexní konverzační boty – a zároveň využívat robustní infrastrukturu IMS pro zabezpečení, autentizaci a účtování. Tím byla řešena potřeba škálovatelné, účtovatelné a bezpečné architektury pro messaging příští generace jako součást přechodu na plně IP sítě. MSCF, zavedený v Rel-6 spolu s IMS, byl základním prvkem pro realizaci vize konvergovaných multimediálních komunikačních služeb, který zajistil, že se messaging vyvíjí v souladu s ostatními službami IMS, jako je Voice over LTE (VoLTE) a videohovory.

## Klíčové vlastnosti

- Funguje jako aplikační server (AS) IMS hostující servisní logiku pro pokročilé messagingové aplikace.
- Řídí služby jako chat, messaging boti, automatická odpověď a odložené doručování prostřednictvím signalizace SIP.
- Komunikuje s S-CSCF přes rozhraní ISC na základě počátečních filtračních kritérií (iFC).
- Odděluje řízení služby (MSCF) od doručování/ukládání zpráv (MSDF) pro architektonickou flexibilitu.
- Integruje se se systémy účtování (OCS/OFCS) přes rozhraní Diameter Ro/Rf pro účtování služeb.
- Spravuje interakci služby a stav účastníka pro interaktivní messagingové relace.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [AS – Angle Spread](/mobilnisite/slovnik/as/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [MSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mscf/)
