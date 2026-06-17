---
slug: "a-csi"
url: "/mobilnisite/slovnik/a-csi/"
type: "slovnik"
title: "A-CSI – Aperiodic Channel State Information"
date: 2025-01-01
abbr: "A-CSI"
fullName: "Aperiodic Channel State Information"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/a-csi/"
summary: "Aperiodické CSI (A-CSI) je dynamický mechanismus hlášení v 5G NR, při kterém gNB vyvolá UE, aby nahlásilo informace o stavu kanálu na vyžádání prostřednictvím DCI. Poskytuje včasnou a přesnou zpětnou"
---

A-CSI je dynamický mechanismus hlášení v 5G NR, při kterém gNB vyvolá (trigger) UE, aby poskytlo informace o stavu kanálu na vyžádání, což umožňuje včasnou adaptaci spojení a rozhodnutí při plánování přenosů.

## Popis

Aperiodické informace o stavu kanálu (A-CSI) jsou základním mechanismem zpětné vazby ve fyzické vrstvě 5G New Radio (NR), konkrétně definovaným pro rozhraní Uu mezi uživatelským zařízením (UE) a gNodeB (gNB). Na rozdíl od periodického nebo semi-persistentního hlášení CSI je A-CSI vyvoláváno dynamicky a na vyžádání sítí prostřednictvím řídicích informací v downlinku (DCI) na Physical Downlink Control Channel (PDCCH). Tento podnět je vložen do povolení pro uplink (DCI formát 0_1 nebo 0_2) nebo v některých případech do přiřazení pro downlink, čímž se UE instruuje, aby provedlo okamžité měření CSI a nahlásilo jej v následném přenosu na Physical Uplink Shared Channel (PUSCH). Proces je úzce integrován s rámcem plánování NR, což umožňuje gNB vyžádat si CSI přesně v okamžiku potřeby, například před plánováním vysoko-prioritního přenosu nebo při podezření na změnu podmínek kanálu.

Konfigurace hlášení A-CSI je stanovena signalizací vyšší vrstvy RRC (CSI-ReportConfig), která definuje podrobné parametry pro hlášení. To zahrnuje množství informací v hlášení CSI (např. indikátor kvality kanálu (CQI), indikátor předkódovací matice (PMI), indikátor hodnosti (RI), indikátor vrstvy (LI) a indikátor zdroje CSI-RS (CRI)), přidruženou sadu zdrojů CSI-RS pro měření a časové chování nastavené na 'aperiodic'. Když se gNB rozhodne, že je vyžadováno hlášení A-CSI, odešle DCI, které obsahuje pole žádosti o CSI. Toto pole odkazuje na jeden nebo více spouštěcích stavů (trigger states), z nichž každý odkazuje na sadu CSI-ReportConfigs. Po přijetí a dekódování podnětu UE změří nakonfigurované referenční signály pro informace o stavu kanálu (CSI-RS), vypočítá požadované metriky CSI a multiplexuje užitečná data hlášení CSI do přiděleného zdroje PUSCH, jak je uvedeno ve stejném povolení DCI.

Mezi klíčové architektonické komponenty zapojené do A-CSI patří zdroje CSI-RS vysílané gNB pro sondování kanálu, jednotka pro zpracování fyzické vrstvy UE pro odhad kanálu a výpočet CSI, vrstva MAC pro zpracování spouštěče DCI a vrstva RRC pro správu semi-statické konfigurace. Úlohou A-CSI v síti je poskytnout plánovači gNB snímek stavu downlink kanálu s nízkou latencí a vysokou přesností. Tyto informace jsou kritické pro několik funkcí správy rádiových zdrojů (RRM): adaptivní modulaci a kódování (výběr MCS na základě CQI), uzavřenou smyčku prostorového multiplexování (výběr prekódoru na základě PMI/RI), správu beamů (výběr beamu na základě CRI) a adaptaci spojení. Díky své aperiodické povaze se vyhýbá stálé režii periodického hlášení a zároveň poskytuje aktuálnější a situačně relevantnější data než semi-persistentní hlášení, což jej činí ideálním pro dynamická prostředí a vzorce provozu.

## K čemu slouží

A-CSI bylo zavedeno ve 3GPP Release 15 jako součást základního rámce 5G NR, aby řešilo omezení mechanismů zpětné vazby CSI v LTE při podpoře různorodých a náročných požadavků 5G. LTE se primárně spoléhalo na periodické (P-CSI) a semi-persistentní hlášení CSI, přenášené na PUCCH. Zatímco tyto metody byly vhodné pro konzistentní provoz, nesly s sebou pevnou režii bez ohledu na potřebu a nemohly poskytnout okamžitou zpětnou vazbu na vyžádání s nízkou latencí požadovanou pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) nebo vysoce dynamický beamforming pro massive MIMO. Pevná periodicita také plýtvala zdroji během období nízké aktivity nebo stabilních kanálů.

Vytvoření A-CSI bylo motivováno potřebou flexibilnějšího, efektivnějšího a rychleji reagujícího systému zpětné vazby o kanálu. 5G NR počítalo se scénáři s extrémní propustností (eMBB), masivním připojením (mMTC) a kritickou spolehlivostí (URLLC), což vyžadovalo, aby síťové zdroje – včetně uplink zdrojů používaných pro řídicí signalizaci – byly využívány pouze tehdy, když je to přínosné. A-CSI to řeší tím, že dává gNB přímou kontrolu nad tím, kdy je CSI hlášeno. To umožňuje síti vyžádat si zpětnou vazbu přesně před plánováním datového přenosu, při detekci selhání beamu a zahájení obnovy nebo při očekávané změně podmínek kanálu. Přímo řeší problém režie odstraněním zbytečných periodických hlášení a zlepšuje výkon tím, že zajišťuje, aby plánovač používal nejaktuálnější informace o kanálu. Navíc díky hlášení na PUSCH může A-CSI přenášet větší a podrobnější užitečná data CSI (např. pro hlášení z více panelů nebo více beamů), než je možné na PUCCH, což je zásadní pro využití plného potenciálu pokročilých anténních systémů v NR.

## Klíčové vlastnosti

- Spouštění na vyžádání prostřednictvím DCI (Formát 0_1/0_2) pro minimální latenci a režii
- Hlášení přenášené na dynamicky plánovaném PUSCH, což umožňuje velké a flexibilní velikosti přenášených dat
- Konfigurovatelné prostřednictvím RRC (CSI-ReportConfig) s časovým chováním (timeDomainBehavior) nastaveným na 'aperiodic'
- Podporuje simultánní spuštění více konfigurací hlášení CSI prostřednictvím spouštěcích stavů (trigger states)
- Integruje se se zdroji CSI-RS pro měření kanálu a interference
- Poskytuje kritické vstupy pro adaptivní MCS, prekódování, správu beamů a adaptaci spojení

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [A-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-csi/)
