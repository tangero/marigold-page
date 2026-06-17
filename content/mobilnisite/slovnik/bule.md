---
slug: "bule"
url: "/mobilnisite/slovnik/bule/"
type: "slovnik"
title: "BULE – Binding Update List Entry"
date: 2025-01-01
abbr: "BULE"
fullName: "Binding Update List Entry"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bule/"
summary: "Datová struktura v bráně paketové datové sítě (PGW), která udržuje informace o vazbě pro mobilní uzly využívající Dual-Stack Mobile IPv6 (DSMIPv6). Ukládá asociaci mezi domácí adresou mobilního uzlu a"
---

BULE je datová struktura v bráně paketové datové sítě, která ukládá vazbu mezi domácí adresou mobilního uzlu a přechodnou adresou pro správu IP mobility v DSMIPv6.

## Popis

Binding Update List Entry (BULE) je klíčová datová struktura v bráně paketové datové sítě (PGW) v sítích 3GPP Evolved Packet Core (EPC), která implementuje funkčnost Dual-Stack Mobile IPv6 (DSMIPv6). Slouží jako centrální úložiště pro udržování vazeb mezi trvalou domácí adresou (HoA) mobilního uzlu a jeho aktuální přechodnou adresou (CoA), když je zařízení připojeno k navštíveným sítím. Každá BULE odpovídá jedné relaci DSMIPv6 mobilního uzlu a obsahuje kompletní stavové informace potřebné pro správné směrování paketů mezi domácí sítí a aktuální polohou mobilního uzlu.

Architektura BULE funguje v rámci implementace DSMIPv6 v PGW, která vystupuje jako domácí agent ([HA](/mobilnisite/slovnik/ha/)) pro mobilní uzly. Když se mobilní uzel přesune do navštívené sítě a získá lokální IP adresu (přechodnou adresu), odešle zprávu Binding Update (BU) svému domácímu agentovi (PGW). PGW tuto zprávu zpracuje a vytvoří nebo aktualizuje odpovídající BULE, která ukládá vazbu mezi domácí adresou mobilního uzlu a jeho aktuální přechodnou adresou. Tato vazba umožňuje PGW zachytávat pakety určené na domácí adresu mobilního uzlu a tunelovat je na aktuální přechodnou adresu pomocí zapouzdření IPv6-in-IPv6 nebo IPv6-in-IPv4 v závislosti na konfiguraci sítě.

Mezi klíčové komponenty uložené v BULE patří domácí adresa mobilního uzlu (IPv4 a/nebo IPv6), aktuální přechodná adresa, doba platnosti vazby (čas vypršení), pořadové číslo pro řazení zpráv, bezpečnostní parametry pro autentizaci a identifikátory koncových bodů tunelu. BULE také udržuje stavové informace o aktuálním stavu vazby (aktivní, vypršená, zrušená), možnosti mobility a případné parametry optimalizace trasy. PGW konzultuje BULE pro každý paket určený na domácí adresu mobilního uzlu, aby rozhodla, zda jej doručit lokálně (pokud je uzel doma), nebo jej tunelovat na aktuální přechodnou adresu (pokud je uzel v roamingu).

Role BULE v síti přesahuje jednoduché mapování adres – umožňuje několik pokročilých funkcí mobility. Podporuje simultánní připojení IPv4 a IPv6 prostřednictvím dvouvrstvého provozu, udržuje více přechodných adres pro scénáře multihomingu a implementuje procedury obnovy vazby pro udržení aktivních relací. BULE také interaguje s dalšími funkcemi PGW, jako je vynucování politik, účtování a správa kvality služeb (QoS), aby zajistila, že mobilita nenaruší kontinuitu služby. Když doba platnosti vazby vyprší nebo mobilní uzly odešlou indikaci zrušení vazby, PGW odpovídající BULE aktualizuje nebo odstraní, čímž uvolní prostředky a udržuje přesné informace o směrování.

Z implementačního hlediska zahrnuje správa BULE složité operace stavových strojů, které zpracovávají vytváření, aktualizaci, obnovu a mazání vazeb. PGW musí synchronizovat informace BULE s dalšími databázemi mobility, zachovávat konzistenci během předávání spojení a zajistit, aby aktualizace vazeb od mobilních uzlů byly autentizované a autorizované. Systém BULE také rozhraní s infrastrukturou 3GPP [AAA](/mobilnisite/slovnik/aaa/) pro správu bezpečnostních přihlašovacích údajů a s funkcemi řízení politik pro aplikaci politik specifických pro mobilitu. Tento komplexní přístup zajišťuje, že IP mobilita je transparentní pro aplikace při zachování síťové bezpečnosti a efektivity.

## K čemu slouží

Binding Update List Entry byla vytvořena, aby řešila základní výzvu udržování kontinuity IP relací pro mobilní zařízení při jejich pohybu mezi různými přístupovými body sítě. Před implementací DSMIPv6 a BULE mobilní zařízení ztrácela svá IP připojení při změně sítě, což vyžadovalo od aplikací znovunavázání relací – rušivý zážitek pro uživatele, zejména u služeb v reálném čase, jako je VoIP a streamování videa. BULE umožňuje správu mobility založenou na síti, kde síťová infrastruktura (konkrétně PGW) udržuje mapování IP adres zařízení, což umožňuje aplikacím nadále používat stejnou IP adresu bez ohledu na změny fyzické polohy.

Historicky trpěly rané implementace mobilní IP několika omezeními, která BULE pomáhá překonat. Jednoduchá řešení IP mobility vyžadovala, aby si mobilní uzly byly neustále vědomy svého stavu mobility a aktivně se účastnily procedur předávání spojení, což spotřebovávalo baterii a výpočetní prostředky zařízení. Předchozí přístupy také zápasily s dvouvrstvými prostředími (IPv4/IPv6), která vyžadovala samostatné mechanismy pro každou verzi IP. BULE jako součást specifikace DSMIPv6 v 3GPP Release 8 poskytla jednotné řešení, které transparentně funguje pro obě verze IP, přičemž přesouvá složitost správy mobility ze zařízení na síťovou infrastrukturu.

Vytvoření BULE bylo motivováno rostoucí poptávkou po bezproblémové mobilitě v sítích 3GPP s rozšířením chytrých telefonů a využívání mobilních dat. Řešila konkrétní problémy, jako je trojúhelníkové směrování (kdy provoz využívá neoptimální cesty), latence při předávání spojení během přechodů mezi sítěmi a neschopnost udržovat více simultánních připojení. Centralizací informací o vazbě v PGW umožňuje BULE efektivní optimalizaci trasy, snižuje signalizační režii ve srovnání s přístupy náročnými na klienta a přirozeně se integruje s existujícími mechanismy autentizace a řízení politik 3GPP. Tato architektura umožňuje operátorům poskytovat lepší kvalitu uživatelského zážitku při optimalizaci využití síťových zdrojů.

## Klíčové vlastnosti

- Udržuje vazbu mezi domácí adresou mobilního uzlu a přechodnou adresou
- Podporuje dvouvrstvý provoz pro simultánní mobilitu IPv4 a IPv6
- Umožňuje transparentní kontinuitu IP relací během předávání spojení mezi sítěmi
- Integruje se s 3GPP AAA pro bezpečnou autentizaci vazeb
- Automaticky spravuje doby platnosti vazeb a procedury obnovy
- Podporuje optimalizaci trasy pro minimalizaci cest směrování paketů

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [BULE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bule/)
