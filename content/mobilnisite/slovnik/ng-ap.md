---
slug: "ng-ap"
url: "/mobilnisite/slovnik/ng-ap/"
type: "slovnik"
title: "NG-AP – NG Application Protocol"
date: 2025-01-01
abbr: "NG-AP"
fullName: "NG Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ng-ap/"
summary: "NG-AP je řídicí protokol mezi 5G Next Generation NodeB (gNB) a funkcí pro správu přístupu a mobility (AMF) přes rozhraní NG. Spravuje procedury jako správa kontextu UE, paging a předávání spojení. Je"
---

NG-AP je řídicí protokol mezi 5G gNB a AMF, který spravuje procedury jako kontext UE, paging a předávání spojení přes rozhraní NG pro signalizaci a mobilitu v 5G.

## Popis

[NG](/mobilnisite/slovnik/ng/) Application Protocol (NG-AP) je klíčový řídicí protokol definovaný 3GPP pro 5G systém (5GS). Působí přes rozhraní NG, konkrétně referenční bod [N2](/mobilnisite/slovnik/n2/), který spojuje Next Generation Radio Access Network (NG-RAN) s 5G jádrem (5GC). NG-AP je zodpovědný za veškerou signalizační interakci mezi gNB (nebo ng-eNB) a funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). Je klíčovým prvkem pro servisně orientovanou architekturu 5G, usnadňující oddělení řídicí a uživatelské roviny.

NG-AP funguje výměnou strukturovaných zpráv, známých jako elementární procedury ([EP](/mobilnisite/slovnik/ep/)), mezi RAN a jádrem sítě. Tyto procedury jsou kategorizovány do třídy 1 (vyžadující odpověď) a třídy 2 (nevyžadující odpověď). Mezi klíčové procedury patří Initial UE Message, která navazuje první signalizační spojení pro uživatelské zařízení (UE); procedury správy kontextu UE pro jeho zřízení, změnu a uvolnění; a procedury přípravy předání spojení a alokace zdrojů pro plynulou mobilitu. Protokol také zajišťuje Paging, indikaci informací o schopnostech UE a samotné zřizování rozhraní NG.

Z architektonického hlediska je NG-AP přenášen přes Stream Control Transmission Protocol (SCTP), aby byl zajištěn spolehlivý, na zprávy orientovaný transport. Jde o peer-to-peer protokol, kde gNB a AMF jsou logické koncové body. Jeho návrh podporuje síťové segmenty (network slicing) tím, že umožňuje RAN být si vědom a směrovat provoz do příslušné instance síťového segmentu přes přidružený AMF. Role NG-AP je ústřední pro správu relací, správu mobility a celkovou orchestraci připojení UE v rámci 5G sítě, poskytuje základní signalizační vrstvu, která umožňuje pokročilé funkce 5G.

## K čemu slouží

NG-AP byl vytvořen jako součást 5G architektury ve 3GPP Release 15, aby poskytl nový, flexibilní a servisně orientovaný signalizační protokol mezi RAN a jádrem sítě. Řeší omezení předchozích protokolů, jako je S1-AP (používaný v 4G LTE mezi [eNB](/mobilnisite/slovnik/enb/) a [MME](/mobilnisite/slovnik/mme/)), které nebyly navrženy pro cloud-nativní, servisně orientovanou a na segmenty citlivou architekturu 5G. Primární motivací byla podpora nových požadavků 5G, včetně rozšířeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivé komunikace s nízkou latencí (URLLC) a komunikace s masivním počtem strojových zařízení (mMTC), které vyžadují agilnější a efektivnější signalizaci řídicí roviny.

Protokol řeší problém rigidní, point-to-point signalizace tím, že umožňuje více oddělený a škálovatelný model interakce. Umožňuje, aby se jediné gNB připojilo k více [AMF](/mobilnisite/slovnik/amf/), čímž podporuje pokročilé funkce jako síťové segmenty a redundance AMF. NG-AP je navržen jako dopředně kompatibilní, s modulární strukturou, která může v budoucích release pojmout nové procedury a parametry, aniž by narušila stávající funkčnost. Jeho vytvoření bylo motivováno potřebou protokolu, který by zvládl zvýšenou složitost a diverzitu 5G služeb, od vysokorychlostního přenosu dat po kritickou IoT komunikaci, a zároveň fungoval ve virtualizovaném a softwarově definovaném síťovém prostředí.

## Klíčové vlastnosti

- Spravuje zřízení, změnu a uvolnění kontextu UE
- Zajišťuje správu rozhraní NG a přenos konfigurace
- Řídí procedury přípravy a provedení předání spojení
- Podporuje iniciaci pagingu a jeho doručení do RAN
- Umožňuje přenos NAS zpráv mezi UE a AMF
- Usnadňuje přenos informací o schopnostech UE a aktualizace konfigurace RAN

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [NG-AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ng-ap/)
