---
slug: "ica"
url: "/mobilnisite/slovnik/ica/"
type: "slovnik"
title: "ICA – Inter-Channel Alignment"
date: 2025-01-01
abbr: "ICA"
fullName: "Inter-Channel Alignment"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ica/"
summary: "Funkce správy a účtování, která sladí data o využití a účtování napříč více kanály přenosu (např. pro hlas a data) používanými jednou relací služby. Zajišťuje konzistentní fakturaci a vynucování polit"
---

ICA je funkce správy a účtování, která sladí data o využití a účtování napříč více kanály přenosu v rámci jedné relace služby, aby zajistila konzistentní fakturaci a vynucování politik.

## Popis

Inter-Channel Alignment (ICA) je koncept v rámci architektury účtování a správy 3GPP, konkrétně definovaný v kontextu služeb IP Multimedia Subsystem (IMS) a paketové domény ([PS](/mobilnisite/slovnik/ps/)). Řeší scénář, kdy jedna relace uživatelské služby (např. videohovor) využívá více současných přenosových kanálů [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) nebo datových toků služby – například jeden pro hlasový médium, jeden pro video médium a jeden signalizaci. ICA zajišťuje, že účtovací systémy (Online Charging System - [OCS](/mobilnisite/slovnik/ocs/), Offline Charging System - [OFCS](/mobilnisite/slovnik/ofcs/)) mohou všechny tyto jednotlivé datové toky korelovat se stejnou nadřazenou instancí služby.

Architektura zahrnuje komponenty v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Klíčovými prvky jsou Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a účtovací triggery v síťových uzlech, jako je [P-GW](/mobilnisite/slovnik/p-gw/)/[PDN-GW](/mobilnisite/slovnik/pdn-gw/) nebo SMF/UPF. Při zahájení služby aplikační funkce (AF), například IMS Call Session Control Function (CSCF), informuje PCRF o relaci služby a jejích přidružených mediálních komponentách. PCRF následně nainstaluje odpovídající filtry datových toků služby a účtovací pravidla do brány. Zásadně přiřadí společný identifikátor ICA všem pravidlům PCC patřícím do stejné relace služby. Tento identifikátor je zahrnut ve všech účtovacích událostech (Credit Control Requests, Charging Data Records) generovaných pro tyto toky.

Funguje to prostřednictvím šíření identifikátoru. Identifikátor ICA, poskytnutý AF, je předán přes PCRF do brány provádějící politiky. Každá zpráva o využití odeslaná do účtovacího systému nese tento identifikátor. Účtovací systémy používají identifikátor ICA ke seskupení všech dílčích záznamů, aplikaci správného tarifu a vygenerování jediné konsolidované položky za uživatelský zážitek ze služby. Tím se zabrání tomu, aby uživatel dostal samostatné, matoucí účty za hlasové minuty, video data a signalizaci spojené s jedním hovorem. Také umožňuje přesné vynucování politik, jako je aplikace jediné datové kvóty pro celou multimediální relaci.

## K čemu slouží

ICA byla vytvořena, aby vyřešila výzvy v oblasti účtování a řízení politik, které přinesly služby IMS a multimediální služby. Tradiční hlas v přepojování okruhů měl jediný přenosový kanál, což činilo účtování přímočarým. S IMS může jediná služba, jako je Multimedia Telephony (MMTel), dynamicky vytvářet více IP toků s různými charakteristikami QoS pro audio, video a sdílení dat.

Problém, který řeší, je oddělení účtovacích záznamů od logické služby. Bez ICA by každý mediální tok generoval nezávislé účtovací záznamy, což by vedlo k nesprávnému účtování, neschopnosti aplikovat relací založené tarify a složitým problémům zákaznické podpory. Předchozí přístupy postrádaly standardizovanou metodu, jak tyto toky v síti vzájemně svázat. ICA poskytuje potřebný korelační mechanismus, motivovaný komerční potřebou přesného, srozumitelného a na službu zaměřeného účtování pro sítě nové generace. Zajišťuje, že obchodní logika služby (např. 'účtování za hovor') může být správně implementována přes paketovou síť s více souběžnými kanály.

## Klíčové vlastnosti

- Poskytuje jedinečný identifikátor ICA pro korelaci více datových toků služby s jedinou relací služby
- Integruje se s architekturou PCC, zahrnuje AF, PCRF a brány
- Podporuje jak online, tak offline účtovací systémy (OCS, OFCS)
- Umožňuje konsolidované účtování pro komplexní IMS služby, jako jsou videohovory
- Umožňuje konzistentní vynucování politik napříč všemi mediálními komponentami relace
- Definována pro použití s přenosovými kanály IP-CAN v sítích GPRS, EPS a 5GS

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [ICA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ica/)
