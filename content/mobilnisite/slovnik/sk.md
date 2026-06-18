---
slug: "sk"
url: "/mobilnisite/slovnik/sk/"
type: "slovnik"
title: "SK – Service Key"
date: 2025-01-01
abbr: "SK"
fullName: "Service Key"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sk/"
summary: "Jedinečný identifikátor používaný v CAMEL (Customised Applications for Mobile network Enhanced Logic) k určení, která logika služby inteligentní sítě má být vyvolána pro hovor nebo relaci účastníka. J"
---

SK je jedinečný identifikátor používaný v CAMEL k určení, která logika služby inteligentní sítě má být vyvolána pro hovor nebo relaci účastníka.

## Popis

Service Key (SK) je základní parametr v architektuře inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) 3GPP [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic). Jedná se o celočíselnou hodnotu, která slouží jako jedinečný identifikátor konkrétního servisního logického programu umístěného na Service Control Point ([SCP](/mobilnisite/slovnik/scp/)). Když je iniciován hovor nebo relace řízená CAMEL, Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) účastníka poskytne obslužnému síťovému uzlu (jako je [MSC](/mobilnisite/slovnik/msc/) nebo [SGSN](/mobilnisite/slovnik/sgsn/)) sadu CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)). Tato CSI zahrnuje adresu příslušného SCP a Service Key.

Operační tok začíná, když je v síťové ústředně (Service Switching Function, [SSF](/mobilnisite/slovnik/ssf/)) dosaženo spouštěcího bodu detekce. SSF sestaví počáteční zprávu CAMEL Application Part (CAP), například InitialDP, a odešle ji na SCP. Tato CAP zpráva nese Service Key jako povinný parametr. Po přijetí zprávy SCP použije Service Key k určení přesně toho servisního logického programu nebo aplikace, která se má pro daný konkrétní hovor nebo relaci spustit. Například hodnota Service Key '10' může odpovídat službě předplaceného účtování, zatímco '20' může odpovídat službě virtuální privátní sítě (VPN).

Tento mechanismus umožňuje jednomu SCP hostovat více různých služeb pro potenciálně miliony účastníků. Síťová ústředna (SSF) nemusí rozumět servisní logice; potřebuje pouze vědět, kdy má spustit SCP a předat příslušná data včetně SK. SCP pomocí SK vybere správný program k provedení cenotvorby v reálném čase, rozhodnutí o směrování nebo jiného pokročilého řízení služeb. Service Key je tedy nezbytným spojovacím článkem mezi generickou spouštěcí událostí v síti a provedením konkrétní, na účastníka přizpůsobené služby inteligentní sítě.

## K čemu slouží

Service Key byl vytvořen, aby umožnil flexibilní a efektivní nasazení služeb inteligentní sítě (IN) v sítích GSM a později 3G/4G prostřednictvím standardu CAMEL. Před CAMEL byly pokročilé služby typicky pevně zakódovány v síťových ústřednách (MSC), což ztěžovalo jejich vytváření, úpravy nebo personalizaci. Tento přístup závislý na dodavateli a konkrétní ústředně byl pomalý, nákladný a bránil přenositelnosti služeb a inovacím.

Service Key řeší problém identifikace a výběru služby v distribuované architektuře IN. Umožňuje centralizovanému Service Control Point (SCP) – který je oddělen od přepojovací hardwarové infrastruktury – hostovat mnoho různých servisních aplikací. Když dojde ke spuštění, ústředna jednoduše informuje SCP *o tom*, že je služba potřeba, a poskytne SK, aby naznačila, *která* služba. Tím je servisní logika oddělena od přepojovací funkčnosti, což operátorům umožňuje rychle zavádět nové přidané služby (jako předplacené, bezplatné linky nebo třídění hovorů) bez nutnosti upgradu každé MSC v síti. Poskytl klíčový mechanismus pro personalizované řízení hovorů a relací v reálném čase a vytvořil tak po mnoho let páteřní vrstvu služeb generujících příjmy pro mobilní operátory.

## Klíčové vlastnosti

- Jedinečný celočíselný identifikátor pro CAMEL servisní logický program
- Přenášen v počáteční CAP (CAMEL Application Part) zprávě z SSF na SCP
- Umožňuje jednomu SCP hostovat více různých služeb
- Klíčová součást CAMEL Subscription Information (CSI) stažené z HLR
- Nasměruje SCP na příslušnou servisní logiku pro řízení hovoru/relace
- Základní pro spouštění služeb jako předplacené, VPN a překlad čísel

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2

---

📖 **Anglický originál a plná specifikace:** [SK na 3GPP Explorer](https://3gpp-explorer.com/glossary/sk/)
