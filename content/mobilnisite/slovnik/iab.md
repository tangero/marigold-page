---
slug: "iab"
url: "/mobilnisite/slovnik/iab/"
type: "slovnik"
title: "IAB – Integrated Access and Backhaul"
date: 2026-01-01
abbr: "IAB"
fullName: "Integrated Access and Backhaul"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iab/"
summary: "IAB je funkce 5G NR, která umožňuje bezdrátovým uzlům využívat část rádiového spektra jak pro přístupové spoje (k UE), tak pro bezdrátové přenosové spoje (k donorovému gNB). Vytváří tak vícekrokovou r"
---

IAB je funkce 5G NR, která umožňuje bezdrátovým uzlům využívat rádiové spektrum jak pro přístupové spoje k uživatelským zařízením, tak pro bezdrátové přenosové spoje (backhaul), čímž vytváří síť s vlastním přenosem (self-backhauling), která snižuje potřebu optických vláken.

## Popis

Integrated Access and Backhaul (IAB, Integrovaný přístup a přenos) je klíčová architektonická inovace v 5G New Radio (NR), která umožňuje jednomu rádiovému uzlu současně fungovat jako přístupový bod pro uživatelská zařízení (UE) a jako přenosový (relay) uzel pro provoz backhaulu. IAB uzel se skládá ze dvou logických komponent: mobilní terminace ([IAB-MT](/mobilnisite/slovnik/iab-mt/)) a distribuované jednotky ([IAB-DU](/mobilnisite/slovnik/iab-du/)). IAB-MT funguje jako UE vůči svému nadřazenému uzlu (dalšímu IAB uzlu nebo IAB donoru) a navazuje bezdrátový přenosový spoj. IAB-DU funguje jako gNB-DU vůči svým podřízeným uzlům (kterými mohou být UE nebo další downstream IAB uzly) a poskytuje rozhraní pro rádiový přístup. IAB donor je gNB, který poskytuje síťový přístup IAB uzlům a obsahuje centrální jednotku ([CU](/mobilnisite/slovnik/cu/)), která řídí celou IAB topologii.

Provoz je založen na sofistikovaném rozdělování a multiplexování zdrojů. Časové, frekvenční a prostorové zdroje jsou dynamicky přidělovány mezi přístupové a přenosové spoje, aby se zabránilo vlastní interferenci a optimalizovala se kapacita. Toto řídí IAB donor CU prostřednictvím aplikačního protokolu F1 (F1-AP) přes backhaulové [RLC](/mobilnisite/slovnik/rlc/) kanály. Klíčové protokoly jsou upraveny: IAB-MT používá pro připojení směrem vzhůru zásobník rozhraní NR Uu ([SDAP](/mobilnisite/slovnik/sdap/), [PDCP](/mobilnisite/slovnik/pdcp/), RLC, [MAC](/mobilnisite/slovnik/mac/), [PHY](/mobilnisite/slovnik/phy/)), zatímco IAB-DU používá pro připojení k donorové CU zásobník rozhraní NR F1, přičemž backhaulový RLC kanál slouží jako transportní síťová vrstva. Směrování v IAB síti je topologicky-aware, přičemž donorová CU spravuje vytváření BH RLC kanálů a BAP (Backhaul Adaptation Protocol) směrování pro efektivní hop-by-hop přeposílání dat uživatelské roviny.

Scénáře nasazení jsou flexibilní a podporují vícekrokové topologie (strom, mesh) pro rozšíření pokrytí hluboko do interiérů nebo do odlehlých oblastí. IAB uzel pro obě funkce využívá stejné 5G NR spektrum a vlnové formy, což zajišťuje jednotné a spektrálně efektivní rádiové rozhraní. Mezi klíčové technické výzvy, které řeší, patří správa topologie, výběr trasy, objevování a integrace nových IAB uzlů a robustní správa zdrojů pro zvládnutí kumulativního zpoždění a kapacitních omezení vícekrokových bezdrátových cest. IAB je základním kamenem pro rychlé a nákladově efektivní zhušťování sítí 5G.

## K čemu slouží

IAB byl vytvořen, aby vyřešil kritickou ekonomickou a logistickou výzvu poskytování vysokokapacitního optického backhaulu ke každé malé buňce v husté 5G síti. Pokládání optických vláken ke každé lampě veřejného osvětlení, semaforu nebo fasádě budovy pro ultra-husté sítě (UDN) je neúměrně drahé a časově náročné. IAB poskytuje bezdrátové řešení s vlastním přenosem, které operátorům umožňuje rychle nasazovat uzly tam, kde je k dispozici pouze napájení a místo pro instalaci, a pro konektivitu využívat již licencované rádiové spektrum.

Historicky se pro bezdrátový backhaul používaly mikrovlnné spoje, ale ty pracovaly ve vyhrazených, často drahých pásmech spektra s odděleným vybavením. IAB tuto funkci integruje přímo do standardu 5G NR a pro přístup i backhaul používá stejnou hardwarovou základnu (baseband) a RF hardware. To dramaticky snižuje náklady na nasazení, složitost získávání lokalit a čas uvedení na trh. Je to motivováno zejména potřebou nasazení rozšířeného mobilního širokopásmového přístupu (eMBB) a masivního IoT v městských kaňonech, stadionech, továrnách a na dočasných akcích.

IAB navíc umožňuje flexibilní síťové topologie, které se mohou samy organizovat a samy hojit. V konfiguraci mesh poskytuje odolnost proti výpadkům spojů tím, že nabízí alternativní cesty. Řeší tak omezení předchozích přenosových (relay) technologií v LTE, které byly často méně integrované a neefektivní. Tím, že je IAB od Release 16 nativní součástí standardu 5G NR, zajišťuje interoperabilitu mezi dodavateli, efektivní využití spektra prostřednictvím dynamického sdílení zdrojů a bezproblémovou integraci s 5G Core sítí, což činí zhušťování sítí v éře 5G ekonomicky životaschopným.

## Klíčové vlastnosti

- Bezdrátový vlastní přenos (self-backhaul) využívající stejné 5G NR spektrum a rádiové rozhraní
- Dvoufunkční IAB uzel s komponentami IAB-MT (pro backhaul) a IAB-DU (pro přístup)
- Podpora vícekrokových (strom, mesh) síťových topologií pro rozšířené pokrytí
- Dynamický multiplex zdrojů (čas/frekvence/prostor) mezi přístupovými a přenosovými spoji
- Správa topologie a tras zajišťovaná centrální jednotkou (CU) IAB donoru
- Integrované směrování prostřednictvím vrstvy Backhaul Adaptation Protocol (BAP)

## Související pojmy

- [IAB-MT – Integrated Access and Backhaul Mobile Termination](/mobilnisite/slovnik/iab-mt/)
- [IAB-DU – IAB Distributed Unit](/mobilnisite/slovnik/iab-du/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.314** (Rel-20) — Management and Orchestration - Plug and Connect
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 28.875** (Rel-19) — Study on IAB Node Management
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.824** (Rel-17) — Security Study for NR Integrated Access & Backhaul
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- … a dalších 29 specifikací

---

📖 **Anglický originál a plná specifikace:** [IAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/iab/)
