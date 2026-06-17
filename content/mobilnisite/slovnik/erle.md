---
slug: "erle"
url: "/mobilnisite/slovnik/erle/"
type: "slovnik"
title: "ERLE – Echo Return Loss Enhancement"
date: 2025-01-01
abbr: "ERLE"
fullName: "Echo Return Loss Enhancement"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/erle/"
summary: "ERLE je klíčový výkonnostní parametr při testování kvality hovoru v 3GPP, který kvantifikuje účinnost akustického potlačovače ozvěny (AEC). Měří snížení úrovně ozvěny dosažené systémem AEC, což přímo"
---

ERLE je klíčový výkonnostní parametr při testování kvality hovoru v 3GPP, který měří snížení úrovně ozvěny dosažené akustickým potlačovačem ozvěny, což přímo ovlivňuje srozumitelnost hovoru.

## Popis

Echo Return Loss Enhancement (ERLE) je standardizovaný logaritmický poměr, vyjádřený v decibelech (dB), který hodnotí výkon Akustického potlačovače ozvěny ([AEC](/mobilnisite/slovnik/aec/)). AEC je komponenta pro digitální zpracování signálu, typicky implementovaná v mobilních zařízeních nebo síťových prvcích, navržená k odstranění akustické ozvěny, která vzniká, když je hlas mluvčího na vzdáleném konci zachycen mikrofonem na blízkém konci poté, co je přehrán místním reproduktorem. Tato ozvěna, pokud není potlačena, výrazně snižuje kvalitu hovoru. Metrika ERLE se vypočítá porovnáním výkonu ozvěnového signálu před potlačením (referenční signál nebo 'send-in' cesta obsahující ozvěnu) s výkonem zbytkového ozvěnového signálu po zpracování AEC ('send-out' cesta). Vyšší hodnota ERLE indikuje účinnější potlačovač ozvěny, což znamená, že bylo odstraněno více energie ozvěny.

Z architektonického hlediska systém AEC, jehož výkon ERLE měří, funguje uvnitř řetězce zpracování hlasu. Kontinuálně adaptuje digitální filtr, aby modeloval akustickou impulsní odezvu lokálního prostředí (cestu od reproduktoru k mikrofonu). Tento adaptivní filtr generuje odhad ozvěny, který je následně odečten od příchozího signálu z mikrofonu. Účinnost této adaptace a odečtení je přesně to, co ERLE kvantifikuje. Mezi klíčové komponenty podílející se na generování a měření ERLE patří referenční signál vzdáleného konce, algoritmus adaptivního filtru (často využívající Normalized Least Mean Squares nebo podobné), chybový signál (zbytková ozvěna) a bloky pro výpočet výkonu pro signály před i po potlačení.

Role ERLE je klíčová pro zajištění kvality hovoru v sítích 3GPP. Není to statická komponenta, ale kritický klíčový výkonnostní indikátor ([KPI](/mobilnisite/slovnik/kpi/)) používaný při certifikaci zařízení, testování sítě a monitorování kvality. Testovací specifikace, jako je 3GPP TS 26.115, definují přísné testovací postupy pro měření ERLE za různých podmínek, včetně různých úrovní šumu na pozadí, úrovní řeči a scénářů dvojitého hovoru (kdy mluví obě strany současně). Tato metrika zajišťuje, že zařízení a síťové uzly splňují minimální výkonnostní prahové hodnoty, a garantuje tak konzistentní a vysoce kvalitní hlasový zážitek pro koncové uživatele napříč různými výrobci a síťovými nasazeními.

## K čemu slouží

ERLE existuje proto, aby poskytl objektivní, kvantifikovatelné měřítko výkonu akustického potlačování ozvěny, což je základní požadavek pro přijatelnou hlasovou telefonii. Před sofistikovaným digitálním [AEC](/mobilnisite/slovnik/aec/) byla komunikace v režimu hands-free zatížena rušivou ozvěnou, což činilo hovory obtížnými a únavnými. Hlavním problémem, který ERLE řeší, je subjektivní a proměnlivá povaha hodnocení kvality hovoru; nahrazuje odhady standardizovanou, opakovatelnou metrikou. To umožňuje inženýrům efektivně navrhovat, testovat a porovnávat algoritmy AEC, čímž se zajišťuje interoperabilita a základní úroveň kvality v ekosystému více dodavatelů.

Vznik ERLE byl motivován rozšířením mobilních zařízení s integrovanými reproduktory a mikrofony v těsné blízkosti a rostoucím využíváním režimů hands-free a hlasitého odposlechu. Tyto případy užití problém akustické ozvěny zhoršují. Standardizace 3GPP byla nutná, protože nekonzistentní výkon potlačování ozvěny mezi zařízeními by vedl ke špatnému a nepředvídatelnému uživatelskému zážitku v síti. Definováním ERLE ve specifikacích jako je TS 26.115 poskytuje 3GPP společný 'jazyk' a testovací metodologii pro výrobce a síťové operátory, aby ověřili, že jejich zařízení nezhorší celkovou hlasovou službu. Řeší problém zajištění toho, aby potlačování ozvěny, což je komplexní úloha zpracování signálu, fungovalo dostatečně v reálných akustických podmínkách.

## Klíčové vlastnosti

- Standardizovaná logaritmická výkonnostní metrika měřená v decibelech (dB)
- Kvantifikuje útlum akustické ozvěny pomocí adaptivního filtru
- Definované testovací postupy v 3GPP TS 26.115 pro reprodukovatelné měření
- Kritický klíčový výkonnostní indikátor (KPI) pro certifikaci kvality hovoru
- Hodnotí výkon za podmínek šumu, dvojitého hovoru a různých úrovní signálu
- Zajišťuje interoperabilitu a konzistentní uživatelský zážitek napříč zařízeními

## Definující specifikace

- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements

---

📖 **Anglický originál a plná specifikace:** [ERLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/erle/)
