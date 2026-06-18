---
slug: "nssaaf"
url: "/mobilnisite/slovnik/nssaaf/"
type: "slovnik"
title: "NSSAAF – Network Slice-specific Authentication and Authorization Function"
date: 2026-01-01
abbr: "NSSAAF"
fullName: "Network Slice-specific Authentication and Authorization Function"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssaaf/"
summary: "NSSAAF je funkce 5G Core Network, která orchestruje Network Slice-Specific Authentication and Authorization (NSSAA). Funguje jako proxy mezi AMF a externími AAA servery a spravuje EAP-based autentizač"
---

NSSAAF je funkce 5G Core Network, která funguje jako proxy mezi AMF a externími AAA servery a spravuje ověřování a autorizaci pro konkrétní síťový slice.

## Popis

Network Slice-specific Authentication and Authorization Function (NSSAAF) je vyhrazená logická funkce v 5G Core Network (5GC), specifikovaná od 3GPP Release 16. Jejím hlavním úkolem je zprostředkování procedury Network Slice-Specific Authentication and Authorization ([NSSAA](/mobilnisite/slovnik/nssaa/)). NSSAAF samotné ověřování neprovádí, ale funguje jako přenosový člen a orchestrátor mezi funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v důvěryhodné doméně operátora a externími servery Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)), které patří tenantovi nebo poskytovateli konkrétního síťového slicu. Tato architektura je zásadní pro scénáře síťového slicingu s více stranami a více doménami.

Operačně NSSAAF přijímá NSSAA požadavky od AMF přes service-based rozhraní Nnssaaf_NSSAA. Tento požadavek obsahuje identitu UE a identifikátor požadovaného síťového slicu ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)). NSSAAF poté zahájí dialog s příslušným externím AAA serverem, který je identifikován na základě S-NSSAI. Komunikace s externím AAA serverem probíhá přes referenční bod N33. NSSAAF transparentně přeposílá pakety Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) mezi UE (které je EAP peer) a externím AAA serverem (který je EAP server). UE a externí AAA server provedou kompletní EAP autentizační metodu (např. EAP-AKA', EAP-TLS), přičemž NSSAAF a AMF pouze přeposílají pakety. NSSAAF je zodpovědné za mapování EAP session na správný kontext UE a AMF.

Klíčové zodpovědnosti NSSAAF zahrnují správu stavu NSSAA procedury, vynucování časových limitů a převod konečného výsledku z externího AAA serveru (EAP Success/Failure) na výsledek NSSAA definovaný 3GPP, který je odeslán AMF. Funkce také řeší možné chybové stavy z externího AAA serveru. Funkce může být implementována jako samostatná Network Function ([NF](/mobilnisite/slovnik/nf/)) nebo může být kombinována s jinou NF, například s Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), v závislosti na implementaci dodavatele a volbách nasazení sítě. Její návrh zdůrazňuje neutralitu vůči konkrétní použité EAP metodě, což umožňuje tenantům slicu používat autentizační mechanismus, který nejlépe vyhovuje jejich bezpečnostním požadavkům.

## K čemu slouží

NSSAAF bylo vytvořeno k realizaci konceptu slice-specific authentication zavedeného s [NSSAA](/mobilnisite/slovnik/nssaa/). Bez vyhrazené funkce pro správu interakce s externími AAA systémy by AMF muselo přímo komunikovat s potenciálně neomezeným počtem AAA serverů specifických pro jednotlivé tenanty, z nichž každý by mohl používat různé protokoly a mít různé bezpečnostní požadavky. To by vytvořilo obrovskou složitost, problémy se škálovatelností a bezpečnostní rizika pro operátora core sítě.

NSSAAF tento problém řeší tím, že poskytuje standardizovaný, bezpečný a řízený mezibod. Abstrahuje složitost interakcí s externími AAA servery od AMF, což umožňuje AMF řešit správu mobility a session management, zatímco deleguje bezpečnostní rozhodnutí specifická pro slice. Toto oddělení odpovědností je klasickým architektonickým principem, který zvyšuje modularitu a bezpečnost. Dále NSSAAF poskytuje v síti operátora jediný bod, kde lze vynucovat politiky týkající se externí konektivity (např. pravidla firewallu, řízení provozu pro AAA zprávy). Jeho vytvoření bylo motivováno potřebou učinit síťový slicing prakticky nasaditelným pro podnikové a vertikální use case, kde tenant slicu požaduje kontrolu nad přístupovým ověřováním, aniž by vyžadoval hlubokou integraci svých AAA systémů do MNO core.

## Klíčové vlastnosti

- Funguje jako proxy/přenašeč pro EAP zprávy mezi UE (přes AMF) a externím AAA serverem
- Poskytuje standardizované service-based rozhraní (Nnssaaf_NSSAA) směrem k AMF
- Využívá referenční bod N33 pro komunikaci s externími AAA servery
- Spravuje stav a kontext probíhajících procedur slice-specific authentication
- Převádí výsledky EAP protokolu na 3GPP-specifické NSSAA výsledkové kódy
- Může být nasazeno jako samostatná NF nebo ko-lokováno s jinými NF, například s AUSF

## Související pojmy

- [NSSAA – Network Slice-Specific Authentication and Authorization](/mobilnisite/slovnik/nssaa/)
- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.204** (Rel-18) — Charging management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 29.526** (Rel-19) — Nnssaaf Service Based Interface Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.290** (Rel-19) — 5G Charging for Service Based Interface
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NSSAAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssaaf/)
