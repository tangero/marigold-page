---
slug: "sic"
url: "/mobilnisite/slovnik/sic/"
type: "slovnik"
title: "SIC – Successive Interference Cancellation"
date: 2025-01-01
abbr: "SIC"
fullName: "Successive Interference Cancellation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sic/"
summary: "Successive Interference Cancellation je technika detekce více uživatelů, při které přijímač nejprve dekóduje nejsilnější signál, odečte jeho odhadovaný příspěvek od složeného přijatého signálu a poté"
---

SIC je technika detekce více uživatelů, při které přijímač dekóduje, odečte a zruší nejsilnější rušivý signál, aby zlepšil dekódování následujících, slabších signálů, čímž zvyšuje spektrální účinnost.

## Popis

Successive Interference Cancellation (SIC) je pokročilý algoritmus zpracování signálu na fyzické vrstvě používaný v přijímači k oddělení více překrývajících se datových proudů vysílaných současně na stejném časově-frekvenčním zdroji. Funguje na principu využití rozdílů ve výkonu mezi uživatelskými signály. V typickém scénáři SIC, například v power-domain Non-Orthogonal [Multiple Access](/mobilnisite/slovnik/multiple-access/) (NOMA), je více uživatelů multiplexováno s různými úrovněmi výkonu. Architektura přijímače pro SIC zahrnuje více stupňů dekódování, regenerace a odečítání.

Proces probíhá sekvenčně. Nejprve přijímač dekóduje signál nejsilnějšího uživatele (toho s nejvyšším přijímaným výkonem) a zachází se signály všech ostatních uživatelů jako se šumem. To je možné, protože vysoký poměr signálu k interferenci a šumu ([SINR](/mobilnisite/slovnik/sinr/)) silného uživatele umožňuje spolehlivé dekódování i za přítomnosti interference. Po dekódování přijímač dokonale rekonstruuje (pře-kóduje a pře-moduluje) odhadovaný signál tohoto silného uživatele včetně jeho kanálových efektů. Tento rekonstruovaný signál je následně odečten od původního složeného přijatého signálu. Tento krok rušení odstraní významnou část interference pro zbývající, slabší uživatele.

Po odečtení reziduální signál obsahuje data zbývajících uživatelů, ale s dominantní interferencí od nejsilnějšího uživatele z velké části eliminovanou. Přijímač poté přejde k dalšímu nejsilnějšímu uživateli v reziduálním signálu a proces opakuje: dekódování, rekonstrukce a odečtení. Toto pokračuje iterativně, dokud nejsou dekódovány všechny zamýšlené uživatelské signály. Klíčem k úspěchu SIC je přesný odhad kanálu a dokonalá rekonstrukce signálu; jakákoli chyba v dekódování nebo rekonstrukci signálu dřívějšího uživatele se přenáší na všechny následující uživatele, což je jev známý jako šíření chyb. SIC je výpočetně složitější než lineární metody detekce, jako je [MMSE](/mobilnisite/slovnik/mmse/), ale nabízí výrazně lepší výkon ve vysoce interferenčních prostředích s omezenou kapacitou. V 3GPP je klíčovou přijímací technikou pro uplinkové schémata NOMA studovaná pro hromadnou komunikaci mezi stroji (mMTC) a je také relevantní pro pokročilou [MIMO](/mobilnisite/slovnik/mimo/) detekci.

## K čemu slouží

SIC existuje, aby překonala základní kapacitní omezení ortogonálních schémat víceuživatelského přístupu, jako je [OFDMA](/mobilnisite/slovnik/ofdma/), kde jsou zdroje rozděleny mezi uživatele bez překrytí. Ortogonalita se vyhýbá interferenci, ale může být spektrálně neefektivní, když mají uživatelé různorodé podmínky kanálu nebo malé datové pakety. SIC umožňuje neortogonální multiplexování, což dovoluje více uživatelům sdílet stejný blok zdrojů, čímž se zvyšuje počet současných připojení a celková propustnost systému – což je klíčový cíl pro 5G a další generace.

Historický kontext spočívá v teorii informace, kde koncept superpozičního kódování a kódování "dirty paper" stanovily teoretické výhody neortogonálního přístupu. Praktické implementace se staly proveditelné se zvýšeným výpočetním výkonem přijímačů. SIC přímo řeší problém víceuživatelské interference. Ve scénářích, jako je uplink mobilní sítě (např. pro IoT zařízení), mnoho zařízení vysílá sporadicky s malými datovými přenosy. Grantový ortogonální přístup by znamenal nadměrnou signalizační režii. Grant-free NOMA s SIC umožňuje zařízením vysílat bez explicitního plánování a základnová stanice používá SIC k oddělení kolizních přenosů, což dramaticky snižuje latenci a signalizaci.

Konkrétně řeší problém blízkého a vzdáleného uživatele v power-domain multiplexování. Přidělením většího výkonu uživatelům se špatnými podmínkami kanálu (vzdálení uživatelé) a menšího výkonu uživatelům s dobrými podmínkami (blízcí uživatelé) může základnová stanice nejprve dekódovat silný signál vzdáleného uživatele a poté signál blízkého uživatele po zrušení interference. Tím je zajištěna spravedlnost a pokrytí. Bez SIC by takové neortogonální přenosy vedly ke katastrofální interferenci a byly by nepoužitelné. SIC je tedy klíčovým umožňovatelem hromadné konektivity a ultra-spolehlivé komunikace s nízkou latencí, kde jsou klíčové efektivita využití zdrojů a nízká režie.

## Klíčové vlastnosti

- Iterativní proces dekódování a odečítání pro separaci víceuživatelských signálů
- Využívá rozdíly ve výkonu mezi uživateli pro uspořádané dekódování
- Klíčová umožňující technologie pro power-domain Non-Orthogonal Multiple Access (NOMA)
- Zlepšuje spektrální účinnost a kapacitu systému v kanálech omezených interferencí
- Vyžaduje přesný odhad kanálu a rekonstrukci signálu ke zmírnění šíření chyb
- Zvyšuje výpočetní složitost přijímače ve srovnání s lineárními detektory

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.904** (Rel-4) — 3GPP UE Baseline Capability Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.859** (Rel-13) — Study on Downlink Multiuser Superposition Transmission
- **TS 36.866** (Rel-12) — Study on Network Assisted Interference Cancellation
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [SIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sic/)
