---
slug: "cap"
url: "/mobilnisite/slovnik/cap/"
type: "slovnik"
title: "CAP – CAMEL Application Part"
date: 2026-01-01
abbr: "CAP"
fullName: "CAMEL Application Part"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cap/"
summary: "CAP je signalizační protokol používaný v CAMEL (Customized Applications for Mobile networks Enhanced Logic) k zajištění inteligentního řízení služeb v reálném čase v mobilních sítích. Propojuje síťové"
---

CAP je signalizační protokol CAMEL Application Part, který propojuje síťové prvky jako SSF s externími platformami, aby umožnil inteligentní řízení služeb v reálném čase, například pokročilé předplacené služby.

## Popis

[CAMEL](/mobilnisite/slovnik/camel/) Application Part (CAP) je protokol založený na Transaction Capabilities Application Part (TCAP), definovaný ve standardech 3GPP, který usnadňuje komunikaci mezi síťovými prvky zapojenými do architektury služeb CAMEL. CAMEL umožňuje poskytování operátorově specifických, inteligentních síťových ([IN](/mobilnisite/slovnik/in/)) služeb napříč domácími i navštívenými sítěmi, nezávisle na výrobci zařízení. CAP funguje nad signalizačními sítěmi SS7 (Signaling System No. 7) nebo SIGTRAN (Signaling Transport) a využívá vrstvu TCAP pro správu spojovaného i nespojovaného dialogu. Jeho hlavní rolí je přenášet instrukce služební logiky a oznámení o událostech mezi Service Switching Function (SSF), která je typicky integrována v [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Center) nebo SGSN (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node), a Service Control Point (SCP) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). To umožňuje řízení zpracování hovorů a relací v reálném čase na základě profilů účastníků a služební logiky.

Architektonicky CAP definuje sadu operací a souvisejících parametrů, které modelují detekční body (DPs) v modelu stavu hovoru nebo relace, jako je Basic Call State Model ([BCSM](/mobilnisite/slovnik/bcsm/)). Když je v SSF splněna spouštěcí podmínka (např. navázání hovoru, odpověď, ukončení) na detekčním bodě ([DP](/mobilnisite/slovnik/dp/)), SSF pozastaví zpracování hovoru a vytvoří CAP operaci, například InitialDP, aby nahlásila událost SCP. SCP, který hostí služební logiku CAMEL, pak žádost analyzuje, aplikuje obchodní pravidla (např. kontrolu stavu předplaceného kreditu, překlad čísla) a vrátí CAP instrukce, jako jsou ApplyCharging, Connect nebo Continue, aby naváděly SSF v dalším postupu s hovorem nebo datovou relací. Tato interakce umožňuje komplexní, stavové řízení služeb bez nutnosti úprav základního přepínacího zařízení.

Klíčovými komponentami v CAP dialogu jsou gsmSCF (GSM Service Control Function), což je SCP implementující služební logiku CAMEL; gsmSSF (GSM Service Switching Function), integrované v MSC nebo [GMSC](/mobilnisite/slovnik/gmsc/); a pro paketové služby gprsSSF v SGSN. Zprávy CAP jsou kódovány pomocí ASN.1 (Abstract Syntax Notation One) a dodržují specifické procedury pro různé fáze hovoru nebo relace, čímž zajišťují interoperabilitu mezi různými síťovými prvky a výrobci. Protokol podporuje různé fáze, jako je navázání hovoru, fáze během hovoru a uvolnění hovoru, což umožňuje služby jako předplacené účtování, kontrola podvodů, vlastní směrování a služby VPN (Virtual Private Network). Jeho návrh zajišťuje, že služební logika je centralizována v SCP, což podporuje rychlé nasazení služeb a konzistentní uživatelský zážitek napříč hranicemi sítí.

V moderních sítích, zejména s vývojem směrem k 3G, 4G LTE a 5G, byl CAP adaptován pro práci s IP signalizací přes SIGTRAN, což zajišťuje pokračující podporu starších CAMEL služeb při integraci s IMS (IP Multimedia Subsystem) a VoLTE (Voice over LTE). Například v sítích 4G/5G se CAP používá mezi MME (Mobility Management Entity) nebo SMF (Session Management Function) fungujícími jako SSF a OCS pro online účtování, což demonstruje jeho trvalou roli v řízení služeb a účtování v reálném čase.

## K čemu slouží

CAP byl vytvořen, aby řešil omezení tradičního, na přepínačích založeného poskytování služeb v sítích GSM a UMTS, které bylo nepružné a vyžadovalo dlouhé, výrobci specifické vývojové cykly pro nové služby. Před CAMEL a CAP byly pokročilé služby jako předplacené hovory, bezplatná čísla nebo virtuální privátní sítě implementovány pomocí proprietárních řešení IN, která často postrádala interoperabilitu mezi různými síťovými operátory nebo při roamingu účastníků. To brzdilo rychlé zavádění konkurenceschopných, nadstandardních služeb. Rámec CAMEL s CAP jako svým signalizačním protokolem standardizoval rozhraní mezi přepínací funkcí a řídicí logikou služeb, což operátorům umožnilo nasazovat služby inteligentních sítí konzistentně napříč vícevýrobcovým prostředím a podporovat bezproblémové poskytování služeb při roamingu účastníků v navštívených sítích.

Primární problém, který CAP řeší, je umožnění řízení hovorů a relací v reálném čase, řízeného událostmi, externími aplikačními servery. To je klíčové pro služby jako předplacené účtování, kde síť musí v reálném čase zkontrolovat stav účtu účastníka před povolením hovoru a následně během hovoru odečítat kredit. Bez CAP by takové služby vyžadovaly hlubokou integraci do každého přepínače, což by je učinilo nákladnými a pomalými na aktualizace. CAP poskytuje standardizovanou, abstraktní signalizační metodu, která umožňuje, aby služební logika sídlila v centralizovaných platformách SCP nebo OCS, a odděluje tak tvorbu služeb od síťové infrastruktury. Toto oddělení urychluje inovace služeb, snižuje provozní náklady a zajišťuje, že účastníci mají stejné služby bez ohledu na svou polohu nebo podkladovou síťovou technologii.

Historicky byl CAP představen v 3GPP Release 99 jako součást specifikací CAMEL Phase 3, navazujících na dřívější fáze (CAMEL Phase 1 a 2 definované ve standardech GSM), aby podpořil složitější služby a další síťové prvky, jako je síť GPRS. Řešil rostoucí poptávku po sofistikovaných předplacených a datových službách s expanzí mobilního využití. V následujících vydáních se CAP vyvíjel, aby podporoval nové síťové architektury, jako jsou IMS a LTE, čímž zajišťoval zpětnou kompatibilitu a zároveň rozšiřoval své schopnosti pro zpracování IP relací a spolupráci s účtovacími systémy založenými na Diameter. Jeho pokračující relevance podtrhuje jeho účinnost při řešení základní potřeby flexibilního řízení služeb v telekomunikacích v reálném čase.

## Klíčové vlastnosti

- Standardizovaná signalizace pro řízení CAMEL služeb mezi SSF a SCP/OCS
- Podporuje interakce v reálném čase řízené událostmi pro správu hovorů a relací
- Umožňuje předplacené účtování, kontrolu podvodů a služby vlastního směrování
- Využívá TCAP přes SS7 nebo SIGTRAN pro spolehlivý přenos zpráv
- Definuje operace jako InitialDP, ApplyCharging, Connect a Continue
- Spolupracuje s účtováním založeným na Diameter v sítích 4G/5G

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [CAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cap/)
