---
slug: "ippr"
url: "/mobilnisite/slovnik/ippr/"
type: "slovnik"
title: "IPPR – Internet Protocol Packet Reporting"
date: 2025-01-01
abbr: "IPPR"
fullName: "Internet Protocol Packet Reporting"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ippr/"
summary: "IPPR je mechanismus zákonitého odposlechu (LI), který umožňuje hlášení konkrétních toků IP paketů oprávněným orgánům činným v trestním řízení (LEA). Poskytuje detailní metadata a obsah cílené komunika"
---

IPPR je mechanismus zákonitého odposlechu pro hlášení konkrétních toků IP paketů, včetně metadat a obsahu, oprávněným orgánům činným v trestním řízení pro bezpečnostní a vyšetřovací účely.

## Popis

Internet Protocol Packet Reporting (IPPR) je standardizovaná funkce v rámci architektury zákonitého odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, definovaná k usnadnění zachycení a hlášení komunikací založených na paketech Internetového protokolu (IP). Funguje jako specifický typ hlášení informací souvisejících s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)), zaměřený na detailní údaje o tocích IP dat spojených s cílem odposlechu. Funkce IPPR je implementována v síťových uzlech, které zpracovávají provoz v uživatelské rovině, jako je brána paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/)), funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) nebo vyhrazená zprostředkovací zařízení. Při aktivaci na základě zákonného pověření jsou tyto uzly nakonfigurovány tak, aby identifikovaly IP provoz patřící určenému cíli – pomocí identifikátorů jako IP adresa, identifikátor předplatného nebo jiných paketových filtrů – a tento provoz spolu s bohatými metadaty duplikovaly a předávaly do monitorovacího zařízení orgánu činného v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)).

Technické fungování IPPR zahrnuje několik klíčových komponent a rozhraní. Nejprve administrační funkce ([ADMF](/mobilnisite/slovnik/admf/)) obdrží zákonné pověření a identitu cíle od [LEA](/mobilnisite/slovnik/lea/) a bezpečně distribuuje příkazy k odposlechu příslušným řídicím prvkům odposlechu (ICE) v síti, jako je brána zpracovávající cílovou relaci. ICE po aktivaci provádí hloubkovou kontrolu a filtrování paketů v uživatelské rovině za účelem izolace IP paketů cíle. Pro každý zachycený tok IPPR generuje strukturovaná hlášení, která zahrnují jak CC (skutečnou datovou část IP paketů), tak přidružená IRI, která obsahují metadata jako zdrojové a cílové IP adresy, čísla portů, typ protokolu (TCP/UDP), časová razítka a velikosti paketů. Tato data jsou formátována podle kódovacích standardů specifikovaných 3GPP (např. pomocí standardů IPDR nebo ETSI HI) a přenášena přes zabezpečená, vyhrazená rozhraní (rozhraní HI2 a HI3) do zprostředkovací funkce (MF), která je přizpůsobí a doručí do LEMF.

Role IPPR je klíčová v moderních sítích, kde je prakticky veškerá komunikace založena na IP. Poskytuje orgánům činným v trestním řízení technickou možnost monitorovat cílené internetové aktivity, včetně prohlížení webu, e-mailů, zasílání zpráv přes IP a hovorů Voice over IP (VoIP), standardizovaným a spolehlivým způsobem. Specifikace zajišťuje, že odposlech je prováděn bez zhoršení kvality služby pro cíl nebo ostatní uživatele a udržuje přísné řízení přístupu a logování, aby se zabránilo zneužití. Detailní hlášení na úrovni paketů umožňuje vyšetřovatelům rekonstruovat komunikační relace, analyzovat vzorce výměny dat a shromažďovat digitální důkazy, což z něj činí účinný nástroj zákonitého sledování v digitálním věku.

## K čemu slouží

IPPR byl vyvinut, aby řešil vyvíjející se požadavky na zákonitý odposlech v čistě IP telekomunikačních sítích. Když mobilní sítě přešly od přepojování okruhů pro hlas k datovým službám s přepojováním paketů (vyvrcholilo v plně IP sítích 4G LTE a 5G), tradiční metody odposlechu navržené pro hlasové hovory se staly nedostačujícími. Orgány činné v trestním řízení (LEA) po celém světě mají právní mandáty vyžadující, aby telekomunikační operátoři poskytli přístup k cílené komunikaci pro vyšetřování trestné činnosti a národní bezpečnost. Účelem IPPR je splnit tyto zákonné povinnosti tím, že poskytuje standardizovaný, škálovatelný a technicky robustní mechanismus k zachycení a hlášení toků IP paketů.

Jeho vznik byl motivován potřebou konzistentního, mezi dodavateli interoperabilního standardu, který by dokázal zvládnout složitost a objem IP provozu. Před takovou standardizací byly možnosti odposlechu často proprietární, což operátorům ztěžovalo nasazení více-dodavatelských sítí a LEA rozhraní s různými operátory. IPPR jako součást širšího rámce LI podle 3GPP (řada TS 33.107) definuje přesné postupy, rozhraní a formáty dat pro hlášení IP paketů, čímž zajišťuje přípustnost shromážděných důkazů a to, že implementace operátorů splňují regionální předpisy. Řeší kritický problém, jak efektivně filtrovat, zachytávat a hlásit konkrétní datové toky z vysokorychlostního, multiplexovaného IP provozu v moderních jádrových sítích, aniž by byla ohrožena výkonnost sítě nebo soukromí uživatelů, kteří nejsou cílem odposlechu.

## Klíčové vlastnosti

- Standardizované zachycení a hlášení toků IP paketů pro zákonitý odposlech
- Poskytuje jak obsah komunikace (CC), tak informace související s odposlechem (IRI)
- Využívá hloubkovou kontrolu a filtrování paketů na základě cílových identifikátorů (IP adresa apod.)
- Funguje přes definovaná rozhraní 3GPP (HI2, HI3) prostřednictvím zprostředkovací funkce
- Podporuje hlášení v reálném čase na základě relací s detailními metadaty paketů
- Zajišťuje zabezpečený, ověřený a zaznamenaný přístup, aby se zabránilo neoprávněnému použití

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [CC – Component Carrier](/mobilnisite/slovnik/cc/)
- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [IPPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ippr/)
