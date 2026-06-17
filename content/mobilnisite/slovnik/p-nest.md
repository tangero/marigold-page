---
slug: "p-nest"
url: "/mobilnisite/slovnik/p-nest/"
type: "slovnik"
title: "P-NEST – Private Network Slice Type"
date: 2026-01-01
abbr: "P-NEST"
fullName: "Private Network Slice Type"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/p-nest/"
summary: "P-NEST je typ síťového segmentu definovaný standardy 3GPP a specificky navržený pro privátní mobilní sítě. Poskytuje standardizovanou šablonu, která definuje charakteristiky, možnosti a servisní požad"
---

P-NEST je standardizovaná šablona typu síťového segmentu (network slice type) podle 3GPP, která definuje charakteristiky a servisní požadavky pro privátní mobilní sítě sloužící podnikovým nebo průmyslovým nasazením.

## Popis

Private Network Slice Type (P-NEST) je koncept zavedený ve vydání 3GPP Release 16 v rámci širšího rámce pro řízení síťového dělení na segmenty (network slicing). Typ síťového segmentu (Network Slice Type, [NEST](/mobilnisite/slovnik/nest/)) je znovupoužitelná předloha nebo šablona definující třídu síťových segmentů se společnými charakteristikami, jako jsou servisní požadavky, síťové funkce a profily zdrojů. P-NEST je specifická kategorie NEST přizpůsobená pro nasazení privátních sítí. Privátní sítě jsou vyhrazené mobilní sítě vybudované pro konkrétní podnik, továrnu, kampus nebo jinou lokalizovanou entitu a nabízejí v porovnání s veřejnými síťovými segmenty vyšší míru kontroly, zabezpečení a výkonu.

Šablona P-NEST standardizuje definici toho, co tvoří segment pro privátní síť. Určuje hodnotu Slice/Service Type (SST), což je standardizovaný identifikátor. Co je ještě důležitější, definuje související požadavky na podsíť síťového segmentu (Network Slice Subnet, NSS). To zahrnuje očekávané výkonnostní atributy, jako je ultranízká latence, vysoká spolehlivost, garantovaná šířka pásma a specifické úrovně bezpečnostní izolace. Dále také popisuje očekávané síťové funkce a jejich konfiguraci. Například P-NEST pro průmyslovou aplikaci IoT může vyžadovat přítomnost lokální User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro edge computing, specifické politiky QoS pro časově kritickou komunikaci a funkce řízení přístupu, které se integrují s podnikovými [IT](/mobilnisite/slovnik/it/) systémy.

Z pohledu řízení se P-NEST používá v rámci frameworků Management Function ([MANO](/mobilnisite/slovnik/mano/)) a Network Slice Management Function (NSMF). Když podnik objedná privátní síťový segment od poskytovatele služeb (kterým může být veřejný operátor nebo specializovaný poskytovatel privátních sítí), může poskytovatel vytvořit instanci segmentu na základě šablony P-NEST. Tím je zajištěno, že nasazený segment splňuje standardizovaný profil pro privátní sítě. Šablona usměrňuje správu životního cyklu segmentu: vytvoření, konfiguraci, monitorování a ukončení. Použitím standardizovaného P-NEST mohou systémy pro správu a síťové funkce různých dodavatelů lépe spolupracovat, protože sdílejí společnou představu o požadavcích na segment. To je klíčové pro nasazení privátních sítí s více dodavateli a pro umožnění poskytovatelům služeb nabízet konzistentní služby privátních síťových segmentů v různých geografických lokalitách nebo na různých místech zákazníků.

## K čemu slouží

Zavedení P-NEST řeší problém efektivního a konzistentního nasazování síťových segmentů pro rychle rostoucí trh privátních 5G sítí. Před jeho standardizací byl koncept "privátního síťového segmentu" nejasný. Každý dodavatel nebo operátor si mohl definovat vlastní sadu funkcí a požadavků, což vedlo k fragmentaci, nedostatku interoperability a složitým integračním snahám podniků. To brzdilo škálovatelnost a adopci řešení pro privátní sítě, zejména pro podniky působící na více místech nebo spolupracující s různými poskytovateli služeb.

P-NEST bylo motivováno potřebou industrializovat a škálovat poskytování služeb privátních sítí. Poskytnutím standardizované šablony v rámci frameworku 3GPP plní několik klíčových úkolů. Za prvé zjednodušuje proces objednávání a poskytování pro zákazníky. Podnik může požadovat "segment kompatibilní s P-NEST" s vědomím, že bude mít známou sadu schopností. Za druhé umožňuje interoperabilitu mezi síťovými zařízeními od různých dodavatelů, protože všechny komponenty jsou navrženy tak, aby podporovaly společný profil P-NEST. Za třetí umožňuje poskytovatelům služeb automatizovat správu životního cyklu segmentů. Namísto manuální konfigurace každého privátního síťového segmentu od nuly mohou jejich orchestrační systémy použít P-NEST jako recept, což dramaticky snižuje čas nasazení a provozní náklady. Nakonec chrání investice do budoucna tím, že zajišťuje, že privátní síťové segmenty jsou budovány na standardizovaném, rozvíjitelém základu, který může v pozdějších vydáních zahrnout nové funkce 3GPP.

## Klíčové vlastnosti

- Standardizovaná šablona definující společné charakteristiky pro privátní síťové segmenty
- Asociace se specifickou hodnotou Slice/Service Type (SST) pro identifikaci
- Definuje výkonnostní požadavky: latence, spolehlivost, šířka pásma, dostupnost
- Určuje požadované síťové funkce a jejich konfiguraci (např. lokální UPF, SMF)
- Usměrňuje bezpečnostní politiky a politiky izolace pro podnikovou úroveň soukromí
- Použití systémů pro správu (NSMF, CSMF) pro automatizované vytváření instancí segmentů a správu jejich životního cyklu

## Definující specifikace

- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.880** (Rel-19) — Study on 5G Energy Efficiency & Saving

---

📖 **Anglický originál a plná specifikace:** [P-NEST na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-nest/)
