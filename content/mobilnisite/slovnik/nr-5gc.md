---
slug: "nr-5gc"
url: "/mobilnisite/slovnik/nr-5gc/"
type: "slovnik"
title: "NR/5GC – New Radio connected to 5G Core Network"
date: 2025-01-01
abbr: "NR/5GC"
fullName: "New Radio connected to 5G Core Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-5gc/"
summary: "NR/5GC označuje kompletní architekturu 5G systému od konce ke konci, kde je přístupová síť New Radio (NR) připojena k 5G jádru (5G Core). Jedná se o standardní, nativní nasazení pro 5G, které umožňuje"
---

NR/5GC je standardní architektura 5G systému, ve které je přístupová síť New Radio nativně připojena k 5G jádru (5G Core), což umožňuje pokročilé služby jako dělení sítě (network slicing).

## Popis

NR/5GC označuje kompletní 5G systémovou architekturu standardizovanou 3GPP, zahrnující přístupovou síť New Radio (NR) RAN a jádro 5G Core (5GC). Jedná se o definitivní, samostatné (Standalone) nasazení 5G, ve kterém se gNB (5G základnová stanice) připojuje prostřednictvím rozhraní [NG](/mobilnisite/slovnik/ng/) k řídicí rovině ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)) a uživatelské rovině ([UPF](/mobilnisite/slovnik/upf/)) 5G jádra. Architektura se zásadně liší od předchozích generací, je postavena na cloud-nativním, na službách založeném designu. Klíčová rozhraní zahrnují N1 (UE-AMF), [N2](/mobilnisite/slovnik/n2/) (gNB-AMF), N3 (gNB-UPF) a N4 (SMF-UPF).

Fungování začíná připojením (attach) UE k síti. gNB směruje počáteční registrační požadavek na funkci AMF. AMF funguje jako jediný vstupní bod pro signalizaci řídicí roviny a zpracovává registraci, správu připojení a mobility. Pro správu relací (session management) AMF komunikuje s funkcí SMF, která vybírá UPF pro zřízení [PDU](/mobilnisite/slovnik/pdu/) relací. Uživatelská data pak proudí z UE přes gNB a UPF do datové sítě ([DN](/mobilnisite/slovnik/dn/)), pro efektivitu obcházejí řídicí rovinu. gNB a 5GC mezi sebou komunikují pomocí protokolu [NGAP](/mobilnisite/slovnik/ngap/) přes rozhraní N2.

Klíčové komponenty na straně přístupové sítě zahrnují gNB, které zajišťuje všechny funkce spojené s rádiovým rozhraním, jako je plánování, beamforming nebo řízení rádiových zdrojů (RRC). Na straně jádra je 5GC dekomponováno na modulární síťové funkce (NF), jako jsou AMF, SMF, UPF, UDM a PCF. Tyto NF spolu komunikují prostřednictvím standardizovaných rozhraní založených na službách (např. Namf, Nsmf) v rámci společného frameworku. Úlohou NR/5GC je poskytnout kompletní sadu 5G schopností: vylepšené mobilní širokopásmové připojení (eMBB) s extrémními přenosovými rychlostmi, ultra-spolehlivé komunikace s nízkou latencí (URLLC) pro kritické aplikace a hromadnou komunikaci mezi stroji (mMTC) pro IoT. Umožňuje dělení sítě (network slicing), při kterém jsou na společné fyzické infrastruktuře vytvářeny více logických sítí se specifickými vlastnostmi, a podporuje edge computing tím, že umožňuje nasazení UPF blízko uživatele.

## K čemu slouží

Architektura NR/5GC byla vytvořena, aby odstranila omezení předchozích generací sítí, zejména 4G jádra EPC, které nebylo navrženo pro podporu různorodých a náročných požadavků 5G. EPC mělo monolitickou architekturu s point-to-point rozhraními, která byla nepružná a pomalu se přizpůsobovala novým službám. Primární motivací bylo vybudovat jádro sítě, které je ze své podstaty flexibilní, škálovatelné a schopné podporovat širokou škálu služeb s velmi odlišnými potřebami – od vysokorychlostního videa přes nízkopříkonové senzory až po kriticky důležité průmyslové řízení.

Historicky časná nasazení 5G (často označovaná jako 'Non-Standalone' nebo NSA) používala rádiové rozhraní NR, ale stále spoléhala na 4G jádro EPC (EPC+NR), což sloužilo jako přechodné řešení, ale neumožnilo využít plný potenciál 5G. Vytvoření nativního systému NR/5GC (Standalone nebo SA) to řeší čistým, nově navrženým konceptem. Přináší architekturu založenou na službách (SBA), kde síťové funkce nabízejí a spotřebovávají služby prostřednictvím API, což umožňuje snadnější integraci, automatizaci a dělení sítě. Tím se řeší problém provozní složitosti a umožňuje se rychlá inovace služeb.

Dále NR/5GC řeší potřebu programovatelnosti sítě a podpory edge computingu. Oddělením uživatelské roviny (UPF) od řídicí roviny (SMF) lze UPF flexibilně nasadit na okraji sítě, čímž se snižuje latence pro aplikace jako autonomní vozidla nebo rozšířená realita. Architektura také vnitřně podporuje vystavení síťových schopností (network exposure), což umožňuje aplikacím třetích stran kontrolovaným způsobem interagovat s možnostmi sítě. V podstatě NR/5GC existuje proto, aby transformovalo mobilní síť z pouhého přenosového potrubí na programovatelnou platformu pro digitální služby.

## Klíčové vlastnosti

- Nativní propojení mezi 5G NR přístupovou sítí (gNB) a 5G jádrem (5GC)
- Architektura založená na službách (SBA) pro funkce jádra sítě
- Podpora dělení sítě (network slicing) od rádiového rozhraní po jádro
- Oddělení řídicí a uživatelské roviny (CUPS) s flexibilním nasazením UPF
- Integrovaná podpora edge computingu prostřednictvím lokálního vyvedení přes UPF (local breakout)
- Vylepšený model kvality služeb (QoS) s identifikátorem 5G QoS (5QI) a reflexivním QoS

## Definující specifikace

- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [NR/5GC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-5gc/)
