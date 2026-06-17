---
slug: "imui"
url: "/mobilnisite/slovnik/imui/"
type: "slovnik"
title: "IMUI – International Mobile User Identity"
date: 2025-01-01
abbr: "IMUI"
fullName: "International Mobile User Identity"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/imui/"
summary: "International Mobile User Identity (IMUI) byl jedinečný identifikátor mobilního uživatele definovaný v raných vydáních 3GPP. Byl součástí rámce pro identifikaci uživatele, ale s vývojem systémů GSM/UM"
---

IMUI je jedinečný identifikátor mobilního uživatele, který byl definován v raných vydáních 3GPP, ale později byl nahrazen trvalejšími identifikátory, jako je IMSI.

## Popis

International Mobile User Identity (IMUI) byl koncept identifikace uživatele definovaný ve velmi raných fázích standardizace 3GPP, především v Release 4 a Release 5. Jak je podrobně popsáno ve specifikacích jako TS 21.111 a TS 21.133, měl IMUI být jedinečný identifikátor přiřazený mobilnímu účastníkovi. Jeho účelem bylo jednoznačně identifikovat uživatele v rámci globálního systému mobilní telekomunikace, odděleně od identity zařízení ([IMEI](/mobilnisite/slovnik/imei/)) nebo telefonního čísla účastníka ([MSISDN](/mobilnisite/slovnik/msisdn/)).

Z architektonického hlediska měl IMUI být datový prvek uložený v profilu účastníka v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo podobné databázi domácí sítě. Během procedur, jako je registrace (attach), aktualizace polohy nebo sestavení hovoru, mohla síť IMUI použít k načtení servisního profilu účastníka a k ověření jeho práva na přístup k síťovým službám. Byl součástí širší sady identifikátorů, která zahrnovala International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), Temporary Mobile Subscriber Identity (TMSI) a Mobile Station International [ISDN](/mobilnisite/slovnik/isdn/) Number (MSISDN). Přesný technický formát a kódovací pravidla pro IMUI byla definována, ale jeho praktické nasazení a použití bylo omezené.

Úloha IMUI v síti byla zásadně pro správu účastníků a mobilitu. Sloužil jako klíč pro vyhledávání v databázích jádra sítě. Nicméně IMSI, což je známější a trvale uložený identifikátor v modulu SIM (Subscriber Identity Module), efektivně plnil stejnou primární roli. IMSI se používá pro kritické procesy, jako je autentizace, kdy síť výzvou ověřuje účastníka pomocí tajných údajů spojených s IMSI. Překryv funkcí mezi IMUI a IMSI spolu s zavedeným globálním používáním IMSI v GSM a jeho následných sítích vedl k tomu, že IMUI nebyl široce přijat nebo implementován v komerčních sítích.

Z provozní perspektivy představoval IMUI raný pokus o standardizaci uživatelsky orientované identity. Ekosystém se však rychle sjednotil na IMSI jako na primárním, trvalém identifikátoru předplatného. IMUI byl nakonec ve vyšších vydáních 3GPP vyřazen z aktivního používání a jeho požadavky a definice se staly zastaralými. Jeho zmínka ve specifikacích nyní slouží především jako historický referenční bod ve vývoji identifikace mobilních účastníků.

## K čemu slouží

IMUI byl vytvořen, aby poskytl standardizovaný, mezinárodně jedinečný identifikátor pro mobilního uživatele, odlišný od identifikátoru zařízení nebo telefonního čísla. V počátcích GSM a přechodu na 3G (UMTS) byla potřeba jasně definovat všechny entity zapojené do mobilní komunikace: uživatele (účastníka), zařízení (mobilní stanici) a předplatné. IMUI měl řešit část této rovnice týkající se 'uživatele'.

Problém, který měl řešit, byla potenciální nejednoznačnost mezi různými identifikátory. [MSISDN](/mobilnisite/slovnik/msisdn/) (telefonní číslo) se mohlo změnit nebo být přeneseno. [IMEI](/mobilnisite/slovnik/imei/) identifikovalo zařízení, které mohlo být vyměněno nebo sdíleno. Uživatelsky orientovaná identita jako IMUI by teoreticky zůstala pro účastníka konstantní a poskytovala by stabilní klíč pro účtování, poskytování služeb a správu mobility napříč různými zařízeními a čísly. To bylo obzvláště relevantní s nástupem konceptů, jako je osobní mobilita (používání předplatného na jakémkoli zařízení) a přenositelnost čísel.

Nicméně [IMSI](/mobilnisite/slovnik/imsi/), které již bylo hluboce zakořeněno v architektuře GSM pro autentizaci (prostřednictvím Authentication Center - AuC) a ukládání dat účastníka (v HLR), se přirozeně rozšířilo, aby tuto roli identifikace uživatele plnilo. SIM karta, která ukládá IMSI, se stala synonymem pro uživatelovo předplatné. To učinilo zavedení samostatné, paralelní uživatelské identity (IMUI) nadbytečným a provozně složitým. Následně IMUI nikdy nebyl široce implementován a systém 3GPP se vyvíjel s použitím IMSI jako primárního trvalého identifikátoru účastníka, čímž se IMUI stal zastaralým.

## Klíčové vlastnosti

- Měl být jedinečný globální identifikátor pro mobilního účastníka
- Oddělený od identifikátoru zařízení (IMEI) a telefonního čísla (MSISDN)
- Uložený v databázi domácí sítě (např. HLR)
- Používaný pro identifikaci účastníka a načítání servisního profilu
- Definovaný v raných vydáních 3GPP (Rel-4, Rel-5)
- V praxi nahrazen identifikátorem IMSI

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TS 21.133** (Rel-5) — 3G Security Requirements

---

📖 **Anglický originál a plná specifikace:** [IMUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/imui/)
