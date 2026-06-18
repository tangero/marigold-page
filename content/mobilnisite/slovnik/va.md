---
slug: "va"
url: "/mobilnisite/slovnik/va/"
type: "slovnik"
title: "VA – Vulnerability Assessment"
date: 2025-01-01
abbr: "VA"
fullName: "Vulnerability Assessment"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/va/"
summary: "Hodnocení zranitelnosti (Vulnerability Assessment, VA) v 3GPP označuje systematické procesy a požadavky pro identifikaci, vyhodnocení a hlášení bezpečnostních slabin v síťových prvcích, protokolech a"
---

VA je systematický proces v rámci bezpečnostního rámce zajištění zabezpečení 3GPP pro identifikaci, vyhodnocení a hlášení bezpečnostních slabin v síťových prvcích a protokolech, který zajišťuje odolnost před nasazením.

## Popis

V rámci standardů 3GPP představuje Hodnocení zranitelnosti (Vulnerability Assessment, VA) formalizovaný bezpečnostní proces a soubor technických požadavků zaměřených na odhalení a analýzu potenciálních bezpečnostních nedostatků v návrhu a implementaci systémů definovaných 3GPP. Jedná se o proaktivní bezpečnostní činnost, odlišnou od reaktivní reakce na incidenty. Proces VA je součástí širšího rámce Specifikace zajištění zabezpečení (Security Assurance Specification, [SCAS](/mobilnisite/slovnik/scas/)) definovaného pracovní skupinou 3GPP SA3, konkrétně v sérii TS 33.1xx. Proces zahrnuje několik klíčových fází: analýzu zranitelností, bezpečnostní testování a vyhodnocení zjištění vůči souboru základních bezpečnostních požadavků.

Technické provedení VA lze aplikovat na různé síťové prvky 3GPP, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) nebo User Equipment (UE). Zahrnuje analýzu architektury systému, rozhraní, protokolů (např. [NAS](/mobilnisite/slovnik/nas/), Diameter, [HTTP](/mobilnisite/slovnik/http/)/2) a implementací za účelem identifikace slabin, které by mohly být zneužity. Mezi techniky patří statická analýza (revize návrhových specifikací a zdrojového kódu), dynamická analýza (penetrační testování, fuzzing) a revize konfigurace. Například VA na síťové funkci 5G core by posoudila její vystavenost útokům, jako jsou signalizační bouře, vkládání chybně formátovaných paketů nebo zranitelnosti v jejím rozhraní založeném na službách (service-based interface, [SBI](/mobilnisite/slovnik/sbi/)).

Výstupem VA je podrobná zpráva identifikující zranitelnosti, jejich potenciální dopad (např. prozrazení informací, odmítnutí služby, zvýšení oprávnění) a hodnocení rizika. Tuto zprávu využívají výrobci zařízení k nápravě nedostatků a síťoví operátoři a certifikační orgány (jako je [GSMA](/mobilnisite/slovnik/gsma/) Network Equipment Security Assurance Scheme - NESAS) k posouzení bezpečnostní úrovně produktu. Specifikace 3GPP, například TS 33.116 (pro 5G), poskytují podrobné testovací případy a hodnotící kritéria pro provádění VA na konkrétních síťových produktech. Tento standardizovaný přístup zajišťuje konzistentní a komplexní bezpečnostní hodnocení napříč odvětvím, což z něj činí základní činnost pro budování důvěry v sítě 3GPP.

## K čemu slouží

Hodnocení zranitelnosti bylo v rámci 3GPP formalizováno, aby se vypořádalo s rostoucí složitostí a kritičností mobilních sítí, které se staly stále atraktivnějším cílem sofistikovaných útočníků. Zabezpečení raných mobilních sítí (před 3G) bylo často ad-hoc, přičemž zajištění zabezpečení bylo z velké části ponecháno na jednotlivých výrobcích a operátorech. Jak se sítě vyvinuly v architektury zcela založené na IP (3G a novější) a staly se nezbytnou veřejnou infrastrukturou, potenciální dopad úspěšného útoku enormně vzrostl, což si vyžádalo standardizovaný, v celém odvětví uplatňovaný přístup k preventivnímu bezpečnostnímu hodnocení.

Vytvoření rámce VA, zejména jako součásti práce na SCAS od 3GPP Release 4, vyřešilo problém nekonzistentního a nesrovnatelného bezpečnostního testování napříč produkty různých výrobců. Stanovilo společný základ bezpečnostních požadavků a testovacích metodologií. To umožňuje síťovým operátorům činit informovanější rozhodnutí o pořízení a vytváří rovné podmínky pro výrobce. Dále řeší regulatorní požadavky a požadavky zákazníků na prokazatelné zabezpečení v kritické komunikační infrastruktuře. Zavedením systematického VA 3GPP pomáhá zajistit, že zranitelnosti jsou odhaleny a řešeny během vývojové a testovací fáze, nikoli až po nasazení, čímž se výrazně snižuje riziko rozsáhlých bezpečnostních narušení v provozních sítích. Je to klíčový faktor umožňující uplatnění principu "zabezpečení již při návrhu" (security by design) v moderní telekomunikaci.

## Klíčové vlastnosti

- Systematický proces pro identifikaci bezpečnostních slabin v produktech 3GPP
- Integrální součást rámce Specifikace zajištění zabezpečení (Security Assurance Specification, SCAS)
- Zahrnuje analýzu architektury, protokolů, rozhraní a implementací
- Vytváří podrobné zprávy s hodnocením rizik pro identifikované zranitelnosti
- Poskytuje standardizované testovací případy a hodnotící kritéria (např. v TS 33.116)
- Podporuje bezpečnostní certifikační schémata jako GSMA NESAS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology

---

📖 **Anglický originál a plná specifikace:** [VA na 3GPP Explorer](https://3gpp-explorer.com/glossary/va/)
