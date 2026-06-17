---
slug: "apf"
url: "/mobilnisite/slovnik/apf/"
type: "slovnik"
title: "APF – API Publishing Function"
date: 2026-01-01
abbr: "APF"
fullName: "API Publishing Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/apf/"
summary: "API Publishing Function (APF) je síťová funkce 3GPP, která bezpečně zpřístupňuje standardizovaná severojižní API autorizovaným aplikačním funkcím (AF) třetích stran. Funguje jako řízená brána, která u"
---

APF (funkce publikování API) je síťová funkce 3GPP, která bezpečně zpřístupňuje standardizovaná severojižní API autorizovaným aplikačním funkcím třetích stran a funguje jako řízená brána pro zpřístupňování služeb a využívání síťových schopností.

## Popis

[API](/mobilnisite/slovnik/api/) Publishing Function (APF) je klíčová komponenta v rámci architektury založené na službách (SBA) 3GPP, konkrétně definovaná v rámci Common API Framework ([CAPIF](/mobilnisite/slovnik/capif/)) pro systémy 5G. Funguje jako centrální entita zodpovědná za správu a publikování dostupnosti standardizovaných síťových aplikačních programových rozhraní (API) externím konzumentům, známým jako aplikační funkce ([AF](/mobilnisite/slovnik/af/)). APF udržuje komplexní katalog dostupných API, který detailně popisuje jejich funkčnost, verze a koncové body služeb (reprezentované API Invokery), kde k nim lze přistupovat. Slouží jako primární bod pro zjišťování dostupnosti (discovery) pro AF, které chtějí využít schopnosti sítě 3GPP, jako je řízení kvality služeb (QoS), informace o poloze, monitorování stavu sítě nebo interakce s účtováním.

Architektonicky je APF logická funkce, kterou lze nasadit jako součást jádra CAPIF nebo v rámci konkrétní domény. Rozhraní má k dalším základním funkcím CAPIF, zejména k API Publishing Function (sama sobě pro správu), k API Invoker Management Function (AIMF), která spravuje entity hostující koncové body API, a spoléhá na bezpečnostní funkce CAPIF pro ověřování a autorizaci. APF přímo nezpracovává provoz spojený s voláním API; místo toho publikuje informace nezbytné pro to, aby AF mohlo objevit a následně vyvolat API na správném koncovém bodě (API Invoker). Toto publikování zahrnuje technické detaily, jako je název API, verze, protokol, datové formáty a síťová adresa obslužného API Invokeru.

Provoz APF se řídí zásadami a zahrnuje několik klíčových procedur. Když je nasazeno nové API nebo je existující aktualizováno, poskytovatel API (např. síťová funkce jako [NEF](/mobilnisite/slovnik/nef/) nebo [PCF](/mobilnisite/slovnik/pcf/)) zaregistruje své API u APF prostřednictvím rozhraní pro publikování API. APF tuto registraci ověří vůči zásadám a aktualizuje svůj katalog. AF, které hledá dostupná API, se dotazuje APF, typicky po vzájemném ověření. APF odpoví filtrovaným seznamem API, která je AF oprávněna vidět a používat, na základě přihlašovacích údajů AF a předplatného. Tento proces zjišťování je základním kamenem pro umožnění dynamického, škálovatelného ekosystému, kde mohou být síťové schopnosti nabízeny jako služba.

Její role v síti spočívá v umožnění bezpečného a spravovatelného zpřístupňování služeb. Centralizací publikace API poskytuje APF jediný zdroj pravdy o dostupnosti API, zjednodušuje zjišťování pro vývojáře aplikací a umožňuje síťovým operátorům udržovat kontrolu nad tím, které schopnosti jsou komu zpřístupněny. Je klíčovým prvkem pro segmentaci vertikálních trhů, zpřístupňování služeb síťového řezání a integraci sítí 5G s podnikovými [IT](/mobilnisite/slovnik/it/) systémy a aplikacemi třetích stran v cloudu, čímž tvoří páteř paradigmatu programovatelné sítě.

## K čemu slouží

APF byla vytvořena, aby řešila kritickou potřebu standardizovaného, bezpečného a spravovatelného zpřístupňování schopností sítí 3GPP externím aplikacím. Před její specifikací ve verzi 3GPP Release 15 byly mechanismy zpřístupňování služeb často proprietární, fragmentované a postrádaly jednotný bezpečnostní rámec. To mobilním síťovým operátorům ztěžovalo a zvyšovalo riziko otevírání jejich sítí vývojářům třetích stran a vertikálním průmyslům (např. automobilovému, zdravotnictví, výrobě), což dusilo inovace a vytváření nových zdrojů příjmů mimo základní konektivitu.

Zavedení APF jako součásti širšího [CAPIF](/mobilnisite/slovnik/capif/) bylo motivováno vizí 5G podporovat rozmanité případy užití a průmyslové vertikály. Tyto vertikály vyžadují programovatelný přístup ke specifickým síťovým funkcím – jako je garantovaná latence, spolehlivá šířka pásma nebo poloha zařízení – aby mohly budovat specializované aplikace. APF řeší problém, jak tyto externí entity mohou dynamicky zjistit, jaké síťové služby jsou dostupné, porozumět tomu, jak k nim přistupovat, a být k tomu ověřeny. Poskytuje nezbytnou vrstvu správy, která zajišťuje, že zpřístupňování není ad-hoc proces, ale spravovaná služba s řádným ověřováním, autorizací, auditováním a správou životního cyklu publikovaných [API](/mobilnisite/slovnik/api/).

Vytvořením společného rámce pro publikování a zjišťování API APF snižuje složitost integrace jak pro síťové operátory, tak pro poskytovatele aplikací. Řeší omezení předchozích nestandardizovaných přístupů tím, že poskytuje škálovatelný, zásadami řízený model, který podporuje komerční dohody, správu verzí API a centralizované protokolování. To umožňuje prosperující ekosystém, kde mohou být síťové schopnosti konzumovány jako služba, což je zásadní pro naplnění plného ekonomického a technologického potenciálu 5G a budoucích generací mobilních sítí.

## Klíčové vlastnosti

- Centralizovaná správa katalogu API pro všechna publikovaná severojižní API 3GPP
- Standardizovaný mechanismus zjišťování API pro autorizované aplikační funkce (AF)
- Řízení viditelnosti a přístupnosti API na základě zásad
- Podpora správy verzí API a životního cyklu (např. publikování, ukončení podpory)
- Integrace s bezpečnostním rámcem CAPIF pro bezpečné ověřování a autorizaci
- Umožňuje zpřístupňování síťových schopností pro vertikály a služby síťového řezání

## Související pojmy

- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 29.222** (Rel-19) — Common API Framework (CAPIF) for 3GPP Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [APF na 3GPP Explorer](https://3gpp-explorer.com/glossary/apf/)
