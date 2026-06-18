---
slug: "t-eas"
url: "/mobilnisite/slovnik/t-eas/"
type: "slovnik"
title: "T-EAS – Target Edge Application Server"
date: 2026-01-01
abbr: "T-EAS"
fullName: "Target Edge Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-eas/"
summary: "Edge Application Server (server aplikací na hraně sítě) vybraný sítí pro hostování konkrétní instance aplikace pro UE ve scénářích Edge Computing. Jedná se o koncový bod, na který je směrován aplikačn"
---

T-EAS je Edge Application Server (cílový server aplikací na hraně sítě) vybraný sítí pro hostování konkrétní instance aplikace a fungující jako koncový bod přenosu pro UE ve scénářích Edge Computing.

## Popis

Target Edge Application Server (T-EAS) je funkční entita definovaná v rámci architektury Edge Computing ([EDGE](/mobilnisite/slovnik/edge/)) podle 3GPP. Představuje konkrétní instanci Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)), která je určena k obsluze uživatelského zařízení (UE) poté, co bylo rozhodnuto o přesunu, migraci nebo počátečním přiřazení aplikační relace. Výběr T-EAS je klíčovým výsledkem procedur objevování a výběru EAS, které řídí Edge Enabler Client ([EEC](/mobilnisite/slovnik/eec/)) v UE a Edge Enabler Server ([EES](/mobilnisite/slovnik/ees/)) v síti. Když aplikace vyžaduje prostředky edge computingu (jako nízkou latenci nebo lokální zpracování dat), síť pomáhá UE najít vhodný EAS. T-EAS je konečný zvolený cíl.

Proces zahrnuje několik kroků. EEC, případně aktivovaný aplikačním požadavkem, kontaktuje svůj přidružený EES. EES, který má přehled o dostupných instancích EAS a jejich schopnostech (prostřednictvím registrace u Edge Configuration Server), provede objevování EAS. Na základě faktorů, jako je poloha UE, požadavky aplikace, vytížení EAS a síťové politiky, EES vybere kandidátský EAS a poskytne jeho informace (včetně IP adresy nebo [FQDN](/mobilnisite/slovnik/fqdn/)) EEC jako T-EAS. UE poté naváže přímé spojení na aplikační vrstvě (např. [TCP/IP](/mobilnisite/slovnik/tcp-ip/)) s tímto T-EAS. Ve scénářích mobility nebo měnících se podmínek může být nutné přenést aplikační relaci z předchozího EAS (Source EAS) na nový T-EAS. Tento postup přesunu spravuje síť s cílem zachovat kontinuitu relace.

T-EAS hostuje vlastní aplikační logiku nebo funkci zpracování dat. Je typicky nasazen na hraně sítě, blízko rádiové přístupové sítě, aby se minimalizovala latence. Role T-EAS je klíčová pro naplnění slibů edge computingu: umožnění komunikace s ultra spolehlivou nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), podpora přesunu výpočetní zátěže pro zařízení IoT a usnadnění pokročilých služeb, jako je rozšířená realita. Specifikace 3GPP definují protokoly a [API](/mobilnisite/slovnik/api/) (např. v 23.558 a 29.558) pro procedury objevování, výběru a přesunu, které nakonec identifikují T-EAS.

## K čemu slouží

Koncept T-EAS byl vytvořen, aby formalizoval výběr koncového bodu ve standardizovaném rámci Edge Computing od 3GPP. Před touto standardizací bylo nasazování aplikací na hraně závislé na proprietárních nebo cloudově orientovaných metodách, které postrádaly integraci s řízením mobilní sítě. To ztěžovalo dynamický, sítí asistovaný výběr optimálního edge serveru na základě reálných podmínek (jako je mobilita UE nebo zatížení sítě). Pracovní položka EDGE měla za cíl bezproblémově integrovat edge computing do systému 5G.

T-EAS řeší problém, jak dynamicky a efektivně směrovat aplikační provoz UE k nejvhodnější instanci edge serveru. Poskytuje jasný cíl pro výběrové algoritmy sítě, což umožňuje optimalizované poskytování služeb. To je zásadní pro aplikace citlivé na latenci nebo polohu, jako je komunikace vozidlo-se-vším (V2X) nebo řízení průmyslového IoT. Díky standardizované entitě 'cíle' mohou být procedury pro navázání, přesun a ukončení relace řízeny jednotně, což zajišťuje interoperabilitu mezi UE, síťovými funkcemi a poskytovateli aplikací na hraně sítě.

## Klíčové vlastnosti

- Vybraná instance Edge Application Server pro aplikační relaci UE
- Identifikována prostřednictvím procedur objevování a výběru EAS
- UE naváže přímé spojení na aplikační vrstvě s T-EAS
- Může být nový EAS nebo cíl pro přesun relace
- Hostuje aplikační logiku nebo zpracování dat na hraně sítě
- Nasazen na hraně sítě, aby poskytoval službu s nízkou latencí

## Související pojmy

- [EAS – Enterprise Application Server](/mobilnisite/slovnik/eas/)
- [EES – Edge Enablement Server](/mobilnisite/slovnik/ees/)
- [EEC – Ethernet Equipment Clock](/mobilnisite/slovnik/eec/)
- [ECS – Edge Configuration Server](/mobilnisite/slovnik/ecs/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [T-EAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-eas/)
