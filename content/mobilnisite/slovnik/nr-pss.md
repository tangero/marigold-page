---
slug: "nr-pss"
url: "/mobilnisite/slovnik/nr-pss/"
type: "slovnik"
title: "NR-PSS – New Radio-Primary Synchronization Signal"
date: 2025-01-01
abbr: "NR-PSS"
fullName: "New Radio-Primary Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-pss/"
summary: "NR-PSS je fyzický vrstvový signál, který UE používají pro počáteční synchronizaci symbolového načasování a hrubou frekvenční synchronizaci s 5G buňkou. Jedná se o krátkou periodickou sekvenci vysílano"
---

NR-PSS je primární synchronizační signál v 5G New Radio, vysílaný v rámci SS/PBCH bloku, který UE detekuje jako první pro získání počáteční synchronizace symbolového načasování a hrubé frekvenční synchronizace během vyhledávání buňky.

## Popis

New Radio-Primary Synchronization Signal (NR-PSS) je základní downlinkový fyzický signál v 5G NR rozhraní. Jeho primární funkcí je umožnit uživatelskému zařízení (UE) dosáhnout počáteční synchronizace na úrovni symbolů a hrubé frekvenční synchronizace s vysílajícím gNB. NR-PSS je jednou ze tří hlavních komponent SS/PBCH bloku (SSB), vedle [NR-SSS](/mobilnisite/slovnik/nr-sss/) a NR-PBCH (který nese [NR-MIB](/mobilnisite/slovnik/nr-mib/)). Je vysílán periodicky a UE provádí slepé prohledávání možných frekvenčních nosných a časových intervalů, aby detekovalo PSS sekvenci. Detekce PSS umožňuje UE určit 5ms časovou hranici rádiového rámce a korigovat velké frekvenční odchylky.

Technicky je NR-PSS založen na frekvenční doméně M-sekvenci délky 127. Na rozdíl od LTE, které používalo Zadoff-Chu sekvenci, NR pro PSS používá M-sekvenci kvůli její lepší detekční výkonnosti při vysokých frekvenčních odchylkách, což je zvláště důležité pro nasazení v mmWave pásmech. Sekvence je mapována na 127 sousedních subnosných (kromě [DC](/mobilnisite/slovnik/dc/) subnosné) v rámci šířky pásma SSB. Existují 3 možné PSS sekvence, odpovídající skupině identit fyzické vrstvy buňky (N_ID^(2) = 0, 1 nebo 2). Detekce toho, která ze tří sekvencí je vysílána, poskytuje UE jednu část fyzické identity buňky (PCI). Vysílání je typicky beamformováno jako součást SSB a v rámci bursty je vysíláno více SSB s různými směry paprsku pro pokrytí servisní oblasti buňky.

Fungování NR-PSS je nedílnou součástí procesu vyhledávání buňky. UE se zapne a začne skenovat podporovaná frekvenční pásma. Koreluje přijímané signály se třemi možnými PSS sekvencemi. Silný korelační pík indikuje detekci buňky a poskytuje synchronizaci symbolového načasování. Jakmile je PSS detekováno, UE zná načasování přidruženého NR-SSS, které se nachází na pevném odstupu ve stejném SSB. Kombinovaná detekce PSS a SSS poskytne UE plnou PCI (0-1007) a umožní jemnější časové zarovnání. Opakující se struktura a známá poloha PSS v rámci vzoru SSB bursty dále pomáhá UE identifikovat SSB index a načasování pro procedury správy paprsků. Návrh zajišťuje robustní výkon v celém širokém rozsahu 5G kanálových šířek pásma a numerologií (rozestupů subnosných).

## K čemu slouží

NR-PSS byl vyvinut, aby poskytoval rychlý a spolehlivý počáteční synchronizační signál pro 5G NR, řešící omezení a nové požadavky nad rámec PSS pro LTE. Hlavní problém, který řeší, je umožnit UE rychle najít a synchronizovat se s vysíláním 5G buňky v čase a frekvenci, což je nezbytný první krok před jakoukoli komunikací. V LTE byly PSS/SSS umístěny ve středu šířky pásma nosné, ale 5G potřebovalo podporovat mnohem širší šířky pásem a flexibilní využití spektra, včetně nelicencovaných a mmWave pásem.

Motivace pro jeho konkrétní návrh vycházela z několika 5G požadavků. Použití M-sekvence namísto Zadoff-Chu sekvence zlepšuje odolnost vůči velkým počátečním frekvenčním chybám, které jsou častější u nízkonákladových oscilátorů v IoT zařízeních a ve vysokofrekvenčních pásmech. 5G PSS také muselo bezproblémově podporovat beamforming. Tím, že je nedílnou součástí SSB, je PSS vysíláno na každém paprsku během SSB bursty, což umožňuje UE nejen najít buňku, ale také identifikovat vhodný paprsek pro počáteční přístup. Toto provozování orientované na paprsky byl významný vývoj oproti všesměrovým nebo sektorovým synchronizačním signálům v LTE. Návrh zajišťuje nízkou složitost detekce a latenci, což je klíčové pro splnění požadavků 5G případů užití pro ultra-spolehlivou nízkolatenční komunikaci (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB).

## Klíčové vlastnosti

- Založeno na M-sekvenci délky 127 pro robustní detekci i při vysoké frekvenční odchylce
- Poskytuje 3 možné sekvence (N_ID^(2) = 0,1,2) reprezentující část fyzické identity buňky (PCI)
- Umožňuje počáteční synchronizaci symbolového načasování a hrubou frekvenční synchronizaci pro UE
- Vysíláno jako součást SS/PBCH bloku (SSB) s podporou beamformingu
- Mapováno na 127 sousedních subnosných v rámci šířky pásma SSB
- Podporuje více numerologií (rozestupů subnosných) pro různá frekvenční pásma

## Související pojmy

- [NR-SSS – New Radio-Secondary Synchronization Signal](/mobilnisite/slovnik/nr-sss/)

## Definující specifikace

- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [NR-PSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-pss/)
