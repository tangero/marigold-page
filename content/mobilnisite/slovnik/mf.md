---
slug: "mf"
url: "/mobilnisite/slovnik/mf/"
type: "slovnik"
title: "MF – Mediation Function"
date: 2026-01-01
abbr: "MF"
fullName: "Mediation Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mf/"
summary: "Mediation Function (MF – funkce zprostředkování) je klíčová komponenta architektury 3GPP Telecommunication Management Network (TMN). Funguje jako zprostředkovatel, který sbírá, zpracovává a předává da"
---

MF (Mediation Function – funkce zprostředkování) je klíčová komponenta TMN, která funguje jako zprostředkovatel pro sběr, zpracování a předávání dat o výkonu a účtování od síťových prvků (Network Elements) k systémům OSS a standardizuje formáty pro interoperabilitu.

## Popis

Mediation Function (MF – funkce zprostředkování) je základní architektonický prvek v rámci 3GPP Telecommunication Management Network ([TMN](/mobilnisite/slovnik/tmn/)), definovaný v řadě specifikací včetně řady 32 pro management. Nachází se ve zprostředkovatelské vrstvě (mediation layer) logické hierarchie TMN, mezi vrstvou síťových prvků ([NE](/mobilnisite/slovnik/ne/) layer) a vrstvami Network Management ([NM](/mobilnisite/slovnik/nm/)) nebo Service Management. Její primární role spočívá v tom, že funguje jako zprostředkovatel a procesor managementových informací, konkrétně se zaměřuje na data performance management ([PM](/mobilnisite/slovnik/pm/)) a záznamy o účtování (CDRs). MF sbírá nezpracovaná data z heterogenních síťových prvků – jako jsou základnové stanice, [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/) a [MME](/mobilnisite/slovnik/mme/) – které mohou používat různé proprietární protokoly a datové formáty.

Operačně MF provádí několik klíčových transformací. Za prvé provádí adaptaci protokolů, převádí data z dodavatelsky specifických protokolů pro správu prvků (jako varianty [SNMP](/mobilnisite/slovnik/snmp/) nebo proprietární rozhraní) na standardizované protokoly používané systémy OSS vyšších vrstev, jako jsou CORBA, FTP, nebo v poslední době webové služby. Za druhé provádí datové zprostředkování (data mediation), které zahrnuje filtrování, agregaci, korelaci a formátování. U dat o výkonu to může zahrnovat výpočet 15minutových nebo hodinových průměrů ze snímků čítačů nebo korelaci dat z více NE pro vytvoření pohledu na úrovni služby. U účtovacích dat shromažďuje CDR od přepojovacích prvků, provádí jejich validaci a sestavuje je do formátovaných souborů pro přenos do Billing System. Kritickou funkcí je standardizace dat podle informačních modelů definovaných 3GPP, což zajišťuje, že OSS přijímá konzistentní a interpretovatelné informace bez ohledu na dodavatele podkladového zařízení.

MF je klíčovým prvkem pro více-dodavatelská síťová prostředí. Tím, že izoluje aplikace OSS od složitostí a variabilit jednotlivých síťových prvků, snižuje integrační náklady a zjednodušuje síťové operace. Architektonicky může být implementována jako samostatný fyzický uzel, virtualizovaná funkce nebo integrovaná v rámci Element Management System (EMS). Její nasazení je klíčové pro škálovatelný síťový management, neboť odlehčuje úlohy zpracování dat jak od omezených síťových prvků (NEs), tak od obchodně orientovaných systémů OSS. V moderních sítích jsou principy MF vtěleny do platforem pro sběr a zprostředkování dat, které zpracovávají obrovské proudy dat ze síťových funkcí 4G a 5G, často téměř v reálném čase, pro podporu pokročilých analýz, automatizovaného zajištění služeb a účtování.

## K čemu slouží

Mediation Function (MF – funkce zprostředkování) byla vytvořena, aby řešila základní výzvu v managementu telekomunikačních sítí: heterogenitu síťového vybavení. V raných digitálních sítích bylo vybavení každého dodavatele dodáváno s vlastním managementovým rozhraním, datovými modely a protokoly. To vytvářelo obrovskou složitost pro síťové operátory, kteří nasazovali více-dodavatelské sítě, protože jejich centrální systémy Operations Support Systems (OSS) potřebovaly vlastní adaptéry pro každý typ síťového prvku. To bylo nákladné, pomalé na integraci a bránilo jednotnému přehledu o síti a automatizovaným procesům.

MF jako součást standardizované architektury TMN byla vytvořena, aby tento problém interoperability vyřešila. Zavádí jasné oddělení odpovědností umístěním normalizační vrstvy mezi síťovou a managementovou vrstvu. Jejím účelem je absorbovat variabilitu vrstvy síťových prvků a prezentovat jednotné, standardizované rozhraní pro OSS. Tím řeší problémy vysokých integračních nákladů, dlouhých cyklů nasazování nových síťových prvků a nemožnosti získat konsolidovaný, na dodavateli nezávislý pohled na výkon a využití sítě. Historicky byla nezbytná pro zavedení systémů pro správu výkonu a účtování, které mohly fungovat napříč GSM, UMTS a pozdějšími generacemi. Podnítila vytvoření standardizovaných informačních modelů (jako jsou ty v řadě 32.3xx) a formátů souborů (jako formát souborů Performance Measurement (PM) v 32.432), které MF implementuje, čímž chrání investice do OSS do budoucna.

## Klíčové vlastnosti

- Adaptace protokolů mezi dodavatelsky specifickými rozhraními NE a standardizovanými rozhraními OSS
- Filtrování, agregace a korelace dat o výkonu a účtování
- Převod formátu na standardizované 3GPP formáty PM souborů a CDR souborů
- Časová agregace (např. převod 5minutových čítačů na hodinové reporty)
- Vyrovnávací paměť (buffering) a spolehlivý přenos managementových dat do nadřazených systémů
- Podpora více-dodavatelských síťových prostředí prostřednictvím normalizace

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.930** (Rel-19) — WebRTC Enhancements for Immersive RTC over 5G
- **TS 29.175** (Rel-19) — IMS AS Service-Based Interface Protocol
- **TS 29.176** (Rel-19) — Nmf Service Based Interface for Media Function
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [MF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mf/)
