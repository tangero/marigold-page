---
slug: "2sb"
url: "/mobilnisite/slovnik/2sb/"
type: "slovnik"
title: "2SB – Double Sideband"
date: 2026-01-01
abbr: "2SB"
fullName: "Double Sideband"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/2sb/"
summary: "Dvojité postranní pásmo (2SB) je technika přenosu rádiových frekvencí, při níž jsou spolu s nosným signálem vysílána jak horní, tak dolní postranní pásmo. Ve standardech 3GPP je specifikováno pro konk"
---

2SB je technika přenosu rádiových frekvencí používaná ve standardech 3GPP, při níž jsou vysílány jak horní, tak dolní postranní pásmo spolu s nosnou vlnou, což optimalizuje spektrální účinnost a kvalitu signálu pro specifická nasazení.

## Popis

Přenos s dvojitým postranním pásmem (2SB) je základní technika rádiových frekvencí, při níž jsou spolu s nosným signálem vysílána obě postranní pásma (horní i dolní) vznikající během modulace. Ve specifikacích 3GPP, konkrétně v dokumentech 38.191, 38.194 a 38.769, je 2SB definováno pro specifické scénáře nasazení a kmitočtová pásma, kde tato přenosová metoda poskytuje optimální výkonnostní charakteristiky. Technika zahrnuje amplitudovou modulaci, kde je informace obsažena v obou postranních pásmech symetricky rozložených kolem nosné frekvence.

Z architektonického hlediska implementace 2SB ovlivňuje návrh vysílačů jak základnové stanice (gNB), tak uživatelského zařízení (UE). Bázové pásmo generuje modulovaný signál, který následně prochází [RF](/mobilnisite/slovnik/rf/) konverzí nahoru při zachování obou postranních pásem. Součásti RF předkonce, včetně výkonových zesilovačů a filtrů, musí být navrženy tak, aby zvládly celou šířku pásma obsahující obě postranní pásma bez zavedení nadměrného zkreslení nebo intermodulačních produktů. Příjmová architektura musí být odpovídajícím způsobem schopna demodulovat obě postranní pásma pro obnovení přenášené informace.

Z pohledu zpracování signálu vyžaduje přenos 2SB pečlivou správu poměru výkonu nosné vlny k postranním pásmům a fázových vztahů. Vysílač musí udržovat správnou linearitu, aby zabránil spektrálnímu opětovného narůstání a rušení sousedního kanálu. V přijímači demodulace typicky zahrnuje koherentní detekci, kde je nosná vlna obnovena a použita k extrakci informace z obou postranních pásem. To vyžaduje přesnou synchronizaci a odhad kanálu pro správné sloučení informací z obou postranních pásem.

Role 2SB v sítích 5G a novějších zahrnuje specifické scénáře nasazení, kde jeho charakteristiky poskytují výhody oproti technikám s jedním postranním pásmem nebo zbytkovým postranním pásmem. Mezi tyto scénáře patří určitá kmitočtová pásma a modulační schémata, kde 2SB nabízí lepší spektrální účinnost nebo jednoduchost implementace. Tato technika musí být koordinována s dalšími aspekty fyzické vrstvy včetně kódování kanálu, schémat mnohonásobného přístupu a beamformingu, aby byl zajištěn celkový výkon systému podle požadavků 3GPP.

## K čemu slouží

Přenos s dvojitým postranním pásmem existuje jako základní technika rádiové komunikace, která poskytuje robustní přenos signálu s jednoduchostí implementace v určitých scénářích. Primární motivací pro specifikaci 2SB ve standardech 3GPP je poskytnout standardizovaný přístup pro scénáře nasazení, kde tato přenosová metoda nabízí technické výhody, zejména v konkrétních kmitočtových pásmech a modulačních schématech, kde by alternativní techniky mohly zavést zbytečnou složitost nebo omezení výkonu.

Historicky bylo 2SB jednou z nejranějších technik amplitudové modulace vyvinutých pro rádiovou komunikaci. Zatímco moderní digitální komunikace často používají spektrálně účinnější modulační schémata, 2SB zůstává relevantní pro specifické aplikace, kde jeho charakteristiky poskytují výhody. Ve standardizaci 3GPP zařazení specifikací 2SB řeší scénáře nasazení, kde tato tradiční technika nabízí praktické výhody z hlediska nákladů na implementaci, energetické účinnosti nebo kompatibility se stávající infrastrukturou.

Specifikace 2SB ve vydání 19 řeší potřebu standardizovaných přístupů k různorodým scénářům nasazení v sítích 5G-Advanced. Poskytnutím jasných technických specifikací v dokumentech jako 38.191, 38.194 a 38.769 zajišťuje 3GPP interoperabilitu a předvídatelný výkon napříč implementacemi různých dodavatelů. Tato standardizace umožňuje operátorům sítí nasadit řešení založená na 2SB tam, kde je to vhodné, při zachování kompatibility s širším ekosystémem 5G.

## Klíčové vlastnosti

- Vysílá obě modulační postranní pásma (horní i dolní)
- Zachovává nosný signál spolu s postranními pásmy
- Specifikováno pro konkrétní scénáře nasazení 3GPP
- Vyžaduje přesnou správu poměru výkonu nosné vlny k postranním pásmům
- Na straně přijímače vyžaduje koherentní demodulaci
- Musí udržovat lineární zesílení, aby se zabránilo zkreslení

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [2SB na 3GPP Explorer](https://3gpp-explorer.com/glossary/2sb/)
