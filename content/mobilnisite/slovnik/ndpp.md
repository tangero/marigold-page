---
slug: "ndpp"
url: "/mobilnisite/slovnik/ndpp/"
type: "slovnik"
title: "NDPP – Network Device Protection Profile"
date: 2025-01-01
abbr: "NDPP"
fullName: "Network Device Protection Profile"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ndpp/"
summary: "Bezpečnostní rámec definující standardizované ochranné profily pro síťová zařízení v systémech 3GPP. Zajišťuje, že zařízení splňují základní bezpečnostní požadavky, což usnadňuje bezpečné nasazení a i"
---

NDPP je bezpečnostní rámec 3GPP, který definuje standardizované ochranné profily pro síťová zařízení, aby bylo zajištěno, že splňují základní bezpečnostní požadavky pro bezpečné nasazení a interoperabilitu.

## Popis

Network Device Protection Profile (NDPP) je bezpečnostní specifikace v rámci standardů 3GPP, která stanovuje standardizovanou sadu bezpečnostních požadavků a schopností pro síťová zařízení. Funguje jako bezpečnostní základna, definující, co musí kompatibilní zařízení chránit (jeho bezpečnostní cíle) a jak tohoto ochrany musí dosáhnout (jeho funkční bezpečnostní požadavky). NDPP není produktová specifikace, ale šablona nebo profil, vůči kterému mohou být konkrétní síťová zařízení, jako jsou firewally, systémy detekce narušení nebo specifické síťové funkce, vyhodnocována a certifikována. Toto hodnocení typicky následuje metodologii Common Criteria a poskytuje nezávislé ujištění, že bezpečnostní tvrzení zařízení jsou platná a jeho implementace je robustní.

Architektura shody s NDPP zahrnuje několik klíčových komponent. Jádrem je samotný dokument Protection Profile ([PP](/mobilnisite/slovnik/pp/)), který je definován ve specifikaci 3GPP 33.916. Tento dokument nastiňuje definici bezpečnostního problému, identifikuje hrozby (např. neoprávněný přístup, odmítnutí služby, únik informací) a předpoklady o provozním prostředí. Dále specifikuje bezpečnostní cíle zařízení pro potlačení těchto hrozeb a podrobné funkční bezpečnostní požadavky ([SFR](/mobilnisite/slovnik/sfr/)), které tyto cíle implementují. Tyto SFR pokrývají oblasti jako identifikace a autentizace, správa zabezpečení, ochrana bezpečnostních funkcí a využití prostředků. Výrobce zařízení vytvoří Security Target ([ST](/mobilnisite/slovnik/st/)), který mapuje vlastnosti jeho konkrétního produktu na požadavky NDPP. Nezávislá laboratoř poté vyhodnotí zařízení vůči tomuto ST.

Jeho role v síti je zásadní pro bezpečnost dodavatelského řetězce a řízení rizik. Poskytnutím společného, přísného bezpečnostního benchmarku umožňuje NDPP síťovým operátorům pořizovat zařízení s ověřenou úrovní bezpečnostní záruky. Snižuje riziko zavedení zranitelného zařízení do sítě, což je obzvláště kritické, jak se sítě stávají více softwarově definovanými a virtualizovanými, čímž se rozšiřuje útočná plocha. Profil pomáhá zajistit, aby byla bezpečnost zabudována již od fáze návrhu, a nebyla až dodatečným doplňkem. I když ne všechny síťové prvky vyžadují certifikaci dle NDPP, je tento profil zvláště relevantní pro bezpečnostně kritické uzly a ty, které tvoří bezpečnostní perimetr síťové domény.

## K čemu slouží

NDPP byl vytvořen, aby řešil rostoucí složitost a bezpečnostní rizika spojená s infrastrukturou telekomunikačních sítí. Jak se sítě vyvíjely s novými technologiemi, jako jsou [NFV](/mobilnisite/slovnik/nfv/) a [SDN](/mobilnisite/slovnik/sdn/), diverzita hardwarových a softwarových komponent dramaticky vzrostla. To operátorům ztěžovalo posuzování a porovnávání bezpečnostní pozice různých zařízení od různých dodavatelů pomocí ad-hoc nebo proprietárních kritérií. Nedostatek standardizovaného bezpečnostního benchmarku vedl k potenciálním nekonzistentnostem, zranitelnostem a zvýšenému provoznímu riziku.

Před zavedením NDPP byla bezpečnostní hodnocení často založena na obecných standardech [IT](/mobilnisite/slovnik/it/) bezpečnosti nebo bilaterálních dohodách mezi operátory a dodavateli, kterým chyběla specifičnost vyžadovaná pro telekomunikační spolehlivost a model hrozeb. NDPP to řeší tím, že poskytuje rámec přizpůsobený potřebám 3GPP a založený na Common Criteria. Definuje konzistentní sadu bezpečnostních požadavků specificky pro síťová zařízení fungující v ekosystému 3GPP, přičemž bere v úvahu jedinečné hrozby, jako jsou signalizační útoky, a požadavky na interoperabilitu. To umožňuje objektivní, nezávislé ověření bezpečnostních tvrzení, dává operátorům větší důvěru v jejich investice do infrastruktury a pomáhá vytvořit celkově bezpečnější a odolnější síťovou strukturu.

## Klíčové vlastnosti

- Standardizovaná bezpečnostní základna pro hodnocení síťových zařízení
- Založeno na metodologii Common Criteria pro nezávislé ověření
- Definuje funkční bezpečnostní požadavky (SFR) a bezpečnostní cíle
- Řeší telekomunikačně specifické hrozby a provozní prostředí
- Usnadňuje bezpečné pořizování a interoperabilitu mezi dodavateli
- Poskytuje šablonu pro vytváření produktově specifických Security Targets (ST)

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [NDPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndpp/)
