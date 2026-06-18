---
slug: "saf"
url: "/mobilnisite/slovnik/saf/"
type: "slovnik"
title: "SAF – Service Announcement Function"
date: 2025-01-01
abbr: "SAF"
fullName: "Service Announcement Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/saf/"
summary: "Síťová funkce v rámci architektury založené na službách (SBA) v 5G, která umožňuje zjišťování a oznamování dostupných služeb aplikacím. Funguje jako registr služeb, díky čemuž si síťové funkce (NF) a"
---

SAF je Service Announcement Function, funkce 5G sítě, která slouží jako registr služeb pro dynamické zjišťování a oznamování dostupných služeb síťovým funkcím (NF) a aplikačním funkcím (AF).

## Popis

Service Announcement Function (SAF) je klíčová komponenta architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) v jádru 5G sítě (5GC). Funguje jako specializovaný repozitář nebo registr, který spravuje dostupnost a přístupnost služeb nabízených různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) a autorizovanými externími aplikačními funkcemi ([AF](/mobilnisite/slovnik/af/)). V paradigmatu SBA jsou síťové schopnosti vystaveny jako znovupoužitelné služby s dobře definovanými rozhraními [API](/mobilnisite/slovnik/api/) a SAF poskytuje mechanismus pro jejich zjišťování.

Architektonicky je SAF samostatná síťová funkce, která komunikuje s ostatními NF prostřednictvím rozhraní založených na službách, primárně za použití [HTTP](/mobilnisite/slovnik/http/)/2 s [JSON](/mobilnisite/slovnik/json/). Typicky spolupracuje s Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), což je hlavní zprostředkovatel zjišťování v 5GC. Zatímco NRF řeší registraci a zjišťování instancí NF (např. nalezení konkrétní [AMF](/mobilnisite/slovnik/amf/) nebo SMF), SAF se zaměřuje na služby nebo servisní schopnosti *uvnitř* sítě nebo *dostupné* síti. Oznamuje, jaké služby jsou dostupné, jejich koncové body, podporované verze a jakákoliv přidružená metadata, jako je geografická poloha nebo podporované názvy datových sítí (DNN).

Jeho fungování je založeno na modelu publikuj-přihlas se (publish-subscribe). Producent služby (např. AF poskytující službu citlivou na latenci pro hraní her nebo Location Management Function) zaregistruje svůj servisní profil u SAF. Tento profil zahrnuje název služby, verzi, URI koncového bodu a další deskriptory. Spotřebitelé služeb (ostatní NF nebo AF) pak mohou dotazovat SAF, aby zjistili dostupné služby odpovídající určitým kritériím. Například edge aplikační server (AF) může oznámit svou přítomnost a schopnosti prostřednictvím SAF, což umožní User Plane Function (UPF) nebo Session Management Function (SMF) jej zjistit pro lokalizované směrování provozu nebo vynucování politik. SAF také může proaktivně zasílat oznámení o dostupnosti služeb přihlášeným spotřebitelům, když jsou registrovány nové služby nebo se mění stav stávajících.

Jeho role je klíčová pro umožnění dynamické, flexibilní orchestrace služeb, zejména ve scénářích edge computingu a síťového řezání. Odděluje poskytovatele služeb od jejich spotřebitelů, což umožňuje agilní nasazování a škálování nových služeb bez nutnosti ruční rekonfigurace všech závislých funkcí. Poskytnutím centralizovaného přehledu dostupných služeb SAF usnadňuje automatizaci, podporuje kontinuitu služeb během mobility a je klíčovým enablerem pro vystavování síťových schopností aplikacím vertikálních odvětví kontrolovaným způsobem, naplňujícím slib 5G o programovatelnosti sítě.

## K čemu slouží

SAF byl vytvořen, aby řešil klíčovou výzvu v architektuře 5G založené na službách (SBA): efektivní a dynamické zjišťování služeb nad rámec prostého zjišťování instancí NF. Zatímco NRF efektivně spravuje životní cyklus a zjišťování *instancí* NF (jako nalezení dostupné SMF), vyvíjející se ekosystém 5G s důrazem na edge computing, síťové řezy a integraci vertikálních odvětví vyžadoval jemnější mechanismus. Aplikace a síťové funkce potřebovaly způsob, jak zjišťovat konkrétní *servisní schopnosti* (např. službu videoanalytiky na konkrétní edge lokalitě, konkrétní API pro reportování kvality uživatelského zážitku), které mohou nabízet různé entity, nejen standardizované NF.

Před SAF bylo vystavování a zjišťování služeb statičtější nebo vyžadovalo přímé, předem nakonfigurované vztahy mezi funkcemi, což bylo nepružné a neškálovatelné. Omezení předchozích přístupů se stala zjevnými s potřebou aplikací s nízkou latencí na edge, kde aplikace na zařízení musí dynamicky zjistit nejbližší instanci služby (jako herní server nebo engine pro zpracování AR). Ruční konfigurace nedokázala držet krok s mobilitou uživatelů a elastickým škálováním služeb v cloudu.

Primární problém, který SAF řeší, je umožnění "tržiště" služeb uvnitř 5G sítě. Umožňuje aplikačním funkcím (AF), které mohou být aplikacemi třetích stran, oznamovat své služby jádru sítě, a síťovým funkcím jádra (NF) tyto služeby zjišťovat a využívat pro vylepšené řízení relací, řízení politik nebo směrování provozu. To bylo motivováno potřebou podporovat nové obchodní modely, jako je Network as a Service (NaaS), a naplnit vizi 5G jako platformy pro inovace, kde vertikální odvětví mohou bezproblémově integrovat své aplikace se síťovými schopnostmi pro optimalizovaný výkon.

## Klíčové vlastnosti

- Dynamická registrace a oznamování servisních profilů od NF a AF
- Dotazovací zjišťování služeb s využitím filtrů (např. název služby, DNN, lokalita)
- Podpora mechanismů publikuj-přihlas se pro oznámení o dostupnosti služeb
- Správa metadat služeb, verzí a informací o koncových bodech
- Integrace s bezpečnostním rámcem 5GC SBA pro ověřenou registraci a zjišťování služeb
- Umožňuje lokalizačně-aware zjišťování služeb klíčové pro nasazení edge computingu

## Související pojmy

- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)

## Definující specifikace

- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point

---

📖 **Anglický originál a plná specifikace:** [SAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/saf/)
