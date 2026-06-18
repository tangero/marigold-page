---
slug: "cna"
url: "/mobilnisite/slovnik/cna/"
type: "slovnik"
title: "CNA – Comfort Noise Addition"
date: 2025-01-01
abbr: "CNA"
fullName: "Comfort Noise Addition"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cna/"
summary: "Comfort Noise Addition (CNA) je technika zavedená ve 3GPP Release 18 pro zlepšení kvality zvuku během diskontinuálního přenosu (DTX) v hlasových službách. Generuje a vkládá umělý šum pozadí během tich"
---

CNA je technika 3GPP, která zlepšuje kvalitu zvuku generováním a vkládáním umělého šumu pozadí během tichých období v hovorech, aby se zabránilo vnímání 'mrtvého ticha'.

## Popis

Comfort Noise Addition (CNA) je sofistikovaná funkce zpracování signálu definovaná v rámci standardů 3GPP, konkrétně v kontextu zpracování médií pro hlasové a audiovizuální služby. Jejím primárním úkolem je řídit zvukový zážitek během období diskontinuálního přenosu ([DTX](/mobilnisite/slovnik/dtx/)), kdy aktivní hlasový kodek přestane vysílat pakety během ticha za účelem úspory síťové kapacity a energie zařízení. Bez CNA by tyto tiché mezery byly vnímány jako úplné, nepřirozené ticho neboli 'mrtvý vzduch', což může být pro uživatele rušivé a může dokonce vést k mylnému domnění o přerušení hovoru.

Architektonicky je CNA implementována v rámci cesty zpracování médií, typicky na přijímacím koncovém bodě nebo v rámci mediální brány či aplikačního serveru, který zpracovává hlasový provoz. Funguje ve spojení s detekcí hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)) a mechanismy potlačení ticha. Když VAD indikuje začátek tiché periody a DTX je aktivní, pravidelné řečové rámce přestanou proudit. Funkce CNA poté převezme kontrolu, generuje a vkládá signál komfortního šumu do výstupního audiostreamu. Tento šum není náhodný bílý šum, ale je pečlivě parametrizován tak, aby odpovídal charakteristikám akustického prostředí pozadí přítomného během posledního aktivního řečového segmentu, čímž zajišťuje plynulý a přirozený sluchový přechod z řeči do ticha a zpět.

Technická implementace zahrnuje analýzu spektrálních vlastností šumu pozadí během aktivních mluvních úseků. Parametry jako úroveň šumu a spektrální tvar jsou extrahovány a mohou být přenášeny k přijímači pomocí nízkokapacitních rámců popisovače vložení ticha ([SID](/mobilnisite/slovnik/sid/)) nebo podobné signalizace, jak je definováno v kodecích jako Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Případně, v pokročilejších nebo síťově orientovaných implementacích, může algoritmus CNA na přijímací straně nezávisle odhadnout nebo generovat odpovídající komfortní šum na základě dříve přijatého zvuku. Generovaný šum je typicky tvarovaný šum nízké úrovně, který napodobuje okolní zvuk, a zabraňuje tak náhlému přechodu do absolutního ticha.

Úloha CNA v síti je klíčová pro kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) u služeb Voice over LTE (VoLTE), Voice over NR (VoNR) a dalších paketových hlasových služeb. Je to klíčová součást koncového audiořetězce, která spolupracuje se základními síťovými prvky, jako je IP Multimedia Subsystem (IMS), a s řídicími politikami, které spravují optimalizaci médií. Udržováním konzistentního akustického pozadí CNA snižuje posluchačskou únavu, zabraňuje zmatení ohledně stavu hovoru a podporuje přirozený průběh konverzace, což je nezbytné pro přijetí efektivních, ale potenciálně rušivých technologií, jako je DTX, ze strany uživatelů.

## K čemu slouží

CNA byla vytvořena, aby vyřešila základní psychoakustický problém v digitální hlasové komunikaci: nepřirozené vnímání absolutního ticha. Rané digitální hlasové systémy, zejména ty používající účinné kodeky s [DTX](/mobilnisite/slovnik/dtx/) pro úsporu šířky pásma, během pauz zcela ztlumily zvukový výstup. To vytvářelo podivný, 'přerušovaný' zvukový obraz, který byl únavný a mohl uživatele vést k domněnce, že hovor byl přerušen. Účelem CNA je vyplnit tato umělá ticha nízkou hladinou komfortního šumu odpovídajícího pozadí, čímž se zachovává přirozený pocit a kontinuita hovoru.

Historický kontext vychází z vývoje hlasových kodeků a opatření pro efektivitu sítě. Jak se mobilní sítě vyvíjely od 2G přes 4G k 5G, použití paketové hlasové komunikace (VoIP) a sofistikovaných kodeků jako [AMR-WB](/mobilnisite/slovnik/amr-wb/) a EVS se stalo standardem. Tyto kodeky intenzivně využívají DTX pro úsporu energie a šířky pásma. Omezení předchozích přístupů však byla zřejmá: buď se DTN nepoužívalo, což plýtvalo zdroji, nebo se používalo bez účinného komfortního šumu, což degradovalo vnímanou kvalitu. CNA poskytuje nezbytný kompromis, který umožňuje ekonomické výhody DTX bez obětování uživatelského komfortu.

Dále CNA řeší výzvy v různých akustických prostředích. Bez ní může přepínání mezi aktivní řečí a úplným tichem způsobovat, že šum pozadí se zdánlivě 'objevuje a mizí', což je zvláště rušivé v prostředích s konstantním nízkourovňovým šumem (např. kanceláře, auta). Generováním konzistentní hladiny šumu CNA maskuje tyto přechody. Její standardizace v 3GPP Release 18, jako součást širších specifikací vylepšení médií, byla motivována potřebou jednotného, vysoce kvalitního hlasového zážitku napříč různými zařízeními a síťovými podmínkami, což je zvláště kritické pro operátorské služby VoLTE/VoNR konkurující over-the-top aplikacím.

## Klíčové vlastnosti

- Generuje umělý šum pozadí během tichých period DTX
- Používá parametry odvozené ze spektra okolního šumu aktivní řeči
- Zajišťuje plynulý a přirozený sluchový přechod z řeči do ticha
- Zabraňuje uživatelskému vnímání 'mrtvého ticha' nebo přerušení hovoru
- Funguje ve spojení s detekcí hlasové aktivity (VAD) a rámci popisovače vložení ticha (SID)
- Zlepšuje kvalitu uživatelského zážitku (QoE) pro paketové hlasové služby jako VoLTE a VoNR

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [CNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cna/)
