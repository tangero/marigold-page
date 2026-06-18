---
slug: "vhe"
url: "/mobilnisite/slovnik/vhe/"
type: "slovnik"
title: "VHE – Virtual Home Environment"
date: 2026-01-01
abbr: "VHE"
fullName: "Virtual Home Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vhe/"
summary: "Koncept servisní architektury umožňující mobilním uživatelům konzistentní přístup k personalizovaným službám a nastavením uživatelského rozhraní bez ohledu na jejich polohu nebo koncové zařízení. Umož"
---

VHE je koncept servisní architektury umožňující mobilním uživatelům konzistentní přístup k jejich personalizovaným službám a nastavením rozhraní, jako by byli ve své domovské síti, bez ohledu na jejich polohu nebo koncové zařízení.

## Popis

Virtual Home Environment (VHE) je komplexní servisní rámec definovaný v 3GPP, jehož cílem je poskytnout uživatelům konzistentní soubor služeb, personalizovaných funkcí a charakteristik uživatelského rozhraní, jako by byli ve své domovské síti, bez ohledu na jejich fyzickou polohu nebo používané koncové zařízení. Koncept je založen na myšlence přenositelnosti a personalizace služeb, které jsou klíčové pro zlepšení uživatelského zážitku v mobilních komunikacích. VHE není jediný síťový prvek, ale spíše architektonický koncept a soubor schopností distribuovaných po síti, včetně domovské sítě, navštívených sítí a uživatelského zařízení (UE). Spoléhá na standardizovaná rozhraní a servisní schopnosti, aby zajistil, že servisní logika a uživatelské preference mohou být přeneseny a provedeny v navštívených sítích, což umožňuje bezproblémový zážitek podobný tomu v domácím prostředí.

Architektonicky VHE zahrnuje několik klíčových komponent a mechanismů. Domovské prostředí ([HE](/mobilnisite/slovnik/he/)) je zodpovědné za ukládání servisního profilu uživatele, který zahrnuje preference, odebírané služby a nastavení uživatelského rozhraní. K tomuto profilu přistupuje navštívená síť (VN), když uživatel roamuje. Koncept VHE využívá schopnosti Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a Customized Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) pro řízení služeb, stejně jako Open Service Architecture ([OSA](/mobilnisite/slovnik/osa/)) a Service Capability Server ([SCS](/mobilnisite/slovnik/scs/)) pro vystavení a provádění služeb. Provádění služeb VHE v navštívené síti vyžaduje podporu servisních zprostředkovatelů, kteří zprostředkovávají komunikaci mezi domovskou a navštívenou sítí, aby zajistili správnou interpretaci a aplikaci servisní logiky s ohledem na schopnosti navštívené sítě a koncového zařízení.

Provoz VHE zahrnuje dynamickou adaptaci služeb na základě kontextu uživatele, který zahrnuje polohu, schopnosti koncového zařízení a síťové podmínky. Když uživatel roamuje do navštívené sítě, systém VHE načte servisní profil uživatele z domovské sítě. Tento profil je pak použit ke konfiguraci služeb dostupných v navštívené síti tak, aby co nejvíce odpovídaly domácímu prostředí uživatele. To může zahrnovat přizpůsobení uživatelského rozhraní, povolení specifických servisních funkcí nebo dokonce stažení potřebných aplikací nebo dat. Rámec VHE podporuje různé typy služeb, včetně hlasových, datových a multimediálních služeb, a je navržen jako rozšiřitelný, aby pojal nové služby, jak vznikají. Role VHE v síti je překlenout propast mezi různými síťovými operátory a technologiemi, poskytnout jednotný servisní zážitek, který podporuje uživatelskou loajalitu a umožňuje inovativní nabídky služeb.

## K čemu slouží

Virtual Home Environment byl vytvořen, aby řešil výzvy přenositelnosti a personalizace služeb v mobilních sítích, zejména v kontextu roamingu. Před VHE, když se uživatelé přesouvali mezi různými sítěmi, zejména při mezinárodním roamingu, často čelili fragmentovanému zážitku, kdy služby dostupné v jejich domovské síti nebyly přístupné nebo se uživatelské rozhraní a chování služeb výrazně lišilo. Toto omezení bránilo adopci pokročilých mobilních služeb a snižovalo spokojenost uživatelů. Primární motivací pro VHE bylo umožnit poskytovatelům služeb nabízet konzistentní a personalizovaný servisní zážitek napříč síťovými hranicemi, čímž se zvýšila hodnotová nabídka mobilních služeb a podpořila se uživatelská mobilita.

Historicky se vývoj VHE začal v 3GPP Release 99, v souladu se zavedením sítí 3G a rostoucím důrazem na datové služby a multimediální aplikace. Koncept byl hnán potřebou podporovat inovativní služby vyžadující vysoký stupeň personalizace a kontextového povědomí, jako jsou služby založené na poloze, multimediální zprávy a mobilní obchod. VHE si kladl za cíl využít schopnosti inteligentních sítí a architektur otevřených služeb k oddělení servisní logiky od síťové infrastruktury, což umožnilo provádět služby v různých síťových prostředích. Tento přístup řešil omezení dřívějších systémů, kde byly služby těsně svázány se specifickými síťovými prvky nebo operátory, což ztěžovalo jejich přenos nebo adaptaci.

Dále byl VHE navržen k řešení problému interoperability služeb mezi různými operátory a technologiemi. Standardizací mechanismů pro správu servisních profilů, provádění služeb a adaptaci uživatelského rozhraní VHE usnadnil spolupráci mezi domovskými a navštívenými sítěmi, což jim umožnilo nabízet bezproblémový zážitek roamujícím uživatelům. To nejen zlepšilo uživatelský komfort, ale také otevřelo nové obchodní příležitosti pro operátory tím, že jim umožnilo nabízet přidané služby navštěvujícím účastníkům. Vývoj VHE v následujících vydáních 3GPP odráží jeho adaptaci na nové síťové architektury, jako je IP Multimedia Subsystem (IMS), a jeho integraci s nově vznikajícími servisními paradigmaty, což zajišťuje jeho relevanci v kontextu sítí 4G a 5G.

## Klíčové vlastnosti

- Přenositelnost služeb napříč různými sítěmi a operátory
- Adaptace personalizovaného uživatelského rozhraní a nastavení služeb
- Dynamické provádění služeb na základě kontextu uživatele a schopností koncového zařízení
- Integrace s Inteligentní sítí (IN) a CAMEL pro řízení služeb
- Podpora architektur otevřených služeb, jako je OSA, pro vystavení služeb
- Správa profilů pro ukládání a načítání uživatelských servisních preferencí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [OSA – Open Services Architecture](/mobilnisite/slovnik/osa/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.141** (Rel-19) — Presence Service Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.970** (Rel-4) — Virtual Home Environment (VHE) Concept and Requirements
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [VHE na 3GPP Explorer](https://3gpp-explorer.com/glossary/vhe/)
