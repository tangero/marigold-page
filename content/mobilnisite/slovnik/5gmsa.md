---
slug: "5gmsa"
url: "/mobilnisite/slovnik/5gmsa/"
type: "slovnik"
title: "5GMSA – 5G Media Streaming Architecture"
date: 2025-01-01
abbr: "5GMSA"
fullName: "5G Media Streaming Architecture"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/5gmsa/"
summary: "5GMSA je standardizovaná architektura pro poskytování služeb streamování médií přes sítě 5G. Definuje funkční entity a rozhraní pro umožnění efektivního, škálovatelného a kvalitativně adaptivního stre"
---

5GMSA je standardizovaná architektura 3GPP pro poskytování efektivních, škálovatelných a kvalitativně adaptivních služeb streamování médií, jako je 4K/8K video a AR/VR, přes sítě 5G.

## Popis

Architektura pro streamování médií v 5G (5GMSA) je komplexní rámec specifikovaný 3GPP pro poskytování mediálních služeb v systému 5G. Poskytuje standardizovanou sadu funkčních entit, referenčních bodů a procedur pro usnadnění streamování médií, včetně obsahu na vyžádání i živého. Architektura je navržena tak, aby byla agnostická vůči základním mediálním formátům a kodekům, což umožňuje flexibilitu při zajištění interoperability mezi různými poskytovateli služeb a síťovými operátory. Integruje se s jádrem sítě 5G (5GC) a využívá síťové schopnosti, jako je kvalita služeb (QoS) a síťové řezání, pro optimalizaci doručování médií.

Jádro 5GMSA tvoří několik klíčových funkčních komponent. Aplikační funkce pro [5GMS](/mobilnisite/slovnik/5gms/) (5GMS-AF) funguje jako centrální řídicí entita, která komunikuje s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) jádra sítě 5G, aby vyžádala a spravovala síťové prostředky šité na míru pro mediální relace. Funkce hostování streamování médií (MSHF) je zodpovědná za hostování a doručování mediálního obsahu, často se integruje se sítěmi pro doručování obsahu ([CDN](/mobilnisite/slovnik/cdn/)). Ovladač mediální relace ([MSH](/mobilnisite/slovnik/msh/)) spravuje navázání, změnu a ukončení relací streamování médií a řeší aspekty jako adaptivní streamování s proměnným datovým tokem ([ABR](/mobilnisite/slovnik/abr/)) a popis relace. Tyto entity komunikují prostřednictvím standardizovaných referenčních bodů, jako je M1 pro doručování médií a M5 pro interakce aplikační funkce.

Architektura funguje tak, že umožňuje dynamické vyjednávání a poskytování síťových prostředků na základě požadavků mediálního proudu. Když uživatel zahájí streamovací relaci, může 5GMS-AF vyžádat konkrétní QoS toky od jádra 5G, aby zajistila nízkou latenci, vysokou šířku pásma nebo jiné výkonnostní metriky. Podporuje funkce jako příjem médií, kdy je obsah nahrán a připraven k distribuci, a spotřebu médií, kdy koncová uživatelská zařízení přijímají a zobrazují proud. 5GMSA také zahrnuje mechanismy pro ochranu obsahu, jako je správa digitálních práv ([DRM](/mobilnisite/slovnik/drm/)), a analytiku pro monitorování výkonu streamování a uživatelského zážitku.

V širší síti 5G hraje 5GMSA klíčovou roli při umožnění pokročilých mediálních služeb tím, že poskytuje jednotný rámec, který propojuje aplikační protokoly pro streamování (jako [DASH](/mobilnisite/slovnik/dash/) a HLS) se schopnostmi síťové vrstvy. Umožňuje poskytovatelům služeb využívat inherentní vlastnosti 5G – jako je síťové řezání pro vyhrazené řezy pro média, edge computing pro snížení latence a massive MIMO pro vysokou propustnost – k doručování kvalitnějších mediálních zážitků. Tato integrace zajišťuje, že streamování médií není jen službou typu over-the-top, ale síťově optimalizovanou aplikací, což vede k spolehlivějšímu a efektivnějšímu doručování obsahu v různých scénářích nasazení 5G.

## K čemu slouží

5GMSA byla vytvořena, aby řešila rostoucí poptávku po vysoce kvalitních, imerzivních službách streamování médií přes sítě 5G, které vyžadují více než jen základní připojení k internetu. Před její standardizací se streamování médií přes mobilní sítě často spoléhalo na proprietární nebo neintegrovaná řešení, která plně nevyužívala pokročilé schopnosti 5G, jako je síťové řezání, ultra spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB). To vedlo k neefektivitám, nekonzistentní kvalitě zážitku (QoE) a výzvám při škálování služeb, jako je 4K/8K video, rozšířená realita (AR), virtuální realita (VR) a streamování živých událostí. 5GMSA poskytuje standardizovanou architekturu pro sjednocení těchto snah, zajišťuje interoperabilitu a umožňuje poskytovatelům služeb doručovat média se zaručeným výkonem.

Historicky byly architektury pro streamování médií, jako jsou ty založené na adaptivním HTTP streamování (např. MPEG-DASH, HLS), vyvíjeny nezávisle na síťové kontrole a fungovaly jako služby typu over-the-top (OTT). Ačkoli byly efektivní, postrádaly přímou interakci se sítí pro dynamické přizpůsobování prostředků na základě podmínek v reálném čase. Se zavedením 5G vznikla potřeba tuto mezeru překlenout tím, že mediální aplikace budou moci vyžadovat konkrétní síťové prostředky a politiky. 5GMSA to řeší definováním rozhraní mezi mediálními aplikacemi a jádrem sítě 5G, což umožňuje funkce jako streamování s ohledem na QoS, integraci edge computingu pro nižší latenci a efektivní využití síťových řezů vyhrazených pro mediální provoz.

Motivace za 5GMSA také vychází z touhy podporovat nové obchodní modely a servisní inovace v mediálním průmyslu. Poskytnutím standardizovaného rámce snižuje vývojovou složitost pro výrobce zařízení, poskytovatele obsahu a síťové operátory a podporuje živý ekosystém. Řeší omezení předchozích přístupů tím, že nabízí end-to-end kontrolu nad doručováním médií, od přípravy obsahu po spotřebu, a zároveň zajišťuje bezpečnost, škálovatelnost a přizpůsobivost budoucím mediálním formátům. Díky tomu je 5GMSA základním prvkem pro realizaci plného potenciálu 5G při transformaci služeb v oblasti médií a zábavy.

## Klíčové vlastnosti

- Standardizovaná rozhraní pro interakci mediální aplikace a sítě
- Integrace s jádrem sítě 5G pro dynamické řízení QoS a politik
- Podpora protokolů pro adaptivní streamování s proměnným datovým tokem (ABR), jako jsou DASH a HLS
- Správa mediální relace pro její navázání, změnu a ukončení
- Mechanismy ochrany obsahu včetně integrace DRM
- Škálovatelnost prostřednictvím podpory edge computingu a sítí pro doručování obsahu (CDN)

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs

---

📖 **Anglický originál a plná specifikace:** [5GMSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gmsa/)
