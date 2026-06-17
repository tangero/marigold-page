---
slug: "dgps"
url: "/mobilnisite/slovnik/dgps/"
type: "slovnik"
title: "DGPS – Differential Global Positioning System"
date: 2025-01-01
abbr: "DGPS"
fullName: "Differential Global Positioning System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dgps/"
summary: "DGPS je technika vylepšení polohování, která zvyšuje přesnost GPS pomocí referenčních stanic, jež vypočítávají a vysílají korekční data do mobilních zařízení. Snižuje chyby způsobené atmosférickým zpo"
---

DGPS je technika vylepšení polohování, která zvyšuje přesnost GPS pro mobilní zařízení pomocí referenčních stanic, které vypočítávají a vysílají korekční data, čímž snižuje chyby a umožňuje přesnost na úrovni metrů.

## Popis

Differential Global Positioning System (DGPS) je vylepšení standardního polohování [GPS](/mobilnisite/slovnik/gps/), které významně zvyšuje přesnost určení polohy korekcí chyb společných pro přijímače GPS v dané geografické oblasti. V sítích 3GPP funguje DGPS jako vylepšení služby určování polohy ([LCS](/mobilnisite/slovnik/lcs/)), kde referenční stanice na přesně známých místech vypočítávají rozdíl mezi svou známou polohou a polohou udávanou satelity GPS. Tyto referenční stanice generují korekční data, která jsou následně přenášena do mobilních zařízení prostřednictvím infrastruktury mobilní sítě, což umožňuje těmto zařízením aplikovat korekce na vlastní GPS měření a dosáhnout podstatně lepší přesnosti polohování.

Architektura DGPS v sítích 3GPP zahrnuje několik klíčových komponent pracujících společně. Referenční stanice (také nazývané základnové stanice nebo monitorovací stanice) jsou rozmístěny na pevných, přesně zaměřených místech, aby nepřetržitě monitorovaly signály GPS satelitů. Tyto stanice vypočítávají korekční faktory porovnáním polohy odvozené ze satelitů se svou známou přesnou polohou. Korekční data jsou následně zpracována a formátována pro přenos prostřednictvím infrastruktury mobilní sítě, typicky přes Serving Mobile Location Center (SMLC) nebo Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)) v core síti. Mobilní zařízení přijímají tyto korekce prostřednictvím vyhrazených řídicích kanálů nebo datových nosičů a aplikují je na svá nezpracovaná GPS měření před výpočtem konečné polohy.

Technická implementace DGPS v sítích 3GPP se řídí specifikacemi, které definují formátování, přenos a aplikaci korekčních dat. Korekční zprávy typicky zahrnují korekce pseudovzdáleností pro jednotlivé satelity, které kompenzují chyby v satelitních hodinách, efemeridách a atmosférickém zpoždění (ionosférickém a troposférickém). Systém podporuje jak korekce v reálném čase přenášené přes rozhraní vzduch, tak korekce zpracovávané dodatečně pro aplikace, které nevyžadují okamžité aktualizace polohy. Zlepšení přesnosti závisí na faktorech včetně vzdálenosti mezi mobilním zařízením a referenční stanicí (prostorová de-korelace), stáří korekčních dat (časová de-korelace) a kvalitě měření samotné referenční stanice.

Integrace DGPS se sítěmi 3GPP umožňuje několik provozních režimů. V režimu s podporou sítě poskytuje síť korekční data mobilnímu zařízení, které provádí konečný výpočet polohy. V režimu založeném na mobilním zařízení může zařízení přijímat korekční data, ale veškeré zpracování zvládá interně. Systém může pracovat s různými systémy augmentace GPS, včetně satelitních systémů augmentace (SBAS) jako WAAS, [EGNOS](/mobilnisite/slovnik/egnos/) a [MSAS](/mobilnisite/slovnik/msas/), stejně jako pozemních systémů augmentace. Přenos korekčních dat může být optimalizován na základě síťových podmínek, možností zařízení a požadavků aplikace, přičemž jsou podporovány různé úrovně kvality služeb pro různé služby založené na poloze.

Výkonnostní charakteristiky DGPS v implementacích 3GPP typicky ukazují zlepšení přesnosti ze standardních 10-15 metrů GPS na 1-3 metry za optimálních podmínek. Systém redukuje chyby společného režimu, které ovlivňují všechny přijímače v místní oblasti, včetně chyb satelitních hodin, nepřesností efemerid a atmosférického zpoždění. Nemůže však korigovat chyby způsobené mnohocestným šířením signálu nebo šum přijímače, které zůstávají lokální pro každé zařízení. Účinnost klesá se vzdáleností od referenčních stanic kvůli prostorové de-korelaci atmosférických chyb, což vedlo k vývoji síťových implementací DGPS s více referenčními stanicemi a interpolačními technikami pro pokrytí širší oblasti.

## K čemu slouží

DGPS bylo zavedeno v sítích 3GPP, aby řešilo omezení přesnosti samostatného [GPS](/mobilnisite/slovnik/gps/) pro služby založené na poloze. Standardní polohování GPS trpí různými zdroji chyb včetně nepřesností satelitních hodin, chyb v datech efemerid, ionosférického a troposférického zpoždění a selektivní dostupnosti (pokud je aktivní). Tyto chyby typicky vedou k přesnosti polohování 10-15 metrů, což bylo nedostatečné pro nově vznikající aplikace, jako je navigace vozidel, sledování majetku, účtování podle polohy a nouzové služby, které vyžadovaly přesnost na úrovni metrů.

Hlavní motivací pro integraci DGPS do standardů 3GPP bylo umožnit komerční a regulační služby určování polohy, které vyžadovaly vyšší přesnost, než mohl poskytnout samostatný GPS. Nouzové služby jako Enhanced 911 v Severní Americe a podobné požadavky v jiných regionech nařizovaly zlepšenou přesnost polohy pro tísňová volání. Komerční aplikace včetně navigace, správy vozových parků, reklamy založené na poloze a rozšířené reality také vyžadovaly lepší možnosti polohování. Infrastruktura mobilní sítě poskytla ideální platformu pro efektivní distribuci korekčních dat DGPS velkému počtu mobilních zařízení.

Předchozí přístupy ke zlepšení přesnosti GPS buď vyžadovaly drahé specializované vybavení, nebo měly omezené pokrytí. Samostatné přijímače GPS nemohly dosáhnout potřebné přesnosti pro mnoho aplikací, zatímco tradiční implementace DGPS využívající rádiové majáky měly omezené pozemní oblasti pokrytí. Využitím stávající infrastruktury mobilní sítě poskytla implementace DGPS podle 3GPP širokopásmové pokrytí, efektivní distribuci dat a integraci s dalšími síťovými službami. Tento přístup vyřešil problém, jak doručit vysoce přesné polohování masově rozšířeným mobilním zařízením bez nutnosti dodatečného hardwaru nebo služeb předplatného mimo mobilní připojení.

## Klíčové vlastnosti

- Generování korekcí na referenčních stanicích na přesně známých místech
- Přenos korekčních dat v reálném čase prostřednictvím infrastruktury mobilní sítě
- Podpora více formátů korekcí včetně standardů RTCM SC-104
- Integrace s architekturou služeb určování polohy 3GPP prostřednictvím SMLC/GMLC
- Redukce chyb společného režimu včetně atmosférického zpoždění a nepřesností satelitních hodin
- Podpora režimů polohování s podporou sítě i založených na mobilním zařízení

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DGPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dgps/)
