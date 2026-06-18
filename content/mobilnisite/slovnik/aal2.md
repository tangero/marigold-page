---
slug: "aal2"
url: "/mobilnisite/slovnik/aal2/"
type: "slovnik"
title: "AAL2 – ATM Adaptation Layer type 2"
date: 2025-01-01
abbr: "AAL2"
fullName: "ATM Adaptation Layer type 2"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aal2/"
summary: "AAL2 je protokolová vrstva, která adaptuje provoz s proměnnou přenosovou rychlostí a citlivý na zpoždění (jako hlas a video) pro přenos přes síť Asynchronous Transfer Mode (ATM). Umožňuje efektivní mu"
---

AAL2 je protokol adaptační vrstvy ATM, který efektivně multiplexuje více nízkorychlostních, na zpoždění citlivých spojení (např. hlas) do jediného ATM virtuálního kanálového spojení (VCC) a optimalizuje tak přenosovou šířku pásma.

## Popis

[ATM](/mobilnisite/slovnik/atm/) Adaptation Layer type 2 (AAL2) je klíčový protokol definovaný [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatý 3GPP pro přenos provozu v reálném čase s proměnnou přenosovou rychlostí v raných verzích síťové architektury UMTS. Funguje jako podvrstva v rámci zásobníku protokolů ATM, umístěná mezi služebně specifické vyšší vrstvy (např. hlasové kodeky, signalizační protokoly) a jádrovou vrstvu ATM. Jejím hlavním úkolem je segmentovat a znovu skládat datové toky od více uživatelů nebo aplikací do pevně velkých buněk (53 bajtů) používaných ATM, při zachování časových vztahů a minimalizaci zpoždění způsobeného paketizací, což je zásadní pro konverzační služby.

Z architektonického hlediska se AAL2 dělí na dvě podvrstvy: Common Part Sublayer ([CPS](/mobilnisite/slovnik/cps/)) a Service Specific Convergence Sublayer ([SSCS](/mobilnisite/slovnik/sscs/)). CPS je jádrem a zodpovídá za multiplexování více AAL2 spojení, nazývaných Channel Identifiers ([CID](/mobilnisite/slovnik/cid/)), do jediného ATM virtuálního kanálového spojení ([VCC](/mobilnisite/slovnik/vcc/)). Toho dosahuje zabalováním proměnně dlouhých CPS-Paketů z různých zdrojů do 48bajtové užitečné zátěže ATM buněk. Každý CPS-Paket se skládá z 3bajtové hlavičky (obsahující CID, ukazatel délky a uživatelský indikátor) a užitečné zátěže o velikosti až 45 nebo 64 bajtů (v závislosti na režimu). Tento mechanismus balení, známý jako multiplexování minibuněk, umožňuje velmi nízké zpoždění, protože buňky mohou být odeslány dříve, než jsou zcela zaplněny (na rozdíl od [AAL1](/mobilnisite/slovnik/aal1/) nebo [AAL5](/mobilnisite/slovnik/aal5/)), což je vysoce efektivní pro sporadický nízkorychlostní provoz.

V kontextu 3GPP byla AAL2 specifikována jako primární přenos pro provoz uživatelské roviny (např. hlas AMR, okruhově přepínaná data) a signalizaci řídicí roviny přes kritická rozhraní v UTRAN. Konkrétně byla používána na rozhraní Iub mezi Node B a Radio Network Controllerem (RNC), na rozhraní Iur mezi RNC a na rozhraní Iu-CS mezi RNC a okruhově přepínanou doménou jádra sítě (MSC). Část SSCS AAL2 byla dále specializována pro tyto role; například Service Specific Connection Oriented Protocol (SSCOP) a Service Specific Coordination Function (SSCF) byly použity pro přenos signalizace, zatímco pro uživatelská data se často používala nulová SSCS nebo SSCS pro segmentaci a opětovné složení. Tento vrstvený přístup poskytoval spolehlivý, nízkolatenční kanál, který byl zásadní pro záruky kvality služeb (QoS) raných 3G služeb.

AAL2 funguje tak, že mezi síťovými prvky vytváří AAL2 spojení koncový bod – koncový bod. Když paket uživatelských dat (např. hlasový rámec) dorazí z vyšší vrstvy, vrstva AAL2 ve zdroji (např. Node B) jej zapouzdří do CPS-Paketu s konkrétním CID odpovídajícím nosiči daného uživatele. Následně je více takových CPS-Paketů z různých CID postupně zabaleno do užitečné zátěže ATM buňky. Buňka je přenesena, jakmile vyprší časovač nebo je užitečná zátěž téměř plná, což zajišťuje kompromis mezi zpožděním a efektivitou. Na přijímacím konci (např. RNC) CPS extrahuje CPS-Pakety na základě CID a ukazatele délky, znovu složí původní datové jednotky a doručí je správné entitě vyšší vrstvy. Tento proces, řízený signalizačním protokolem AAL2 (Q.2630.1/Q.2150.1 v 3GPP), umožňoval dynamické vytváření a uvolňování těchto nízkorychlostních kanálů, což dokonale odpovídalo procedurám sestavování a uvolňování hovorů v UMTS.

## K čemu slouží

AAL2 byla vytvořena, aby řešila specifický problém efektivního přenosu trhavého, nízkorychlostního a na zpoždění citlivého provozu přes ATM sítě, které byly dominantní vysokorychlostní páteřní technologií na přelomu 90. a 00. let. Předchozí přístupy jako AAL1 byly navrženy pro provoz s konstantní přenosovou rychlostí (např. emulace okruhu E1/T1) a pro hlas, který má období ticha, byly neefektivní, zatímco AAL5 byla optimalizována pro velké, trhavé datové pakety, ale zaváděla významné zpoždění způsobené paketizací, nevhodné pro komunikaci v reálném čase. Telekomunikační průmysl, směřující k integrovaným sítím, potřeboval metodu pro přenos komprimovaného hlasu (např. pomocí kodeků AMR) a dalších služeb v reálném čase bez plýtvání pevnou šířkou pásma ATM buněk.

V historickém kontextu 3GPP Release 99, které standardizovalo první sítě UMTS, bylo ATM vybráno jako přenosová technologie pro nový UTRAN díky své prověřené spolehlivosti, správě provozu a schopnostem QoS. Aby však bylo toto řešení životaschopné pro množství nízkorychlostních rádiových přístupových nosičů, byla vyžadována adaptační vrstva, která by mohla statisticky multiplexovat stovky hlasových hovorů na jediný ATM VCC při zachování přísných limitů zpoždění. AAL2 toto vyřešila tím, že umožnila částečné zaplňování buněk a prokládání paketů z více zdrojů, což dramaticky zlepšilo využití šířky pásma ve srovnání s vyčleněním plného VCC na každý hovor. Tato efektivita byla ekonomicky klíčová pro mobilní operátory zavádějící 3G infrastrukturu.

Primární motivací pro přijetí AAL2 v 3GPP tedy bylo umožnit nákladově efektivní, kvalitní přenos pro okruhově přepínané služby přes paketově orientované ATM jádro, čímž překlenula propast mezi požadavky tradiční telefonie a moderních paketově přepínaných páteřních sítí. Poskytla potřebné řízení provozu pro podporu tříd QoS definovaných pro UMTS, zejména konverzační a streamovací třídy, až do doby, kdy průmysl nakonec přešel na čistě IP přenos s technologiemi jako IP přes Ethernet v pozdějších verzích.

## Klíčové vlastnosti

- Statistické multiplexování více nízkorychlostních spojení (CID) do jediného ATM VCC
- Nízké zpoždění způsobené paketizací díky částečnému zaplnění buněk a časovačem řízenému přenosu
- Podpora proměnné velikosti užitečné zátěže (až 45/64 bajtů) na CPS-Paket
- 3bajtová hlavička na CPS-Paket obsahující identifikátor kanálu (CID) a délku
- Signalizace koncový bod – koncový bod (Q.2630.1) pro dynamické vytváření a správu spojení
- Schopnost segmentace a opětovného složení pro služební datové jednotky větší než užitečná zátěž CPS-Paketu

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [AAL2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/aal2/)
