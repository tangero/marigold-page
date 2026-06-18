---
slug: "mers"
url: "/mobilnisite/slovnik/mers/"
type: "slovnik"
title: "MERS – Mean Effective Radiated Sensitivity"
date: 2025-01-01
abbr: "MERS"
fullName: "Mean Effective Radiated Sensitivity"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mers/"
summary: "MERS je klíčový metrik výkonu pro testování přijímače uživatelského zařízení (UE), který kvantifikuje průměrnou citlivost anténního systému zařízení v realistickém vícecestném útlumovém prostředí. Je"
---

MERS je klíčový metrik výkonu přijímače uživatelského zařízení (UE), který kvantifikuje průměrnou citlivost antény v realistickém vícecestném útlumovém prostředí, aby zajistil spolehlivý výkon v uplinku.

## Popis

Mean Effective Radiated Sensitivity (MERS, průměrná efektivní vyzařovaná citlivost) je standardizované měření definované v dokumentu 3GPP TS 25.914 pro hodnocení vyzařovaného výkonu přijímače uživatelského zařízení (UE). Na rozdíl od vedených testů citlivosti prováděných přímo na anténním portu MERS posuzuje celý přijímací řetězec včetně výkonu antény v kontrolovaném, ale realistickém rádiovém prostředí simulujícím vícecestný útlum. Test se provádí v bezodrazové komoře za použití simulátoru útlumu a emulátoru základnové stanice k vytvoření specifických podmínek vícecestného šíření, jako jsou ty definované v útlumových profilech 3GPP. UE je umístěno na polohovacím systému, který jej otáčí v různých prostorových orientacích, aby se vyprůměrovaly efekty vyzařovacího diagramu a polarizace antény. Metrika představuje průměrnou úroveň výkonu, měřenou na vstupu vysílací antény emulátoru základnové stanice, potřebnou k dosažení stanoveného minimálního výkonnostního kritéria UE, typicky cílové chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)).

Z architektonického hlediska zahrnuje testovací sestava MERS několik klíčových komponent: testované UE, simulátor útlumu modelující rádiový kanál, emulátor základnové stanice generující downlinkový signál a polohovací systém pro otáčení UE. Test se provádí bezdrátově ([OTA](/mobilnisite/slovnik/ota/)), což znamená, že signály jsou bezdrátově přenášeny a přijímány mezi anténou testovacího zařízení a anténou UE. Tento holistický přístup zachycuje kombinované efekty [RF](/mobilnisite/slovnik/rf/) předkoncového přijímače, základnového pásma a vyzařovací účinnosti, zisku, diagramu a polarizačních charakteristik antény. Výraz 'mean' (průměrný) v MERS odkazuje na statistický průměr měření citlivosti provedených napříč mnoha prostorovými vzorky (orientacemi UE) a realizacemi kanálu, což poskytuje komplexní a opakovatelné hodnocení reálného výkonu.

MERS hraje klíčovou roli v ekosystému rádiové přístupové sítě (RAN) tím, že zajišťuje splnění minimálních výkonnostních požadavků UE pro uplinkové připojení. UE se špatnou hodnotou MERS bude vyžadovat silnější downlinkový signál od základnové stanice k udržení spojení, což efektivně zmenšuje pokrytí buňky a zvyšuje interferenci pro ostatní uživatele. Standardizací tohoto OTA testu umožňuje 3GPP konzistentní srovnávání kvality přijímače UE napříč různými výrobci a modely zařízení. To zvyšuje celkovou efektivitu sítě, protože základnové stanice mohou pracovat s nižším vysílacím výkonem pro uživatele s vysoce citlivými zařízeními, což zlepšuje výdrž baterie koncových uživatelů a snižuje celkovou energetickou spotřebu sítě. Je to základní metrika pro typové schvalování, certifikaci a optimalizaci sítě.

## K čemu slouží

MERS byl zaveden, aby vyřešil kritickou mezeru v ověřování výkonu UE: samotné vedené testy nebyly dostatečné pro zaručení reálného výkonu. Před jeho standardizací se citlivost primárně měřila na anténním portu ve vedeném uspořádání, které izolovalo přijímací elektroniku, ale zcela ignorovalo výkon integrované antény. V reálném nasazení účinnost antény, její vyzařovací diagram a manipulace uživatele se zařízením (efekty hlavy a ruky) drasticky ovlivňují skutečnou sílu přijímaného signálu. UE s výbornou vedenou citlivostí mohlo v terénu stále podávat špatný výkon, pokud byl jeho anténní systém neúčinný nebo špatně přizpůsobený.

Vytvoření MERS bylo motivováno potřebou holističtějšího a realističtějšího výkonnostního metrika, který by mohl přímo korelovat se zážitkem koncového uživatele, zejména pro datové služby, kde je konzistentní výkon v uplinku zásadní. Řeší problém nepředvídatelného výkonu v terénu tím, že poskytuje kontrolovanou laboratorní metodu pro kvantifikaci 'skutečné' citlivosti kompletního zařízení. To umožňuje síťovým operátorům mít větší důvěru v zařízení připojující se k jejich sítím, zajišťuje základní úroveň kvality služeb a umožňuje přesnější plánování a optimalizaci rádiové sítě. Stanovením společné testovací metodologie také podporuje spravedlivou konkurenci mezi výrobci zařízení, protože všechna zařízení jsou hodnocena podle stejných realistických výkonnostních kritérií.

## Klíčové vlastnosti

- Bezdrátové (OTA) měření celého přijímacího řetězce UE
- Používá standardizované 3GPP profely vícecestných útlumových kanálů
- Zahrnuje prostorové průměrování prostřednictvím rotace UE, aby zohlednilo vyzařovací diagramy antén
- Měří průměrnou citlivost potřebnou k dosažení cílové chybovosti bloků (BLER)
- Poskytuje opakovatelný etalon pro reálný výkon přijímače
- Nezbytný pro typové schvalování a certifikační testování UE

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods

---

📖 **Anglický originál a plná specifikace:** [MERS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mers/)
