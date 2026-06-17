---
slug: "g-msc"
url: "/mobilnisite/slovnik/g-msc/"
type: "slovnik"
title: "G-MSC – Gateway Mobile Switching Centre"
date: 2002-01-01
abbr: "G-MSC"
fullName: "Gateway Mobile Switching Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/g-msc/"
summary: "Prvek jádrové sítě v legacy systémech GSM a UMTS, který funguje jako brána mezi mobilní sítí a externími sítěmi s přepojováním okruhů, jako je PSTN. Zajišťuje směrování hovorů, správu mobility a inter"
---

G-MSC je brána jádrové sítě v GSM a UMTS, která propojuje mobilní síť s externími sítěmi s přepojováním okruhů, jako je PSTN, a zajišťuje směrování hovorů a interworking pro hlasové a SMS služby.

## Popis

Gateway Mobile Switching Centre (G-MSC) je klíčová komponenta v jádrové síti s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) systémů 2G GSM a 3G UMTS, jak je definováno ve specifikacích 3GPP, například 22.945 a 24.228. Slouží jako primární rozhraní mezi mobilní sítí a externími sítěmi s přepojováním okruhů, včetně veřejné telefonní sítě (PSTN) a sítí dalších mobilních operátorů. Funkčně je G-MSC odpovědný za směrování příchozích a odchozích hlasových hovorů a SMS zpráv, provádění analýzy čísel a správu interworking protokolů pro zajištění bezproblémové komunikace napříč heterogenními síťovými doménami. Funguje ve spolupráci s dalšími prvky CS jádra, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visitor Location Register (VLR), pro získání informací o poloze a profilu účastníka pro sestavení a doručení hovoru.

Architektonicky je G-MSC typicky implementován jako specializovaný [MSC](/mobilnisite/slovnik/msc/), který zahrnuje bránové schopnosti, ačkoli v některých nasazeních může být integrován se standardním MSC. Když dorazí příchozí hovor z externí sítě, G-MSC dotazuje HLR pomocí protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), aby získal aktuální obsluhující MSC nebo SGSN (pro GSM/UMTS) volaného účastníka. Na základě této informace směruje hovor na příslušný síťový uzel, čímž zajišťuje efektivní a přesné doručení. Pro odchozí hovory G-MSC komunikuje s externími sítěmi prostřednictvím standardizovaných signalizačních systémů, jako je Signaling System No. 7 (SS7), a zajišťuje překlad mezi mobilními specifickými protokoly a protokoly PSTN. Klíčové komponenty zahrnují funkci řízení hovoru, jednotku správy mobility a interworking funkci, které společně umožňují funkce jako přesměrování hovoru, roaming a nouzové služby.

Jak to funguje, zahrnuje vícekrokový proces: po přijetí hovoru G-MSC analyzuje volané číslo, iniciuje dotaz na HLR k lokalizaci účastníka a naváže spojení s přepojováním okruhů prostřednictvím obsluhujícího MSC. Také spravuje předávání mezi MSC během hovorů a podporuje doplňkové služby, jako je čekání na hovor nebo konferenční hovor. V širší síti hraje G-MSC klíčovou roli při umožnění globálního roamingu a interoperability, funguje jako most, který překládá mezi interní signalizací mobilní sítě a požadavky externí sítě. Ačkoli jeho význam poklesl s přechodem na plně IP sítě a přijetím IP Multimedia Subsystem (IMS) pro hlasové služby, G-MSC zůstává základním prvkem v legacy nasazeních a pro pochopení historických mobilních architektur.

## K čemu slouží

G-MSC byl vyvinut k řešení potřeby bezproblémového propojení mezi mobilními sítěmi a externími sítěmi s přepojováním okruhů, což byl klíčový požadavek v počátcích GSM a UMTS. Před jeho zavedením fungovaly mobilní sítě izolovaně a postrádaly standardizované mechanismy pro směrování hovorů do pevných sítí nebo k jiným mobilním operátorům, což omezovalo rozsah mobilní telefonie. G-MSC tento problém vyřešil poskytnutím specializované bránové funkce, která dokázala překládat mezi různými signalizačními protokoly, jako je [MAP](/mobilnisite/slovnik/map/) pro mobilní sítě a [ISUP](/mobilnisite/slovnik/isup/) pro PSTN, čímž umožnila globální hlasovou komunikaci a roamingové schopnosti.

Motivováno rychlou expanzí služeb GSM na konci 90. let, 3GPP standardizovalo G-MSC v Release 99 pro usnadnění interoperability a škálování mobilních sítí pro masové přijetí. Řešilo to omezení dřívějších přístupů, kde ad-hoc brány vedly k neefektivitě, vysokým nákladům a nespolehlivému doručování hovorů. Historicky se G-MSC vyvíjelo spolu s architekturou [MSC](/mobilnisite/slovnik/msc/), s vylepšeními v pozdějších vydáních, jako je Rel-4 a Rel-5, pro podporu rozdělených architektur MSC (oddělení serverových a bránových funkcí) a zlepšení kapacity pro rostoucí základnu účastníků. Jeho vytvoření bylo hnací silou nutnosti podporovat základní služby, jako jsou hlasové hovory a SMS, které byly v té době hlavním generátorem příjmů operátorů.

Dále G-MSC umožnilo klíčové funkce, jako je přenositelnost čísel a zákonné odposlechy, centralizací bránových funkcí. Jak sítě přecházely na IP technologie, jako je IMS a VoLTE, byla role G-MSC z velké části nahrazena prvky jako [MGCF](/mobilnisite/slovnik/mgcf/) (Media Gateway Control Function) a SBC (Session Border Controllers). Jeho odkaz však přetrvává v pochopení vývoje jádrových mobilních sítí a základních principů interworkingu, které jsou základem moderních telekomunikačních systémů.

## Klíčové vlastnosti

- Funguje jako brána mezi mobilní CS sítí a externími sítěmi, jako je PSTN
- Směruje příchozí a odchozí hlasové hovory a SMS zprávy pomocí dotazů na HLR
- Podporuje interworking protokoly, jako jsou MAP, SS7 a ISUP, pro signalizační překlad
- Umožňuje globální roaming rozhraním se sítěmi jiných operátorů
- Spravuje sestavení, ukončení a předávání hovorů během událostí mobility
- Poskytuje doplňkové služby včetně přesměrování hovoru a zpracování nouzových hovorů

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows

---

📖 **Anglický originál a plná specifikace:** [G-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-msc/)
