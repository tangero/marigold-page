---
slug: "slm-s"
url: "/mobilnisite/slovnik/slm-s/"
type: "slovnik"
title: "SLM-S – SEAL Location Management Server"
date: 2025-01-01
abbr: "SLM-S"
fullName: "SEAL Location Management Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/slm-s/"
summary: "Síťový server pro správu polohy definovaný v rámci architektury 3GPP SEAL (Service Enabler Architecture Layer). Poskytuje polohové služby, jako je periodické, spouštěné nebo okamžité získání polohy pr"
---

SLM-S je SEAL Location Management Server (server pro správu polohy v rámci SEAL), síťový server v architektuře 3GPP SEAL, který poskytuje aplikacím polohové služby, jako je periodické nebo okamžité získání polohy.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Location Management Server (SLM-S) je server s možnostmi služeb v rámci vrstvy Service Enabler Architecture Layer (SEAL) standardu 3GPP pro vertikální aplikace. SEAL poskytuje standardizovanou sadu společných služeb (jako je správa polohy, skupin a konfigurace) pro usnadnění vývoje aplikací pro sítě 3GPP. SLM-S funguje jako centrální entita, která vystavuje síťové polohové služby autorizovaným aplikačním klientům ([AC](/mobilnisite/slovnik/ac/)). Přijímá požadavky na polohu, řídí proces určování polohy s podkladovou sítí (např. 5GC, EPC) a vrací výsledky polohy.

Architektonicky SLM-S rozhraní s dvěma hlavními entitami. Za prvé, vystavuje severozápadní [API](/mobilnisite/slovnik/api/) (založené na RESTful principech) pro aplikačního klienta, definované v 3GPP TS 24.545. Toto API umožňuje AC požadovat určení polohy cílového uživatelského zařízení (UE) pomocí různých typů požadavků: Okamžitý (jedno určení), Periodický (určení v intervalech) nebo Spouštěný (určení při vstupu/opuštění UE určité oblasti). Za druhé, na jihozápadní straně SLM-S rozhraní s mechanismy pro získání polohy v jádrové síti. V systému 5G se typicky jedná o Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) prostřednictvím standardizovaných rozhraní (např. Nlg, NLs). SLM-S překládá aplikační požadavek na polohu na úrovni služby do odpovídajících procedur na síťové úrovni, jako je zahájení Mobile Terminated Location Request ([MT-LR](/mobilnisite/slovnik/mt-lr/)).

Jeho činnost zahrnuje správu relací, vynucování politik a zpracování ochrany soukromí. Když AC odešle požadavek, SLM-S jej ověří vůči nastavením ochrany soukromí účastníka (uloženým v Privacy Profile Register) a autorizaci AC. Pokud je povoleno, vytvoří polohovou relaci, komunikuje se sítí za účelem získání polohy UE (pomocí metod jako [GNSS](/mobilnisite/slovnik/gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/) nebo cell-ID) a streamuje výsledky zpět k AC. Může také podporovat odložené hlášení, ukládání poloh, pokud je AC dočasně nedostupné. Tím, že funguje jako abstrakční vrstva, SLM-S chrání vývojáře aplikací před složitostmi přímé interakce s prvky sítě 3GPP, jako je GMLC nebo LMF.

## K čemu slouží

SLM-S byl vytvořen za účelem zjednodušení a standardizace způsobu, jakým vertikální průmyslové aplikace (např. logistika, záchranné služby, sledování IoT aktiv) vyžadují a spotřebovávají informace o poloze ze sítí 3GPP. Před SEAL si každá vertikála často vyvíjela vlastní, neinteroperabilní integrace se síťovými polohovými službami, jako je GMLC, což vedlo k fragmentaci, vysokým nákladům na vývoj a nekonzistentnímu zacházení s ochranou soukromí a zabezpečením. SLM-S poskytuje jednotné, pro aplikace vhodné API, které je konzistentní napříč různými operátory a generacemi sítí (4G, 5G).

Jeho vývoj byl motivován vizí 5G v oblasti vystavení sítě a podpory vertikál. 3GPP uznalo, že poloha je základním prvkem pro nespočet služeb, ale stávající mechanismy (např. LCS API) potřebovaly modernizaci pro cloudové, API řízené ekosystémy. SLM-S jako součást SEAL řeší omezení předchozích přístupů tím, že nabízí architekturu založenou na službách, která je v souladu s principy 5G. Řeší problém složitosti přístupu tím, že poskytuje jediný, dobře definovaný koncový bod pro všechny typy polohových služeb. Dále centralizuje kritické funkce, jako je autorizace ochrany soukromí a řízení politik, a zajišťuje, že regulační shoda (např. GDPR) je řešena konzistentně sítí, nikoliv delegována na každého jednotlivého vývojáře aplikací.

## Klíčové vlastnosti

- Vystavuje standardizované RESTful API (3GPP TS 24.545) pro aplikace k vyžádání polohy UE.
- Podporuje více typů požadavků na polohu: Okamžitý, Periodický a Spouštěný oblastí.
- Funguje jako abstrakční vrstva mezi aplikacemi a funkcemi jádrové sítě pro správu polohy (GMLC, LMF).
- Vynucuje politiky ochrany soukromí účastníka a autorizaci aplikace před zpracováním požadavků.
- Spravuje polohové relace, včetně odloženého hlášení, pokud je aplikační klient nedostupný.
- Integruje se s širším rámcem SEAL pro společnou autentizaci, správu skupin a konfiguraci.

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.545** (Rel-19) — SEAL Location Management Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SLM-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/slm-s/)
