---
slug: "ksi"
url: "/mobilnisite/slovnik/ksi/"
type: "slovnik"
title: "KSI – Key Set Identifier"
date: 2026-01-01
abbr: "KSI"
fullName: "Key Set Identifier"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ksi/"
summary: "Identifikátor sady klíčů (KSI) je bezpečnostní parametr používaný v systémech 3GPP k jednoznačné identifikaci konkrétní sady kryptografických klíčů sdílených mezi uživatelským zařízením (UE) a sítí. J"
---

KSI je bezpečnostní parametr používaný v systémech 3GPP k jednoznačné identifikaci konkrétní sady kryptografických klíčů sdílených mezi uživatelským zařízením a sítí pro šifrování a ochranu integrity.

## Popis

Identifikátor sady klíčů (KSI) je základní bezpečnostní identifikátor v rámci rámce 3GPP pro autentizaci a dohodu o klíčích ([AKA](/mobilnisite/slovnik/aka/)). Funguje jako krátký a efektivní odkaz na kompletní sadu odvozených kryptografických klíčů, které existují jak v uživatelském zařízení (UE), tak v bezpečnostním kontextu sítě. Primárními klíči, které identifikuje, jsou šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) a integritní klíč ([IK](/mobilnisite/slovnik/ik/)), které jsou vygenerovány během procedury AKA. V pozdějších verzích (např. pro 5G) odkazuje také na kotvící klíč (K_[AMF](/mobilnisite/slovnik/amf/)) a z něj odvozené klíče.

Technicky je KSI malá hodnota (např. 3 bity v UMTS/LTE, část většího identifikátoru v 5G), kterou síť přiřadí při úspěšné autentizaci. Síť ukládá celou sadu klíčů (CK, IK a pořadové číslo SQN) ve své databázi bezpečnostních kontextů, indexovanou pomocí KSI a trvalé identity uživatele (jako [IMSI](/mobilnisite/slovnik/imsi/) nebo SUPI). UE ukládá stejnou sadu klíčů lokálně, také asociovanou s KSI. Když je následně zahájena komunikace chráněná zabezpečením (např. při žádosti o službu nebo aktualizaci polohy), může síť zahrnout KSI do signalizační zprávy (jako [RRC](/mobilnisite/slovnik/rrc/) Connection Reconfiguration nebo [NAS](/mobilnisite/slovnik/nas/) Security Mode Command) namísto odesílání celých klíčů. UE použije přijatý KSI k vyhledání odpovídajících lokálně uložených klíčů CK a IK, které jsou pak použity k inicializaci algoritmů pro šifrování a ochranu integrity (např. SNOW 3G, [AES](/mobilnisite/slovnik/aes/), ZUC).

Existují různé typy KSI pro správu klíčových kontextů pro různé domény sítě. V UMTS a LTE se používá KSI_ASME (kde ASME je Access Security Management Entity) pro kontext zabezpečení EPS. Síť může také udržovat samostatné KSI pro šifrování (KSI_C) a integritu (KSI_I) v některých starších kontextech. Mechanismus KSI umožňuje efektivní správu klíčů tím, že se vyhne potřebě znovu spouštět plnou, výpočetně náročnou proceduru AKA pro každé navázání spojení. Podporuje přenos bezpečnostního kontextu mezi síťovými uzly (např. při předávání spojení) a umožňuje opakované použití navázaných bezpečnostních kontextů po určitou dobu, čímž zlepšuje efektivitu signalizace a doby navazování spojení při zachování robustního zabezpečení.

## K čemu slouží

Identifikátor sady klíčů byl vytvořen k řešení problému efektivního a bezpečného odkazování na klíče v mobilních sítích. Bez takového identifikátoru by síť musela buď opakovaně provádět plnou autentizaci (což zvyšuje latenci a signalizační zátěž), nebo nějakým způsobem přenášet nebo vyjednávat, kterou sadu klíčů použít, a to nezabezpečeným způsobem. KSI poskytuje bezpečnou zkratku.

Jeho primárním účelem je umožnit opakované použití navázaných bezpečnostních kontextů. Po počáteční autentizaci je navázán bezpečnostní kontext obsahující čerstvé kryptografické klíče. KSI umožňuje na tento kontext odkazovat a znovu jej aktivovat pro následná spojení bez opakování plné autentizace, což výrazně urychluje procedury jako přechody z klidového stavu do aktivního nebo předávání spojení. To je klíčové pro uživatelský zážitek, zejména u služeb vyžadujících časté, krátké přenosy.

Historicky se tento koncept vyvinul z čísla posloupnosti klíčů (Key Sequence Number) v GSM, ale byl výrazně vylepšen pro 3G UMTS, aby poskytl silnější zabezpečení v rámci nového protokolu AKA. V GSM bylo zabezpečení slabší a správa klíčů méně sofistikovaná. Zavedení vzájemné autentizace a silnějších algoritmů v 3G si vyžádalo robustnější hierarchii a systém správy klíčů, jehož je KSI klíčovou součástí. Řeší omezení spočívající v absenci bezpečného, dohodnutého odkazu na předem sdílený klíčový materiál, což je nezbytné pro výkon a škálovatelnost zabezpečené mobilní komunikace. V 5G jeho role pokračuje v rámci nových protokolů 5G AKA a EAP-AKA', což zajišťuje zpětnou kompatibilitu a efektivní správu bezpečnostních kontextů v komplexnějším prostředí síťového řezání (network slicing).

## Klíčové vlastnosti

- Jedinečný odkaz na klíče: Jednoznačně identifikuje konkrétní sadu kryptografických klíčů (CK, IK) jak v UE, tak v síti.
- Efektivita signalizace: Umožňuje bezpečnou reaktivaci bezpečnostního kontextu přenosem krátkého identifikátoru namísto plných klíčů nebo opětovné autentizace.
- Oddělení domén: Různé typy KSI (např. KSI_ASME) mohou identifikovat sady klíčů pro různé síťové domény (CS, PS, EPS).
- Podpora předávání spojení: Umožňuje zdrojovému síťovému uzlu informovat cílový uzel o bezpečnostním kontextu UE pomocí KSI, což usnadňuje bezpečný přenos kontextu.
- Ochrana integrity: Samotný KSI je při signalizaci často chráněn integritou, aby se zabránilo manipulaci a chybnému přiřazení kontextu.
- Zpětná kompatibilita: Koncept a struktura se vyvíjely, ale zachovaly kontinuitu od UMTS přes LTE až po bezpečnostní architektury 5G.

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [CK – Confidentiality Key](/mobilnisite/slovnik/ck/)
- [IK – Integrity Key](/mobilnisite/slovnik/ik/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [KSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ksi/)
