---
slug: "moba"
url: "/mobilnisite/slovnik/moba/"
type: "slovnik"
title: "MOBA – Multiplayer Online Battle Arena"
date: 2025-01-01
abbr: "MOBA"
fullName: "Multiplayer Online Battle Arena"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/moba/"
summary: "MOBA označuje žánr online strategických videoher v reálném čase, často zahrnujících týmový boj v definované aréně. V kontextu 3GPP se vztahuje k požadavkům na výkon sítě pro takové interaktivní herní"
---

MOBA je žánr online videoher citlivých na latenci, který pohání specifikace 3GPP pro výkon mobilních sítí s nízkou latencí a vysokou spolehlivostí.

## Popis

Ve specifikacích 3GPP není Multiplayer Online Battle Arena (MOBA) protokolem nebo síťovou funkcí jako takovou, ale reprezentativním typem služby používaným k definování a vyhodnocování požadavků na výkon sítě. Je klíčovým případem užití zvažovaným při vývoji funkcí rozšířeného mobilního širokopásmového přístupu (eMBB) a ultra-spolehlivé komunikace s nízkou latencí (URLLC). Charakteristiky žánru – hra v reálném čase, synchronní, týmová, s častými interakcemi malých paketů – jej činí vysoce citlivým na síťovou latenci, zpoždění (jitter) a ztrátu paketů. Technické specifikace 3GPP, zejména ty z pracovních skupin pro aspekty služeb a systémů (SA), analyzují vzorce provozu MOBA, aby odvodily kvantitativní klíčové ukazatele výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)) pro systém 5G. Tyto KPI informují o návrhu síťových funkcí, rámců kvality služeb (QoS) a algoritmů pro správu rádiových prostředků, aby byla zajištěna přijatelná kvalita uživatelského prožitku (QoE).

Architektonický dopad podpory služeb typu MOBA je patrný napříč jádrem sítě 5G (5GC) a novou generací rádiové přístupové sítě (NG-RAN). 5GC musí implementovat politiky správy relací, které upřednostňují toky provozu MOBA s přísnými identifikátory třídy kvality služeb ([QCI](/mobilnisite/slovnik/qci/)) nebo identifikátory kvality služeb 5G ([5QI](/mobilnisite/slovnik/5qi/)). Funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) spolupracují na vytváření relací přenosových datových jednotek (PDU) se zaručenými přenosovými rychlostmi a nízkým rozpočtem zpoždění paketů. Na rádiové straně musí gNB využívat rychlé plánování, podporu edge computingu prostřednictvím umístění funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a potenciálně nové techniky fyzické vrstvy, aby se minimalizovala latence na rádiovém rozhraní.

Klíčové síťové komponenty zapojené do poskytování služeb MOBA zahrnují uživatelské zařízení (UE), které generuje herní provoz; gNB, který musí plánovat prostředky s minimálním zpožděním; UPF, která může být nasazena na okraji sítě pro snížení přenosové latence; a funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), která poskytuje pravidla politik řídících QoS pro herní relaci. Role MOBA jako benchmarkové služby je klíčová pro ověřování možností síťového řezání, kde by pro prémiový herní provoz mohl být vytvořen vyhrazený řez s optimalizovanými prostředky, což zajišťuje izolaci od provozu s běžným úsilím a konzistentní výkon.

## K čemu slouží

Zařazení MOBA jako definovaného typu služby do specifikací 3GPP slouží jasnému účelu: poskytnout konkrétní, náročnou reálnou aplikaci pro vedení vývoje schopností sítí 5G a dalších generací. Před 5G byly mobilní sítě primárně optimalizovány pro asymetrický provoz (jako je prohlížení webu a streamování videa) a nemohly konzistentně garantovat nízké latence a vysokou spolehlivost požadovanou interaktivním hraním v reálném čase. Rozšíření mobilního hraní, a zejména konkurenčních titulů MOBA, vytvořilo poptávku trhu po síťovém výkonu, na který architektura 4G LTE nebyla navržena.

Práce 3GPP na požadavcích MOBA přímo řeší omezení předchozích generací mobilních sítí stanovením kvantifikovaných cílů pro koncovou latenci, zpoždění (jitter) a pravděpodobnost ztráty paketů. Tato formalizace motivuje a ospravedlňuje zavedení nových funkcí 5G, jako je síťové řezání, edge computing ([MEC](/mobilnisite/slovnik/mec/)) a vylepšené mechanismy URLLC. Analýzou konkrétní služby kritické na latenci mohou normalizační orgány zajistit, že vyvinutá síťová architektura není jen teoreticky schopná, ale je prakticky ověřena proti známým náročným modelům provozu. Tento přístup pomáhá překlenout propast mezi abstraktními síťovými schopnostmi a hmatatelnými uživatelskými prožitky.

## Klíčové vlastnosti

- Představuje model provozu interaktivního hraní citlivého na latenci
- Pohání požadavky na ultra-spolehlivou komunikaci s nízkou latencí (URLLC)
- Používá se k definování klíčových ukazatelů výkonnosti (KPI) pro QoS v 5G
- Informuje o případech užití síťového řezání pro vyhrazené herní služby
- Ovlivňuje strategie nasazení edge computingu (MEC) pro snížení latence
- Poskytuje benchmark pro vyhodnocování algoritmů rádiového plánování a přidělování prostředků

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [MOBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/moba/)
