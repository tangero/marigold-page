---
slug: "opg"
url: "/mobilnisite/slovnik/opg/"
type: "slovnik"
title: "OPG – Operator Platform Group"
date: 2026-01-01
abbr: "OPG"
fullName: "Operator Platform Group"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/opg/"
summary: "Operator Platform Group (OPG) je řídicí rámec 3GPP, který operátorům umožňuje zpřístupňovat síťové schopnosti a data aplikacím třetích stran prostřednictvím standardizovaných API. Usnadňuje bezpečnou"
---

OPG je řídicí rámec 3GPP, který operátorům umožňuje bezpečně zpřístupňovat síťové schopnosti a data aplikacím třetích stran prostřednictvím standardizovaných API za účelem podpory inovací služeb.

## Popis

Operator Platform Group (OPG) je komplexní architektonický rámec definovaný v rámci domény řízení a orchestrace ([MANO](/mobilnisite/slovnik/mano/)) konsorcia 3GPP. Jeho hlavní funkcí je poskytnout standardizovaný, bezpečný a řízený mechanismus, který mobilním síťovým operátorům ([MNO](/mobilnisite/slovnik/mno/)) umožňuje zpřístupňovat své síťové schopnosti, data a služby autorizovaným poskytovatelům aplikací ([AP](/mobilnisite/slovnik/ap/)) třetích stran. Toto zpřístupnění je realizováno prostřednictvím sady severovýchodních aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), která abstrahují základní komplexitu sítě 3GPP. OPG funguje jako důvěryhodný zprostředkovatel, který zajišťuje, že aplikace třetích stran mohou využívat síťové služby – jako je správa kvality služeb (QoS), informace o poloze, stav sítě nebo prostředky edge computingu – aniž by vyžadovaly hlubokou znalost interních protokolů sítě nebo získaly přímý, neomezený přístup k síťovým prvkům.

Architektura OPG je soustředěna kolem klíčových funkčních entit definovaných v dokumentech jako TS 23.558. Ústřední součástí je Operator Platform Exposure Function (OPEF), která je zodpovědná za zpřístupnění API, autentizaci a autorizaci požadavků od AP. Překládá volání API do interních síťových příkazů. Rámec také definuje roli Operator Platform Data Collection Function (OPDCF), která agreguje a zpracovává data z různých síťových funkcí a uživatelských zařízení. Dále architektura zahrnuje Operator Platform Gateway (OPGW), která může sloužit jako jediný vstupní bod pro požadavky API, a Operator Platform Enabler (OPE), která poskytuje společné podpůrné funkce, jako je zjišťování služeb. Tyto entity spolupracují a často interagují s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) z jádra 5G pro registraci a zjišťování služeb.

Z provozní perspektivy OPG implementuje robustní model správy. Řídí celý životní cyklus API produktů, včetně publikace, předplatného a správy verzí. Vynucuje přísné bezpečnostní politiky, provádí autentizaci AP (často pomocí OAuth 2.0) a autorizaci na základě předdefinovaných smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a politik. OPG také zvládá správu provozu, včetně omezení rychlosti a regulace, aby ochránila síť před přetížením. Poskytuje komplexní monitorování, analytiku a zprostředkování účtování, generuje záznamy o využití, které mohou být předávány do zúčtovacích systémů. Poskytnutím této řízené vrstvy pro zpřístupnění umožňuje OPG případy užití, jako je dynamická QoS pro podnikové aplikace, hraní her v reálném čase se zárukami nízké latence, služby rozšířené reality využívající edge computing a správa zařízení IoT s rozšířenými kontrolami konektivity.

## K čemu slouží

OPG bylo vytvořeno, aby řešilo základní výzvu éry 5G: monetizaci sítě nad rámec základní konektivity. Předchozí generace mobilních sítí byly do značné míry uzavřené systémy, jejichž schopnosti byly přístupné pouze vlastním službám operátora. To omezovalo inovace a ztěžovalo vývojářům třetích stran vytvářet aplikace, které by mohly využívat jedinečné síťové atributy, jako je nízká latence, vysoká spolehlivost nebo přesná poloha zařízení. Vzestup cloud-nativních architektur a servisně orientované architektury ([SBA](/mobilnisite/slovnik/sba/)) jádra 5G vytvořil technický základ pro zpřístupnění, ale chyběla standardizovaná, komerční a bezpečná platforma.

Hlavním účelem OPG je transformovat mobilní síť z pouhé konektivní trubky na programovatelnou platformu. Řeší problém fragmentovaných proprietárních řešení pro zpřístupnění tím, že poskytuje standardizovaný rámec 3GPP. Tím se snižují integrační náklady pro poskytovatele aplikací a operátoři mohou konzistentně nabízet své schopnosti na různých trzích. Řeší kritické obavy týkající se bezpečnosti a integrity sítě tím, že dává operátorovi plnou kontrolu nad tím, co je zpřístupněno, komu a za jakých podmínek. OPG umožňuje nové obchodní modely, jako je Network-as-a-Service (NaaS), kde mohou podniky programově a na požádání žádat a platit za konkrétní síťové řezy nebo úrovně QoS, čímž se odemykají nové zdroje příjmů z vertikálních odvětví, jako je výroba, automobilový průmysl a zdravotnictví.

## Klíčové vlastnosti

- Standardizovaná severovýchodní API pro zpřístupnění síťových schopností (např. QoS, poloha, šířka pásma na požádání)
- Komplexní správa životního cyklu API včetně publikace, zjišťování a předplatného
- Robustní bezpečnostní rámec s autentizací založenou na OAuth 2.0 a podrobnými autorizačními politikami
- Schopnosti správy provozu a jeho regulace, jako je omezení rychlosti a regulace, pro ochranu síťových zdrojů
- Integrované monitorování, analytika a zprostředkování účtování pro komerční monetizaci API
- Podpora pro zpřístupnění prostředků edge computingu a mobility aplikací

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [OPG na 3GPP Explorer](https://3gpp-explorer.com/glossary/opg/)
