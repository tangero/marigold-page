---
slug: "csp"
url: "/mobilnisite/slovnik/csp/"
type: "slovnik"
title: "CSP – Communications Service Provider"
date: 2026-01-01
abbr: "CSP"
fullName: "Communications Service Provider"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/csp/"
summary: "Communications Service Provider (CSP) je v 3GPP definovaná entita, která poskytuje komunikační služby koncovým uživatelům; zahrnuje mobilní operátory, pevné operátory a konvergované operátory. Předsta"
---

CSP (Communications Service Provider) je v 3GPP definovaná obchodní entita, například mobilní nebo pevný operátor, která nabízí komunikační služby, spravuje vztahy se zákazníky a provozuje síť pro poskytování služeb.

## Popis

Ve specifikacích 3GPP je Communications Service Provider (CSP) definován jako organizační entita poskytující komunikační služby účastníkům. To zahrnuje široké spektrum operátorů včetně mobilních síťových operátorů ([MNO](/mobilnisite/slovnik/mno/)), mobilních virtuálních síťových operátorů ([MVNO](/mobilnisite/slovnik/mvno/)), operátorů pevných sítí a konvergovaných poskytovatelů služeb nabízejících jak mobilní, tak pevné služby. Koncept CSP slouží jako abstraktní vrstva v architektuře 3GPP, která odděluje funkce poskytování služeb od podkladové síťové infrastruktury, a umožňuje tak standardizovaná rozhraní pro správu služeb, účtování, zabezpečení a regulatorní shodu.

CSP působí v rámci komplexního ekosystému definovaného specifikacemi 3GPP a spravuje vztahy s mnoha zainteresovanými stranami včetně koncových uživatelů, regulatorních orgánů, dalších CSP prostřednictvím roamingových dohod a poskytovatelů služeb třetích stran. Z architektonické perspektivy CSP zahrnuje různé funkční domény včetně jádrové sítě (CN), rádiové přístupové sítě (RAN) a systémů pro podporu podnikání ([BSS](/mobilnisite/slovnik/bss/)). CSP je odpovědný za zřizování, provoz a údržbu těchto síťových prvků za účelem poskytování služeb při zajištění kvality služeb, zabezpečení a regulatorní shody.

Klíčové komponenty v operační doméně CSP zahrnují Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro správu dat účastníků, Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) pro vynucování pravidel služeb, účtovací systémy ([OCS](/mobilnisite/slovnik/ocs/)/[OFCS](/mobilnisite/slovnik/ofcs/)) pro fakturaci a systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) pro provozní podporu. CSP také spravuje rozhraní k externím sítím včetně sítí jiných CSP pro roaming, propojení s veřejnými telefonními sítěmi (PSTN) a připojení k internetu prostřednictvím poskytovatelů internetových služeb (ISP).

Z perspektivy poskytování služeb CSP implementuje kompletní životní cyklus služby včetně její tvorby, zřizování, aktivace, zajištění a ukončení. To zahrnuje koordinaci více síťových funkcí napříč přístupovou, jádrovou a transportní doménou za účelem poskytování služeb od konce ke konci. CSP také zvládá správu vztahů se zákazníky, včetně registrace účastníků, přizpůsobení služeb, podpory a fakturace. V sítích 5G a novějších se role CSP vyvinula tak, aby podporovala síťové řezy, kde jeden CSP může provozovat více logických sítí přizpůsobených různým požadavkům služeb na sdílené fyzické infrastruktuře.

Odpovědnosti CSP se rozšiřují na regulatorní shodu, včetně zákonného odposlechu, podpory tísňových služeb, přenositelnosti čísel a povinností univerzální služby. Zabezpečovací funkce spravované CSP zahrnují autentizaci, autorizaci, šifrování a ochranu před síťovými útoky. CSP také implementuje systémy řízení kvality pro monitorování výkonu služeb, řešení problémů a udržování smluv o úrovni služeb (SLA) se zákazníky a partnery.

## K čemu slouží

Koncept Communications Service Provider byl formálně definován ve 3GPP Release 11, aby stanovil jasný architektonický rámec pro poskytování služeb v rozvíjejících se telekomunikačních sítích. Před touto standardizací telekomunikační operátoři fungovali s proprietárními architekturami, které ztěžovaly interoperabilitu, roaming a integraci více dodavatelů. Abstrakce CSP poskytuje standardizovaný referenční model, který odděluje logiku služeb od síťové implementace, což umožňuje flexibilnější tvorbu a poskytování služeb napříč heterogenními síťovými prostředími.

Koncept CSP řeší několik kritických potřeb odvětví včetně schopnosti podporovat více obchodních modelů (MNO, MVNO, konvergovaní operátoři), usnadňovat regulatorní shodu prostřednictvím standardizovaných rozhraní a umožňovat efektivní správu služeb napříč stále složitějšími síťovými architekturami. Jak se sítě vyvíjely od přepojování okruhů k přepojování paketů a směrem k plně IP sítím, rámec CSP poskytoval kontinuitu pro poskytování služeb a zároveň akceptoval technologickou transformaci. Také řešil rostoucí potřebu automatizované správy služeb, řízení politik a účtování ve stále dynamičtějších servisních prostředích.

S přechodem na 5G a síťové řezy se koncept CSP stal ještě kritičtějším, neboť poskytuje organizační rámec pro správu více virtualizovaných sítí na sdílené infrastruktuře. Model CSP umožňuje operátorům nabízet diferencované služby se specifickými výkonnostními charakteristikami při zachování provozní efektivity. Také podporuje vznikající obchodní modely, jako je síť jako služba (NaaS), a usnadňuje partnerství mezi poskytovateli infrastruktury a inovátory služeb v rámci ekosystému 5G.

## Klíčové vlastnosti

- Správa poskytování služeb od konce ke konci napříč přístupovými, jádrovými a transportními sítěmi
- Správa životního cyklu účastníka včetně zřizování, autentizace a fakturace
- Integrace řízení politik a účtování pro diferenciaci služeb
- Implementace regulatorní shody včetně zákonného odposlechu a tísňových služeb
- Správa roamingu a propojení s jinými CSP
- Orchestrace a správa síťových řezů v systémech 5G

## Související pojmy

- [MNO – Mobile Network Operator](/mobilnisite/slovnik/mno/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.557** (Rel-19) — Management of Non-Public Networks (NPN)
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G
- **TR 28.812** (Rel-17) — Study on Intent Driven Management Services
- **TR 28.824** (Rel-18) — Technical Report on Network Slice Capability Exposure
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 28.869** (Rel-20) — Study on cloud aspects of management and orchestration
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TR 32.847** (Rel-18) — Technical Report
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/csp/)
