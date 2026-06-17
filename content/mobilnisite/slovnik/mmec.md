---
slug: "mmec"
url: "/mobilnisite/slovnik/mmec/"
type: "slovnik"
title: "MMEC – Mobile Metaverse Enablement Client"
date: 2026-01-01
abbr: "MMEC"
fullName: "Mobile Metaverse Enablement Client"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mmec/"
summary: "Klientská entita umožňující ponořující se zážitky v metavesmíru přes sítě 3GPP. Spravuje vysoce náročné XR relace s velkou šířkou pásma a nízkou latencí a koordinuje se síťovými funkcemi pro QoS a edg"
---

MMEC je klientská entita, která umožňuje ponořující se zážitky v metavesmíru přes mobilní sítě tím, že spravuje relace rozšířené reality a koordinuje se sítí pro kvalitu služeb a edge computing.

## Popis

Mobile Metaverse Enablement Client (MMEC) je funkční entita umístěná v uživatelském zařízení (UE) nebo přidružené aplikaci, navržená k usnadnění služeb metavesmíru a pokročilé rozšířené reality (XR) přes mobilní sítě 3GPP. Jejím hlavním úkolem je fungovat jako inteligentní zprostředkovatel mezi ponořující aplikací a sítí, přičemž překládá požadavky aplikace na síťové servisní požadavky. MMEC je odpovědný za správu relací, včetně zřizování, změny a ukončování relací metavesmíru, které se vyznačují náročnými požadavky na ultra vysokou šířku pásma, ultra nízkou latenci a vysokou spolehlivost. Rozhraní s funkcemi jádra sítě, jako je Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), slouží k vyjednání a zabezpečení potřebných toků kvality služeb (QoS) a síťových prostředků. To zajišťuje, že datové proudy pro vykreslování, zvuk a haptickou zpětnou vazbu jsou doručovány s odpovídající prioritou a zárukami výkonu.

Z architektonického hlediska MMEC komunikuje jak s aplikační vrstvou, tak s protokolovým zásobníkem 3GPP. Přijímá požadavky na aplikační úrovni, jako je požadovaná snímková frekvence, rozlišení a latence od pohybu k fotonu, a mapuje je na konkrétní síťové parametry. Využívá rozhraní založená na službách, potenciálně s využitím funkcí jako Network Exposure Functions ([NEF](/mobilnisite/slovnik/nef/)), ke komunikaci svých potřeb s jádrem sítě. Klíčovou součástí jeho fungování je schopnost žádat o prostředky edge computingu. Pro aplikace metavesmíru je často třeba zpracování přesunout na platformy Multi-access Edge Computing ([MEC](/mobilnisite/slovnik/mec/)), aby se snížila latence end-to-end. MMEC může iniciovat procedury pro výběr User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a směrování provozu k optimální instanci aplikačního serveru na okraji sítě.

MMEC navíc hraje zásadní roli v mobilitě a kontinuitě relací. Jak se uživatel pohybuje, klient musí spolupracovat se sítí, aby zajistil plynulé předávání bez zhoršení ponořujícího zážitku, přičemž může iniciovat síťově řízená předávání na základě stavu aplikace. Také řeší aspekty zabezpečení a soukromí, zajišťuje, že uživatelská data a biometrické informace používané v XR relacích jsou chráněny v souladu se síťovými politikami. V podstatě MMEC abstrahuje složitost podkladové sítě 3GPP od aplikace metavesmíru a poskytuje standardizovaný způsob využití pokročilých síťových schopností, jako je síťové dělení (network slicing), edge computing a přesná správa QoS, k zajištění konzistentních a vysoce kvalitních ponořujících zážitků.

## K čemu slouží

MMEC byl vytvořen, aby vyřešil zásadní nesoulad mezi extrémními požadavky na výkon metavesmíru a tradičním best-effort charakterem mobilních datových služeb. Před jeho konceptualizací musely ponořující XR aplikace fungovat přes obecná datová připojení, potýkaly se s výkyvy latence, chvěním a nedostatečnou šířkou pásma, což vedlo ke špatným uživatelským zážitkům, jako je nevolnost z pohybu a narušení ponoření. Vzestup metavesmíru, zahrnujícího sociální interakci, hraní her, školení a digitální dvojčata, si vyžádal nový paradigmat, kde je síť aktivním, vědomým účastníkem poskytování služeb.

Technologie byla motivována potřebou standardizovaného, síťově-uvědomělého klienta, který by mohl dynamicky vyjednávat servisní požadavky. Bez takového klienta by každá aplikace metavesmíru musela implementovat proprietární a neinteroperabilní metody pro interakci s různými síťovými operátory, což by dusilo růst ekosystému. MMEC poskytuje společnou abstraktní vrstvu, která umožňuje vývojářům aplikací specifikovat 'záměr' (např. 'ponořující [AR](/mobilnisite/slovnik/ar/) relace') místo příkazů na nízké síťové úrovni. To umožňuje operátorům optimalizovat své prostředky pomocí nástrojů, jako je síťové dělení, kde může být pro relaci MMEC vytvořena vyhrazená část (slice) se zaručeným výkonem. Jeho vznik je přímou reakcí na posun průmyslu směrem k architekturám založeným na službách a programovatelnosti sítě, s cílem otevřít nové zdroje příjmů z prémiových XR služeb.

## Klíčové vlastnosti

- Správa relací pro ponořující XR aplikace a aplikace metavesmíru
- Dynamické vyjednávání toků QoS pro vysokou šířku pásma a nízkou latenci
- Integrace s edge computingem (MEC) pro přesun výpočetní zátěže
- Podpora mobility a předávání s ohledem na aplikaci
- Standardizované rozhraní k jádru sítě 3GPP (např. přes NEF)
- Abstrakce síťové složitosti pro vývojáře aplikací

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC

---

📖 **Anglický originál a plná specifikace:** [MMEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmec/)
