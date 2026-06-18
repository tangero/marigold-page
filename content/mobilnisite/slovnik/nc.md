---
slug: "nc"
url: "/mobilnisite/slovnik/nc/"
type: "slovnik"
title: "NC – Network Control Mode"
date: 2025-01-01
abbr: "NC"
fullName: "Network Control Mode"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nc/"
summary: "Konfigurační parametr síťových prvků, zejména v samoorganizujících se sítích (SON), který definuje míru autonomie udělené uzlu pro provádění provozních rozhodnutí. Režimy zahrnují NC0 (plně manuální),"
---

NC je konfigurační parametr síťových prvků, který definuje míru autonomie udělené uzlu pro provádění provozních rozhodnutí, vyvažující centrální řízení s distribuovanou inteligencí.

## Popis

Network Control Mode (NC) je základní provozní koncept v rámci řídicího rámce 3GPP, zvláště klíčový pro funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)). Definuje stupeň automatizace a místo řízení pro úlohy správy a optimalizace sítě. Režim je typicky konfigurován na úrovni jednotlivých síťových prvků (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) nebo jednotlivých SON funkcí a určuje, zda rozhodnutí činí samotný síťový prvek (distribuovaný SON), centrální řídicí systém (centralizovaný SON), nebo prostřednictvím hybridního přístupu. Tři hlavní režimy jsou NC0, [NC1](/mobilnisite/slovnik/nc1/) a [NC2](/mobilnisite/slovnik/nc2/), z nichž každý představuje jinou rovnováhu mezi dohledem lidského operátora a automatizací řízenou strojem.

NC0 neboli manuální režim představuje tradiční přístup k řízení sítě. V tomto režimu jsou všechny konfigurační, optimalizační a obnovovací akce po poruše plánovány a prováděny manuálně síťovými operátory prostřednictvím systému Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)). Síťový prvek funguje striktně podle své statické konfigurace a poskytuje systému OAM měření výkonu, ale neiniciuje žádné autonomní změny. Tento režim nabízí maximální kontrolu a předvídatelnost, ale je pomalý v reakci na dynamické síťové podmínky a špatně škáluje s velkými a hustými sítěmi.

NC1 neboli asistovaný režim zavádí určitou míru automatizace při zachování centrálního dohledu. V tomto hybridním režimu může síťový prvek (distribuovaný SON) nebo vyhrazený SON server (centralizovaný SON) analyzovat data o výkonu a generovat doporučení pro konfigurační změny. Tato doporučení však nejsou automaticky aplikována. Místo toho jsou předložena síťovému operátorovi prostřednictvím systému OAM k posouzení a manuálnímu schválení. To umožňuje operátorům využít datové zpracovací schopnosti SON algoritmů při zachování lidského činitele ve smyčce pro validaci, zejména u kritických změn, které by mohly ovlivnit službu.

NC2 neboli plně automatický režim představuje nejvyšší úroveň automatizace. Zde je SON funkci (ať už distribuované v uzlu, nebo centralizované) udělena pravomoc autonomně analyzovat síťové podmínky, činit optimalizační rozhodnutí a přímo aplikovat potřebné konfigurační změny na síťový prvek bez nutnosti předchozího lidského schválení. To umožňuje reálnou nebo téměř reálnou adaptaci na kolísání provozu, interference, poruchy a integraci nových buněk. NC2 je nezbytný pro dosažení plných výhod SON, jako je rychlé samoléčení a průběžná optimalizace, vyžaduje však robustní, důkladně otestované algoritmy a komplexní rámce politik, aby se zabránilo nestabilnímu nebo nežádoucímu chování sítě.

## K čemu slouží

Koncept Network Control Mode byl vytvořen, aby poskytl strukturovanou a postupnou cestu operátorům pro zavádění automatizace do jejich sítí, konkrétně prostřednictvím [SON](/mobilnisite/slovnik/son/) funkcí definovaných od 3GPP Release 8 a dále. Před SON byly nasazení sítě, její optimalizace a údržba zcela manuálními procesy, které se s růstem velikosti a složitosti sítí v éře LTE a heterogenních nasazení zahrnujících makro buňky, small buňky a různá kmitočtová pásma staly neúměrně drahé, pomalé a náchylné k chybám.

Hlavním problémem, který NC režimy řeší, je "důvěrová propast" v síťové automatizaci. Přechod od plně manuálního modelu k plně autonomnímu představuje pro operátory významný provozní a kulturní posun. Hierarchie NC0, [NC1](/mobilnisite/slovnik/nc1/), [NC2](/mobilnisite/slovnik/nc2/) poskytuje řízenou migrační cestu s ohledem na rizika. Operátor mohou začít s NC1 (asistovaným režimem) u nekritických optimalizačních funkcí, což jejich týmům umožní získat důvěru v SON algoritmy prostřednictvím posuzování doporučení před jejich aplikací. Jakmile se algoritmy osvědčí jako spolehlivé za různých podmínek, mohou operátoři převést konkrétní funkce do NC2 (plně automatického režimu), aby dosáhli provozní efektivity a rychlejších reakčních dob.

Navíc NC režimy umožňují flexibilitu na základě kritičnosti síťové funkce a provozní filozofie operátora. Například operátor může provozovat funkci Mobility Load Balancing v režimu NC2 pro rychlou reakci na přetížení, ale řešení konfliktů Physical Cell ID může provozovat v režimu NC1, aby zajistil manuální dohled nad základním rádiovým parametrem. Tento koncept také usnadňuje multi-vendorovou interoperabilitu v SON, neboť definuje jasná rozhraní a odpovědnosti mezi síťovým prvkem (který změny provádí) a řídicím systémem (který je může autorizovat), v závislosti na nakonfigurovaném režimu. Tento strukturovaný přístup k delegování řízení je základním kamenem moderního, softwarově definovaného a autonomního řízení mobilních sítí.

## Klíčové vlastnosti

- Definuje tři provozní režimy: Manuální (NC0), Asistovaný (NC1) a Plně automatický (NC2)
- Řídí úroveň autonomie funkcí samoorganizujících se sítí (SON)
- Poskytuje řízenou migrační cestu od manuálních k plně automatizovaným operacím
- Umožňuje hybridní modely řízení, kde algoritmy navrhují změny a lidé je schvalují (NC1)
- Umožňuje optimalizaci sítě v reálném čase a samoléčení v režimu NC2
- Standardizuje interakci mezi síťovými prvky a řídicími systémy pro automatizované akce

## Definující specifikace

- **TS 32.303** (Rel-9) — Notification IRP CORBA Solution Set
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties
- **TR 44.901** (Rel-19) — Extended NACC for External Cell Change

---

📖 **Anglický originál a plná specifikace:** [NC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nc/)
