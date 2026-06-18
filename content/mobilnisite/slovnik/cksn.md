---
slug: "cksn"
url: "/mobilnisite/slovnik/cksn/"
type: "slovnik"
title: "CKSN – Ciphering Key Sequence Number"
date: 2025-01-01
abbr: "CKSN"
fullName: "Ciphering Key Sequence Number"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cksn/"
summary: "CKSN je bezpečnostní parametr identifikující, který šifrovací klíč je aktuálně aktivní mezi UE a sítí. Umožňuje bezpečnou správu klíčů synchronizací šifrovacích klíčů během autentizačních a handover p"
---

CKSN je bezpečnostní parametr, který identifikuje aktivní šifrovací klíč mezi UE a sítí a umožňuje bezpečnou synchronizaci klíčů při autentizaci a předávání spojení, čímž zabraňuje narušení bezpečnosti v důsledku neshody klíčů.

## Popis

Ciphering Key Sequence Number (CKSN) je základní bezpečnostní parametr v sítích 3GPP, který slouží jako index nebo identifikátor pro aktuálně aktivní šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) používaný k šifrování uživatelských dat a signalizace mezi uživatelským zařízením (UE) a sítí. Funguje jako součást rámce autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)), konkrétně v rámci procedur UMTS AKA a EPS AKA. CKSN je uložen jak v nevolatilní paměti UE, tak v autentizačním centru (AuC) nebo home subscriber server ([HSS](/mobilnisite/slovnik/hss/)) sítě, což zajišťuje, že obě entity mohou odkazovat na stejný kryptografický klíč bez nutnosti přenášet samotný klíč přes rozhraní vzduchu.

Z architektonického hlediska je CKSN integrován do systému správy bezpečnostního kontextu. Při počátečním připojení (attach) nebo periodické autentizaci UE síť vygeneruje nový šifrovací klíč (CK) spolu s integritním klíčem ([IK](/mobilnisite/slovnik/ik/)) a přiřadí hodnotu CKSN, typicky v rozsahu 0 až 7. Tento CKSN je přenesen na UE v rámci autentizačních vektorů (např. v UMTS) nebo jako součást [NAS](/mobilnisite/slovnik/nas/) bezpečnostního kontextu (v LTE/5G). UE klíč CK uloží a asociuje jej s přijatým CKSN. Při následných připojeních UE zahrne CKSN do svých zpráv typu attach nebo service request, což síti umožní získat odpovídající CK ze své databáze bez nutnosti pokaždé provádět plnou autentizaci.

CKSN hraje klíčovou roli během událostí mobility, jako jsou předání spojení (handover) mezi různými rádiovými přístupovými technologiemi (např. z UMTS na LTE) nebo mezi síťovými uzly. Když se UE přesune k novému obsluhujícímu uzlu, cílový uzel požaduje bezpečnostní kontext od zdrojového uzlu nebo HSS. CKSN je součástí tohoto přenosu kontextu, což umožňuje cílovému uzlu identifikovat a aplikovat správný šifrovací klíč bez přerušení šifrovací relace. Tento mechanismus zajišťuje plynulou kontinuitu zabezpečení a zabraňuje expozici dat během přechodů. V systémech 5G, ačkoliv se koncept vyvíjí se zavedením Key Set Identifier ([KSI](/mobilnisite/slovnik/ksi/)), zůstává CKSN relevantní ve scénářích interworkingu se staršími sítěmi.

Klíčové komponenty spojené s CKSN zahrnují bezpečnostní modul UE ([USIM](/mobilnisite/slovnik/usim/)), mobility management entity ([MME](/mobilnisite/slovnik/mme/)) nebo serving GPRS support node (SGSN) obsluhující sítě a home subscriber server/autentizační centrum (HSS/AuC) domovské sítě. CKSN je typicky 3bitová hodnota, což umožňuje současnou správu až osmi různých sekvencí klíčů. Tento omezený rozsah vyžaduje pečlivou správu životního cyklu klíčů, včetně periodických aktualizací klíčů prostřednictvím přeautentizace, aby se zabránilo vyčerpání posloupnostních čísel. CKSN se také používá spolu s Key Set Identifier (KSI) v EPS a 5GS pro zajištění zpětné kompatibility a podpory procedur vyjednávání šifrovacích klíčů.

## K čemu slouží

CKSN byl zaveden, aby řešil kritické výzvy správy klíčů v raných sítích 3G (UMTS), kde byla bezpečná a efektivní synchronizace šifrovacích klíčů mezi UE a sítí zásadní pro udržení důvěrnosti. Před zavedením CKSN používaly systémy 2G, jako GSM, jednodušší přístup odvození klíčů bez explicitního číslování sekvencí, což vedlo ke zranitelnostem během předávání spojení a potenciálním neshodám klíčů. Tyto neshody mohly způsobit přerušení služeb nebo bezpečnostní mezery, protože síť a UE se mohly pokoušet použít různé šifrovací klíče, což vedlo k selhání dešifrování nebo expozici dat.

Primární motivací pro CKSN bylo umožnit robustní správu bezpečnostního kontextu během scénářů mobility a opětovného připojení. Bez identifikátoru klíče by síť musela provádět plnou autentizaci a dohodu o klíči pro každý pokus o připojení, což by zvyšovalo signalizační režii a latenci. CKSN umožňuje síti rychle identifikovat a znovu použít dříve navázané šifrovací klíče, čímž snižuje frekvenci autentizace při zachování bezpečnosti. To bylo zvláště důležité pro paketové služby v UMTS, kde zařízení často přecházela mezi stavem idle a připojeným stavem.

CKSN dále řešil omezení v řízení životního cyklu klíčů tím, že poskytl mechanismus pro sledování verzí klíčů. Tím se zabraňuje opětovnému použití zastaralých nebo kompromitovaných klíčů a podporují se procedury obnovy klíčů. Při mezisystémových předáních spojení (např. mezi GSM a UMTS) CKSN usnadňuje plynulý přenos bezpečnostního kontextu, což zajišťuje nepřetržitou ochranu bez nutnosti zásahu uživatele. Návrh CKSN jako malého, efektivního identifikátoru odráží potřebu minimalizovat režii v rádiových zprávách při poskytování spolehlivého indexování klíčů napříč různými síťovými architekturami.

## Klíčové vlastnosti

- Identifikuje aktivní šifrovací klíč mezi UE a sítí
- Umožňuje synchronizaci klíčů bez přenosu klíčů vzduchem
- Podporuje plynulé zabezpečení během předání spojení a událostí mobility
- Snižuje signalizační režii autentizace umožněním opětovného použití klíčů
- Poskytuje zpětnou kompatibilitu při mezisystémových předáních spojení (inter-RAT handover)
- Integruje se s autentizačními vektory a NAS bezpečnostním kontextem

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [CKSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cksn/)
