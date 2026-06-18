---
slug: "m2pa"
url: "/mobilnisite/slovnik/m2pa/"
type: "slovnik"
title: "M2PA – Message Transfer Part 2 - User Peer-to-Peer Adaptation Layer"
date: 2025-01-01
abbr: "M2PA"
fullName: "Message Transfer Part 2 - User Peer-to-Peer Adaptation Layer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/m2pa/"
summary: "M2PA je protokolová adaptační vrstva umožňující přenos signalizace SS7 MTP2 přes IP sítě. Poskytuje spolehlivé a sekvenované doručování zpráv MTP3 mezi signalizačními body, což usnadňuje migraci z TDM"
---

M2PA je protokolová adaptační vrstva, která umožňuje spolehlivý a sekvenovaný přenos signalizačních zpráv SS7 MTP2 přes IP sítě, a tím usnadňuje migraci z TDM na IP jádrové sítě.

## Popis

M2PA (Message Transfer Part 2 - User Peer-to-Peer Adaptation Layer) je protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) (SIGTRAN) a přijatý 3GPP pro přenos signalizačních zpráv [SS7](/mobilnisite/slovnik/ss7/) [MTP](/mobilnisite/slovnik/mtp/) úrovně 2 ([MTP2](/mobilnisite/slovnik/mtp2/)) přes IP sítě. Funguje jako adaptační vrstva, která emuluje služby tradiční linkové vrstvy MTP2 nad asociací protokolu [SCTP](/mobilnisite/slovnik/sctp/) (Stream Control Transmission Protocol). Hlavní architektonickou rolí M2PA je umožnit MTP úrovni 3 ([MTP3](/mobilnisite/slovnik/mtp3/)) fungovat, jako by komunikovala přes standardní MTP2 linku založenou na [TDM](/mobilnisite/slovnik/tdm/), zatímco podkladovým fyzickým přenosem je IP. Toho je dosaženo mapováním primitiv a zpráv MTP2 na streamy SCTP a zajištěním mechanismů pro doručování ve správném pořadí, řízení toku a detekci/opravu chyb srovnatelných s původním MTP2.

V jádru M2PA vytváří peer-to-peer spojení mezi dvěma signalizačními body ([SP](/mobilnisite/slovnik/sp/)) nebo signalizačními přenosovými body (STP) pomocí SCTP, které poskytuje spolehlivý, spojení orientovaný přenos s podporou multihomingu. Pakety M2PA obsahují hlavičku adaptační vrstvy identifikující zprávu jako M2PA a včetně sekvenčních čísel pro zarovnání a testování (proving) linky. Protokol řeší správu stavu linky, včetně odesílání a přijímání testovacích jednotek pro ověření integrity a zarovnání linky, podobně jako testovací perioda v TDM MTP2. Také spravuje procedury změny (changeover) a návratu (changeback) pro udržení signalizačního provozu při výpadcích linky nebo událostech údržby.

Klíčové součásti implementace M2PA zahrnují rozhraní adaptační vrstvy M2PA User Adaptation (UA) k MTP3, správu asociace SCTP a funkci řízení stavu linky. Vrstva M2PA přijímá zprávy MTP3, zapouzdřuje je s hlavičkou M2PA a předává je SCTP k přenosu. Naopak přijímá pakety ze SCTP, odstraní hlavičku M2PA a doručí zprávu MTP3 ve správném pořadí. Její role v síti je klíčová ve signalizačních bránách (SGs) a IP signalizačních přenosových bodech (IP-STPs), kde umožňuje bezproblémovou interoperabilitu mezi staršími sítěmi SS7 a IP signalizačními sítěmi, jako je IP Multimedia Subsystem (IMS) nebo jádrové sítě 4G/5G, čímž zajišťuje zpětnou kompatibilitu a hladký přechod k plně IP architekturám.

## K čemu slouží

M2PA bylo vytvořeno, aby řešilo potřebu odvětví migrovat tradiční okruhově přepínané signalizační sítě SS7 na nákladově efektivnější, škálovatelnější a flexibilnější infrastruktury založené na IP. Historicky signalizace SS7 spoléhala na TDM linky (např. E1/T1) používající protokol MTP2 pro spolehlivou signalizaci na linkové vrstvě. Tyto TDM sítě byly nákladné na údržbu, postrádaly flexibilitu šířky pásma a nebyly nativně kompatibilní s moderními IP jádrovými sítěmi. Omezení TDM, včetně pevné kapacity a vysokých provozních nákladů, motivovala vývoj adaptačních vrstev pro přenos SS7 přes IP.

Hlavní problém, který M2PA řeší, je umožnění existujícím síťovým prvkům MTP3, jako jsou Service Switching Points (SSP) nebo STP, komunikovat přes IP linky bez nutnosti modifikace samotné vrstvy MTP3. Poskytuje transparentní náhradu za fyzickou vrstvu MTP2, což umožňuje operátorům využívat výhod IP sítí, jako je statistické multiplexování, snadnější provisioning a integrace s IP bezpečnostními mechanismy. To usnadnilo vytvoření IP Signalizačních přenosových bodů (IP-STP) a Signalizačních bran, které jsou nezbytnými komponentami hybridních a plně IP jádrových sítí.

Jeho vznik byl poháněn širšími snahami pracovní skupiny SIGTRAN (Signaling Transport) v rámci IETF definovat sadu protokolů pro SS7 přes IP. M2PA konkrétně slouží scénářům vyžadujícím přímou peer-to-peer náhradu MTP2 linky, často v národních signalizačních sítích nebo mezi sousedními signalizačními body. Doplňuje další adaptační vrstvy, jako je M3UA, která se používá pro jiný architektonický model (komunikace s IP aplikačními servery).

## Klíčové vlastnosti

- Emuluje služby MTP2 přes IP pomocí transportu SCTP
- Poskytuje spolehlivé doručování zpráv MTP3 ve správném pořadí
- Podporuje správu stavu linky a procedury zarovnání
- Umožňuje bezproblémovou interoperabilitu mezi TDM a IP signalizačními body
- Usnadňuje migraci sítě na plně IP jádrové sítě
- Umožňuje škálovatelnost šířky pásma a flexibilní provisioning sítě

## Související pojmy

- [M3UA – SS7 MTP3 – User Adaptation Layer](/mobilnisite/slovnik/m3ua/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)

## Definující specifikace

- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures

---

📖 **Anglický originál a plná specifikace:** [M2PA na 3GPP Explorer](https://3gpp-explorer.com/glossary/m2pa/)
