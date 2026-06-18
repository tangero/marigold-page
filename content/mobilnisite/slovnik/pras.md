---
slug: "pras"
url: "/mobilnisite/slovnik/pras/"
type: "slovnik"
title: "PRAS – Premises Radio Access Station"
date: 2026-01-01
abbr: "PRAS"
fullName: "Premises Radio Access Station"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pras/"
summary: "Premises Radio Access Station (PRAS) je typ zařízení umístěného u zákazníka (CPE), které poskytuje lokalizované rádiové pokrytí 5G NR uvnitř budovy nebo firemního kampusu. Připojuje se k síti mobilníh"
---

PRAS je zařízení umístěné u zákazníka (customer-premises equipment), které poskytuje lokalizované pokrytí 5G NR uvnitř budov. Připojuje se přes kabelovou přenosovou síť (wired backhaul) a funguje jako malá buňka (small cell) pro zvýšení kapacity a umožňuje privátní síťové řezy (network slicing).

## Popis

Premises Radio Access Station (PRAS) je síťový prvek zavedený ve specifikaci 3GPP Release 18, který spadá do širší kategorie zařízení umístěných u zákazníka ([CPE](/mobilnisite/slovnik/cpe/)) pro systémy 5G. Jedná se v podstatě o 5G NR rádiový přístupový uzel (radio access node) nasazený v prostorách zákazníka, například v továrně, kancelářské budově, univerzitním kampusu nebo nemocnici. PRAS poskytuje rádiové rozhraní (Uu) standardním 5G uživatelským zařízením (UE) ve své oblasti pokrytí, čímž vytváří lokalizovanou 5G buňku. Je klíčovým prvkem pro 5G neveřejné sítě ([NPN](/mobilnisite/slovnik/npn/)) a síťové řezy (network slicing), což podnikům umožňuje mít vyhrazený a řízený bezdrátový přístup.

Z architektonického hlediska PRAS obsahuje celý zásobník protokolových vrstev 5G NR rádiového rozhraní: fyzickou vrstvu ([PHY](/mobilnisite/slovnik/phy/)), řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)), protokol konvergence paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) a řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)). Implementuje funkčnost gNB-DU (Distributed Unit), jak je definována v architektuře rozděleného 5G RAN. PRAS se připojuje k páteřní síti mobilního operátora nebo k vyhrazené edge páteřní síti přes kabelový přenosový spoj (wired backhaul link), jako je optický kabel, Ethernet nebo xDSL. Toto připojení obvykle využívá standardní rozhraní F1 pro komunikaci s centralizovanou jednotkou gNB-CU (Centralized Unit) nebo, v jednodušší implementaci, více integrované rozhraní směrem k 5G Core (5GC). Tento přenosový spoj přenáší jak data uživatelské roviny, tak signalizaci řídicí roviny.

Z provozního hlediska je PRAS spravován mobilním operátorem nebo neutrálním hostitelem, i když je fyzicky umístěn v prostorách zákazníka. Správa může probíhat přes standardní rozhraní, jako je O-RAN rozhraní O1 nebo rozhraní pro správu definovaná 3GPP. PRAS podporuje klíčové funkce 5G relevantní pro podniková prostředí. To zahrnuje podporu síťových řezů (network slicing), což operátorovi umožňuje zřizovat vyhrazené logické sítě se specifickými výkonnostními charakteristikami (např. ultra-nízká latence, vysoká spolehlivost) pro různé aplikace nebo nájemce v rámci daného prostoru. Dále podporuje mechanismy kvality služeb (QoS), oddělení uplink/downlink a může být integrován s platformami Mobile Edge Computing ([MEC](/mobilnisite/slovnik/mec/)) pro lokální hostování aplikací.

Role PRAS spočívá v překlenutí mezery mezi pokrytím veřejné makro sítě a vyhrazenými privátními bezdrátovými řešeními. Nabízí výkon, zabezpečení a přizpůsobení výhod privátní sítě, přičemž využívá operátorovo spektrum, infrastrukturu páteřní sítě a odborné znalosti v oblasti správy. Od tradiční femtobuňky (HeNB) se liší tím, že je to schopnější, programovatelný a na řezy (slice-aware) citlivý uzel navržený pro škálovatelné a rozmanité požadavky Průmyslu 4.0, digitální transformace podniků a služeb přesné vnitřní lokalizace.

## K čemu slouží

PRAS byl vytvořen pro řešení rostoucí poptávky podniků a průmyslových vertikál po vysoce výkonném, zabezpečeném a přizpůsobitelném bezdrátovém připojení v jejich prostorách. Tradiční pokrytí makro sítě často nedokáže poskytnout potřebnou kapacitu, ultra-spolehlivou komunikaci s nízkou latencí (URLLC) nebo ochranu dat vyžadovanou pro kritickou průmyslovou automatizaci, rozšířenou realitu ve skladech nebo citlivé zdravotnické aplikace. Zatímco Wi-Fi je všudypřítomná, postrádá deterministický výkon, plynulou mobilitu a integrovaný bezpečnostní model systémů 3GPP.

Předchozí přístupy zahrnovaly podnikové malé buňky (small cells) a femtobuňky, ty však byly často omezené ve schopnostech, těsně svázané s architekturou veřejné sítě a nebyly navrženy s ohledem na síťové řezy (network slicing) nebo edge computing. Motivací pro standardizaci PRAS v rámci 3GPP bylo vytvořit jednotný, mezi dodavateli interoperabilní model pro 5G přístup založený na umístění u zákazníka, který se hladce integruje s operátorskými sítěmi. Řeší problém poskytování 'sítě jako služby' uvnitř privátních zařízení, což operátorům umožňuje rozšířit své služební nabídky za pouhé připojení a zahrnout vyhrazené privátní síťové řezy.

PRAS dále usnadňuje nové obchodní modely. Umožňuje operátorům nasazovat a spravovat rádiovou infrastrukturu na straně zákazníka, aniž by se vzdali kontroly nad spektrem nebo páteřní sítí. Pro podniky představuje alternativu spravované služby k budování a údržbě vlastní privátní 5G sítě od nuly. Standardizace v Release 18, jako součást širší evoluce '5G Advanced', byla poháněna případy použití definovanými v 3GPP SA1 (TS 22.261 o fázi 3 systému 5G a TS 22.858 o automatizaci sítí), které zdůrazňují potřebu automatizovaných, flexibilních a na služby orientovaných nasazení RAN na okraji sítě, včetně prostor u zákazníka.

## Klíčové vlastnosti

- Nasazuje se jako zařízení umístěné u zákazníka (CPE) a poskytuje lokalizované rádiové pokrytí 5G NR uvnitř budov nebo v kampusu.
- Připojuje se k operátorově páteřní síti 5G Core přes kabelovou přenosovou síť (např. optický kabel, Ethernet) pomocí standardních rozhraní 3GPP (např. F1).
- Podporuje 5G síťové řezy (network slicing), což umožňuje vytváření vyhrazených logických sítí pro různé podnikové služby nebo nájemce.
- Může být integrován s platformami Mobile Edge Computing (MEC) pro lokální hostování aplikací pro služby s ultra-nízkou latencí.
- Spravován síťovým operátorem nebo neutrálním hostitelem přes standardizovaná rozhraní pro správu (např. O1, NETCONF/YANG).
- Umožňuje vylepšené vnitřní určování polohy a služby založené na poloze díky svému přesnému, lokalizovanému nasazení.

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.858** (Rel-18) — Technical Report on Residential 5G Services

---

📖 **Anglický originál a plná specifikace:** [PRAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pras/)
