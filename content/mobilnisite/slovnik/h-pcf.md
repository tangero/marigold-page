---
slug: "h-pcf"
url: "/mobilnisite/slovnik/h-pcf/"
type: "slovnik"
title: "H-PCF – Home Policy Control Function"
date: 2026-01-01
abbr: "H-PCF"
fullName: "Home Policy Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-pcf/"
summary: "Home Policy Control Function (H-PCF) je funkce 5G jádra sítě, která spravuje řízení politik a účtování pro roamující účastníky. Sídlí v domovské síti (HPLMN) a poskytuje rozhodnutí o politikách pro PC"
---

H-PCF je Home Policy Control Function (domácí funkce řízení politik), funkce v 5G jádru sítě v domovské síti, která zajišťuje řízení politik a účtování pro roamující účastníky za účelem konzistentní kvality služeb.

## Popis

Home Policy Control Function (H-PCF) je klíčová komponenta v architektuře 5G Core (5GC), konkrétně definovaná v rámci Policy Control Framework. Funguje jako rozhodovací bod pro politiky pro účastníky roamující mimo jejich domovskou síť. H-PCF sídlí v Home Public Land Mobile Network ([HPLMN](/mobilnisite/slovnik/hplmn/)) a komunikuje s Visited [PCF](/mobilnisite/slovnik/pcf/) ([V-PCF](/mobilnisite/slovnik/v-pcf/)) umístěným v Visited [PLMN](/mobilnisite/slovnik/plmn/) ([VPLMN](/mobilnisite/slovnik/vplmn/)) přes rozhraní N24. Její primární rolí je poskytovat domovem směrované řízení politik, což zajišťuje, že politiky domovského operátora, včetně Quality of Service (QoS), pravidel účtování a řízení přístupu, jsou vynucovány i když je uživatelské zařízení (UE) připojeno k cizí síti.

Architektonicky je H-PCF součástí Policy Control Function (PCF), což je jednotný rámec pro politiky v 5G. Pro roamingové scénáře je PCF logicky rozdělena na V-PCF a H-PCF. V-PCF přímo komunikuje s Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v navštívené síti, aby vynutila politiky na úrovni relace. Když rozhodnutí o politice vyžaduje vstup z domovské sítě – například pro specifická oprávnění služeb účastníka, limity utrácení nebo profily QoS definované domovskou sítí – V-PCF se dotazuje H-PCF. H-PCF následně učiní autoritativní rozhodnutí o politice na základě dat účastníka z Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)) a potenciálně dalších funkcí domovské sítě.

H-PCF funguje tak, že přijímá požadavky na politiky od V-PCF přes rozhraní N24, které je založeno na [HTTP](/mobilnisite/slovnik/http/)/2 a používá service-based interfaces (SBI) na bázi JSON. Tyto požadavky obsahují informace o relaci UE, jako je požadovaná QoS, název datové sítě (DNN) a identifikátory předplatného. H-PCF je vyhodnotí vůči politikám domovské sítě a profilům účastníků. Poté vrátí rozhodnutí o politikách, která mohou zahrnovat autorizované parametry QoS, metody účtování (online/offline) a pravidla specifická pro služby. V-PCF tato rozhodnutí převede na instrukce pro SMF a další funkce. Toto oddělení umožňuje navštívené síti řešit místní vynucování politik, zatímco pro účastníkově specifickou a potenciálně citlivou logiku politik se odvolává na domovskou síť.

Klíčové komponenty spojené s H-PCF zahrnují rozhraní N24 pro komunikaci s V-PCF, rozhraní Npcf pro interní service-based interakce PCF a integraci s UDR přes rozhraní Nudr pro přístup k datům předplatného a politik. Její role je klíčová pro udržení konzistence služeb, umožnění pokročilých modelů účtování, jako je sponzorovaný přenos dat, a podporu regulatorních požadavků pro roaming. Centralizací rozhodnutí o domovských politikách H-PCF zjednodušuje složitost řízení politik v navštívené síti a zajišťuje, že obchodní pravidla domovského operátora jsou konzistentně uplatňována globálně.

## K čemu slouží

H-PCF byla zavedena v 3GPP Release 15 jako součást nové architektury 5G System (5GS) za účelem řešení omezení předchozích rámců řízení politik v roamingových scénářích, zejména těch z Evolved Packet Core (EPC). V 4G EPC bylo roamingové řízení politik řešeno Home PCRF (H-PCRF) komunikující s Visited PCRF (V-PCRF) přes rozhraní S9. Ačkoli funkční, tento přístup měl složitosti v řetězení služeb, latenci způsobenou více přeskoky signalizace a omezenou flexibilitu pro nové 5G služby, jako je síťové dělení (network slicing) a edge computing.

Vytvoření H-PCF bylo motivováno potřebou agilnějšího, cloud-nativního a service-based rámce pro politiky v 5G. Architektura 5GC přijala Service-Based Architecture (SBA) s HTTP/2 a JSON, nahrazující protokoly založené na Diameter používané v EPC. H-PCF, jako součást tohoto nového rámce, je navržena tak, aby podporovala dynamická rozhodnutí o politikách vyžadovaná pro 5G případy užití, jako je síťové dělení, kde přístup roamujícího účastníka ke slici musí být autorizován domovskou sítí. Také umožňuje efektivnější modely domovem směrovaného provozu a podporuje integraci s funkcemi pro vystavení sítě pro služby třetích stran.

Dále H-PCF řeší problém konzistentního vynucování politik přes administrativní domény. Umožňuje domovským operátorům zachovat kontrolu nad zážitkem účastníka a účtováním, což je klíčové pro diferenciaci služeb a zajištění příjmů. Oddělením rozhodovacího bodu pro politiky (H-PCF) od bodu vynucení politik (v navštívené síti) usnadňuje plynulejší meziodběratelské dohody a snižuje zátěž navštívené sítě při správě politik cizích účastníků. Tento design je zásadní pro globální škálovatelnost 5G služeb a podporu složitých IoT a podnikových roamingových scénářů.

## Klíčové vlastnosti

- Poskytuje autoritativní rozhodnutí o politikách pro roamující účastníky z domovské sítě
- Využívá service-based interface (SBI) N24 pro komunikaci s Visited PCF
- Podporuje dynamické řízení politik pro 5G síťové dělení (network slicing) a QoS v roamingových scénářích
- Umožňuje domovem směrované řízení účtování a integraci s online/offline systémy účtování
- Přistupuje k profilům účastníků a datům politik z Unified Data Repository (UDR)
- Usnadňuje konzistentní vynucování obchodních pravidel domovského operátora přes navštívené sítě

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [V-PCF – Visited Policy Control Function](/mobilnisite/slovnik/v-pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [H-PCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-pcf/)
