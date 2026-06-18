---
slug: "mts"
url: "/mobilnisite/slovnik/mts/"
type: "slovnik"
title: "MTS – MUROS Test Scenario"
date: 2025-01-01
abbr: "MTS"
fullName: "MUROS Test Scenario"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mts/"
summary: "MTS označuje sadu standardizovaných testovacích scénářů definovaných 3GPP pro ověření výkonu a funkčnosti MUROS (Multi-User Reusing One Slot) v sítích GSM/EDGE. MUROS je technika zvýšení hlasové kapac"
---

MTS je sada standardizovaných testovacích scénářů 3GPP pro ověření výkonu a funkčnosti techniky zvýšení hlasové kapacity MUROS v sítích GSM/EDGE.

## Popis

[MUROS](/mobilnisite/slovnik/muros/) Test Scenario (MTS) je rámec pro testování shody specifikovaný v dokumentu 3GPP TS 45.914 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). MUROS (Multi-User Reusing One Slot) je klíčová funkce zavedená za účelem zvýšení hlasové kapacity v sítích GSM tím, že umožňuje dvěma hovorům sdílet jeden fyzický [TDMA](/mobilnisite/slovnik/tdma/) časový slot pomocí pokročilých modulačních a kódovacích schémat, čímž se efektivně zdvojnásobuje potenciální počet hlasových kanálů. MTS definuje komplexní sadu testovacích případů, které musí výrobci zařízení a operátoři sítí použít k ověření, že jak síťová infrastruktura (Base Station System, [BSS](/mobilnisite/slovnik/bss/)), tak mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) správně implementují funkcionalitu MUROS.

Z architektonického hlediska testování zahrnuje mobilní stanici (testované zařízení) a testovací systém, který emuluje Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)). Testovací scénáře pokrývají různé vrstvy protokolového zásobníku, včetně fyzické vrstvy (rádiový přenos) a vrstvy spojení dat (LAPDm pro signalizaci). Klíčovými testovanými komponentami jsou přijímač a vysílač MS, které musí být schopny zpracovat specifickou modulaci (např. 8-PSK pro jednoho uživatele a GMSK pro druhého na stejném časovém slotu) a vyrovnat se se zvýšeným rušením, které je inherentní při sdílení prostředku. Testovací systém generuje standardizované rádiové signály a signalizační zprávy pro simulaci reálných síťových podmínek, ve kterých je MUROS aktivní.

Jak testování funguje: Každý MTS je podrobný popis postupu, který nastaví specifické rádiové prostředí a sled událostí. Například testovací scénář může simulovat buňku, ve které je MUROS povoleno, s MS provádějícím sestavení hovoru, po kterém následuje předání spojení do jiné buňky také používající MUROS. Test ověřuje, že MS dokáže správně dekódovat přiřazený subkanál (pomocí např. technik Orthogonal Sub-Channel (OSC)) a zároveň potlačit nebo zmírnit rušení od spárovaného uživatele na stejném časovém slotu. Měří se parametry jako Bit Error Rate (BER), Frame Erasure Rate (FER) a přesnost signalizačních zpráv. Scénáře také testují procedury mobility, řízení výkonu a nespojitý přenos (DTX) v kontextu MUROS.

Role MTS je klíčová pro zajištění úspěšného nasazení MUROS. Poskytnutím standardizovaného měřítka zaručuje interoperabilitu mezi mobilními terminály od různých výrobců a síťovým zařízením a předchází tak degradaci služeb. Důkladné testování výkonu fyzické vrstvy v podmínkách rušení je obzvláště důležité, protože MUROS posouvá hranice tradiční GSM modulace. Tyto testovací scénáře dávají operátorům jistotu, že slib zdvojnásobení kapacity díky MUROS může být realizován v živých sítích bez kompromisů v kvalitě hlasu nebo stabilitě hovoru.

## K čemu slouží

MUROS byl vyvinut pro řešení kritického nedostatku spektra a kapacitních omezení ve zralých sítích GSM, zejména v přetížených městských oblastech. Před MUROS vyžadovalo zvýšení hlasové kapacity přidělení dalších časových slotů nebo frekvencí, což jsou omezené a drahé zdroje. Účelem MUROS Test Scenarios (MTS) bylo poskytnout důkladnou, standardizovanou metodologii pro ověření této inovativní a komplexní technologie. Bez takových testů shody by se různé implementace MUROS od různých výrobců mohly ukázat jako nekompatibilní, což by vedlo k přerušeným hovorům, špatné kvalitě hlasu a v konečném důsledku k selhání této funkce při plnění zamýšlených přínosů.

Vytvoření MTS bylo motivováno potřebou zajistit, aby teoretické zisky MUROS mohly být spolehlivě dosaženy v praxi. MUROS zásadně mění způsob využití rádiového rozhraní, zavádí nové struktury signálů a vyžaduje pokročilejší algoritmy přijímačů jak v mobilním terminálu, tak v základnové stanici. Testování takových změn není triviální a přesahuje rámec standardních GSM testů. MTS poskytlo společný 'jazyk' a sadu podmínek, vůči kterým mohlo být hodnoceno veškeré zařízení, čímž snížilo riziko nasazení pro operátory a urychlilo přijetí v odvětví.

Historicky byl MTS definován v 3GPP Release 8 spolu se základními specifikacemi MUROS. Jeho vývoj byl výsledkem spolupráce síťových operátorů, výrobců mobilních terminálů a výrobců testovacích zařízení. Stanovením těchto testovacích scénářů v rané fázi 3GPP usnadnilo hladší zavedení funkcí zvyšujících kapacitu do rozsáhlé instalované základny sítí GSM, prodloužilo jejich životnost a oddálilo potřebu nákladného přerozdělování spektra nebo výměny sítí.

## Klíčové vlastnosti

- Standardizované testovací postupy pro validaci funkčnosti MUROS
- Pokrývá testy shody jak pro mobilní stanici (MS), tak pro síťovou stranu
- Testuje výkon fyzické vrstvy za podmínek rušení spárovaným subkanálem
- Zahrnuje scénáře pro sestavení hovoru, předání spojení a mobilitu s MUROS
- Ověřuje správnou funkci technik Orthogonal Sub-Channel (OSC)
- Zajišťuje interoperabilitu mezi implementacemi od různých výrobců

## Související pojmy

- [MUROS – Multi-User Reusing One Slot](/mobilnisite/slovnik/muros/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mts/)
