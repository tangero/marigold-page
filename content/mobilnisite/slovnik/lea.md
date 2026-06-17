---
slug: "lea"
url: "/mobilnisite/slovnik/lea/"
type: "slovnik"
title: "LEA – Law Enforcement Agency"
date: 2025-01-01
abbr: "LEA"
fullName: "Law Enforcement Agency"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lea/"
summary: "LEA označuje autorizovaný vládní nebo donucovací orgán, který vyžaduje a přijímá data z legálního odposlechu od telekomunikačních operátorů. V rámci 3GPP je definována jako externí entita, pro kterou"
---

LEA je autorizovaný vládní nebo donucovací orgán, pro který 3GPP definuje standardizovaná rozhraní a postupy pro vyžádání a příjem dat z legálního odposlechu od telekomunikačních operátorů.

## Popis

V architektuře 3GPP není orgán činný v trestním řízení (Law Enforcement Agency – LEA) síťovou funkcí, ale externí administrativní a právní entitou. Jedná se o vládou autorizovaný subjekt (např. policie, zpravodajské služby), kterému je na základě konkrétního soudního příkazu nebo rozhodnutí povoleno zachycovat telekomunikační provoz a související informace. Systém 3GPP definuje funkční požadavky, rozhraní a datové formáty nezbytné pro to, aby systém legálního odposlechu (Lawful Interception – [LI](/mobilnisite/slovnik/li/)) operátora doručil zachycený obsah a informace související s odposlechem (Intercept-Related Information – [IRI](/mobilnisite/slovnik/iri/)) jednomu nebo více LEA. Samotná LEA se nachází mimo důvěryhodnou hranici sítě 3GPP.

Z architektonického hlediska je interakce s LEA zprostředkována několika standardizovanými body. Operátor nasazuje interní funkce odposlechu: Administrativní funkci (Administration Function – [ADMF](/mobilnisite/slovnik/admf/)), která spravuje příkazy k odposlechu a identity LEA, a Doručovací funkce (Delivery Functions – [DF2](/mobilnisite/slovnik/df2/) a [DF3](/mobilnisite/slovnik/df3/)). DF2 doručuje informace související s odposlechem (IRI – data o hovoru/komunikaci, jako jsou účastníci, čas, poloha) a DF3 doručuje obsah komunikace (Content of Communication – [CC](/mobilnisite/slovnik/cc/) – skutečný hlasový, video nebo datový přenos). Tyto doručovací funkce se připojují k jedné nebo více Mediačním funkcím (Mediation Function – [MF](/mobilnisite/slovnik/mf/)), které převádějí interní formáty 3GPP (např. založené na 3GPP TS 33.108) do standardizovaného formátu předávacího rozhraní (Handover Interface – [HI2](/mobilnisite/slovnik/hi2/) pro IRI, HI3 pro CC) určeného pro doručení LEA. LEA provozuje Sběrnou funkci (Collection Function – CF), která tyto toky HI2 a HI3 přijímá.

Jak to funguje v praxi, zahrnuje zabezpečený a auditovatelný proces. Když je v ADMF aktivován platný příkaz k odposlechu, nakonfiguruje příslušné síťové uzly (např. MSC, SGW, PGW, AMF, SMF), aby duplikovaly provoz cílového účastníka. Interní systém LI tato data shromažďuje, zabalí je společně s metadaty a Mediační/Doručovací funkce je zabezpečeně přenášejí do prostor LEA. Specifikace 3GPP, jako je série 33.1xx, podrobně definují protokoly (např. standardizovaná předávací rozhraní ETSI), datové modely a bezpečnostní požadavky (šifrování, autentizaci) pro tuto výměnu, aby byla zajištěna integrita, důvěrnost a doručování pouze autorizovaných dat. Role LEA v kontextu 3GPP je tedy definována jako koncový bod složitého, regulovaného datového kanálu, který vyvažuje zákonné povinnosti a soukromí účastníka.

## K čemu slouží

Formální definice a architektonické zohlednění orgánu činného v trestním řízení (LEA) v normách 3GPP existuje za účelem splnění zákonných povinností uvalených na síťové operátory ve většině zemí. Tyto povinnosti vyžadují, aby operátoři měli technickou schopnost pomáhat donucovacím orgánům s autorizovaným odposlechem komunikací. Před standardizací mohl každý stát nebo operátor vyvíjet proprietární rozhraní, což vedlo k problémům s interoperabilitou, vysokým nákladům pro dodavatele zařízení a potenciálním nesrovnalostem při plnění zákonných příkazů. Účelem práce 3GPP v oblasti LI je vytvořit jednotný, na technologii nezávislý rámec, který lze implementovat globálně, a zajistit tak, že sítě jsou již svým návrhem 'připraveny na odposlech'.

Motivace pro jeho vytvoření, zejména od verze Rel-8 s rostoucím důrazem, pramenila z vývoje síťové technologie od okruhově přepínaného hlasu k paketovým plně IP sítím (IMS, LTE). Tradiční metody odposlechu vázané na okruhové přepínače zastarávaly. 3GPP potřebovalo definovat, jak konzistentně zachycovat VoIP, zasílání zpráv a datové relace napříč různými síťovými architekturami (GSM, UMTS, EPS, 5GS). Tím se řešilo omezení předchozích ad-hoc přístupů a zajistilo, že schopnosti legálního odposlechu držely krok s inovacemi služeb, čímž se zabránilo tomu, aby komunikační služby byly pro donucovací orgány 'neviditelné'.

Standardizace rozhraní LEA navíc poskytuje jasné oddělení odpovědností. Definuje striktní hranici mezi sítí operátora a vládním orgánem. To chrání interní detaily sítě operátora a data ostatních účastníků, zatímco poskytuje LEA předvídatelný a zabezpečený datový tok. Také umožňuje prostředí s více dodavateli, kde sběrné zařízení na straně LEA od jednoho dodavatele může spolupracovat s mediačními systémy od jiného, což podporuje konkurenci a snižuje náklady pro vlády. Vývoj napříč releasy tyto rozhraní neustále přizpůsobuje novým službám, jako je VoLTE, RCS a síťové slicing v 5G.

## Klíčové vlastnosti

- Externí entita definovaná jako příjemce dat z legálního odposlechu
- Komunikuje prostřednictvím standardizovaných předávacích rozhraní HI2 (pro IRI) a HI3 (pro CC)
- Vyžaduje zabezpečené, autentizované a důvěrné spojení ze sítě operátora
- Provozuje Sběrnou funkci (CF) pro příjem a zpracování datových kanálů odposlechu
- Interakce je řízena zákonným příkazem zpracovaným Administrativní funkcí (ADMF) operátora
- Specifikace zajišťují izolaci od jádra sítě za účelem ochrany dat ostatních účastníků

## Související pojmy

- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 41.033** (Rel-14) — GSM Lawful Interception Interface Requirements
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [LEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lea/)
