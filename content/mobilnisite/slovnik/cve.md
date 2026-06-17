---
slug: "cve"
url: "/mobilnisite/slovnik/cve/"
type: "slovnik"
title: "CVE – Common Vulnerabilities and Exposures"
date: 2026-01-01
abbr: "CVE"
fullName: "Common Vulnerabilities and Exposures"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cve/"
summary: "CVE je standardizovaný systém identifikátorů pro veřejně známé kybernetické zranitelnosti a expozice (Common Vulnerabilities and Exposures). Poskytuje jedinečný, společný identifikátor pro každou zran"
---

CVE je standardizovaný systém identifikátorů pro veřejně známé kybernetické bezpečnostní zranitelnosti a expozice (Common Vulnerabilities and Exposures), který poskytuje jedinečné identifikátory pro konzistentní sledování a správu v rámci sítí 3GPP.

## Popis

Systém Common Vulnerabilities and Exposures (CVE) není sám o sobě databází zranitelností, ale standardizovaným slovníkem nebo katalogem. Poskytuje jedinečný identifikátor (CVE ID) a stručný popis pro každou veřejně oznámenou kybernetickou bezpečnostní zranitelnost nebo expozici. V rámci ekosystému 3GPP, jak je podrobně popsáno ve specifikacích jako 33.117 (Security Assurance Specification) a 33.916 (Security Assurance Methodology), se identifikátory CVE používají k jednoznačnému odkazování na konkrétní bezpečnostní chyby objevené v síťových funkcích, protokolech nebo implementacích. To umožňuje přesnou komunikaci o zranitelnostech mezi výrobci zařízení, mobilními operátory, bezpečnostními výzkumníky a normalizačními orgány.

Záznam CVE typicky sestává z CVE ID (např. CVE-YYYY-NNNN), stručného popisu bezpečnostního problému a odkazů na oznámení a zprávy. Subjekty CVE Numbering Authorities ([CNA](/mobilnisite/slovnik/cna/)), které mohou zahrnovat členské organizace 3GPP a hlavní výrobce, jsou odpovědné za přidělování těchto ID pro zranitelnosti ve svých příslušných oblastech působnosti. Když je zranitelnost identifikována v protokolu definovaném 3GPP nebo v implementaci síťové funkce od výrobce, příslušný CNA přidělí CVE ID. Toto ID je pak použito ve všech následných bezpečnostních oznámeních, dokumentaci k záplatám a zprávách o bezpečnostních chybách 3GPP, což zajišťuje, že všechny strany odkazují na naprosto stejný problém.

Role CVE v bezpečnostní architektuře 3GPP je základním kamenem pro Metodologii zajištění bezpečnosti (Security Assurance Methodology). Umožňuje systematické sledování zranitelností od objevení až po vyřešení a testování. Například, když je zranitelnost nahlášena vůči specifikaci 3GPP, je zaevidována s CVE ID. Toto ID se použije k propojení chyby s konkrétními testovacími případy ve Specifikaci zajištění bezpečnosti (SCAS), což zajišťuje, že výrobci testují přítomnost této konkrétní zranitelnosti ve svých produktech. Systém CVE tak integruje správu zranitelností přímo do životního cyklu vývoje a certifikace produktů, posouváním od ad-hoc bezpečnostních oprav k strukturovanému, ověřitelnému procesu.

V konečném důsledku použití CVE v rámci 3GPP mění správu zranitelností z roztříštěné, výrobci specifické činnosti na koordinované úsilí celého odvětví. Umožňuje agregaci dat o zranitelnostech z různých zdrojů, což podporuje analýzu trendů, hodnocení rizik a vývoj robustnějších bezpečnostních požadavků v budoucích vydáních 3GPP. Tím, že poskytuje společný jazyk pro bezpečnostní chyby, je základním kamenem pro budování důvěry v bezpečnost mobilních sítí.

## K čemu slouží

Systém CVE byl vytvořen, aby vyřešil problém nekonzistentní a nejednoznačné identifikace kybernetických bezpečnostních zranitelností. Před jeho přijetím mohla být stejná zranitelnost známa pod různými názvy, ID nebo popisy v různých bezpečnostních databázích, oznámeních výrobců a výzkumných pracích. To velmi ztěžovalo korelaci informací, sledování stavu nápravy a přesné vyhodnocení celkové hrozební situace. Pro komplexní, vícevýrobcový ekosystém, jako jsou sítě 3GPP, mohla tato nejednoznačnost vést k chybné komunikaci, opožděným záplatám a neřešeným bezpečnostním rizikům.

V rámci 3GPP bylo formální přijetí CVE (počínaje Release 13) motivováno potřebou vytvořit důkladný Rámec zajištění bezpečnosti (Security Assurance Framework). Jak se sítě stávaly více softwarově definovanými a spoléhaly na komerční standardní hardware, útočná plocha se rozšiřovala. Standardizovaná metoda identifikace zranitelností byla nezbytná pro podporu nové Specifikace zajištění bezpečnosti (SCAS) a s ní spojeného testování. CVE poskytuje potřebný společný referenční bod pro propojení objevené zranitelnosti, odpovídajícího testovacího případu pro její detekci a potvrzení výrobce o její nápravě, čímž uzavírá smyčku správy zranitelností.

Integrace CVE řeší omezení předchozích, méně formalizovaných přístupů k zacházení se zranitelnostmi v telekomunikacích. Posouvá odvětví od reaktivního, neprůhledného procesu k transparentnímu, spolupracujícímu modelu. Povinným používáním CVE ID v hlášeních bezpečnostních chyb (dle 3GPP TS 33.117) zajišťuje, že zranitelnosti ve specifikacích a implementacích 3GPP jsou sledovány se stejnou důsledností jako v širším [IT](/mobilnisite/slovnik/it/) odvětví, sladěním telekomunikační bezpečnosti s globálními osvědčenými postupy a umožněním efektivní koordinace v dodavatelském řetězci s nesčetnými zúčastněnými stranami.

## Klíčové vlastnosti

- Poskytuje jedinečné, standardizované identifikátory (CVE ID) pro bezpečnostní zranitelnosti
- Umožňuje jednoznačnou komunikaci a korelaci dat o zranitelnostech napříč výrobci a nástroji
- Integruje se se Specifikací zajištění bezpečnosti 3GPP (SCAS) pro mapování testovacích případů
- Podporuje koordinovaný proces oznamování zranitelností (CVD) mezi členy 3GPP
- Umožňuje sledování životního cyklu zranitelnosti od objevení po ověření záplaty
- Umožňuje agregaci a analýzu trendů zranitelností v technologii mobilních sítí

## Definující specifikace

- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [CVE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cve/)
