---
slug: "jvm"
url: "/mobilnisite/slovnik/jvm/"
type: "slovnik"
title: "JVM – Java™ Virtual Machine"
date: 2025-01-01
abbr: "JVM"
fullName: "Java™ Virtual Machine"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jvm/"
summary: "Běhové prostředí, které vykonává bajtkód Javy a umožňuje nasazení aplikací nezávislé na platformě. Ve 3GPP je specifikováno pro prostředí mobilní stanice (UE) za účelem umožnění bezpečné, stahovatelné"
---

JVM (Java™ Virtual Machine, virtuální stroj Javy) je běhové prostředí, které vykonává bajtkód Javy a umožňuje nasazení aplikací nezávislé na platformě v mobilních stanicích (Mobile Stations). Tvoří základ pro bezpečné, stahovatelné služby jako MIDP ve standardech 3GPP.

## Popis

Java Virtual Machine (JVM, virtuální stroj Javy) je abstraktní výpočetní stroj s instrukční sadou a běhovým stavem definovaným specifikací Java Virtual Machine. Ve standardech 3GPP je JVM specifikována zejména pro Mobile Execution Environment (MExE) a (U)SIM Application Toolkit (USAT/STK). Poskytuje zabezpečené, izolované běhové prostředí (sandbox) na uživatelském zařízení (UE), ve kterém mohou být vykonávány aplikace v Javě, často ve formě MIDletů (pro [MIDP](/mobilnisite/slovnik/midp/)) nebo apletu (pro SIM Toolkit). Architektura zahrnuje interpretaci nebo just-in-time (JIT) kompilaci nezávislého bajtkódu Javy do nativních instrukcí procesoru zařízení pomocí JVM. Správu paměti zajišťuje automaticky pomocí garbage collection a vynucuje zabezpečení prostřednictvím sandbox modelu, který omezuje přístup aplikací k citlivým prostředkům zařízení, pokud nejsou výslovně udělena oprávnění.

Jak to funguje v kontextu UE 3GPP: začíná na hardwaru a operačním systému zařízení. Implementace JVM, přizpůsobená omezeným prostředkům mobilního zařízení, je buď předinstalovaná, nebo stahovatelná. Aplikace v Javě jsou doručovány přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)) jako soubory Java Archive (JAR) obsahující bajtkód a Java Application Descriptor ([JAD](/mobilnisite/slovnik/jad/)). JVM bajtkód načte, ověří jeho bezpečnost a integritu, aby zabránila škodlivému kódu, a poté jej vykoná ve svém řízeném prostředí. Mezi klíčové komponenty patří Class Loader, který načítá bajtkód; Bytecode Verifier; Execution Engine (interpret/JIT kompilátor); a Runtime Data Areas (např. halda, oblast metod a zásobníky Javy pro každé vlákno). Pro USAT běží specifická JVM na samotné kartě UICC, což umožňuje apletům na SIM komunikovat s [ME](/mobilnisite/slovnik/me/) (Mobile Equipment) prostřednictvím proaktivních příkazů.

Její role v síti je jako prostředek pro stahovatelné, přidané služby a bezpečné vykonávání aplikací. Umožňuje síťovým operátorům a vývojářům třetích stran vytvářet služby, které lze dynamicky nasadit na širokou škálu telefonů bez nutnosti portování kódu pro každou konkrétní hardwarovou platformu. Toto bylo základem pro ekosystém mobilních aplikací předcházející moderním OS chytrých telefonů. Specifikace 3GPP (např. TS 23.057 pro MExE, TS 51.013 pro USAT) standardizují požadavky na JVM, bezpečnostní modely a [API](/mobilnisite/slovnik/api/) (jako profily [CLDC](/mobilnisite/slovnik/cldc/) a MIDP), aby zajistily interoperabilitu napříč zařízeními od různých výrobců a garantovaly, že certifikovaná služba v Javě bude správně fungovat na jakémkoli kompatibilním telefonu.

## K čemu slouží

JVM byla začleněna do standardů 3GPP, aby vyřešila problém přenositelnosti služeb a bezpečného vykonávání v heterogenním prostředí mobilních zařízení. Koncem 90. a počátkem 2000. let měly mobilní telefony proprietární, fragmentované operační systémy, což extrémně ztěžovalo vytvoření aplikace schopné běžet na více než jednom modelu nebo značce. To dusilo inovace v mobilních datových službách. Účelem bylo vytvořit standardizované, bezpečné prostředí, kde by se servisní logika dala napsat jednou v Javě a běžela kdekoliv – klíčový princip Javy – a tím umožnit živý trh se stahovatelnými hrami, utility a službami specifickými pro operátora.

Historicky, před standardizovanými běhovými prostředími jako JVM v MExE, vyžadovala jakákoli nová servisní funkce hlubokou integraci s firmware telefonu, což vedlo k dlouhým vývojovým cyklům a omezené dostupnosti služeb. JVM spolu s profily jako Mobile Information Device Profile ([MIDP](/mobilnisite/slovnik/midp/)) poskytovala řízený sandbox, který řešil kritické obavy síťových operátorů: zabezpečení (zabránění poškození sítě nebo zařízení škodlivým kódem), správu prostředků (zvládnutí omezené paměti a [CPU](/mobilnisite/slovnik/cpu/)) a interoperabilitu. Pro SIM Toolkit umožnila JVM na UICC, aby SIM karta hostovala aplikace, které mohou ovládat rozhraní telefonu, a tím umožnila služby jako bankovnictví přes menu, dobíjení kreditu a informační služby bez nutnosti úprav telefonu. To dávalo operátorům možnost nasazovat služby přímo na SIM kartu účastníka.

## Klíčové vlastnosti

- Nezávislé vykonávání bajtkódu Javy na platformě
- Automatická správa paměti a garbage collection
- Zabezpečený sandbox model vykonávání s verifikací bajtkódu
- Podpora pro over-the-air (OTA) provizionování aplikací
- Standardizovaná API pro mobilní zařízení (např. CLDC, MIDP)
- Umožňuje vykonávání apletů SIM Toolkit na UICC

## Související pojmy

- [MIDP – Mobile Information Device Profile](/mobilnisite/slovnik/midp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [JVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/jvm/)
